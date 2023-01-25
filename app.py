from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def Hello():
    return jsonify("hi everyone")

if __name__== '__main__':
    app.run(debug=True)