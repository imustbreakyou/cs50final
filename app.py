# ATTRIBUTIONS #flask 
# environmental variable information from: https://ioflood.com/blog/python-get-environment-variable/#:~:text=to%20access%20it.-,Use%20os.,to%20safely%20access%20environment%20variables.#
# calling environmental variables in python from this source: https://dagster.io/blog/python-environment-variables
# further .env assitance from here: https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv # 
# API response assitance from: https://www.geeksforgeeks.org/response-json-python-requests/
# Form to dict from here https://vortex.hashnode.dev/how-to-obtain-dict-from-a-flask-request-form-ck6c6ertx006s3cs1rw60rsk8 #
# Help with parsing Json: https://brightdata.com/blog/how-tos/parse-json-data-with-python

from flask import Flask, request, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
import requests




app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('layout.html')
    else:
        return redirect('index.html')





@app.route("/form_handler", methods=['GET', 'POST'])  
def form_handler():
    if request.method == "POST":
        print("form_handler fired")
        return call_api()
# if data
#   for data in data:
#       data[f'variable_{n}'] = ""
#       n += 1
# return data 
#
#

    
def build_api_url(source_url):
    
    
    # parameter_1['value'] = en -- To use one we have handle_form function
          # Set API call params with f"url?{}{}{}""
        

    #hard coded value
    parameter_1_name = "language="
    parameter_1_value = "en"

    
    final_url = source_url+"?"+parameter_1_name+parameter_1_value
    print(final_url)
    return final_url
        



def call_api():
    
    print("call_apifired")

    # Prepare API Call
    source_url = "https://api.twitch.tv/helix/streams"
    url = build_api_url(source_url)
    
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
    response = requests.get(url, headers=headers)
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