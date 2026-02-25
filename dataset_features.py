import os
import pickle
from feature_extractor import extract_features

image_folder = "dataset/product_images"

features = []
img_paths = []

for img in os.listdir(image_folder):

    img_path = os.path.join(image_folder, img)

    try:
        feat = extract_features(img_path)
        features.append(feat)
        img_paths.append(img_path)
        print("Processed:", img)

    except:
        print("Error in:", img)

pickle.dump(features, open("model_files/features.pkl","wb"))
pickle.dump(img_paths, open("model_files/images.pkl","wb"))

print("Feature Extraction Completed")