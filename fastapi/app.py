from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector as mysql


app = FastAPI(title="Student Management API")


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():
    # क्योंकि आपने 'as mysql' किया है, इसलिए यहाँ सीधे mysql.connect काम करेगा
    return mysql.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="college12"
    )


# =========================================================
# CREATE TABLE
# =========================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INTEGER,
        course VARCHAR(100)
    )
    """

    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()


create_table()


# =========================================================
# PYDANTIC MODEL
# =========================================================

class Student(BaseModel):
    name: str
    age: int
    course: str


class StudentUpdate(BaseModel):
    course: str





# =========================================================
# ADD STUDENT
# =========================================================

@app.post("/students")
def add_student(student: Student,name,age,course):

    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
    INSERT INTO students (name, age, course)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, age, course))

    student_id = cursor.lastrowid

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "Student added successfully!",
        "student_id": student_id
    }



# =========================================================
# GET SINGLE STUDENT
# =========================================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT id, name, age, course
    FROM students
    WHERE id = %s
    """

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    cursor.close()
    conn.close()

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student not found!"
        )

    return {
        "id": student[0],
        "name": student[1],
        "age": student[2],
        "course": student[3]
    }


# =========================================================
# UPDATE STUDENT
# =========================================================

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentUpdate
):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    UPDATE students
    SET course = %s
    WHERE id = %s
    """

    cursor.execute(
        query,
        (student.course, student_id)
    )

    conn.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    conn.close()

    if updated_rows == 0:

        raise HTTPException(
            status_code=404,
            detail="Student not found!"
        )

    return {
        "message": "Student updated successfully!"
    }


# =========================================================
# DELETE STUDENT
# =========================================================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM students
    WHERE id = %s
    """

    cursor.execute(query, (student_id,))

    conn.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    conn.close()

    if deleted_rows == 0:

        raise HTTPException(
            status_code=404,
            detail="Student not found!"
        )

    return {
        "message": "Student deleted successfully!"
    }