import mysql.connector
from flask import jsonify
import datetime

class DB():
  def __init__(self):
    self.mydb = mysql.connector.connect(
                                        host="localhost",
                                        user="root",
                                        password="",
                                        database="Suhaila"
                                        )
    
  def getConnectionDB(self):
    return self.mydb  
        
  def getData(self):
    mycursor = self.mydb.cursor()
    mycursor.execute("SELECT * FROM sensor")
    result = mycursor.fetchall()
    return result
    
    
    
    
  def insert(self,data):
        
    print("jsonify = ", (data["name"]))
    cursor = self.mydb.cursor()


    now = datetime.datetime.now()
    
    query = 'INSERT INTO sensor (`sensor`, `Data`, `date`) VALUES (%s, %s, %s)'
    values = (data["name"], data["Data"], str(now.strftime('%m/%d/%Y %H:%M:%S')))
    cursor.execute(query, values)


    self.mydb.commit()
    self.mydb.close()

    return 'Data added successfully'
    
