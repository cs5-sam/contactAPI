from flask import Flask, request, Response
import logging as logger
import sqlite3

logger.basicConfig(level="DEBUG")

app = Flask(__name__)

if __name__ == '__main__':
    from api import *
    logger.debug("Starting the application")
    app.run(debug=True, use_reloader=True)
