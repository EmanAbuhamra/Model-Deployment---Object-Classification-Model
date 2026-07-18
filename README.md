# Device Detector Web Application using YOLOv8, Flask, and Docker

## Project Overview

This project demonstrates the deployment of a deep learning object detection model through a web application. A YOLOv8 model was trained to distinguish between **Nintendo Switch** and **Steam Deck** handheld gaming devices. The trained model is integrated into a Flask application, containerized using Docker, and prepared for online deployment.

The application allows users to upload an image through a web interface and receive an annotated image containing the detected device(s).

---

## Features

- YOLOv8 object detection model
- Flask-based web application
- Image upload through a browser
- Automatic object detection and annotation
- Dockerized for portable deployment
- Ready for deployment on platforms such as Render or Hugging Face Spaces

---

## Project Structure

```
Device-Detector/
│
├── app.py                     # Flask application
├── best.pt                    # Trained YOLOv8 model
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── Module_7_Challenge.ipynb   # Development notebook
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── uploads/
    └── results/
```

---

## Model

- **Architecture:** YOLOv8
- **Task:** Object Detection
- **Classes:**
  - Nintendo Switch
  - Steam Deck

The model accepts an uploaded image and predicts the location and class of each detected gaming device.

---

## Technologies Used

- Python
- Flask
- Ultralytics YOLOv8
- OpenCV
- Pillow
- Docker
- Gunicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/device-detector.git
cd device-detector
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python app.py
```

Open your browser:

```
http://localhost:5000
```

---

## Docker

Build the Docker image:

```bash
docker build -t device-detector .
```

Run the container:

```bash
docker run -p 5000:5000 device-detector
```

---

## Deployment

This application is designed to be deployed using Docker on cloud platforms such as:

- Render
- Hugging Face Spaces
- Railway
- Fly.io

---

## Example Workflow

1. Upload an image.
2. The Flask application loads the trained YOLOv8 model.
3. Object detection is performed.
4. The annotated image is displayed to the user.

---

## Future Improvements

- Support for video inference
- Confidence threshold adjustment
- Detection history
- Multiple model selection
- Improved user interface
- Batch image processing

---

## Author

**Eman Abuhamra**

M.Sc. Applied Mathematics  
Khalifa University

---

## License

This project was developed for educational purposes as part of the **ZAKA Machine Learning Diploma – Module 7 Deployment Challenge**.
