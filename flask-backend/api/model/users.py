import functools
import db
import pymysql



def connect_db():
    return pymysql.connect(**db_config)

# Funciones para la tabla 'users'
def get_users():
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
    finally:
        con.close()

def get_user(user_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE USER_ID = %s", (user_id,))
            return cursor.fetchone()
    finally:
        con.close()

def create_user(data):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("INSERT INTO users (USER_NAME, USER_LAST_NAME, USER_EMAIL, USER_PASSWORD, USER_PROFILE) VALUES (%s, %s, %s, %s, %s)",
                           (data['name'], data['last_name'], data['email'], data['password'], data['profile']))
            con.commit()
            return cursor.lastrowid
    finally:
        con.close()

def update_user(user_id, data):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("UPDATE users SET USER_NAME = %s, USER_LAST_NAME = %s, USER_EMAIL = %s, USER_PASSWORD = %s, USER_PROFILE = %s WHERE USER_ID = %s",
                           (data['name'], data['last_name'], data['email'], data['password'], data['profile'], user_id))
            con.commit()
            return cursor.rowcount
    finally:
        con.close()

def delete_user(user_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE USER_ID = %s", (user_id,))
            con.commit()
            return cursor.rowcount
    finally:
        con.close()


def get_patients():
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
    finally:
        con.close()

def get_patient(pat_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE PAT_ID = %s", (pat_id,))
            return cursor.fetchone()
    finally:
        con.close()

def create_patient(data):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            # Asegúrate de que las claves en 'data' coincidan con las columnas de tu tabla.
            cursor.execute("INSERT INTO patients (PAT_BIRTHDATE, PAT_GENRE, PAT_ADDRESS, PAT_PHONE_NUMBER, PAT_OTHER_INFO, PAT_IDCC, users_USER_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (data['birthdate'], data['genre'], data['address'], data['phone_number'], data['other_info'], data['idcc'], data['user_id']))
            con.commit()
            return cursor.lastrowid
    finally:
        con.close()

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

def delete_patient(pat_id):
    con = db.get_connection()
    try:
        with con.cursor() as cursor:
            cursor.execute("DELETE FROM patients WHERE PAT_ID = %s", (pat_id,))
            con.commit()
            return cursor.rowcount
    finally:
        con.close()