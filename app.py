from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['DEBUG'] = True 

@app.route('/')
def index():
	return render_template('index.html', name='Jonathan')

@app.route('/login')
def login():
	# username = request.form['username']
	# print username
	return render_template('login.html')

if __name__ == '__main__':
	app.run()
	