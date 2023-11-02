from flask import Flask, render_template, request, send_file
import base64
import io
import numpy as np
import cv2 as cv
from Utils import FromBGR_To_Gray, FromGray_To_Lap, FromGray_To_Canny, FromImage_To_Blue, FromImage_To_Green, FromImage_To_Red, Detect_Faces
# TODO: Drag and Drop
# TODO: Android

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')


#######
# 1) Congert To Gray 
# 2) Segmetation and replace (Adaptive Thresholding, Laplacian, Canny)
# 3) Adaptive threshold
# 4) Resize 
# 5) Gym tracker
# 6) Realtime Face Recognizer
# 7) Mouse control, Volume control

@app.route('/EditImage', methods=['GET', 'POST'])
def EditImage():
    return render_template('EditImage.html')

uploaded_image_data = None

@app.route('/display_image', methods=['GET', 'POST'])
def display_image():
    global uploaded_image_data
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        # Read the image data from the FileStorage object and store it
        uploaded_image_data = image.read()
        encoded_image = base64.b64encode(uploaded_image_data).decode('utf-8')
        uploaded_image = f"data:image/png;base64,{encoded_image}"
    else:
        uploaded_image = None
    return render_template('EditImage.html', uploaded_image=uploaded_image)

@app.route('/ConertToGray', methods=['POST'])
def ConertToGray():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        gray = FromBGR_To_Gray(image)
        _, img_buffer = cv.imencode('.png', gray)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', gray_image=img_str)
    return "Error"

image_download = None

@app.route('/download_image', methods=['GET'])
def download_image():
    global image_download
    if image_download is not None:
        # Create a file-like object and serve it as a downloadable file
        img_io = io.BytesIO(image_download)
        img_io.seek(0)
        return send_file(img_io, as_attachment=True, download_name='image.png', mimetype='image/png')
    return "Not Found"




@app.route('/ConvertToLap', methods=['POST'])
def ConvertToLap():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        lap = FromGray_To_Lap(image)
        _, img_buffer = cv.imencode('.png', lap)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', lap_image=img_str)
    return "Error"



@app.route('/ConvertToCanny', methods=['POST'])
def ConvertToCanny():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        canny = FromGray_To_Canny(image)
        _, img_buffer = cv.imencode('.png', canny)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', canny_image=img_str)
    return "Error"


@app.route('/ConvertToRed', methods=['POST'])
def ConvertToCaConvertToRednny():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        red = FromImage_To_Red(image)
        _, img_buffer = cv.imencode('.png', red)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', red_image=img_str)
    return "Error"

@app.route('/ConvertToBlue', methods=['POST'])
def ConvertToBlue():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        blue = FromImage_To_Blue(image)
        _, img_buffer = cv.imencode('.png', blue)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', blue_image=img_str)
    return "Error"


@app.route('/ConvertToGreen', methods=['POST'])
def ConvertToGreen():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        green = FromImage_To_Green(image)
        _, img_buffer = cv.imencode('.png', green)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', green_image=img_str)
    return "Error"



@app.route('/Detect_Faces', methods=['POST'])
def DetectFaces():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        detect = Detect_Faces(image)
        _, img_buffer = cv.imencode('.png', detect)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', detect_image=img_str)
    return "Error"









@app.route('/EditVideo', methods=['GET'])
def EditVideo():
    return render_template('EditVideo.html')



@app.route('/FingerCounting', methods=['GET'])
def FingerCounting():
    return render_template('FingerCounting.html')


@app.route('/GetFingers', methods=['GET'])
def GetFingers():
    return render_template('FingerCounting.html')







@app.route('/FingerCounting', methods=['GET'])
def Scanner():
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


