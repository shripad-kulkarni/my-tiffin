import os
from flask import Flask, redirect, render_template, request, session
from ModulePackage import admin, menu,customer, mess,order
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['MESS_UPLOAD_FOLDER'] = 'static/images/mess'

allMenus = menu.Menu.getMenus()
@app.route('/')
def home():
    allMenus = menu.Menu.getMenus()
    return render_template('index.html',allMenus=allMenus)


@app.route('/addMenu',methods=['POST','GET'])
def addMenu():
    return render_template('mess.html')


@app.route('/messLogin',methods=['POST','GET'])
def messLogin():
    if 'messusername' not in session:
        if request.method=='POST':
            username = request.form.get('username')
            password= request.form.get('password')
            
            if mess.Mess.checkValidMess(username,password):
                session['messusername']=username
                messdetails = mess.Mess.getMessDetails(username)
                viewmessmenuDetails = menu.Menu.viewmessmenu(session['messusername'])
                 
                getmessorders = mess.Mess.getmessorderdetails(session['messusername'])
                
                return render_template('mess.html',messdetails=messdetails,viewmessmenuDetails=viewmessmenuDetails,getmessorders=getmessorders)
    else:
        username = session['messusername']
        messdetails = mess.Mess.getMessDetails(username)
         
        viewmessmenuDetails = menu.Menu.viewmessmenu(session['messusername'])
        
        getmessorders = mess.Mess.getmessorderdetails(session['messusername'])
        return render_template('mess.html',messdetails=messdetails,viewmessmenuDetails=viewmessmenuDetails,getmessorders=getmessorders)
        
    return redirect('/')
            
  
    


@app.route('/addItems',methods=['POST','GET'])
def addItems():
    if request.method=='POST':
        messid = session['messusername'] 
        price = request.form.get('price')
        itemNo = request.form.get('itemNo')
        items = ""
            
        for i in range(1,int(itemNo)+1):
            itemName = "item"+str(i)
            items +=request.form.get(itemName)+","
        
        menu.Menu(messid,items,price)
        return redirect('/messLogin')


@app.route('/addCustomer',methods=['POST','GET'])
def addCustomer():
    if request.method=='POST':
        cname = request.form.get('cname')
        cemail= request.form.get('cemail')
        cmobile= request.form.get('cmobile')
        caddress= request.form.get('caddress') 
        cpass= request.form.get('cpass') 
        if customer.Customer.checkCustomerExists(cemail):
            return render_template("index.html",accountexistsstatus=True,allMenus=allMenus)  
        else:
            customer.Customer(cname,cemail,cmobile,caddress,cpass)
            return render_template("index.html",accountstatus=True,allMenus=allMenus)             
    return redirect('/')

@app.route('/customerdash')
def customerdash():
    if 'customerusername' in session:
        customerDetails = customer.Customer.getCustomer(session['customerusername']) 
        orderDetails = order.Order.getCustomerOrderByEmail(session['customerusername'])
        print(orderDetails)
        
        return render_template('customerdash.html',customerDetails=customerDetails,username=session['customerusername'],orderDetails=orderDetails)
    else:
        return redirect('/')    


@app.route('/customerLogin',methods=['POST','GET'])
def customerLogin():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        validStatus = customer.Customer.checkValidCustomer(email,password)
        if validStatus:
            session['customerusername']=email
            return redirect('/customerdash')
        else:
            return render_template('index.html',allMenus=allMenus,loginstatus=True)


@app.route('/adminLogin',methods=['POST','GET'])
def adminLogin():
    if request.method=='POST':
        email = request.form.get('adminEmail')
        password = request.form.get('adminPassword')
        
        validStatus = admin.Admin.checkValidAdmin(email,password)
        
        if validStatus:
            aviewmess = admin.Admin.adminviewmess()
             
            aviewcustomer = admin.Admin.adminviewcustomer()
            
            avieworders = admin.Admin.adminvieworders()

            countmess = admin.Admin.countadminviewmess()

            countcustomer = admin.Admin.countadminviewcustomer()

            countorders = admin.Admin.countadminvieworders()
            
            return render_template('admin.html',aviewmess=aviewmess,aviewcustomer=aviewcustomer,avieworders=avieworders,countmess=countmess,countcustomer=countcustomer,countorders=countorders)
    
    return redirect('/')      
 
 
@app.route('/addMess',methods=['POST','GET'])
def addMess():
    if request.method=='POST':
        mname = request.form.get('messname')
        oname = request.form.get('messowner')
        email = request.form.get('messemail')
        mobile = request.form.get('messmobile')
        password = request.form.get('cpassword')
        address = request.form.get('address')
        mlocation = request.form.get('mlocation')
        
        if mess.Mess.checkMessExists(email):
            return render_template("index.html",accountexistsstatus=True,allMenus=allMenus)
        else:
            f = request.files['file']
            photo = f.filename
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['MESS_UPLOAD_FOLDER'],f.filename)) 
            
            mess.Mess(mname, oname, email, mobile,password, address, photo, mlocation)
            return render_template("index.html",accountstatus=True,allMenus=allMenus)
    return redirect('/')


@app.route('/updateCustomer',methods=['POST','GET'])
def updateCustomer():
    if request.method == 'POST':
        email = session['customerusername']
        name = request.form.get('name')
        mobile = request.form.get('mobile')
        address = request.form.get('address')
        password = request.form.get('password')
        customer.Customer.updateCustomer(email,name,mobile,address,password)
        customerDetails = customer.Customer.getCustomer(email) 
        return render_template('customerdash.html',customerDetails=customerDetails,username=session['customerusername'],updatestatus=True)
    return redirect('/')


@app.route('/order',methods=['POST','GET'])
def orderPage():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        menuid= request.form.get('menuid')
        validStatus = customer.Customer.checkValidCustomer(username,password)
        
        if validStatus:
            session['customerusername']=username
            customerDetails = customer.Customer.getCustomer(session['customerusername']) 
            menuDetail = menu.Menu.getDetailMenu(menuid)
            messEmail = menu.Menu.getMessEmail(menuid)
            print(menuDetail)
            return render_template('order.html',customerDetails=customerDetails,username=session['customerusername'],menuid=menuid,menuDetail=menuDetail,memail=messEmail)
    return redirect('/')


@app.route('/orderTiffin',methods=['POST','GET'])
def orderTiffin():
    if request.method=='POST':
        email = session['customerusername']
        memail = request.form.get('memail')
        name = request.form.get('cname')
        mobile = request.form.get('mobile')
        messname = request.form.get('mname')
        nooftiffeen = request.form.get('nooftiffeen')
        price = request.form.get('totalprice')
        omenu = request.form.get('omenu')
        address = request.form.get('address')
        # date and time 
        current_day_text = datetime.now().strftime('%a') 
        current_month_text = datetime.now().strftime('%h')
        current_day = datetime.now().strftime('%d') 
        current_minute = datetime.now().strftime('%M')
        current_hour = datetime.now().strftime('%H') 
        current_hour = datetime.now().strftime('%I')
        current_hour_am_pm = datetime.now().strftime('%p') 
        
        odate = current_day_text+","+current_day+" "+current_month_text
        otime  =current_hour+":"+current_minute+" "+current_hour_am_pm
        order.Order(odate,otime,nooftiffeen,price,name,email,mobile,memail,messname,omenu,address)
        customerDetails = customer.Customer.getCustomer(session['customerusername'])
        return render_template('customerdash.html',customerDetails=customerDetails,username=session['customerusername'],orderstatus=True)

@app.route('/payment',methods=['POST','GET'])
def payment():
    return render_template('customerdash.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)