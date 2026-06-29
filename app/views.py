
import tensorflow as tf
import keras
import base64

print("TensorFlow:", tf.__version__)
print("Keras:", keras.__version__)

from django.core.files.base import ContentFile
from django.shortcuts import render
from .models import PlantDisease
from .predict import predict_disease


def index(request):

    results = []

    if request.method == 'POST':

        print("POST request received")

        captured_data = request.POST.get("captured_data")

        if captured_data:

            print("Camera image received")

            format, imgstr = captured_data.split(';base64,')

            ext = format.split('/')[-1]

            image_file = ContentFile(
                base64.b64decode(imgstr),
                name=f"captured.{ext}"
            )

            images = [image_file]

        else:

            images = request.FILES.getlist('images')

            print("Images:", images)
            print("Number of images:", len(images))

        for img in images:

            disease = PlantDisease.objects.create(
                image=img
            )

            prediction = predict_disease(
                disease.image.path
            )

            disease.prediction = prediction["disease"]
            disease.save()

            results.append({
                "image_url": disease.image.url,
                "disease": prediction["disease"],
                "confidence": prediction["confidence"],
                "cause": prediction["cause"],
                "symptoms": prediction["symptoms"],
                "prevention": prediction["prevention"]
            })
            print(results)

    return render(
        request,
        'index.html',
        {
            'results': results
        }
    )