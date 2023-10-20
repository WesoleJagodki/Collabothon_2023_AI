import openai

class ParametersExtractorOpenAI:
    def __init__(self):
        with open('openai_api_key.txt', 'r') as f:
            openai.api_key = f.read()
        
        self.system_message_total = "You are a machine that is supposed to extract the following parameters from the document text: \n" \
                        "1. Total pricetag \n" \
                        "2. Date of purchase \n" \
                        "3. Location of purchase \n" \
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
        
        print(text)
        basic_info = self.get_completion(self.system_message_total, text)
        product_list = self.get_completion(self.system_message_products, text)
        
        basic_info = basic_info.split("\n")[1:]
        basic_info = [x.split(",") for x in basic_info]
        basic_info = {x[0].lower(): x[1] for x in basic_info}

        product_list = product_list.split("\n")[1:]
        product_list = [x.split(",") for x in product_list]
        product_list = [{"product_name": x[0], "product_price": x[1], "product_quantity": x[2]} for x in product_list]

        return {"basic_info": basic_info, "product_list": product_list}
