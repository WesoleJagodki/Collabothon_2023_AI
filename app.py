from app.recommendations import on_new_data
from app.api_processing import *
from processing.ocr import LineExtractor
from processing.openai import ParametersExtractorOpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from PIL import Image
import base64
import io

USER_ID_IMAGES =  7
app = Flask(__name__)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})


content_extractor = ParametersExtractorOpenAI()
line_extractor = LineExtractor()

@app.route('/')
def index():
    return "Welcome to the Magic API!"

@app.route('/process-receit', methods=['POST'])
@cross_origin()
def process_receit():
    """
    file = request.form.get("file")
    file = file.split(",")[1]
    file = base64.b64decode(file)
    img = Image.open(io.BytesIO(file))
    img = img.convert("RGB")
    """

    # LOL ocr lib does not implement pil support.
    #img.save("temp.png")

    lines = line_extractor.get_lines("samples/receit_1.jpg")
    content = content_extractor.get_parameters(lines)

    process_receit_from_img(USER_ID_IMAGES, content['basic_info'], content['product_list'])

    on_new_data()

    return jsonify({"result": "OK"})

@app.route('/add-transaction', methods=['POST'])
def add_transaction_from_api():
    request_json = request.get_json()
    
    process_api_transaction(request_json)

    return jsonify({"result": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
