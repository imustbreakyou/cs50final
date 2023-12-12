from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

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

        results = "data"
        return render_template('results.html', results=results)
    else:
        return redirect("/")
    

