from sanic import Sanic,text
from yt_dlp import YoutubeDL
from cors import add_cors_headers
from options import setup_options


app = Sanic('xtractify')

@app.get('/')
async def index(request):
    return text('Please enter a 11 letter id followed by a 3 digit itag /uid/itag')

@app.get('/<id>/<itag>')
async def main(request,id,itag):
    ydl = YoutubeDL({'format': itag}).extract_info('https://youtu.be/'+id, download=False)
    if ydl :
        return text(ydl['url'])

# Add OPTIONS handlers to any route that is missing it
app.register_listener(setup_options, "before_server_start")

# Fill in CORS headers
app.register_middleware(add_cors_headers, "response")
