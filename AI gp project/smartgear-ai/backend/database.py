import sqlite3

def init_db():
    conn = sqlite3.connect("smartgear.db")
    cursor = conn.cursor()
    
    # Drop the old table so we can start fresh with 10 items
    cursor.execute("DROP TABLE IF EXISTS inventory")
    
    cursor.execute('''
        CREATE TABLE inventory (
            item_id TEXT PRIMARY KEY,
            item_type TEXT NOT NULL,
            status TEXT NOT NULL,
            borrower_id TEXT
        )
    ''')
    
    # Insert the 10 sports items the AI already knows
    items = [
        ('B01', 'Sports Ball', 'borrowed', 'student_123'),
        ('R01', 'Tennis Racket', 'borrowed', 'student_456'),
        ('F01', 'Frisbee', 'borrowed', 'student_789'),
        ('B02', 'Baseball Bat', 'borrowed', 'student_101'),
        ('G01', 'Baseball Glove', 'borrowed', 'student_102'),
        ('S01', 'Skateboard', 'borrowed', 'student_103'),
        ('S02', 'Surfboard', 'borrowed', 'student_104'),
        ('S03', 'Snowboard', 'borrowed', 'student_105'),
        ('S04', 'Skis', 'borrowed', 'student_106'),
        ('K01', 'Kite', 'borrowed', 'student_107')
    ]
    
    cursor.executemany("INSERT INTO inventory VALUES (?, ?, ?, ?)", items)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database rebuilt with 10 items successfully.")