# pip install mysql-connector
# pip install mysql-connector-python
import mysql.connector

# starting connection to the database
def get_db():
    db = mysql.connector.connect(
        host="localhost",
        database='hospital',
        user="root",
        password="<password>"
        )
    return db

# closing connection to the database
def close_db(db):
    if db:
        db.close()

# getting version of the database
def db_version():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("select version()")
    version = cursor.fetchone()
    print(version)
    close_db()

# getting hospital info from hospital id
def hospital_info(hospital_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""select * from hospital where hospital_id = %s""", (hospital_id,))
    h_info = cursor.fetchall()
    for detail in h_info:
        print(detail[0], detail[1], detail[2])
    close_db()

# getting doctor info from doctor id
def doctor_info(doctor_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""select * from doctor where doctor_id = %s""", (doctor_id,))
    d_info = cursor.fetchall()
    for detail in d_info:
        print(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6])
    close_db()

# updating doctor speciality
def update_doctor_speciality(speciality, doctor_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""update doctor set speciality = %s where doctor_id = %s """, (speciality, doctor_id))
    db.commit()
    close_db()

# getting doctor from speciality and salary
def doctor_speciality_salary(speciality, salary):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""select * from doctor where speciality = %s and salary > %s""", (speciality, salary))
    d_speciality_salary = cursor.fetchall()
    for detail in d_speciality_salary:
        print(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6])
    close_db()

# getting doctors from hospital id
def hospital_doctors(hospital_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""select * from doctor where hospital_id = %s""", (hospital_id,))
    d_list = cursor.fetchall()
    for detail in d_list:
        print(detail[0], detail[1], detail[2], detail[3], detail[4], detail[5], detail[6])
    close_db()

# updating doctor experience
def update_doctor_experience(experience, doctor_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""update doctor set experience = %s where doctor_id = %s """, (experience, doctor_id))
    db.commit()
    close_db()