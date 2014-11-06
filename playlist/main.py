import jinja2
import os
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import time

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Playlist(ndb.Model):
    title = ndb.StringProperty()
    owner = ndb.UserProperty()
    def url(self):
        url = '/playlist?key=%s' % self.key.urlsafe()
        return url

class Song(ndb.Model):
    artist = ndb.StringProperty()
    title = ndb.StringProperty()
    playlist_key = ndb.KeyProperty(kind=Playlist)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}

        if user:
            logout_url = users.create_logout_url('/')
            template_values['user'] = user
            template_values['logout_url'] = logout_url

            playlists = Playlist.query(Playlist.owner == user).fetch(100)
            template_values['playlists'] = playlists

        else:
            login_url = users.create_login_url('/')
            template_values['login_url'] = login_url


        template = jinja_environment.get_template('home.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        title = self.request.get('title')
        user = users.get_current_user()

        #TODO: check for errors

        playlist = Playlist(title = title, owner = user)
        playlist.put()
        time.sleep(2)

        self.redirect('/')

class PlaylistHandler(webapp2.RequestHandler):
    def get(self):
        urlsafe = self.request.get('key')
        playlist_key=ndb.Key(urlsafe=urlsafe)
        playlist = playlist_key.get()
        #TODO: better error handling
        songs = Song.query(Song.playlist_key == playlist_key).fetch(100)

        template_values = {}
        template_values['playlist'] = playlist
        template_values['songs'] = songs 
        template = jinja_environment.get_template('playlist.html')
        self.response.out.write(template.render(template_values))
    def post(self):
        artist = self.request.get('artist')
        title = self.request.get('title')
        urlsafe_playlist_key = self.request.get('playlist_key')
        playlist_key = ndb.Key(urlsafe=urlsafe_playlist_key)
        playlist = playlist_key.get()
        song = Song(artist=artist, title=title, playlist_key=playlist_key)
        song.put()

        time.sleep(2)
        self.redirect(playlist.url())




routes = [
    ('/', MainHandler),
    ('/playlist', PlaylistHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
