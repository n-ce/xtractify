from sanic import Sanic,text
from yt_dlp import YoutubeDL

app = Sanic('xtractify')

@app.get('/<id>/<itag>')
async def index(request,id,itag):
    ydl = YoutubeDL({'format': itag}).extract_info('https://youtu.be/'+id, download=False)
    if ydl :
        return text(ydl["url"])

# api/<youtube-id>/<itag-required> returns an authenticated url string

