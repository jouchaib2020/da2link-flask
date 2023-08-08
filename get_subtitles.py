import requests

def extract_subtitles(url):
    response = requests.get(url)
    if response.status_code == 200:
        subtitles_data = response.json()
        subtitles_text = ""
        for event in subtitles_data.get('events', []):
            segs = event.get('segs', [])
            if segs:
                subtitle_text = ' '.join(seg.get('utf8', '') for seg in segs)
                subtitles_text += subtitle_text + " "

        return subtitles_text.strip()
    else:
        print("Error: Unable to fetch subtitles.")
        return []