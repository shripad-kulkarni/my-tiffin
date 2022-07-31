from ModulePackage.connection import mydb

class Admin:
    def checkValidAdmin(email,password):
        myCursor = mydb.cursor()
        query = f"select * from admin where adminid='{email}' and adminpass='{password}'"  
        myCursor.execute(query)
        result = myCursor.fetchall()
        if result == []:
            return False
        else:
            return True
        
    def adminviewmess():
        myCursor = mydb.cursor()
        query = f"select * from mess"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def adminviewcustomer():
        myCursor = mydb.cursor()
        query = f"select * from customer"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def adminvieworders():
        myCursor = mydb.cursor()
        query = f"select * from orders"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
        
    def countadminviewmess():
        myCursor = mydb.cursor()
        query = f"select count(*) from mess"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def countadminviewcustomer():
        myCursor = mydb.cursor()
        query = f"select count(*) from customer"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result
    
    def countadminvieworders():
        myCursor = mydb.cursor()
        query = f"select count(*) from orders"
        myCursor.execute(query)
        result = myCursor.fetchall()
        return result