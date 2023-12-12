from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/results", methods=['GET', 'POST'])
def results():
    print("hit results root")
    return render_template('results.html')
