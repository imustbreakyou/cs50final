# Twitch API Research

#### Video Demo: https://youtu.be/uQba-u_K03o


#### Description:
Twitch API Research is a simple project built to demonstrate a beginner's command of frontend and backend development. The project accesses an API to pull, process, and display data. The user is presented with an empty state screen and expandable filters to allow querying the Twitch livestreams API for the 20 most popular live streams ranked by viewer count. The filter values are hard coded into dictionaries and dynamically visualized to allow for parameters for: language, type, or game category. The app displays the information live with a stylized indication of stream information.

This project was built with Git for version control using adds, commits, branches, and hosting on GitHub. This was motivated by my desire to align with industry best practices and address my frustrations with version control..

#### Frontend Development:
This project features a built from scratch front-end development. To complete this project,  information from The Odin Projects CSS/HTML basics was used, to layout my project as desired. While the responsiveness could be improved, I'm pleased with the initial outcome and the “from scratch” origin.

- **HTML Files**:
  - `layout.html`: The master template for the project. Includes the basic HTML structure, head, header, main container, and scripts common across all pages, utilizing Jinja templating for dynamic title and content insertion.
  - `index.html`: The main landing page that extends `layout.html`.
  - `filter.html`: Contains the HTML structure for the filtering functionality with checkboxes and input elements for filtering Twitch livestreams.
  - `results.html`: Displays the results fetched from the Twitch API.
  - `default-results.html`: Pre-search Empty State

Jinja templating was used for dynamic content rendering, applying DRY practices in filter selectors.

#### Backend Development (`app.py`):
This file could be more pythonic with more modular functions but DRY practices were attempted. The `app.py` file handles:
- **Flask Application Initialization**: Setting up and configuring the Flask app
- **Environmental Variable Handling**: Securely accessing environment variables for API authentication.
- **Route Handling**:
  - `@app.route("/")`: main route for the application, handling both GET and POST requests. It renders the `index.html` with data based on user queries.
- **Form Handling and API Call**: Processes user input from forms, constructs query parameters, and makes an API call to Twitch.
- **Data Parsing**: Parses the JSON response from the API and organizes it into a usable format for the frontend.

- **Environmental Variables**:
  - `load_dotenv('/absolute/path/to/.env')`: Loads environmental variables from a `.env` file, ensuring sensitive data like API keys and OAuth tokens are secure.
  - `client_id = os.getenv('TWITH_CLIENT_ID')` and `oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')`: Retrieves Twitch API client ID and OAuth token from the environment variables for secure API access.

- **Dictionary Builder**:
  - Constructs a dictionary named `streams` from JSON data received from the Twitch API, organizing stream information like user name, game name, viewer count, and language for front-end use.

#### JavaScript Implementation (`scripts.js`):
The `scripts.js` file adds interactivity to the web application:

Grossest violation of DRY. I was unable to figure out querySelectorAll and instead copy and pasted the collapsable JS that I found on stack exchange.

- **Filter Expansion and Collapse**: Implements logic to expand and collapse filter sections, enhancing the user experience.
- **Clearing Checkboxes**: Provides functionality to clear all selected checkboxes with a single click, making the UI more user-friendly and efficient.

#### Attributions and Acknowledgements:
- Git and GitHub for version control.
- Flask for the backend framework.
- HTML/CSS basics course for frontend development.
- Various online resources for specific issues and guidance.
 origin main


