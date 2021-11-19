from itertools import product
import re
from flask import Flask,render_template,request,redirect,session
from flask.helpers import url_for
from flask_mysqldb import MySQL
from datetime import datetime
import math
from flask_mail import Mail,Message
from random import randint

from werkzeug.utils import send_file


app=Flask(__name__)
mail=Mail(app)

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
app.config["MAIL_USERNAME"] = 'abdullahalmizan644@gmail.com'  
app.config['MAIL_PASSWORD'] = '********'  
mail=Mail(app)
otp=randint(000000,999999)


app.secret_key="Ali"
app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='InteriorShop'






mysql=MySQL(app)









"""Landing Page"""

@app.route("/")
def index():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products=cur.fetchall()

    cur.execute("SELECT * FROM shops")
    shops=cur.fetchall()
    return render_template("index.html", products=products, shops=shops)















""""User Autintecation"""

@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=="POST":
        user_message=request.form.get("message")
        name=request.form.get("name")
        email=request.form.get('email')
        my_email="abdullahalmizan644@gmail.com"
        msg=Message('MESSAGE from : '+name,sender=email, recipients=[my_email])   
        msg.body=user_message
        mail.send(msg)
        return "Mail send successfully"
    return render_template("contact.html")


@app.route("/signup", methods=['GET','POST'])
def signup():
    return render_template("signup.html")

