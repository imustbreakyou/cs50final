# Twitch API Research

#### Video Demo: https://youtu.be/uQba-u_K03o


#### Description:
Twitch API Research is a simple project built to demonstrate a novice command of frontend development and an ability to pull, process, and display data. The user is presented with an empty state screen and expandable filters that allow querying the Twitch livestreams API for the 20 most popular live streams based on language, type, or game category. The app displays the information live with a stylized textual indication of stream information.

During this project, I learned and applied the basics of Git, including adds, commits, branches, and hosting on GitHub. This was motivated by my desire to align with industry best practices and address my own version control struggles.

#### Frontend Development:
I made significant progress in front-end development, starting with Bootstrap and moving to a more hands-on approach with HTML/CSS. I took a course in CSS/HTML basics, which empowered me to layout my project as desired. While the responsiveness could be improved, I'm pleased with the initial outcome and the fact that I built it from scratch.

- **HTML Files**:
  - `layout.html`: The master template for the project. It includes the basic HTML structure, head, header, main container, and scripts common across all pages, utilizing Jinja templating for dynamic title and content insertion.
  - `index.html`: The main landing page that extends `layout.html`. It includes specific content like the filter container and results display logic, determining whether to show default results or fetched data based on user input.
  - `filter.html`: Contains the HTML structure for the filtering functionality with checkboxes and input elements for filtering Twitch livestreams based on various criteria.
  - `results.html`: Displays the results fetched from the Twitch API, formatting and presenting the data in a user-friendly way.
  - `default-results.html`: Shows a default or placeholder view when no specific search has been conducted yet.

Jinja templating was used for dynamic content rendering, applying DRY practices in filter selectors.

#### Backend Development (`app.py`):
The `app.py` file is the heart of the backend development, handling several critical functionalities:
- **Flask Application Initialization**: Setting up the Flask app and configuring it for development.
- **Environmental Variable Handling**: Securely accessing environmental variables for API authentication.
- **Route Handling**:
  - `@app.route("/")`: Defines the main route for the application, handling both GET and POST requests. It renders the `index.html` with data based on user queries.
- **Form Handling and API Call**: Processes user input from forms, constructs query parameters, and makes an API call to Twitch.
- **Data Parsing**: Parses the JSON response from the API and organizes it into a usable format for the frontend.

- **Environmental Variables**:
  - `load_dotenv('/absolute/path/to/.env')`: Loads environmental variables from a `.env` file, ensuring sensitive data like API keys and OAuth tokens are secure.
  - `client_id = os.getenv('TWITH_CLIENT_ID')` and `oauth_token = os.getenv('TWITCH_OAUTH_TOKEN')`: Retrieves Twitch API client ID and OAuth token from the environment variables for secure API access.

- **Dictionary Builder**:
  - Constructs a dictionary named `streams` from JSON data received from the Twitch API, organizing stream information like user name, game name, viewer count, and language for front-end use.

#### JavaScript Implementation (`scripts.js`):
The `scripts.js` file adds interactivity to the web application:
- **Filter Expansion and Collapse**: Implements logic to expand and collapse filter sections, enhancing the user experience.
- **Clearing Checkboxes**: Provides functionality to clear all selected checkboxes with a single click, making the UI more user-friendly and efficient.

#### Attributions and Acknowledgements:
- Git and GitHub for version control.
- Flask for the backend framework.
- HTML/CSS basics course for frontend development.
- Various online resources for specific issues and guidance.