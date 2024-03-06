from flask import Flask,jsonify,request
from ouo.api import Ouo

# add your api key
ouo = Ouo("ANeq6B81")
app = Flask(__name__)

@app.route('/')

def hello():
    return jsonify({'message' :  "Hello World"})

@app.route('/shortenlink')

def shortenLink():
    long_url = request.args.get('link')
    link = ouo.short(long_url)
    if(link):
        return jsonify({'link' :  link})



if __name__ == '__main__':
    app.run(debug=True)