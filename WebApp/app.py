from flask import Flask, jsonify, render_template, request, send_file
import base64
import io
import numpy as np
import cv2 as cv
from Utils import FromBGR_To_Gray, FromGray_To_Lap, FromGray_To_Canny, FromImage_To_Blue, FromImage_To_Green, FromImage_To_Red, Detect_Faces, From_Image_to_Text, Resize_Image, Segmentation_Image

app = Flask(__name__)

app.static_folder = 'static'

image_download = None


#######
# 1) Gym tracker
# 2) Realtime Face Recognizer
# 3) Mouse control, Volume control
# 4) Scanner
# 5) Edit Video (Pose Estimation, Finger Counting)


@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')


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
        # it reads the image data, encodes it using Base64, and constructs a data URI for the uploaded image
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
        # The resulting grayscale image is encoded back into a PNG image buffer using 
        # It then encodes this grayscale image buffer into a Base64 string (img_str) to display it in the HTML template.
        _, img_buffer = cv.imencode('.png', gray)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', gray_image=img_str)
    return "Error"




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



@app.route('/Resize_Image', methods=['POST'])
def ResizeImage():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        width = int(request.form['width'])  # Get width value from the form
        height = int(request.form['height'])  # Get height value from the form

        image = Resize_Image(image, width, height)
        _, img_buffer = cv.imencode('.png', image)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', detect_image=img_str)
    return "Error"


@app.route('/Segmentation_Image', methods=['POST'])
def SegmentationImage():
    global uploaded_image_data
    global image_download
    if uploaded_image_data is not None:
        # Convert the uploaded image data to an OpenCV-compatible format
        image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
        Segmentation = Segmentation_Image(image)
        _, img_buffer = cv.imencode('.png', Segmentation)
        image_download = img_buffer
        img_str = base64.b64encode(img_buffer).decode('utf-8')
        return render_template('EditImage.html', Segmentation_Image=img_str)
    return "Error"


# @app.route('/From_Image_to_Text', methods=['POST'])
# def FromImagetoText():
#     global uploaded_image_data
#     global image_download
#     if uploaded_image_data is not None:
#         # Convert the uploaded image data to an OpenCV-compatible format
#         image = cv.imdecode(np.frombuffer(uploaded_image_data, np.uint8), cv.IMREAD_COLOR)
#         Image_to_Text = From_Image_to_Text(image)
#         _, img_buffer = cv.imencode('.png', Image_to_Text)
#         image_download = img_buffer
#         img_str = base64.b64encode(img_buffer).decode('utf-8')
#         return render_template('EditImage.html', From_Image_to_Text=img_str)
#     return "Error"



@app.route('/EditVideo', methods=['GET'])
def EditVideo():
    return render_template('EditVideo.html')


# detector = estimator.poseDetector()

# @app.route("/process_video", methods=["POST"])
# def process_video():
#     file = request.files["video"]
#     file_path = "static/uploaded_video.mp4"
#     file.save(file_path)
#     file_path = detector.findPose(file_path)
#     lmList = detector.findPosition(file_path, draw=False)
#     if len(lmList)!=0:
#         cv.circle(file_path, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv.FILLED)
#     return jsonify({"message": "Pose estimation completed"})  # Return a response



# detector = handDetector()

@app.route('/FingerCounting', methods=['GET'])
def FingerCounting():
    return render_template('FingerCounting.html')


@app.route('/GetFingers', methods=['GET'])
def GetFingers():
    return render_template('GetFingers.html')


@app.route('/FaceRecognition', methods=['GET'])
def FaceRecognition():
    return render_template('FaceRecognition.html')

@app.route('/MouseControl', methods=['GET'])
def MouseControl():
    return render_template('MouseControl.html')

@app.route('/GymTracker', methods=['GET'])
def GymTracker():
    return render_template('GymTracker.html')


### Scanner
@app.route('/Scanner', methods=['GET'])
def Scanner():
    return render_template('Scanner.html')

uploaded_image_data_scanner = None
@app.route('/display_image_scanner', methods=['GET', 'POST'])
def display_image_scanner():
    global uploaded_image_data_scanner
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        # Read the image data from the FileStorage object and store it
        uploaded_image_data_scanner = image.read()
        # it reads the image data, encodes it using Base64, and constructs a data URI for the uploaded image
        encoded_image = base64.b64encode(uploaded_image_data_scanner).decode('utf-8')
        uploaded_image = f"data:image/png;base64,{encoded_image}"
    else:
        uploaded_image = None
    return render_template('Scanner.html', uploaded_image=uploaded_image)


# scan = Scanner()


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)