@app.route("/verify", methods=["GET","POST"])
def verify():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        division=request.form.get('division')
        district=request.form.get('district')
        area=request.form.get('area')
        password=request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute(' INSERT INTO users(name,email,phone,division,district,area,password,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(name,email,phone,division,district,area,password,datetime.now()))
        mysql.connection.commit()

        msg=Message('OTP',sender="abdullahalmizan644@gmail.com", recipients=[email])
        print(msg)
        msg.body=str(otp)
        mail.send(msg)
        return render_template("verify.html")

    return render_template("verify.html")



@app.route("/validate", methods=["POST"])
def validate():
    user_otp=request.form['otp']
    if otp == int(user_otp):
        return render_template("login.html")
    else:
        return "wrong otp"

    


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        session["user"]=email
        password=request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s ",(email,password,))
        data=cur.fetchone()
        if data is not None:
            return redirect("/userProfile")
        else:
            return"<script>alert('wrong email or password')</script>"
    return render_template("login.html")



@app.route("/userProfile")
def userProfile():
    if 'user' in session:
        session_email=session["user"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(session_email,))
        users=cur.fetchall()
        return render_template("userProfile.html",users=users)
    else:
        return redirect("/login")




@app.route("/userLogout")
def userLogout():
    session.pop("user", None)
    return redirect("/")



















"""Shop"""

@app.route("/allShop")
def allShop(): 
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM shops")
    shops=cur.fetchall()
    return render_template("allShop.html",shops=shops)


@app.route("/shop/<int:shopId>")
def shop(shopId):
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  products WHERE shopId=%s",(shopId,))
    shopProducts=cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  products")
    products=cur.fetchall()
    return render_template("shop.html",shopProducts=shopProducts,products=products)

        

@app.route("/singleProduct/<int:id>",methods=["GET","POST"])
def singleProduct(id):
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
    single_product=cur.fetchone()

    productId=single_product[0]
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  products")
    products=cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  reviews WHERE productId=%s",(id,))
    comments=cur.fetchall()


    if request.method=="POST":
        name=request.form.get("name")
        email=request.form.get("email")
        number=request.form.get("number")
        message=request.form.get("message")

        cur=mysql.connection.cursor()
        cur.execute(' INSERT INTO reviews(name,email,number,comment,date,productId) VALUES (%s,%s,%s,%s,%s,%s)',(name,email,number,message,datetime.now(),productId))
        mysql.connection.commit()

        return redirect(request.url)

    
    return render_template("singleProduct.html", products=products,single_product=single_product,comments=comments)


        




@app.route("/checkout/<int:id>")
def checkout(id):
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
    single_product=cur.fetchone()
    return render_template("checkout.html",single_product=single_product)


@app.route("/order/<int:id>", methods=["GET","POST"])
def order(id):
    if request.method=="POST":
        firstName=request.form.get("firstName")
        lastName=request.form.get("lastName")
        number=request.form.get("number")
        email=request.form.get("email")
        address=request.form.get("address")
        selector=request.form.get("selector")

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
        single_product=cur.fetchone()

        productName=single_product[0]
        productPrice=int(single_product[3])+100



        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO orders (firstName,lastName,number,email,address,paymentMethod,productName,total,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,(firstName,lastName,number,email,address,selector,productName,productPrice,datetime.now(),) )
        mysql.connection.commit()
        return "order taken"

    else:
        return "fill all "


@app.route("/cart")
def cart():
    return render_template("cart.html")







""""Admin Panel"""
@app.route("/adminLogin", methods=["GET","POST"])
def adminLogin():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        print(email)
        if email=="admin@gmail.com" and password=="12345":
            return redirect("/dashboard")
        else:
            return"<script>alert('wrong email or password')</script>"
    return render_template("adminLogin.html")



@app.route("/dashboard")
def dashboard():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users=cur.fetchall()   
    print(users)
    return render_template("dashboard.html",users=users)



@app.route("/tables")
def tables():
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    products=cur.fetchall() 
    cur.execute("SELECT * FROM users")  
    users=cur.fetchall() 

    cur.execute("SELECT * FROM shops")  
    shops=cur.fetchall() 
    return render_template("tables.html",products=products,users=users,shops=shops)




""""Seller login"""

@app.route("/openShop", methods=["GET","POST"])
def openShop():
    if request.method=="POST":
        shopName=request.form.get("shopName")
        password=request.form.get("password")
        cur=mysql.connection.cursor()
        cur.execute(' INSERT INTO shops(shopName,password,date) VALUES (%s,%s,%s)',(shopName,password,datetime.now()))
        mysql.connection.commit()
        return redirect("/")
    return render_template("openShop.html")



@app.route("/sellerLogin",methods=["GET","POST"])
def sellerLogin():
    
    if request.method=="POST":
        name=request.form.get("username")
        password=request.form.get("password")
        
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM shops WHERE shopName=%s AND password=%s",(name,password,))
        data=cur.fetchone()
        if data is not None:
            session["seller"]=data[0]
            return redirect("/sellerProfile")
        else:
            return"<script>alert('wrong email or password')</script>"
    return render_template("sellerLogin.html")



@app.route("/sellerProfile")
def sellerProfile():
    if 'seller' in session:
        session_id=session["seller"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM shops WHERE shopId=%s",(session_id,))
        seller=cur.fetchall()
        return render_template("sellerProfile.html",seller=seller)
    else:
        return redirect("/sellerLogin")

@app.route("/sellerLogout")
def sellerLogout():
    session.pop("seller", None)
    return redirect("/")







@app.route("/sellerDashboard")
def sellerDashboard():
    if 'seller' in session:
        session_id=session["seller"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM products WHERE shopId=%s",(session_id,))
        products=cur.fetchall()
    return render_template("sellerDashboard.html",products=products)





@app.route("/sellerAddProduct",methods=["GET","POST"])
def sellerAddProduct():
    if "seller" in session:
        if request.method=='POST':
            productName=request.form.get('productName')
            productDescription=request.form.get('productDescription')
            productPrice=request.form.get('productPrice')
            productImage=request.form.get('productImage')
            category=request.form.get('category')
            shopId=session["seller"]
            cur=mysql.connection.cursor()
            cur.execute('INSERT INTO products(product_name,product_description,product_price,product_image,category,sold,rating,date,shopId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (productName,productDescription,productPrice,productImage,category,0,0,datetime.now(),shopId,) )
            mysql.connection.commit()
            return redirect("/sellerDashboard")
    return render_template("sellerAddProduct.html")









if __name__=="__main__":
    app.run(debug=True)
