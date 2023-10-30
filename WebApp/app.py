from flask import Flask, render_template, request

# TODO: Drag and Drop
# TODO: Android

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')



@app.route('/EditImage', methods=['GET'])
def EditImage():
    return render_template('EditImage.html')

@app.route('/EditVideo', methods=['GET'])
def EditVideo():
    return render_template('EditVideo.html')

@app.route('/FingerCounting', methods=['GET'])
def FingerCounting():
    return render_template('FingerCounting.html')

@app.route('/FaceRecognition', methods=['GET'])
def FaceRecognition():
    return render_template('FaceRecognition.html')

@app.route('/MouseControl', methods=['GET'])
def MouseControl():
    return render_template('MouseControl.html')

@app.route('/GymTracker', methods=['GET'])
def GymTracker():
    return render_template('GymTracker.html')

@app.route('/Scanner', methods=['GET'])
def Scanner():
    return render_template('Scanner.html')



@app.route("/process_video", methods=["POST"])
def process_video():
    file = request.files["video"]
    # Add your video processing code here
    # For example, you can save the video to a specific location
    # file.save("uploaded_video.mp4")
    return render_template('Home.html')



if __name__ == '__main__':
    app.run(debug='True')


