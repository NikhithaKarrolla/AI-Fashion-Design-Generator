from sklearn.neighbors import NearestNeighbors
import pickle
from price_filter import get_affordable_products
import os

def recommend(generated_feature):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    features_path = os.path.join(BASE_DIR, "model_files", "features.pkl")
    images_path = os.path.join(BASE_DIR, "model_files", "images.pkl")

    features = pickle.load(open(features_path, "rb"))
    images = pickle.load(open(images_path, "rb"))

    model = NearestNeighbors(n_neighbors=10)
    model.fit(features)

    distances, indices = model.kneighbors([generated_feature])

    rec_images = []

    for i in indices[0]:
        rec_images.append(images[i])

    affordable = get_affordable_products(rec_images)

    return affordable[:5]