from flask_restful import Resource
import logging as logger
from datetime import datetime
from app import mysql
import mysql.connector
import json
class ProjectAPI(Resource):

    def get(self):
        def myconverter(o):
            if isinstance(o, datetime):
                return o.__str__()

        con = mysql.connector.connect(host='192.168.99.100',database='dev',user='root',password='root',auth_plugin='mysql_native_password')
        cur = con.cursor()
        logger.info('Start reading database')
        cur.execute("SELECT * from logs")
        row_headers=[x[0] for x in cur.description]
        data = cur.fetchall()
        json_data=[]
        for result in data:
            json_data.append(dict(zip(row_headers,result)))
        cur.close()
        return json.dumps(json_data,default= myconverter),200

    def post(self):
        now = datetime.now()
        con = mysql.connector.connect(host='192.168.99.100',database='dev',user='root',password='root',auth_plugin='mysql_native_password')
        cur = con.cursor()
        message = "logger.debug"
        server_time = now.strftime("%H:%M:%S")
        server_date = now.strftime("%m/%d/%y")
        log_type = "Debug"
        platform = "Chrome"
        cur.execute("INSERT INTO logs(message, server_time,server_date,log_type,platform) VALUES (%s, %s,%s,%s,%s)", (message, server_time,server_date,log_type,platform))
        con.commit()
        cur.close()
        return {"message":"inside post method"},200

    
    