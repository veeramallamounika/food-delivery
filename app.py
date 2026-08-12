import streamlit as st
import requests

st.set_page_config(
    page_title="Food Delivery App",
    page_icon="🍔"
)

st.title("🍔 Food Delivery App")
st.write("Welcome to our Food Delivery App!")

backend_url = "https://food-delivery-1-p2kg.onrender.com"

try:
    response = requests.get(f"{backend_url}/foods", timeout=30)
    response.raise_for_status()

    foods = response.json()

    st.subheader("Available Food")

    for food in foods:
        st.write(f"### {food['name']}")
        st.write(f"Price: ₹{food['price']}")
        st.button("Add to Cart", key=food["id"])

except requests.exceptions.RequestException as e:
    st.error("Unable to connect to the backend.")
    st.write(e)
