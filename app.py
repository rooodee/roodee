from flask import Flask,render_template


app = Flask(__name__)


file = open ( "filename.hth" , "r" )

file.close()

sfsf = '''
hi meedoo
'''

@app.route('/')
def hello():

    return render_template('aa.html')
  
@app.route('/home')
def home():

    return sfsf



if __name__ == "__main__":
	app.run(port=3000,
    debug=False
    )
