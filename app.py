import os
from datetime import datetime

from flask import Flask
from flask_moment import Moment

from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'suck my balls'

moment = Moment(app)

@app.route('/')
def main():
	return render_template('main.html', 
						   current_time=datetime.utcnow())

if __name__ == '__main__':
	for directory in 'static', 'templates':
		if not os.path.exists(directory):
			os.mkdir(directory)
			
	app.run(debug=True)	
