# ATTRIBUTIONS #flask 
# environmental variable information from: https://ioflood.com/blog/python-get-environment-variable/#:~:text=to%20access%20it.-,Use%20os.,to%20safely%20access%20environment%20variables.#
# calling environmental variables in python from this source: https://dagster.io/blog/python-environment-variables
# further .env assitance from here: https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv # 
# API response assitance from: https://www.geeksforgeeks.org/response-json-python-requests/
# Form to dict from here https://vortex.hashnode.dev/how-to-obtain-dict-from-a-flask-request-form-ck6c6ertx006s3cs1rw60rsk8 #
# Help with parsing Json: https://brightdata.com/blog/how-tos/parse-json-data-with-python
# Dynamic URL creation from: https://stackoverflow.com/questions/74435785/python-create-dynamic-url-for-api-call
# Negative Indexing to remove final character from string: https://www.geeksforgeeks.org/python-program-to-remove-last-character-from-the-string/
# Rendering a dictionary in jinja and python: https://stackoverflow.com/questions/19141073/rendering-a-dictionary-in-jinja2
# remove final character from string: https://www.w3schools.com/python/ref_string_rstrip.asp#:~:text=The%20rstrip()%20method%20removes,default%20trailing%20character%20to%20remove.

from flask import Flask, request, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
import requests




app = Flask(__name__)
app.debug = True

source_url = "https://api.twitch.tv/helix/streams"




@app.route("/", methods=['GET', 'POST'])
def index():
    # hard coded top games TODO def get_top-games()
    top_games = [{'game_name': 'League of Legends', 'game_id': '21779'}, 
            {'game_name': 'Just Chatting', 'game_id': '509658'},
            {'game_name': 'World of Warcraft', 'game_id': '18122'},
            {'game_name': 'Fortnite', 'game_id': '33214'},
            {'game_name': 'Minecraft', 'game_id': '27471'}]
    
    language = [{'language': 'English', 'code': 'en'}, 
            {'language': 'Spanish', 'code': 'es'},
            {'language': 'German', 'code': 'de'}
    ]
       
    search_executed = False

    if request.method == "POST":

        search_executed = True
     
        streams = form_handler()

        total_results = str(len(streams))

        return render_template('index.html', top_games=top_games, streams=streams, total_results=total_results, search_executed=search_executed, language=language)
    
    else:
    
        return render_template('index.html', top_games=top_games, search_executed=search_executed, language=language)



def form_handler():


    # language intake
    language = request.form.getlist('language')

   
    # type intake
    type = request.form.getlist('type')

    # game intake 
    
    game = request.form.getlist('game')

    
    return process_form(language, type, game)


    
def process_form(language, type, game):

    # set empty string
    parameter_string = ""

    if language:  
        #iterate over dictionary
        for lang in language:
            #use f-string for url creation
            parameter_string += f"language={lang}&"



     
    if type:  
        for item in type:
            #use f-string for url creation
            parameter_string += f"type={item}&"
            print("item processed")
    


    if game:
        for item in game:
             #use f-string for url creation
            parameter_string += f"game_id={item}&"



    parameter_string = parameter_string.rstrip('&')

    return build_api_url(source_url, parameter_string)
    



def build_api_url(source_url, parameter_string):

     # Prepare API Call
    api_url = f"{source_url}?{parameter_string}"

    

    #return final_url
    return call_api(api_url)
        





def call_api(api_url):

    load_dotenv('/absolute/path/to/.env')
    client_id = os.getenv('TWITH_CLIENT_ID')
    oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')

    # Error handling for missing access tokens
    if not client_id or not oauth_token:
 
        return None
    
    headers = {
        
        'Client-Id': client_id,
        'Authorization': f'Bearer {oauth_token}'

    }
    # THIS MAKES THE REQUEST 
    response = requests.get(api_url, headers=headers)

    
    # Error Handling for failed API Call 
    if response.status_code != 200:
    
        return None

    
    # Store json data in dictionary 
    json_data = response.json()
    
    # dictionary builder 
    streams = {}
    stream_counter = 0
    for item in json_data['data']:
        # TODO safe search filter! (if is_mature == FALSE
        stream_counter += 1
        streams[item['user_id']] = {
            'user_id': item['user_id'],
            'user_name': item['user_name'],
            'game_name': item['game_name'],
            'viewer_count': str(item['viewer_count']),
            'language': item['language'],
            'type': item['type'],
            
            'game_id': item['game_id']
        }
        
    

    return streams
