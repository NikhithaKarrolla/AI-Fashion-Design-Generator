from sklearn.neighbors import NearestNeighbors
import pickle
from price_filter import get_affordable_products

features = pickle.load(open("model_files/features.pkl","rb"))
images = pickle.load(open("model_files/images.pkl","rb"))

model = NearestNeighbors(n_neighbors=10)
model.fit(features)

def recommend(generated_feature):

    distances, indices = model.kneighbors([generated_feature])

    rec_images = []

    for i in indices[0]:
        rec_images.append(images[i])

    affordable = get_affordable_products(rec_images)

    return affordable[:5]