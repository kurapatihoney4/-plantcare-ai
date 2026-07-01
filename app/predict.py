import os
from tensorflow import keras
from tensorflow.keras.layers import BatchNormalization
import numpy as np
from PIL import Image
from tensorflow.keras.utils import load_img, img_to_array


class CompatBatchNormalization(BatchNormalization):
    def __init__(self, **kwargs):
        kwargs.pop('renorm', None)
        kwargs.pop('renorm_clipping', None)
        kwargs.pop('renorm_momentum', None)
        super().__init__(**kwargs)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "model.keras")

model = None

def get_model():
    global model
    if model is None:
        with keras.saving.custom_object_scope({'BatchNormalization': CompatBatchNormalization}):
            model = keras.models.load_model(
                MODEL_PATH,
                compile=False
            )
    return model


classes = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry_(including_sour)___healthy',
    'Cherry_(including_sour)___Powdery_mildew',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___healthy',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___healthy',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___healthy',
    'Potato___Late_blight',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___healthy',
    'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___healthy',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]

disease_info = {

    "Apple___Apple_scab": {
        "cause": "Venturia inaequalis fungus",
        "symptoms": "Dark olive-green spots on leaves and fruits",
        "prevention": "Remove infected leaves and apply fungicides"
    },

    "Apple___Black_rot": {
        "cause": "Botryosphaeria obtusa fungus",
        "symptoms": "Dark circular lesions on fruits and leaves",
        "prevention": "Prune infected branches and maintain orchard sanitation"
    },

    "Apple___Cedar_apple_rust": {
        "cause": "Gymnosporangium fungus",
        "symptoms": "Orange-yellow spots on leaves",
        "prevention": "Remove nearby cedar trees and use fungicides"
    },

    "Apple___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy leaves and fruits",
        "prevention": "Continue proper care"
    },

    "Blueberry___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy plant",
        "prevention": "Maintain regular irrigation and nutrition"
    },

    "Cherry_(including_sour)___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy foliage",
        "prevention": "Maintain plant health"
    },

    "Cherry_(including_sour)___Powdery_mildew": {
        "cause": "Powdery mildew fungus",
        "symptoms": "White powder-like growth on leaves",
        "prevention": "Improve air circulation and apply fungicides"
    },

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "cause": "Cercospora fungus",
        "symptoms": "Gray rectangular lesions on leaves",
        "prevention": "Crop rotation and resistant hybrids"
    },

    "Corn_(maize)___Common_rust_": {
        "cause": "Puccinia sorghi fungus",
        "symptoms": "Rust-colored pustules on leaves",
        "prevention": "Use resistant varieties"
    },

    "Corn_(maize)___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy corn plant",
        "prevention": "Maintain good field practices"
    },

    "Corn_(maize)___Northern_Leaf_Blight": {
        "cause": "Exserohilum turcicum fungus",
        "symptoms": "Long cigar-shaped lesions",
        "prevention": "Crop rotation and resistant hybrids"
    },

    "Grape___Black_rot": {
        "cause": "Guignardia bidwellii fungus",
        "symptoms": "Brown leaf spots and black fruit rot",
        "prevention": "Remove infected fruit and apply fungicides"
    },

    "Grape___Esca_(Black_Measles)": {
        "cause": "Complex fungal infection",
        "symptoms": "Leaf discoloration and fruit spots",
        "prevention": "Prune infected wood"
    },

    "Grape___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy grapevine",
        "prevention": "Regular vineyard management"
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "cause": "Isariopsis fungus",
        "symptoms": "Brown leaf spots",
        "prevention": "Use fungicides and proper pruning"
    },

    "Orange___Haunglongbing_(Citrus_greening)": {
        "cause": "Bacterial infection spread by psyllids",
        "symptoms": "Yellow shoots and misshapen fruits",
        "prevention": "Control psyllids and remove infected trees"
    },

    "Peach___Bacterial_spot": {
        "cause": "Xanthomonas bacteria",
        "symptoms": "Dark spots on leaves and fruits",
        "prevention": "Use disease-free planting material"
    },

    "Peach___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy peach plant",
        "prevention": "Regular care"
    },

    "Pepper,_bell___Bacterial_spot": {
        "cause": "Xanthomonas bacteria",
        "symptoms": "Water-soaked leaf lesions",
        "prevention": "Use certified seeds and avoid overhead irrigation"
    },

    "Pepper,_bell___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy pepper plant",
        "prevention": "Maintain good cultivation practices"
    },

    "Potato___Early_blight": {
        "cause": "Alternaria solani fungus",
        "symptoms": "Brown concentric rings on leaves",
        "prevention": "Crop rotation and sanitation"
    },

    "Potato___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy potato plant",
        "prevention": "Maintain proper nutrition"
    },

    "Potato___Late_blight": {
        "cause": "Phytophthora infestans",
        "symptoms": "Dark water-soaked lesions",
        "prevention": "Use fungicides and certified seed"
    },

    "Raspberry___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy raspberry plant",
        "prevention": "Regular maintenance"
    },

    "Soybean___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy soybean plant",
        "prevention": "Good agricultural practices"
    },

    "Squash___Powdery_mildew": {
        "cause": "Powdery mildew fungus",
        "symptoms": "White powder on leaves",
        "prevention": "Improve airflow and use fungicides"
    },

    "Strawberry___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy strawberry plant",
        "prevention": "Maintain proper irrigation"
    },

    "Strawberry___Leaf_scorch": {
        "cause": "Fungal infection",
        "symptoms": "Reddish-purple leaf margins",
        "prevention": "Remove infected leaves"
    },

    "Tomato___Bacterial_spot": {
        "cause": "Xanthomonas bacteria",
        "symptoms": "Dark leaf and fruit spots",
        "prevention": "Use certified seeds"
    },

    "Tomato___Early_blight": {
        "cause": "Alternaria solani fungus",
        "symptoms": "Brown target-like spots",
        "prevention": "Crop rotation and sanitation"
    },

    "Tomato___healthy": {
        "cause": "No disease detected",
        "symptoms": "Healthy tomato plant",
        "prevention": "Continue proper care"
    },

    "Tomato___Late_blight": {
        "cause": "Phytophthora infestans",
        "symptoms": "Dark lesions on leaves and fruits",
        "prevention": "Avoid excess moisture and apply fungicides"
    },

    "Tomato___Leaf_Mold": {
        "cause": "Passalora fulva fungus",
        "symptoms": "Yellow spots and mold under leaves",
        "prevention": "Reduce humidity and improve ventilation"
    },

    "Tomato___Septoria_leaf_spot": {
        "cause": "Septoria lycopersici fungus",
        "symptoms": "Small circular spots with dark borders",
        "prevention": "Remove infected leaves and use fungicides"
    },

    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "cause": "Spider mite infestation",
        "symptoms": "Yellow speckling and webbing",
        "prevention": "Use miticides and maintain humidity"
    },

    "Tomato___Target_Spot": {
        "cause": "Corynespora cassiicola fungus",
        "symptoms": "Circular lesions with concentric rings",
        "prevention": "Improve airflow and apply fungicides"
    },

    "Tomato___Tomato_mosaic_virus": {
        "cause": "Tomato Mosaic Virus",
        "symptoms": "Mottled leaves and stunted growth",
        "prevention": "Use virus-free seeds and disinfect tools"
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "cause": "Whitefly-transmitted virus",
        "symptoms": "Yellow curled leaves",
        "prevention": "Control whiteflies and remove infected plants"
    }
}

    # Add remaining diseases here



