from flask import Flask, jsonify, render_template, request, send_file
import base64
import io
import numpy as np
import cv2 as cv
from Utils import FromBGR_To_Gray, FromGray_To_Lap, FromGray_To_Canny, FromImage_To_Blue, FromImage_To_Green, FromImage_To_Red, Detect_Faces, From_Image_to_Text, Resize_Image, Segmentation_Image
from Utils import UtilScanner
import mediapipe as mp 
from flask import send_file


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



UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/EditVideo', methods=['GET'])
def EditVideo():
    return render_template('EditVideo.html')

import os
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/process_video", methods=["POST"])
def process_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file received'})

    video_file = request.files['video']

    if video_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if video_file and allowed_file(video_file.filename):
        filename = secure_filename(video_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            video_file.save(file_path)
        except Exception as e:
            return jsonify({'error': f'Failed to save file: {e}'})

        cap = cv.VideoCapture('C:/Users/chris/Desktop/Dimitris/Tutorials/OpenCV/OpenCV/ComputerVision/Videos/Gym.mp4')
        detector = poseDetector()
        frame_list = []  # To store processed frames

        while True:
            success, img = cap.read()
            if not success:
                break

            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            imgRGB = detector.findPose(imgRGB)
            # Perform pose estimation and any other processing here

            frame_list.append(cv.cvtColor(imgRGB, cv.COLOR_RGB2BGR))

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

        processed_video_path = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_' + filename)
        height, width, layers = frame_list[0].shape
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        out = cv.VideoWriter(processed_video_path, fourcc, 30.0, (width, height))

        for frame in frame_list:
            out.write(frame)

        out.release()

        return send_file(processed_video_path, as_attachment=False)

    return jsonify({'error': 'Invalid file format'})







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


scan = UtilScanner()

@app.route('/scanned_image', methods=['POST'])
def scanned_image():
    if uploaded_image_data_scanner is not None:
        img = cv.imdecode(np.frombuffer(uploaded_image_data_scanner, np.uint8), cv.IMREAD_COLOR)
        img = cv.resize(img, (480, 640)) # resizing the image
        imgProcessed = scan.preProcessing(img)
        biggest = scan.getContours(imgProcessed)
        if biggest.size != 0:
            imgWarp = scan.getWarp(img, biggest)
            print("Warp", len(imgWarp))
            imgWarpGray = cv.cvtColor(imgWarp,cv.COLOR_BGR2GRAY)
            imgAdaptiveThre = cv.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
            imgResult = cv.bitwise_not(imgAdaptiveThre)
            print("Result 1", len(imgResult))
            _, img_buffer = cv.imencode('.png', imgResult)
            result = base64.b64encode(img_buffer).decode('utf-8')
            print("Result 2", len(result))  # Changed from print(result.size())
        else:
            imgResult = np.zeros((640, 480, 3), np.uint8)
            print(imgResult.size)
        return render_template('Scanner.html', uploaded_image_scanned=result if biggest.size != 0 else None)
    # Ensure to handle cases when uploaded_image_data_scanner is None
    return render_template('Scanner.html', uploaded_image=None)




class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        # self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth)

    def findPose(self, img, draw=True):

        self.imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        # Utilizes the pose instance to process the RGB image.
        self.results = self.pose.process(self.imgRGB)    
        # If pose landmarks are detected in the image, it draws the landmarks on the original image using mpDraw.draw_landmarks.
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            
        return img 
    
    # Takes an image (img) as input and processes it to find the positions of landmarks.
    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            # Iterates through the detected landmarks.
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # Retrieves the (x, y) coordinates of each landmark, scales them according to the image size, and appends them along with the landmark ID to lmList.
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255,0,0), cv.FILLED)
        return lmList


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)


