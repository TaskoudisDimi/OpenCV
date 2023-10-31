from flask import Flask, render_template, request
import base64
import io
import numpy as np
import cv2 as cv

# TODO: Drag and Drop
# TODO: Android

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')


#######
# 1) Congert To Gray 
# 2) Segmetation and replace
# 3) Adaptive threshold
# 4) Resize 
# 5) Gym tracker
# 6) Realtime Face Recognizer
# 7) Mouse control, Volume control

@app.route('/EditImage', methods=['GET', 'POST'])
def EditImage():
    return render_template('EditImage.html')

def FromBGR_To_Gray(img):
    # Read the image data from the file-like object
    image_data = img.read()
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv.imdecode(nparr, cv.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return gray

@app.route('/ConertToGray', methods=['POST'])
def ConertToGray():
    if 'image' in request.files:
        image = request.files['image']
        gray = FromBGR_To_Gray(image)

        # Convert the grayscale image to a PNG byte array
        img_buffer = cv.imencode('.png', gray)[1].tobytes()
        img_str = base64.b64encode(img_buffer).decode('utf-8')

        return render_template('EditImage.html', gray_image=img_str)

    return render_template('EditImage.html')





@app.route('/EditVideo', methods=['GET'])
def EditVideo():
    return render_template('EditVideo.html')



@app.route('/FingerCounting', methods=['GET'])
def FingerCounting():
    return render_template('FingerCounting.html')


@app.route('/GetFingers', methods=['GET'])
def GetFingers():
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


