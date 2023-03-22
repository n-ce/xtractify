from bottle import route, request, run
from yt_dlp import YoutubeDL


@route('/<a>/<b>')
def index(a, b):
    if request.headers['referer'] == "https://ytify.netlify.app/":
        return YoutubeDL({
            'format': b
        }).extract_info('https://youtu.be/' + a, download=False)["url"]

# api/<youtube-id>/<itag-required> returns an authenticated url string

run(host='0.0.0.0', port='1234')
