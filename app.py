import streamlit as st
import requests

# Page settings
st.set_page_config(
    page_title="Food Delivery App",
    page_icon="🍔"
)

# Title
st.title("🍔 Food Delivery App")

st.write("Welcome to our Food Delivery App!")

# Backend API URL
backend_url = "http://127.0.0.1:8000/foods"

# Get food data from backend
try:
    response = requests.get(backend_url)

    if response.status_code == 200:

        foods = response.json()

        st.subheader("🍽️ Available Food")

        for food in foods:

            st.write(f"### {food['name']}")
            st.write(f"💰 Price: ₹{food['price']}")

            st.button(
                "Add to Cart",
                key=food["id"]
            )

            st.divider()

    else:
        st.error("Backend is not responding.")

except requests.exceptions.ConnectionError:
    st.error("❌ Cannot connect to FastAPI backend.")
    st.write("Please make sure your backend is running.")
