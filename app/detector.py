from ultralytics import YOLO
import cv2
import os

model = YOLO("models/best.pt")

def detect_plate(img, save_dir="results"):
    # Kiểm tra thư mục "results" có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    results = model(img)
    
    # Duyệt qua các kết quả nhận diện
    for result in results:
        for i, box in enumerate(result.boxes.xyxy):  # enumerate để tạo tên ảnh duy nhất
            x1, y1, x2, y2 = map(int, box)  # Chuyển đổi tọa độ về kiểu int
            plate_img = img[y1:y2, x1:x2]  # Cắt ảnh biển số
            
            # Tạo tên file để lưu ảnh đã cắt
            file_name = f"plate_{i+1}.png"
            save_path = os.path.join(save_dir, file_name)
            
            # Lưu ảnh đã cắt vào thư mục "results"
            cv2.imwrite(save_path, plate_img)
            print(f"Saved cropped plate image to {save_path}")
            
            return plate_img  # Trả về ảnh đã cắt đầu tiên
    print("no image")
    return None 
    
    