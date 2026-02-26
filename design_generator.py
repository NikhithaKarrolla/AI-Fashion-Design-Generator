import streamlit as st
from diffusers import AutoPipelineForText2Image
import torch

@st.cache_resource
def load_model():
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sd-turbo",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")
    return pipe

def generate_design(prompt):
    pipe = load_model()
    image = pipe(prompt).images[0]
    image.save("generated/generated_design.png")
    return "generated/generated_design.png"