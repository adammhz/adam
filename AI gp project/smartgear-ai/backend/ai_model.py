from ultralytics import YOLO
from PIL import Image
import io

# Load the pre-trained, lightweight YOLOv8 nano model
# It will automatically download a small file (yolov8n.pt) the first time you run it
model = YOLO('yolov8n.pt') 

def predict_image(image_bytes):
    # Convert raw bytes into an image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Run the image through YOLOv8
    results = model(image)
    
    # Extract the names of objects the AI detected in the image
    detected_classes = []
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            detected_classes.append(class_name)
            
    # List of the 10 items our system cares about
    valid_sports_gear = [
        'sports ball', 'tennis racket', 'frisbee', 'baseball bat', 
        'baseball glove', 'skateboard', 'surfboard', 'snowboard', 'skis', 'kite'
    ]
    
    # Check if the AI saw any of our 10 items
    for item in detected_classes:
        if item in valid_sports_gear:
            return item.title() # Capitalizes it (e.g., 'sports ball' -> 'Sports Ball')
            
    # If it detects a person, a dog, a car, etc., but no sports gear:
    return "Unknown Object"