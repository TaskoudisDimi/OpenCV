from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')

@app.route('/FaceRecognition', methods=['GET'])
def FaceRecognition():
    return render_template('FaceRecognition.html')

@app.route('/EditImage', methods=['GET'])
def EditImage():
    return render_template('EditImage.html')



if __name__ == '__main__':
    app.run(debug='True')