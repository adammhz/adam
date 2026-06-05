from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from ai_model import predict_image

app = FastAPI()

# Allow the HTML frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_expected_item(item_id):
    """Fetch the correct item type from the SQLite database."""
    conn = sqlite3.connect("smartgear.db")
    cursor = conn.cursor()
    cursor.execute("SELECT item_type FROM inventory WHERE item_id = ?", (item_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

@app.post("/return/{item_id}")
async def return_equipment(item_id: str, file: UploadFile = File(...)):
    # 1. Read the uploaded image and pass it to YOLOv8
    image_bytes = await file.read()
    ai_detected_item = predict_image(image_bytes)
    
    # 2. Ask the database what this item ID is supposed to be
    expected_item = get_expected_item(item_id)
    
    if not expected_item:
        return {"status": "error", "message": f"Item ID {item_id} not found in database."}

    # 3. Compare the AI's vision with the Database's reality
    if ai_detected_item == expected_item:
        # Success! Update the database to show it was returned
        conn = sqlite3.connect("smartgear.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE inventory SET status = 'available' WHERE item_id = ?", (item_id,))
        conn.commit()
        conn.close()
        
        return {"status": "success", "message": f"{ai_detected_item} returned successfully!"}
    else:
        # AI mismatch error
        return {"status": "error", "message": f"Expected {expected_item} but AI detected {ai_detected_item}."}