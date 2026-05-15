from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class_names = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'P', 'R', 'S', 'T', 'V', 'W', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'Õ', 'SPACE'
]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_trained_model():
    model = models.efficientnet_v2_s(weights=None)
    num_ftrs = model.classifier[1].in_features
    
    model.classifier[1] = nn.Linear(num_ftrs, 27) 
    
    model.load_state_dict(torch.load("model_effnet.pth", map_location=device))
    model.to(device)
    model.eval()
    return model

model = load_trained_model()

preprocess = transforms.Compose([
    transforms.Resize((260, 260)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    image = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    input_tensor = preprocess(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, preds = torch.max(probabilities, 1)
    
    return {
        "prediction": class_names[preds[0].item()],
        "confidence": f"{confidence[0].item()*100:.2f}%"
    }

@app.get("/")
def home():
    return {"status": "API is online!"}