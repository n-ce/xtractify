import bottle
import yt_dlp

@bottle.route('/<query>')
def index(query):
  return '<!DOCTYPE html><html><audio controls src=\"'+ yt_dlp.YoutubeDL({'format':query.split("+")[1]}).extract_info("https://www.youtube.com/watch?v="+query.split("+")[0])["url"]+'\"></audio></html>' 

bottle.run(host='0.0.0.0', port=1234)