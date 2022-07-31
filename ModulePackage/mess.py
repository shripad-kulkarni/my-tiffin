from unittest import result
from ModulePackage.connection import mydb


class Mess:

    def __init__(self, messname, ownername, messemail, messmobile,
                 messpassword, messaddress, messphoto, messlocation):
        myCursor = mydb.cursor()
        query = "insert into mess(messname, ownername,messemail,messmobile,messpassword,               messaddress, messphoto, messlocation) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (messname, ownername, messemail, messmobile, messpassword,
               messaddress, messphoto, messlocation)
        myCursor.execute(query, val)
        mydb.commit()

    def checkValidMess(email, password):
        myCursor = mydb.cursor()
        query = f"select * from mess where messemail='{email}' and messpassword='{password}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True

    def getMessDetails(email):
        myCursor = mydb.cursor()
        query = f"select * from mess where messemail='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result

    def checkMessExists(email):
        myCursor = mydb.cursor()
        query = f"select * from mess where messemail='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True
        
    def getmessorderdetails(email):
        myCursor = mydb.cursor()
        query = f"select * from orders where messemail='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
