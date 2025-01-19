from cffi.cffi_opcode import CLASS_NAME
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
from typing import List
import nest_asyncio  # Fixes nested asyncio loop issues with PyCharm debugger
import tensorflow as tf


# Apply nest_asyncio to avoid conflicts with PyCharm's debugger
nest_asyncio.apply()

# Define a FastAPI app
app = FastAPI()
MODEL = tf.keras.models.load_model("../models/7")
CLASS_NAME = ["Early Blight","Late_Blight", "Healthy"]

# Health check endpoint
@app.get("/ping")
async def ping():
    return {"message": "Hello, I am alive"}


def read_file_as_image(data) -> np.ndarray:
    try:
        image = np.array(Image.open(BytesIO(data)))
        return image
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid image file")


# Prediction endpoint placeholder that handles file uploads
@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    try:
        # Read image file
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, axis=0)
        predictions = MODEL.predict(img_batch)# Placeholder prediction logic
        predicted_class = CLASS_NAME[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except HTTPException as e:
        raise e  # Propagate HTTP exceptions
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


# Run the server if this is the main module
if __name__ == "__main__":
    # Use uvicorn to run the app
    uvicorn.run(app, host="127.0.0.1", port=8001)