def predict_disease(img_path):

    img = load_img(
        img_path,
        target_size=(224, 224)
    )

    img_array = img_to_array(img)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = img_array / 255.0

    # Check if image contains enough green pixels
    img_check = Image.open(img_path).convert("RGB")
    arr = np.array(img_check)

    green_pixels = np.sum(
        (arr[:, :, 1] > arr[:, :, 0]) &
        (arr[:, :, 1] > arr[:, :, 2])
    )

    green_ratio = green_pixels / (arr.shape[0] * arr.shape[1])

    # Reject non-leaf images
    if green_ratio < 0.30:
        return {
            "disease": "Not a Plant Leaf",
            "confidence": 0,
            "cause": "No plant leaf detected.",
            "symptoms": "N/A",
            "prevention": "Please upload a clear plant leaf image."
        }

    # Model prediction
    model = get_model()
    prediction = model.predict(img_array)

    confidence = float(np.max(prediction)) * 100

    # Reject unknown images
    if confidence < 80:
        return {
            "disease": "Unknown Image",
            "confidence": round(confidence, 2),
            "cause": "Image does not appear to be a supported plant leaf.",
            "symptoms": "N/A",
            "prevention": "Upload a clear image of a plant leaf."
        }

    predicted_class = classes[np.argmax(prediction)]

    info = disease_info.get(
        predicted_class,
        {
            "cause": "Information unavailable",
            "symptoms": "Information unavailable",
            "prevention": "Information unavailable"
        }
    )

    return {
        "disease": predicted_class,
        "confidence": round(confidence, 2),
        "cause": info["cause"],
        "symptoms": info["symptoms"],
        "prevention": info["prevention"]
    }