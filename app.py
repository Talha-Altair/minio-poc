from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from minio import Minio

MINIO_API_HOST = "http://localhost:9000"

MINIO_CLIENT = Minio(
        "localhost:9000", access_key="talha", secret_key="12345678", secure=False   
    )

BUCKET_NAME = "altair"

app = Flask(__name__)

def get_all_images():

    images = []

    for single_object in MINIO_CLIENT.list_objects(BUCKET_NAME, recursive=True):

        if single_object.object_name.endswith((".jpg", ".png", ".jpeg")):

            images.append(single_object.object_name)

    images = [f"{MINIO_API_HOST}/{BUCKET_NAME}/{image}" for image in images]

    return images

@app.route('/', methods = ['GET', 'POST'])
def index():

    all_images = get_all_images()

    return render_template('index.html', images = all_images)

if __name__ == "__main__":
    
    app.run(debug=True)

# MINIO_ROOT_USER=talha MINIO_ROOT_PASSWORD=12345678 minio server ./data1 ./data2 ./data3 ./data4 ./data5 --console-address :9001

# http://192.168.0.103:9000/altair/137.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=F6DX5PBV3EQXPL26VBCJ%2F20211226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211226T140417Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJGNkRYNVBCVjNFUVhQTDI2VkJDSiIsImV4cCI6MTY0MDUyODYxNywicGFyZW50IjoidGFsaGEifQ.vqt-LQ-j05_VJxIoFHogiSiQIgSvwZrFoho5KxsTtVhBIts7Sey_vs8R-frKFXY3MWlOY1PSIx9kc5mnUGaDaQ&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=3fcc43e213948e8076081a03035498811d66cd61ba95f6ce56cc29022401440d