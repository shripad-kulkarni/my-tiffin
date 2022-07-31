from ModulePackage import mess
from ModulePackage.connection import mydb

class Menu:
    def __init__(self,messid,items,price):
        myCursor = mydb.cursor()
        query = 'insert into menu(messemail,items,price)values(%s,%s,%s)'
        val = (messid,items,price)
        myCursor.execute(query,val)
        mydb.commit()
    
       
    def getMenus():
        myCursor = mydb.cursor()
        query = "select mno,messname,messaddress,messphoto,messlocation,items,price from menu INNER JOIN mess  ON menu.messemail = mess.messemail"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def getDetailMenu(mno):
        myCursor = mydb.cursor()
        query = f"select items,price,messname,messmobile from menu INNER JOIN mess ON menu.messemail = mess.messemail where mno={mno}"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def getMessEmail(mno):
        myCursor = mydb.cursor()
        query = f"select messemail from menu where mno={mno}"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def viewmessmenu(email):
        myCursor = mydb.cursor()
        query = f"select items,price from menu where messemail='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result