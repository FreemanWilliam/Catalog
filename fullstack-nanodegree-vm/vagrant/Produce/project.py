from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/produce')
def Produce():
	return "Test"

if __name__ == '__main__':
	app.debug = True
	