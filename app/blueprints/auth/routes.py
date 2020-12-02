from app import db, mail, Message 
from . import bp as auth
from flask import request, render_template, redirect, url_for, flash
from app.forms import PhoneForm, LoginForm
from app.models import Avenger
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import check_password_hash 



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = PhoneForm()
    context = {
        'form': form
    }
    if request.method == 'POST' and form.validate():
            #Get Information
        
        firstname = form.firstname.data
        lastname = form.lastname.data
        heroname = form.heroname.data 
        address = form.address.data
        phonenumber = form.phonenumber.data
        email = form.email.data 
        password = form.password.data
        
        

       # print(username, email, password)
       
        #Create new instance of User
       # new_user = User(username, email, password)
        new_avenger = Avenger(firstname, lastname, heroname, address, phonenumber, email, password)
        #Add user to db
        db.session.add(new_avenger)
        db.session.commit()

        # flash success message
        flash("You have successfully registered!", 'success')

        #Flask Email Sender 
       # msg = Message(f'Thanks for signing up, {heroname}!', recipients=[email])
       # msg.body = ('Congrats on signing up! We hope you enjoy our site!')
        #msg.html = ('<h1>Welcome to Our Site</h1>' '<p>We hope you enjoy it!</p>')

       # mail.send(msg)



        return redirect(url_for('index'))
    return render_template('register.html', **context)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {
        'form': form
    }

    if request.method == 'POST' and form.validate():
        heroname = form.heroname.data
        password = form.password.data

        avenger = Avenger.query.filter_by(heroname=heroname).first()

        if avenger is None or not check_password_hash(avenger.password, password):
            flash('Incorrect Email/Password. Please try again.', 'success')
            return redirect(url_for('login'))

        login_user(avenger, remember=form.remember_me.data)
        flash('You have successfully logged in', 'success')
        

        # redirect to index
        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'primary') #Specifying Colors for flash message 
    return redirect(url_for('index'))  