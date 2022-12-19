import bottle
from bottle import route, request, response, template
import yt_dlp

@bottle.route('/')
def index():
    return '<audio controls src=\"' + yt_dlp.YoutubeDL({'format':request.query.format}).extract_info(request.query.id)["url"] + '\"></audio>'

bottle.run(host='0.0.0.0', port=1234)
