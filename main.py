import os
from flask import Flask, render_template, request
#from werkzeug import secure_filename
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import * 
from flask import Flask
from flask import Flask, flash, render_template, request , redirect 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from Models1 import appointments ,User,Doctor,Contact_us
from flask_login import LoginManager , UserMixin , login_required ,login_user, logout_user,current_user
import json
import urllib.request

with open ('config.json','r') as c:
  params = json.load(c)["params"]


local_server = True


app = Flask( __name__)

app.config['SECRET_KEY']= 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///E:/healthcare portal/healthcare.db'
app.config['SECRET_KEY']='654321'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['UPLOAD_FOLDER']	='E:/healthcare portal/static/img/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

#importing user class from Models1.py using from Models1 import User
#here



@login_manager.user_loader
def get(id):
    return User.query.get(id)

@app.route('/',methods=['GET'])
#@login_required
def get_home():
    return render_template('login.html', params=params) 

@app.route('/login',methods=['GET'])
def get_login():
    return render_template('index.html' , params=params)


@app.route('/signup',methods=['GET'])
def get_signup():
    return render_template('signup.html',params=params)

@app.route('/login',methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password = password).first()
    uemail=user.email
    uname=user.username
    
    session['uemail']= uemail
    session['uname']= uname
    if user.password == password:
        login_user(user)
    return redirect('/login')
  
    

@app.route('/signup',methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    gen = request.form['r1']
    image = "/static/img/patient/default.jpg"   
    user = User(username=username,email=email,password=password,gen=gen,image=image)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=email).first()
    login_user(user)
    return redirect('/login')



@app.route('/userprofile',methods=['GET','POST'])
def userprofile():
    if request.method=='POST':
   
        email_id=session['uemail']
        address=request.form['address']
        city=request.form['city']
        state=request.form['state']
        info=Userinfo(address=address,city=city,state=state,u_email_id=email_id)
        db.session.add(info)
        db.session.commit()
        
        uaddress=info.address
        ucity=info.city
        ustate=info.state
        session['uaddress']=uaddress
        session['ucity']=ucity
        session['ustate']=ustate
    return render_template("userprofile.html",params=params)



@app.route('/doctor',methods=['GET'])
def get_doctor():
    return render_template('dclogin.html',params=params)





@app.route('/dentist',methods=['POST'])
def get_dentist():
    return render_template('dentist.html',params=params)

@app.route('/cardio',methods=['POST'])
def get_cardio():
    return render_template('cardio.html',params=params)

@app.route('/neuro',methods=['POST'])
def get_neuro():
    return render_template('neuro.html',params=params)

@app.route('/eyes',methods=['POST'])
def get_eyes():
    return render_template('eyes.html',params=params)

@app.route('/general',methods=['POST'])
def get_general():
    return render_template('general.html',params=params)


    

@app.route('/dvideos',methods=['GET','POST'])
def get_dvideo():
    return render_template('dvideos.py',params=params)


@app.route('/setting',methods=['GET'])
def get_setting():
    return render_template('settings.html',params=params)
@app.route('/DocProfile')
def docprofile():
    return render_template('DocProfile.html',params=params)


@app.route('/dietplans',methods=['GET','POST'])
def get_ddiet():
    return render_template('dplan.html',params=params)
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

@app.route('/dplans',methods=['POST'])
def get_dplans():
    # if request.method == 'POST':
    #     f = request.files['filename']
    #     f.save(secure_filename(f.filename))
    #     return render_template('dplan.html',params=params)
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed')
		return render_template('dplan.html', params=params,filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='img/uploads/' + filename), code=301)


@app.route('/Pricing',methods=['GET','POST'])
def Pricing_doctor():

    pid=Pricing.pid
    pname=Pricing.pname
    pprice=Pricing.pprice
    pvalid=Pricingg.pvalid

  
    session['pid']= pid 
    session['pname']= pname 
    session['pprice']= pprice 
    session['pvalid']= pvalid 

    return render_template('Pricing.html',params=params)

@app.route('/doctor',methods=['POST'])
def doctor_post():
    email = request.form['email']
    password = request.form['password']
    doctor = Doctor.query.filter_by(doctorid=email, doctorpwd=password).first()
    
    docimg=doctor.doctorimg
    docname=doctor.doctorname
    docemail=doctor.doctorid
    
    session['docimg']= docimg 
    session['docname']= docname 
    session['docemail']= docemail 


    if doctor.doctorpwd == password:
        login_user(doctor)
    return redirect('/doctorhp')

@app.route('/doctorhp',methods=['GET'])
def get_doctorhp():
    return render_template('doctorhp.html' , params=params)


@app.route('/avdoctors',methods=['GET'])
def avdoctor_post():
        return render_template('avdoctors.html', params=params)




@app.route('/appointmentd',methods=['GET'])
def apdoctor_post():
        return render_template('appointmentd.html', params=params)



@app.route('/logout',methods=['GET'])

def logout():
    logout_user()
    return redirect('/')






@app.route("/Home form", methods=['GET', 'POST'])


def appointment():
    
    if request.method == 'POST':

        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        issue = request.form.get('issue')
        

        entry = appointments(firstname=firstname,lastname = lastname, email=email, phonenumber=phone,issue=issue, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
       
    return render_template('index.html', params=params) 



@app.route("/index-cta")
def CTA():
    return render_template('index-cta.html', params=params)

@app.route("/index-video")
def video():
    return render_template('index-video.html', params=params)

#contact us (information layout footer) for any issue 
@app.route("/contact-us" , methods=['GET', 'POST'])
def contact_us():
        
    if request.method == 'POST':
        email = request.form.get('email')
        message = request.form.get('message')

        entry = Contact_us( email= email, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact_us.html",params=params)
        
   

if __name__ == '__main__':

    app.run(debug=True)


