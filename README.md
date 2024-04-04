# Xtractify Reborn

- Reborn with Sanic, with 
  - **17.5x** more requests per second
  - **15x** lesser latency on average compared to bottle.py.
- zero dependencies, well technically sanic & yt-dlp are still required.

#### [`main.py`](https://github.com/n-ce/xtractify/blob/main/main.py)
```py
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
        return text(ydl['url'])
```

Thanks to render for hosting the web service.
