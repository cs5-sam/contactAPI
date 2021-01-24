from flask_restful import Api

from app import app
from .Task import Task
from .TaskById import TaskById
restServer = Api(app)

# FOR CREATE, UPDATE, DELETE (POST,PUT,DELETE)
# http://localhost:5000/task?args
restServer.add_resource(Task,"/api/task")
# FOR SEARCH (GET)
# https://localhost:5000/task/search?args
restServer.add_resource(TaskById,"/api/task/search")