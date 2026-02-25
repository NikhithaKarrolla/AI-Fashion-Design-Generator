import streamlit as st
from design_generator import generate_design
from feature_extractor import extract_features
from recommender import recommend

st.title("AI Fashion Design Generator")

prompt = st.text_input("Enter your clothing design")

if st.button("Generate Design"):

    with st.spinner("Generating AI Design... Please wait ⏳"):

        img = generate_design(prompt)

    st.success("Design Generated Successfully!")

    st.image(img)

    st.write("Finding Similar Affordable Products...")

    feat = extract_features(img)

    results = recommend(feat)

    st.subheader("Recommended Affordable Products")

    for r in results:
        st.image(r)