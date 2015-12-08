from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps

import pymysql

app = Flask(__name__)

#need a random key generator
app.secret_key = "so secret"

#Open Database connection

hoppa = pymysql.connect( 'us-cdbr-azure-west-c.cloudapp.net', 'bb633b141d2f93', '9966c0ab', 'hoppa_db')

cur = hoppa.cursor()
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please login.')
			return redirect(url_for('addgroup'))
	return wrap

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
	return redirect(url_for('addgroup'))

@app.route('/newsfeed', methods=['GET', 'POST'])
def newsfeed(userid):
	return render_template('newsfeed.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error = None

	if request.method == 'POST':

		useremail = request.form['useremail']
		password = request.form['password']

		# users_credentials = "SELECT (user_email,user_pass) FROM hoppa_db.hoppers WHERE user_email='" + useremail + "' AND user_pass='" + password +"'"
		users_credentials = "SELECT * FROM hoppa_db.hoppers"
		print (users_credentials)
		try:
			cur.execute(users_credentials)
			print (users_credentials)
			user = cur.fetchone()
			print(user)
			# for row in cur:
   # 				print(row)

			if user is None:
				error = " Username or Password is wrong. Please try again."
			else:
				userid = "SELECT user_id FROM hoppa_db.hoppers WHERE user_email='" + useremail + "' AND user_pass= '" + password +"'"
				session['logged_in'] = True
				flash("Welcome to Hoppa!")
				return redirect(url_for('newsfeed', userid=userid))
		except:
			error = "Error fetching the data. Please try again."
	return render_template('index.html', error=error)

@app.route('/register', methods=['GET','POST'])
def register():
	error = None

	if request.method == 'POST':

		userfirst = request.form['fname']
		usermiddle = request.form['mname']
		userlast = request.form['lname']
		user_bdate = request.form['user_bdate']
		email = request.form['email']
		user_phone = request.form['user_phone']
		user_type = request.form['user_type']
		password = request.form['password']
		user_rank = 'Tadpole'
		address_street = request.form['street']
		address_city = request.form['city']
		address_state = request.form['state']
		address_country = request.form['country']
		address_zipcode = request.form['zipcode']

		# print ("ESTOY" + request.form['fname'])

		new_user = "INSERT INTO hoppa_db.hoppers (user_email, user_phone, user_first, user_middle, user_last, user_bdate, user_pass, user_type, user_rank) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (email,user_phone,userfirst, usermiddle, userlast, user_bdate, password, user_type, user_rank)

		try:
			cur.execute(new_user)
			hoppa.commit()
			flash("Welcome to Hoppa! Please confirm your email.")
			return redirect(url_for('login'))
		except:
			error = "Error adding the data. Please try again."
			hoppa.rollback()

	return render_template('register.html', error=error)

@app.route('/addgroup', methods=['GET', 'POST'])
def addgroup():
	print ('IM HRE')
	if request.method == 'POST':
		group_name = request.form['groupname'];
		group_desc = request.form['groupdesc'];
		new_group = "INSERT INTO hoppa_db.groups (group_name, group_description) VALUES ('%s','%s');"  %(group_name, group_desc)
		print(new_group)
		try:
			cur.execute(new_group)
			print("SUCCESS1")
			hoppa.commit()
			print("SUCCESS2")
			hoppa.close()
			print("SUCCESS3")
			#return redirect(url_for('register'))
		except:
			hoppa.rollback()
		
	return render_template('addgroup.html')


@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash("Hope to see you back soon!")
	return redirect(url_for('home'))


if __name__ == '__main__':
	app.run(debug=True)