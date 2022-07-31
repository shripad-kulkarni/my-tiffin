import re
from ModulePackage.connection import mydb

class Customer:
    def __init__(self,cname,cemail,cmobile,caddress,cpass):
        myCursor = mydb.cursor()
        query = 'insert into customer(cname,cemail,cmobile,caddress,cpass)values(%s,%s,%s,%s,%s)'
        val = (cname,cemail,cmobile,caddress,cpass)
        myCursor.execute(query,val)
        mydb.commit()
        
    def checkValidCustomer(email,password):
        myCursor = mydb.cursor()
        query = 'select * from customer where cemail=%s and cpass=%s'
        val = (email,password)
        myCursor.execute(query,val)
        result = myCursor.fetchall()
        if result==[]:
            return False
        else:
            return True
        
    def checkCustomerExists(email):
        myCursor = mydb.cursor()
        query = f"select * from customer where cemail='{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result==[]:
            return False
        else:
            return True

    def getCustomer(email):
        myCursor = mydb.cursor()
        query = f"select * from customer where cemail = '{email}'"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def updateCustomer(email,name,mobile,address,password):
        myCursor = mydb.cursor()
        query = f"update customer set cname='{name}',cmobile='{mobile}',caddress='{address}',cpass='{password}' where cemail='{email}'"
        myCursor.execute(query)
        mydb.commit()