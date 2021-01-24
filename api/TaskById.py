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

class TaskById(Resource):

    #R
    def get(self):
        logger.debug("GET method")
        conn = sqlite3.connect("task.sqlite3", check_same_thread=False)
        c = conn.cursor()
        args = request.args
        all_data = c.execute("SELECT * FROM contact WHERE email=:email and name=:name",{"email":args.get("email"),"name":args.get("name")}).fetchall()
        if len(all_data) != 0:
            list_data = []
            for row in all_data:
                list_data.append(row)
            return {"success":True,
                "message":"Contact Found",
                "display":list_data}, 200
        else:
            return {"success":False,
            "message":"Contact Not Found"}, 200