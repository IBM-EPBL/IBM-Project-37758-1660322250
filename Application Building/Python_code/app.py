model = load_model(r"Updated-Xception-diabetic-retinopathy.h5")

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/afterreg',methods=['POST'])
def afterreg():
	x= [x for x in request.torm.values()]
	print(x)
	data={
	'_id': x[1],  #Setting _id is  optional
	'name':x[0],
	 'psw':x[2]
	 }
	print(data)

	query={'_id': {'Seq': data['_id']}}
	
	docs=my_database.got_query_result(query)
	print(docs)
	
	print(len(docs.all()))
	if(len(docs.all())==0):
		url=my_database.create_document(data)
		#response=requests.get(url)
		return render_template('register.html', pred="Registration Successful, please login using your details")
	else:
		return render_template('register.html', pred="You are a already a member, please login using your details")

    	
#login page
@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/afterlogin',methods=['POST'])
def afterlogin ():
	user - request.form('_ id')
	passw = request.form['psw']
	print (user, passw)
	query = {'_id': {'Seq': user}}
	docs =my_database.get_query_result(query)
	print (docs)
	print (len (docs.all ()))
	if (len (docs.all())==0):
		return render_template ('login.html', pred="The username is not found.")
	else:
		if ((user==docs [0][0]['_id'] and passw==docs [0] [0] ['psw'])):
			return redirect (url_for ('prediction'))
		else:
			print ('Invalid User')
							
@app.route('/logout')
def logout():
	return render_template('logout.html')

@app.route('/prediction')
def logout():
	return render_template('prediction.html') 
 

if __name__ == "__main__":
	app.run(debug=False)
	
	