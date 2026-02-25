import pandas as pd

df = pd.read_csv("dataset/cleaned_fashion_data.csv")

def get_affordable_products(image_paths):

    affordable = []

    for path in image_paths:

        img_id = path.split("/")[-1].split(".")[0]

        try:
            price = df[df['p_id'] == int(img_id)]['price'].values[0]

            if price <= 1500:
                affordable.append(path)

        except:
            pass

    return affordable