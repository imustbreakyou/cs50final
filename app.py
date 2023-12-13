# ATTRIBUTIONS #flask 
# environmental variable information from: https://ioflood.com/blog/python-get-environment-variable/#:~:text=to%20access%20it.-,Use%20os.,to%20safely%20access%20environment%20variables.#
# calling environmental variables in python from this source: https://dagster.io/blog/python-environment-variables
# further .env assitance from here: https://stackoverflow.com/questions/41546883/what-is-the-use-of-python-dotenv # 
from flask import Flask, request, render_template
from dotenv import load_dotenv, find_dotenv
import os
import requests



app = Flask(__name__)
app.debug = True

print(os.environ)



@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/results", methods=['GET', 'POST'])
def results():
    print("hit results root from nav")
    return render_template('results.html')









    

@app.route("/call_api", methods=['GET', 'POST'])
def call_api():
    if request.method == "POST":
        print("post request received")
    
        # Access API keys 
        load_dotenv('/absolute/path/to/.env')
        client_id = os.getenv('TWITH_CLIENT_ID')
        oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')

        if not client_id or not oauth_token:
            print("missing API token or id")
            return None

        url = "https://api.twitch.tv/helix/streams"

        headers = {
            
            'Client-Id': client_id,
            'Authorization': f'Bearer {oauth_token}'

        }
        
        response = requests.get(url, headers=headers)
        print(response)

        if response.status_code == 200:
            #return repsonse.json()
            results = "data"
            return render_template('results.html', results=results)
        
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
    else:
        return redirect('/')

    

        