import streamlit as st
import pandas as pd
import altair as alt

# Load data (gantilah dengan metode pemuatan data yang sesuai)
@st.cache_data
def load_data():
    # Contoh data, ganti dengan data asli
    all_data = pd.DataFrame({
        'product_id': ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"],
        'order_item_id': [100, 95, 90, 85, 80, 75, 70, 65, 60, 55]
    })
    return all_data

df = load_data()

# Proses data
sum_order_items_df = df.groupby("product_id")["order_item_id"].count().reset_index()
sum_order_items_df = sum_order_items_df.rename(columns={"order_item_id": "products"})
sum_order_items_df = sum_order_items_df.sort_values(by="products", ascending=False)
sum_order_items_df = sum_order_items_df.head(10)

# Streamlit UI
st.title("Analisis Produk Terlaris")
st.write("Berikut adalah 10 produk terlaris berdasarkan jumlah penjualan.")

# Visualisasi dengan Altair
chart = alt.Chart(sum_order_items_df).mark_bar().encode(
    x=alt.X('products', title='Jumlah Produk Terjual'),
    y=alt.Y('product_id:N', sort='-x', title='Produk ID'),
    color=alt.Color('products:Q', scale=alt.Scale(scheme='blues'), legend=None),
    tooltip=['product_id', 'products']
).properties(
    title='Perbandingan Jumlah Produk Terjual Antar Produk (Top 10)',
    width=600,
    height=400
)

st.altair_chart(chart)
