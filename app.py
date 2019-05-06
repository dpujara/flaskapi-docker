from flask import Flask
import logging as logger
from flaskext.mysql import MySQL
from datetime import datetime
import mysql.connector

logger.basicConfig(level="DEBUG")


flaskAppInstance = Flask(__name__)

mysql = MySQL()
mysql.init_app(flaskAppInstance)

if __name__ == '__main__':

    logger.debug("Starting Flask Server")    
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True,threaded=True)