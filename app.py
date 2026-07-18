
import os
import uuid

from flask import Flask, render_template, request
from ultralytics import YOLO
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

MODEL_PATH = "/content/drive/MyDrive/Object_Detection_Deployment/best.pt"
model = YOLO(MODEL_PATH)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    error = None

    if request.method == "POST":
        if "image" not in request.files:
            error = "No image was uploaded."
            return render_template(
                "index.html",
                result_image=result_image,
                error=error
            )

        file = request.files["image"]

        if file.filename == "":
            error = "Please choose an image."
            return render_template(
                "index.html",
                result_image=result_image,
                error=error
            )

        if not allowed_file(file.filename):
            error = "Only PNG, JPG, and JPEG files are allowed."
            return render_template(
                "index.html",
                result_image=result_image,
                error=error
            )

        original_filename = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{original_filename}"
        upload_path = os.path.join(UPLOAD_FOLDER, unique_name)

        file.save(upload_path)

        results = model.predict(
            source=upload_path,
            conf=0.25
        )

        plotted_image = results[0].plot()

        result_filename = f"result_{unique_name}"
        result_path = os.path.join(RESULT_FOLDER, result_filename)

        import cv2
        cv2.imwrite(result_path, plotted_image)

        result_image = result_filename

    return render_template(
        "index.html",
        result_image=result_image,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
