from bs4 import BeautifulSoup
from flask import Flask, render_template

#
import iec

app = Flask(__name__)

@app.route('/')
def index():

    rows = iec.get_details()
    return render_template('index.html', rows = rows)

if __name__ == '__main__':
    app.run(debug=True)
