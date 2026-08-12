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
backend_url = "https://food-delivery-2-pr16.onrender.com/foods"

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
                key=f"cart_{food['id']}"
            )

            st.divider()

    else:
        st.error(
            f"Backend returned an error. Status code: {response.status_code}"
        )

except requests.exceptions.RequestException as e:
    st.error("❌ Cannot connect to FastAPI backend.")
    st.write("Please check whether your backend URL is working.")
    st.write(e)
