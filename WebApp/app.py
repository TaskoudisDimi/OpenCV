from flask import Flask, render_template, request

# TODO: Drag and Drop
# TODO: Android

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


@app.route('/HandTracking', methods=['GET'])
def HandTracking():
    return render_template('HandTracking.html')


@app.route("/process_video", methods=["POST"])
def process_video():
    file = request.files["video"]
    # Add your video processing code here
    # For example, you can save the video to a specific location
    # file.save("uploaded_video.mp4")
    return render_template('Home.html')



if __name__ == '__main__':
    app.run(debug='True')


