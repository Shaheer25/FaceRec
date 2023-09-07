from deepface import DeepFace
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/face",methods=["POST"])
def faceRec():
    try:
        result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
        result_str = "Same Person" if result else "Different Person"
        return jsonify({"result":result_str}),200
    except Exception as ex:
        return jsonify({"error":ex}),500


if __name__ == '__main__':
    app.run(port=5000, debug=True)


    result_str = "Same Person" if result else "Different Person"