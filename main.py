from itertools import product
import re
from unicodedata import category
from flask import Flask,render_template,request,redirect,session,flash
from flask.helpers import url_for
from flask_mysqldb import MySQL
from datetime import datetime
import math
from flask_mail import Mail,Message
from random import randint
from werkzeug.utils import secure_filename
import os
from werkzeug.utils import send_file
from PIL import Image


UPLOAD_FOLDER = '/home/zeus/Mulriseller-shop-python-flask/static/front/img'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app=Flask(__name__)
mail=Mail(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
app.config["MAIL_USERNAME"] = 'southern.rakib@gmail.com'  
app.config['MAIL_PASSWORD'] = 'bangladesh523395'  
mail=Mail(app)
otp=randint(000000,999999)


app.secret_key="rakib"
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
        my_email="southern.rakib@gmail.com"
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


        if len(name)<4:
            flash("name must be greater than 4 alphabet.",category="error")
            return redirect(request.url)

        elif len(email)<5:
            flash("email must be greater than 5 alphabet.",category="error")
            return redirect(request.url)

        elif len(phone)<11:
            flash("Phone must be greater than 10 digit.",category="error")
            return redirect(request.url)

        elif len(password)<8:
            flash("Password must be greater than 8 digit.",category="error")
            return redirect(request.url)
        else:
            cur=mysql.connection.cursor()
            cur.execute(' INSERT INTO users(name,email,phone,division,district,area,password,date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(name,email,phone,division,district,area,password,datetime.now()))
            mysql.connection.commit()

            msg=Message('OTP',sender="southern.rakib@gmail.com", recipients=[email])
            msg.body=str(otp)
            mail.send(msg)
            flash("Send a otp number in your mail.",category="success")
            return render_template("verify.html")

    return render_template("signup.html")



@app.route("/validate", methods=["POST"])
def validate():
    user_otp=request.form['otp']
    if otp == int(user_otp):
        flash("Matched otp and account created succesfully!")
        return render_template("login.html")
    else:
        flash("Wrong otp",category="error")
        return redirect(request.url)

    


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s AND password=%s ",(email,password,))
        data=cur.fetchone()
        if data:
            session["user"]=email
            return redirect("/userProfile")
        else:
            flash("Wrong email or password",category="error")
            return redirect(request.url)
    return render_template("login.html")


@app.route("/changeUserPassword",methods=["GET","POST"])
def changeUserPassword():
    if 'user' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s ",(session['user'],))
        users=cur.fetchone()
        password=users[7]
        if request.method=="POST":
            old=request.form.get('old')
            new=request.form.get('new')
            confirm=request.form.get('confirm')

            if old=='' or new=='':
                flash("blank")
                return redirect(request.url)
            if old!=password:
                flash("old pasword not correct")
                return redirect(request.url)
            elif new!=confirm:
                flash("password doesn't match")
                return redirect(request.url)
            else:
                cur=mysql.connection.cursor()
                cur.execute("UPDATE users SET password=%s WHERE email=%s ",(new,session['user'],))
                mysql.connection.commit()

                flash("password changed")
                return redirect(request.url)
        
        return render_template("changeUserPassword.html",users=users)

@app.route("/changeUserName",methods=["GET","POST"])
def changeUserName():
    if 'user' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s ",(session['user'],))
        users=cur.fetchone()
        name=users[1]
        if request.method=="POST":
            old=request.form.get('old')
            new=request.form.get('new')

            if old=='' or new=='':
                flash("blank")
                return redirect(request.url)
            if old!=name:
                flash("old name not correct")
                return redirect(request.url)
            else:
                cur=mysql.connection.cursor()
                cur.execute("UPDATE users SET name=%s WHERE email=%s ",(new,session['user'],))
                mysql.connection.commit()

                flash("name changed")
                return redirect(request.url)
        
        return render_template("changeUserName.html",users=users)
            




@app.route("/userProfile")
def userProfile():
    if 'user' in session:
        session_email=session["user"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(session_email,))
        users=cur.fetchone()
        return render_template("userProfile.html",users=users)
    else:
        return redirect("/login")



@app.route('/userImageUploader', methods = ['GET', 'POST'])
def userImageUploader():
    if 'user' in session:
        session_id=session["user"]
        if request.method=='POST':
            f = request.files['file']
            if f.filename == '':
                flash('No selected file')
                return redirect("/userProfile")
            else:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
                cur =mysql.connection.cursor()
                cur.execute("UPDATE users SET image = %s WHERE email = %s", (f.filename,session_id))
                mysql.connection.commit()
                return redirect("/userProfile")
        return redirect("/userProfile")




@app.route("/orderHistory")
def orderHistory():
    if "user" in session:
        session_email=session["user"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s",(session_email,))
        users=cur.fetchone()
        cur =mysql.connection.cursor()
        cur.execute("SELECT * FROM orders WHERE email=%s",(session_email,))
        orders=cur.fetchall()
        return render_template("orderHistory.html", orders=orders,users=users)




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


@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/shop/<int:shopId>")
def shop(shopId):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(shopId,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products WHERE shopId=%s",(shopId,))
        shopProducts=cur.fetchall()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products")
        products=cur.fetchall()
        return render_template("shop.html",shopProducts=shopProducts,products=products,shop=shop)
    else:
    	return redirect("/login")
    
        

@app.route("/singleProduct/<int:id>",methods=["GET","POST"])
def singleProduct(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
        single_product=cur.fetchone()
        a_rating=single_product[7]

        if float(a_rating) < 252:
            a=5
            
        if float(a_rating)<124:
            a=4
        if float(a_rating)<40:
            a=3
        if float(a_rating)<29:
            a=2
        if float(a_rating)  <39:
            a=1

        productId=single_product[0]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products")
        products=cur.fetchall()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  reviews WHERE productId=%s",(id,))
        comments=cur.fetchall()


        if request.method=="POST":
            message=request.form.get("message")

            cur=mysql.connection.cursor()
            cur.execute("SELECT * FROM  users WHERE email=%s",(session['user'],))
            users=cur.fetchone()

            name=users[1]
            email=users[2]
            number=users[3]


            cur=mysql.connection.cursor()
            cur.execute(' INSERT INTO reviews(name,email,number,comment,date,productId) VALUES (%s,%s,%s,%s,%s,%s)',(name,email,number,message,datetime.now(),productId))
            mysql.connection.commit()

            return redirect(request.url)

    
        return render_template("singleProduct.html", products=products,single_product=single_product,comments=comments,a=a)


@app.route("/rating/<int:id>", methods=["GET","POST"])
def rating(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
        single_product=cur.fetchone()


        if request.method=="POST":
            new_rating=request.form.get("product_rating")
            if new_rating=='':
                flash("please enter a rating between 1 to 5")
            else:
                rating=float(new_rating)
            

                total_rating=rating+float(single_product[7])

                cur=mysql.connection.cursor()
                cur.execute("UPDATE products set rating=%s WHERE id=%s",(total_rating,id))
                mysql.connection.commit()
    return"""<script> alert("Thanks for your rating")</script>"""


        
@app.route("/category/furniture/<int:id>",methods=["GET","POST"])
def category(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        products=cur.fetchall()
        

        return render_template("furniture.html",products=products, shop=shop)



@app.route("/category/electronics/<int:id>",methods=["GET","POST"])
def electronics(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        products=cur.fetchall()

        return render_template("electronics.html",products=products,shop=shop)


@app.route("/category/sanitarySystems/<int:id>",methods=["GET","POST"])
def sanitary(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        products=cur.fetchall()

        return render_template("sanitary.html",products=products, shop=shop)


@app.route("/category/wallDecoration/<int:id>",methods=["GET","POST"])
def wall(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        products=cur.fetchall()

        return render_template("wall.html",products=products, shop=shop)


@app.route("/category/painting/<int:id>",methods=["GET","POST"])
def painting(id):
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        shop=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products where shopId=%s",(id,) )
        products=cur.fetchall()

        return render_template("painting.html",products=products, shop=shop)



@app.route("/checkout",methods=["POST","GET"])
def checkout():
    if "user" in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  products WHERE id=%s",(id,))
        single_product=cur.fetchone()

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM  users WHERE email=%s",(session["user"],))
        user=cur.fetchone()

        if request.method=="POST":
            address=request.form.get("address")
            selector=request.form.get("selector")


            productId=single_product[0]
            print(single_product[0])
            productName=single_product[1]
            productPrice=single_product[3]

            p=float(productPrice)*0.05
            
            total=int(single_product[3])+100
            cur=mysql.connection.cursor()  
            cur.execute('INSERT INTO orders (name,number,email,address,paymentMethod,productId,total,date,productName,productPrice,profit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,(user[1],user[3],user[2],address,selector,productId,total,datetime.now(),productName,productPrice,p) )
            mysql.connection.commit()
            return render_template("confirmation.html")

        return render_template("checkout.html",single_product=single_product)





""""Admin Panel"""
@app.route("/adminLogin", methods=["GET","POST"])
def adminLogin():
    if 'admin' in session:
        return redirect("/dashboard")
    if request.method=="POST":
        email=request.form.get("email")
        session['admin']=email
        password=request.form.get("password")
        print(email)
        if email=="admin@gmail.com" and password=="12345":
            return redirect("/dashboard")
        else:
            flash("wrong name or password")
            return redirect(request.url)
    return render_template("adminLogin.html")

@app.route("/adminLogout")
def adminLogout():
    session.pop("admin", None)
    return redirect("/")




@app.route("/dashboard")
def dashboard():
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall() 

        cur=mysql.connection.cursor()
        cur.execute("SELECT COUNT(sno) FROM orders WHERE STATUS=1")
        pending=cur.fetchone() 

        cur=mysql.connection.cursor()
        cur.execute("SELECT SUM(profit) FROM orders")
        earning=cur.fetchone()


        return render_template("dashboard.html",users=users,pending=pending,earning=earning)
    else:
        return redirect("/adminLogin")


@app.route("/deleteUser/<int:sno>")
def deleteUser(sno):
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM users WHERE sno=%s",(sno,))
        mysql.connection.commit()
        return redirect("/tables")




@app.route("/deleteShop/<int:id>")
def deleteShop(id):
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM shops WHERE shopId=%s",(id
        ,))
        mysql.connection.commit()
        return redirect("/tables")


@app.route("/deleteOrder/<int:id>")
def deleteOrder(id):
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM orders WHERE sno=%s",(id,))
        mysql.connection.commit()
        return redirect("/tables")





@app.route("/tables")
def tables():
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM products")
        products=cur.fetchall() 

        cur.execute("SELECT * FROM users")  
        users=cur.fetchall() 

        cur.execute("SELECT * FROM shops")  
        shops=cur.fetchall() 

        cur.execute("SELECT * FROM orders")  
        orders=cur.fetchall() 
        

        return render_template("tables.html",products=products,users=users,shops=shops,orders=orders)

    else:
        return redirect("/adminLogin")




@app.route("/approveOrder/<int:id>")
def approveOrder(id):
    if 'admin' in session:
        cur=mysql.connection.cursor()
        cur.execute("UPDATE orders set status=%s WHERE sno=%s",("1",id))
        mysql.connection.commit()
        return redirect("/tables")





@app.route("/openShop", methods=["GET","POST"])
def openShop():
    if request.method=="POST":
        shopName=request.form.get("shopName")
        password=request.form.get("password")
        cur=mysql.connection.cursor()
        cur.execute(' INSERT INTO shops(shopName,password,date) VALUES (%s,%s,%s)',(shopName,password,datetime.now()))
        mysql.connection.commit()
        flash("Congratution you successfully open a shop.now you are a seller of interior shop!!",category="success")
        return redirect("/allShop")
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
            flash("Wrong Shop Name or password")
    return render_template("sellerLogin.html")




@app.route("/sellerProfile")
def sellerProfile():
    if 'seller' in session:
        session_id=session["seller"]
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM shops WHERE shopId=%s",(session_id,))
        seller=cur.fetchone()
        return render_template("sellerProfile.html",seller=seller)
    else:
        return redirect("/sellerLogin")



@app.route('/sellerImageUploader', methods = ['GET', 'POST'])
def sellerImageUploader():
    if 'seller' in session:
        session_id=session["seller"]
        if request.method=='POST':
            f = request.files['file']
            if f.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
                cur =mysql.connection.cursor()
                cur.execute("UPDATE shops SET shopImage = %s WHERE shopId = %s", (f.filename,session_id))
                mysql.connection.commit()
                return redirect(request.url)
        return redirect("/sellerProfile")

            
        


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

        cur=mysql.connection.cursor()
        cur.execute("SELECT COUNT(id) FROM products WHERE shopId=%s",(session_id,))
        total=cur.fetchone()
        print(total) 

    return render_template("sellerDashboard.html",products=products, total=total)

@app.route("/changeShopPassword",methods=["GET","POST"])
def changeShopPassword():
    if 'seller' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM shops WHERE shopId=%s ",(session['seller'],))
        shops=cur.fetchone()
        password=shops[3]
        if request.method=="POST":
            old=request.form.get('old')
            new=request.form.get('new')
            confirm=request.form.get('confirm')

            if old=='' or new=='':
                flash("blank")
                return redirect(request.url)
            if old!=password:
                flash("old pasword not correct")
                return redirect(request.url)
            elif new!=confirm:
                flash("password doesn't match")
                return redirect(request.url)
            else:
                cur=mysql.connection.cursor()
                cur.execute("UPDATE shops SET password=%s WHERE shopId=%s ",(new,session['seller'],))
                mysql.connection.commit()

                flash("password changed")
                return redirect(request.url)
        
        return render_template("changeShopPassword.html",shops=shops)

@app.route("/changeShopName",methods=["GET","POST"])
def changeShopName():
    if 'seller' in session:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM shops WHERE shopId=%s ",(session['seller'],))
        shops=cur.fetchone()
        name=shops[1]
        if request.method=="POST":
            old=request.form.get('old')
            new=request.form.get('new')

            if old=='' or new=='':
                flash("blank")
                return redirect(request.url)
            if old!=name:
                flash("old name not correct")
                return redirect(request.url)
            else:
                cur=mysql.connection.cursor()
                cur.execute("UPDATE shops SET shopName=%s WHERE shopId=%s ",(new,session['seller'],))
                mysql.connection.commit()

                flash("name changed")
                return redirect(request.url)
        
        return render_template("changeShopName.html",shops=shops)



@app.route("/deleteProduct/<int:id>")
def deleteProduct(id):
    if 'seller' in session:
        cur=mysql.connection.cursor()
        cur.execute("DELETE FROM products WHERE Id=%s",(id,))
        mysql.connection.commit()
        return redirect("/sellerDashboard")




@app.route("/sellerAddProduct",methods=["GET","POST"])
def sellerAddProduct():
    if "seller" in session:
        if request.method=='POST':
            productName=request.form.get('productName')
            productDescription=request.form.get('productDescription')
            productPrice=request.form.get('productPrice')
            #productImage=request.form.get('productImage')
            productImage = request.files['productImage']
            if productImage.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                productImage.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(productImage.filename)))
                category=request.form.get('category')
                shopId=session["seller"]
                cur=mysql.connection.cursor()
                cur.execute('INSERT INTO products(product_name,product_description,product_price,product_image,category,sold,rating,date,shopId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', (productName,productDescription,productPrice,productImage.filename,category,0,0,datetime.now(),shopId,) )
                mysql.connection.commit()
                return redirect("/sellerDashboard")
    return render_template("sellerAddProduct.html")





@app.route("/searchProduct",methods=["GET","POST"])
def searchProduct():
    if "user" in session:
        if request.method=="POST":
            search_name=request.form.get("searchProduct")
            cur=mysql.connection.cursor()
            cur.execute(f"SELECT * FROM products WHERE product_name LIKE '%{search_name}%'")
            s_result=cur.fetchall()

        return render_template("searchProduct.html",s_result=s_result,search_name=search_name)

    else:
        return redirect("/login")





if __name__=="__main__":
    app.run(debug=True)
