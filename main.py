# app.py

import streamlit as st
from menu import menu
from PIL import Image
import os

st.set_page_config(page_title="Restaurant Menu", layout="wide")

st.title("🍽️ Welcome to Desi Delight Menu")
st.markdown("Enjoy our freshly prepared items with love 💖🙌")

for category, items in menu.items():
    st.subheader(f"📌 {category}")
    cols = st.columns(2)

    for idx, item in enumerate(items):
        with cols[idx % 2]:
            # Load image from images folder
            image_path = f"./images/{item['img']}"
            image = Image.open(image_path)

            # ✅ Updated here
            st.image(image, use_container_width=True)

            st.markdown(
                f"""
                <div style='padding:10px; background:##999999; border-radius:10px; margin-top:-10px;'>
                    <h4 style='margin-bottom:0;'>{item['name']}</h4>
                    <p style='color:gray;'>Price: Rs. {item['price']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")

st.caption("Made with ❤️ in Pakistan")
st.caption("Iqra Ikram")

