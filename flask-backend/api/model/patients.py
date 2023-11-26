import db
import pymysql

# def connect_db():
#     # You should define your db_config with the database connection settings
#     return pymysql.connect(**db_config)

# Function to get all patients
def get_patients():
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
    finally:
        con.close()

# Function to get a single patient by ID
def get_patient(pat_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE PAT_ID = %s", (pat_id,))
            return cursor.fetchone()
    finally:
        con.close()

# Function to create a new patient
def create_patient(data):
    con = db.get_connection()
    try:
        print(data)
        with con.cursor() as cursor:
            cursor.execute("INSERT INTO patients (PAT_BIRTHDATE, PAT_GENRE, PAT_ADDRESS, PAT_PHONE_NUMBER, PAT_OTHER_INFO, PAT_IDCC, users_USER_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (data['birthdate'], data['genre'], data['address'], data['phone_number'], data['other_info'], data['idcc'], data['user_id']))
            con.commit()
            return cursor.lastrowid
    finally:
        con.close()

# Function to update a patient by ID
def update_patient(pat_id, data):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("UPDATE patients SET PAT_BIRTHDATE = %s, PAT_GENRE = %s, PAT_ADDRESS = %s, PAT_PHONE_NUMBER = %s, PAT_OTHER_INFO = %s, PAT_IDCC = %s, users_USER_ID = %s WHERE PAT_ID = %s",
                           (data['birthdate'], data['genre'], data['address'], data['phone_number'], data['other_info'], data['idcc'], data['user_id'], pat_id))
            con.commit()
            return cursor.rowcount
    finally:
        con.close()

# Function to delete a patient by ID
def delete_patient(pat_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("DELETE FROM patients WHERE PAT_ID = %s", (pat_id,))
            con.commit()
            return cursor.rowcount
    finally:
        con.close()
