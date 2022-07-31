from ModulePackage.connection import mydb

class Order:
    def __init__(self,odate,otime,nooftiffeen,oprice,cname,cemail,mobile,messemail,messname,menu,address):
        myCursor = mydb.cursor()
        query = 'insert into orders(odate,otime,nooftiffeen,oprice,cname,cemail,mobile,messemail,messname,menu,address)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (odate,otime,nooftiffeen,oprice,cname,cemail,mobile,messemail,messname,menu,address)
        myCursor.execute(query,val)
        mydb.commit()
    
    def getCustomerOrderByEmail(email):
        print('order email : ',email)
        myCursor = mydb.cursor()
        query = f"select * from orders where cemail='{email}'"
        myCursor.execute(query)
        return myCursor.fetchall()
    
   
        