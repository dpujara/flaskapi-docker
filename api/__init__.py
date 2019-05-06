from flask_restful import Api
from app import flaskAppInstance
from .ProjectAPI import ProjectAPI
from .TestAPI import TestAPI


restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(ProjectAPI,"/")
restServerInstance.add_resource(TestAPI,"/test")