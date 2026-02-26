import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np

model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*list(model.children())[:-1])
model.eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

def extract_features(img_path):
    img = Image.open(img_path).convert('RGB')
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        features = model(img)

    return features.squeeze().numpy()