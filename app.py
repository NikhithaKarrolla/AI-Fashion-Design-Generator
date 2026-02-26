import streamlit as st
from design_generator import generate_design
from recommender import recommend

st.title("AI Fashion Design Generator 👗")

prompt = st.text_input("Enter your clothing design")

if st.button("Generate Design"):

    with st.spinner("Generating AI Design... Please wait ⏳"):
        generated_feature, img_path = generate_design(prompt)

    st.success("Design Generated Successfully!")

    st.image(img_path)

    st.write("Finding Similar Affordable Products...")

    results = recommend(generated_feature)

    st.subheader("Recommended Affordable Products")

    for r in results:
        st.image(r)