from tensorflow import keras

model = keras.models.load_model("app/ml_model/model.h5", compile=False)

model.save("app/ml_model/model.keras")

print("Converted successfully")