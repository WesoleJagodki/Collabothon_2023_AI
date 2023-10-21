from app.database import add_transaction
from processing.ocr import LineExtractor
from processing.openai import ParametersExtractorOpenAI
from flask import Flask, request, jsonify
from PIL import Image

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

    lines = line_extractor.extract(img)
    content = content_extractor.extract(lines)
    basic_parameters = content['basic_info']
    products = content['product_list']
    basic_parameters['TRANSACTION_TYPE'] = "cash"

    add_transaction(basic_parameters, 1)

    return 200

@app.route('/add-transaction', methods=['POST'])
def process_receit():
    request_json = request.get_json()
    add_transaction(request_json["parameters"], request_json["user_id"])
    return 200

if __name__ == "__main__":
    app.run()
