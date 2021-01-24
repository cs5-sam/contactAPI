from flask_restful import Api

from app import app
from .Task import Task
from .TaskById import TaskById
restServer = Api(app)

# FOR CREATE, UPDATE, DELETE (POST,PUT,DELETE)
restServer.add_resource(Task,"/api/task")
# FOR SEARCH (GET)
restServer.add_resource(TaskById,"/api/task/search")