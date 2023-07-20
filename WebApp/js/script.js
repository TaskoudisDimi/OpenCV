document.addEventListener("DOMContentLoaded", () => {
  const cameraButton = document.getElementById("cameraButton");
  const videoInput = document.getElementById("videoInput");
  const videoPlayer = document.getElementById("videoPlayer");

  cameraButton.addEventListener("click", () => {
    openCamera();
  });

  videoInput.addEventListener("change", () => {
    loadVideo();
  });

  function openCamera() {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      alert("Camera not supported in this browser.");
      return;
    }

    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        videoPlayer.srcObject = stream;
      })
      .catch(error => {
        console.error("Error accessing camera: ", error);
      });
  }

  function loadVideo() {
    const file = videoInput.files[0];
    if (file) {
      const videoURL = URL.createObjectURL(file);
      videoPlayer.src = videoURL;
      
      // Call the process_video endpoint
      processVideo(file);
    }
  }

  function processVideo(videoFile) {
    const formData = new FormData();
    formData.append("video", videoFile);

    fetch("/process_video", {
      method: "POST",
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.message); // Print the response message from the server
      })
      .catch(error => {
        console.error("Error while processing video: ", error);
      });
  }
});
