from sanic import Sanic,text
from yt_dlp import YoutubeDL

app = Sanic('xtractify')

@app.get('/')
async def index(request):
    return text('/uid/itag')

@app.get('/<id>/<itag>')
async def main(request,id,itag):
    ydl = YoutubeDL({'format': itag}).extract_info('https://youtu.be/'+id, download=False)
    if ydl :
        return text(ydl["url"])

