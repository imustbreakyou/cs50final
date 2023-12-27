# ATTRIBUTIONS #flask 
# environmental variable information from: https://ioflood.com/blog/python-get-environment-variable/#:~:text=to%20access%20it.-,Use%20os.,to%20safely%20access%20environment%20variables.#
# calling environmental variables in python from this source: https://dagster.io/blog/python-environment-variables
# further .env assitance from here: https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv # 
# API response assitance from: https://www.geeksforgeeks.org/response-json-python-requests/
# Form to dict from here https://vortex.hashnode.dev/how-to-obtain-dict-from-a-flask-request-form-ck6c6ertx006s3cs1rw60rsk8 #
# Help with parsing Json: https://brightdata.com/blog/how-tos/parse-json-data-with-python
# Dynamic URL creation from: https://stackoverflow.com/questions/74435785/python-create-dynamic-url-for-api-call
# Negative Indexing to remove final character from string: https://www.geeksforgeeks.org/python-program-to-remove-last-character-from-the-string/


from flask import Flask, request, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
import requests




app = Flask(__name__)
app.debug = True

source_url = "https://api.twitch.tv/helix/streams"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('layout.html')
    else:
        return redirect('index.html')





@app.route("/form_handler", methods=['GET', 'POST'])  
def form_handler():
    if request.method == "POST":
        language = request.form.getlist('language')
        #type = request.form.getlist('type')
        #game_name = request.form.getlist('game_name')
        print(language)


        return process_form(language)


    
def process_form(language):
    print("process_form fired!")
    # set empty string
    parameter_string = ""
    print("Pre iteration parameter string =", parameter_string)

    #iterate over dictionary
    for language in language:
        #use f-string for url creation
        parameter_string += f"language={language}&"
        print("language processed")

    print (f"Post Iteration Param String = {parameter_string}")
        
    
    
    # remove final character using negative indexing
    parameter_string = parameter_string[:-1]

    print(f"final parameter string before api_url: {parameter_string}")
    
    # pass to build_api_url
    return build_api_url(source_url, parameter_string)
    
        

def build_api_url(source_url, parameter_string):

     # Prepare API Call
    api_url = f"{source_url}?{parameter_string}"
    print(f"api_url: {api_url}")
    
    print(api_url)
    #return final_url
    return call_api(api_url)
        





def call_api(api_url):
    
    print("call_apifired")

   
    
    load_dotenv('/absolute/path/to/.env')
    client_id = os.getenv('TWITH_CLIENT_ID')
    oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')


    # Error handling for missing access tokens
    if not client_id or not oauth_token:
        print("missing API token or id")
        return None
    
    headers = {
        
        'Client-Id': client_id,
        'Authorization': f'Bearer {oauth_token}'

    }
    # THIS MAKES THE REQUEST 
    response = requests.get(api_url, headers=headers)
    print(response)
    
    # Error Handling for failed API Call 
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return None

    
    # Store json data in dictionary 
    json_data = response.json()
            
    streams = {}
    stream_counter = 0
    for item in json_data['data']:
        stream_counter += 1
        streams[item['user_id']] = {
            'user_id': item['user_id'],
            'user_name': item['user_name'],
            'game_name': item['game_name'],
            'viewer_count': item['viewer_count'],
            'language': item['language'],
            'type': item['type'],
            'result_count': stream_counter 
        }
    print(stream_counter)
        

    dynamic_header = stream_counter

    return render_template('index.html', dynamic_header=dynamic_header, streams=streams)