from flask import Flask, render_template, request
from get_subtitles import extract_subtitles
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        subs = extract_subtitles(url)  
        return render_template('result.html', subs=subs)
    
    return render_template('index.html')
    
