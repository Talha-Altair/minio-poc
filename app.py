from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from minio import Minio

MINIO_CLIENT = Minio(
        "localhost:9000", access_key="altair", secret_key="12345678", secure=False   
    )

IMAGES_DIR = "images"

BUCKET_NAME = "altair"

app = Flask(__name__)

def get_all_images():

    images = []

    for single_object in MINIO_CLIENT.list_objects(BUCKET_NAME):

        if single_object.name.endswith(".jpg"):

            images.append(single_object.name)

    return images

@app.route('/', methods = ['GET', 'POST'])
def index():

    all_images = get_all_images()

    print(all_images)

    

if __name__ == "__main__":
    
    app.run(debug=True)

# MINIO_ROOT_USER=talha MINIO_ROOT_PASSWORD=12345678 minio server ./data1 ./data2 ./data3 ./data4 ./data5 --console-address :9001