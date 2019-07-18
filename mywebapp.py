from flask import *
import json
import os
app = Flask(__name__)
items = [] 
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/Abtus.html')
def Abtus():
    return render_template('Abtus.html')

@app.route('/foo/<name>')
def foo(name):
	return render_template("index.html", to=name)

@app.route('/whereami')
def whereami():
    return 'Ghana!'
 
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)


