# === Import Libraries ===
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="📊 Dashboard E-Commerce"
)

# === Caching Function for Data Loading ===
@st.cache_data
def load_data():
    # Load dataset
    data = pd.read_csv('merged_data_ecommerce.csv')

    # Konversi kolom tanggal menjadi tipe datetime
    datetime_columns = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
    ]
    for col in datetime_columns:
        data[col] = pd.to_datetime(data[col], errors='coerce')

    # Buat kolom baru untuk durasi pengiriman
    data['delivery_time'] = (
        data['order_delivered_customer_date'] - data['order_purchase_timestamp']
    ).dt.days

    return data

# === Load Data ===
merged_data = load_data()

# === Data Cleaning ===
merged_data = merged_data.dropna(subset=['order_purchase_timestamp', 'order_delivered_customer_date'])
merged_data['review_score'] = merged_data['review_score'].astype(int)

# === Streamlit Dashboard Layout ===
st.title("📊 Dashboard E-Commerce")
st.markdown("""
Dashboard ini menyediakan analisis data e-commerce berdasarkan kategori produk, waktu pengiriman, ulasan pelanggan, 
dan tren penjualan untuk membantu pengambilan keputusan bisnis.
""")

# === Sidebar: Filter Data ===
st.sidebar.header("Filter Data")
categories = st.sidebar.multiselect(
    "Pilih Kategori Produk",
    options=merged_data['product_category_name_english'].dropna().unique(),
    default=merged_data['product_category_name_english'].dropna().unique()
)

states = st.sidebar.multiselect(
    "Pilih Provinsi Pembeli",
    options=merged_data['customer_state'].dropna().unique(),
    default=merged_data['customer_state'].dropna().unique()
)

min_time = merged_data['order_purchase_timestamp'].min().date()
max_time = merged_data['order_purchase_timestamp'].max().date()

time_range = st.sidebar.slider(
    "Rentang Waktu Pembelian",
    min_value=min_time,
    max_value=max_time,
    value=(min_time, max_time),
    format="YYYY-MM-DD"
)

# === Filter Data Berdasarkan Pilihan ===
filtered_data = merged_data[
    (merged_data['product_category_name_english'].isin(categories)) &
    (merged_data['customer_state'].isin(states)) &
    (merged_data['order_purchase_timestamp'].between(pd.to_datetime(time_range[0]), pd.to_datetime(time_range[1])))
]

# === Section 1: Tren Penjualan Bulanan ===
st.subheader("📈 Tren Penjualan Bulanan")
monthly_sales = filtered_data.groupby(filtered_data['order_purchase_timestamp'].dt.to_period('M')).size()

fig1 = px.line(
    x=monthly_sales.index.astype(str),
    y=monthly_sales.values,
    labels={"x": "Bulan", "y": "Jumlah Penjualan"},
    title="Tren Penjualan Bulanan"
)
fig1.update_traces(mode="lines+markers")
st.plotly_chart(fig1)

# === Section 2: Kategori Produk Terpopuler ===
st.subheader("🛍️ Top Kategori Produk")
top_categories = filtered_data['product_category_name_english'].value_counts().sort_values(ascending=False).head(10)

fig2 = px.bar(
    x=top_categories.values,
    y=top_categories.index,
    orientation='h',
    labels={"x": "Jumlah Penjualan", "index": "Kategori Produk"},
    title="10 Kategori Produk Teratas"
)
fig2.update_layout(yaxis=dict(categoryorder='total ascending'))
st.plotly_chart(fig2)

# === Section 3: Distribusi Durasi Pengiriman ===
st.subheader("🚚 Distribusi Durasi Pengiriman")
fig3 = px.histogram(
    filtered_data,
    x="delivery_time",
    nbins=20,
    color_discrete_sequence=['#636EFA'],
    title="Distribusi Durasi Pengiriman (Hari)",
    labels={"delivery_time": "Durasi Pengiriman (Hari)"}
)
st.plotly_chart(fig3)

# === Section 4: Korelasi Durasi Pengiriman dan Skor Ulasan ===
st.subheader("📦 Korelasi Durasi Pengiriman dan Skor Ulasan")
correlation = filtered_data[['delivery_time', 'review_score']].corr().iloc[0, 1]
st.markdown(f"**Korelasi antara durasi pengiriman dan skor ulasan:** {correlation:.2f}")

fig4 = px.box(
    filtered_data,
    x="review_score",
    y="delivery_time",
    color="review_score",
    title="Durasi Pengiriman Berdasarkan Skor Ulasan",
    labels={"review_score": "Skor Ulasan", "delivery_time": "Durasi Pengiriman (Hari)"},
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(fig4)

# === Section 5: Distribusi Skor Ulasan ===
st.subheader("💬 Distribusi Skor Ulasan")
fig5 = px.histogram(
    filtered_data,
    x="review_score",
    nbins=5,
    color_discrete_sequence=['#EF553B'],
    title="Distribusi Skor Ulasan",
    labels={"review_score": "Skor Ulasan", "count": "Jumlah Ulasan"}
)
st.plotly_chart(fig5)

# === Section 6: Proporsi Tipe Pembayaran ===
st.subheader("💳 Proporsi Tipe Pembayaran")
payment_types = filtered_data['payment_type'].value_counts()

fig6 = px.pie(
    names=payment_types.index,
    values=payment_types.values,
    title="Distribusi Tipe Pembayaran",
    hole=0.4
)
st.plotly_chart(fig6)

# === Section 7: Pendapatan Berdasarkan Kategori Produk ===
st.subheader("💰 Pendapatan Berdasarkan Kategori Produk")
category_revenue = filtered_data.groupby('product_category_name_english')['price'].sum().sort_values(ascending=False).head(10)

fig7 = px.bar(
    x=category_revenue.values,
    y=category_revenue.index,
    orientation='h',
    labels={"x": "Total Penjualan (BRL)", "index": "Kategori Produk"},
    title="Pendapatan Top 10 Kategori Produk"
)
fig7.update_layout(yaxis=dict(categoryorder='total ascending'))
st.plotly_chart(fig7)
