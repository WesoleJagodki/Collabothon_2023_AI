from app.database import add_transaction
from app.api_processing import *
from processing.ocr import LineExtractor
from processing.openai import ParametersExtractorOpenAI
from flask import Flask, request
from PIL import Image

USER_ID_IMAGES =  7
app = Flask(__name__)

content_extractor = ParametersExtractorOpenAI()
line_extractor = LineExtractor()

@app.route('/')
def index():
    return "Welcome to the Magic API!"

@app.route('/process-receit', methods=['POST'])
def process_receit():
    file = request.files['image']
    img = Image.open(file.stream)

    # LOL ocr lib does not implement pil support so this is pretty crap.
    img.save("temp.jpg")

    lines = line_extractor.get_lines("temp.jpg")
    content = content_extractor.get_parameters(lines)

    process_receit_from_img(USER_ID_IMAGES, content['basic_info'], content['product_list'])

    return "OK"

@app.route('/add-transaction', methods=['POST'])
def add_transaction_from_api():
    request_json = request.get_json()
    
    process_api_transaction(request_json)

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
