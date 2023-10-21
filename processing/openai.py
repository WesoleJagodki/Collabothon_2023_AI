import openai

def _to_float(input: str):
    try:
        return float(input)
    except ValueError as _:
        return float("nan")

def _to_int(input: str):
    try:
        return int(input)
    except ValueError as _:
        return 1

class ParametersExtractorOpenAI:
    def __init__(self):
        with open('openai_api_key.txt', 'r') as f:
            openai.api_key = f.read()
        
        self.system_message_total = "You are a machine that is supposed to extract the following parameters from the document text: \n" \
                        "1. Total price tag (TOTAL_PRICE_TAG) \n" \
                        "2. Date of purchase (PURCHASE_DATE)) \n" \
                        "3. Location of purchase(PURCHASE_LOCATION) \n" \
                        "If you cannot find the parameter, please write 'None' \n" \
                        "Please output in two columns using csv format: PARAMETER_NAME, VALUE \n" \
        
        self.system_message_products = "You are a machine that is supposed to extract the following parameters from the document text: \n" \
                        "1. Product name \n" \
                        "2. Product price \n" \
                        "3. Product quantity \n" \
                        "If you cannot find the parameter, please write 'None' \n" \
                        "Please output in two columns using csv format: PRODUCT_NAME, PRODUCT_PRICE, PRODUCT_QUANTITY \n"
    
    def get_completion(self, system_message, user_input):
        completion = openai.ChatCompletion.create(
            temperature=0.0,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_input},
            ]
        )

        return completion.choices[0].message["content"]

    def get_parameters(self, lines):
        text = ""
        for line in lines:
            text += line + "\n"
        
        basic_info = self.get_completion(self.system_message_total, text)
        product_list = self.get_completion(self.system_message_products, text)
        
        basic_info = basic_info.split("\n")[1:]
        basic_info = [x.split(",") for x in basic_info]
        basic_info = {x[0].lower(): x[1].strip() for x in basic_info}

        product_list = product_list.split("\n")[1:]
        product_list = [x.split(",") for x in product_list]
        product_list = [{"product_name": x[0].strip(), "product_price": _to_float(x[1].strip()), "product_quantity": _to_int(x[2].strip())} for x in product_list]

        return {"basic_info": basic_info, "product_list": product_list}
