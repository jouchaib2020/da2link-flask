from flask import Flask, render_template, request
from get_subtitles import extract_subtitles
from get_sumarry import get_response
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def index():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        subs = await extract_subtitles(url) 
        if subs == []:
            return render_template('result.html', subs="Couldn't fetch subtitles please check the provided url")
        data = await get_response(subs)
        return render_template('result.html', subs=data)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 
