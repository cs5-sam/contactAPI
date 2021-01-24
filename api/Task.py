from flask import jsonify
from flask_restful import Resource, request
import logging as logger
import sqlite3

# PAGINATION FUNCTION
BOOKS_PER_SHELF = 10
def paginate_books(request,selection):
    page=request.args.get('page',1,type=int)
    start = (page-1)*BOOKS_PER_SHELF
    end=start+BOOKS_PER_SHELF

    books = [book.format() for book in selection]
    current_books= books[start:end]
    return current_books

class Task(Resource):

    #READ ALL CONTACT
    def get(self):
        logger.debug("GET method")
        conn = sqlite3.connect("task.sqlite3", check_same_thread=False)
        c = conn.cursor()
        args = request.args
        all_data = c.execute("SELECT * FROM contact").fetchall()
        if len(all_data) != 0:
            list_data = []
            for row in all_data:
                list_data.append(row)
            return {"success":True,
                "display":list_data}, 200
        else:
            return {"success":False,
            "message":"Contact Not Found"}, 200
    
    #CREATE NEW CONTACT
    def post(self):
        logger.debug("POST method")
        conn = sqlite3.connect("task.sqlite3", check_same_thread=False)
        c = conn.cursor()
        args = request.args
        # Checking Duplicate Email
        exists = c.execute("SELECT * FROM contact WHERE email=:email",{"email":args.get("email")}).fetchall()
        if len(exists) != 0:
            return {"message":"Contact Already Exists"}, 200
        else:
            c.execute("INSERT INTO contact (email, name, phone) VALUES (:email, :name, :phone)", {"email": args.get("email"), "name": args.get("name"), "phone": args.get("phone")})
            conn.commit()
            return {"message":"Contact Created"}, 200
    
    #UPDATE EXISTING CONTACT
    def put(self):
        logger.debug("PUT method")
        conn = sqlite3.connect("task.sqlite3", check_same_thread=False)
        c = conn.cursor()
        args = request.args
        c.execute("UPDATE contact SET name=:name, phone=:phone WHERE email=:email",{"email":args.get("email"),"name":args.get("name"),"phone":args.get("phone")})
        conn.commit()
        return {"message":"Contact Updated"}, 200
    
    #DELETE
    def delete(self):
        logger.debug("DELETE method")
        conn = sqlite3.connect("task.sqlite3", check_same_thread=False)
        c = conn.cursor()
        args = request.args.get("email")
        c.execute("DELETE FROM contact WHERE email=:email",{"email":args})
        conn.commit()
        return {"message":"Deleted"}, 200