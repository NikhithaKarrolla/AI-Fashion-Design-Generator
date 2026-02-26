import numpy as np
from PIL import Image, ImageDraw
import os

def generate_design(prompt):

    # create generated folder if not exists
    if not os.path.exists("generated"):
        os.makedirs("generated")

    # simulate AI generated feature vector (2048 same as ResNet50)
    generated_feature = np.random.rand(2048)

    # create dummy generated design image
    img = Image.new('RGB', (256,256), color=(200,200,200))
    draw = ImageDraw.Draw(img)
    draw.text((40,120), "AI Design", fill=(0,0,0))

    img_path = "generated/generated_design.png"
    img.save(img_path)

    return generated_feature, img_path