from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
from app.detector import detect_plate
from app.ocr import recognize_text

app = FastAPI()

@app.post("/detect_plate/")
async def detect_plate_api(file: UploadFile = File(...)):
    # Đọc ảnh từ file upload
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Nhận diện biển số
    plate_img = detect_plate(img)

    if plate_img is None:
        return {"error": "No license plate detected"}

    # OCR nhận diện ký tự
    plate_text = recognize_text(plate_img)
    
    return {"license_plate": plate_text}
