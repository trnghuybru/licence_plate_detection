import cv2
import numpy as np
from paddleocr import PaddleOCR

def preprocess_image(plate_img):
    # Phóng to ảnh để giữ chi tiết (tăng kích thước lên gấp 2 lần hoặc hơn)
    height, width = plate_img.shape[:2]
    scale_factor = max(2, 300 / min(height, width))
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    enlarged = cv2.resize(plate_img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    # Chuyển ảnh sang grayscale
    gray = cv2.cvtColor(enlarged, cv2.COLOR_BGR2GRAY)
    
    # Áp dụng Gaussian Blur nhẹ để giảm nhiễu mà không làm mất chi tiết chữ
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Binarization bằng Otsu threshold
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Dilation nhẹ để làm đậm chữ, giúp OCR nhận diện tốt hơn
    kernel = np.ones((2, 2), np.uint8)
    binary = cv2.dilate(binary, kernel, iterations=1)
    
    return binary

# Khởi tạo PaddleOCR reader
ocr = PaddleOCR(use_angle_cls=False, lang='en')

def recognize_text(plate_img):
    # Tiền xử lý ảnh
    processed_img = preprocess_image(plate_img)
    
    # Nhận diện văn bản từ ảnh đã xử lý
    result = ocr.ocr(processed_img, cls=False)  # Xóa tham số text_threshold
    
    # Gộp các kết quả nhận diện được
    detected_text = []
    for line in result:
        if line:
            for word_info in line:
                detected_text.append(word_info[1][0])
    
    return " ".join(detected_text).strip()
