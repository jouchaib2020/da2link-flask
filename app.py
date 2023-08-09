from flask import Flask, render_template, request
from get_subtitles import extract_subtitles
from get_sumarry import get_response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        subs = extract_subtitles(url)  
        data = get_response(subs)
        return render_template('result.html', subs=data)
    
    return render_template('index.html')
    
