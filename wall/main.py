import webapp2
import jinja2
import os
from google.appengine.ext import ndb

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class WallPost(ndb.Model):
    sender = ndb.StringProperty()
    message = ndb.TextProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)
    mood = ndb.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        wall_posts = WallPost.query().order(-WallPost.timestamp).fetch(100)

        template_values = {}
        template_values['wall_posts'] = wall_posts
        template = jinja_environment.get_template('wall.html')
        self.response.out.write(template.render(template_values))

    def post(self):
        
        #1. Read request.
        sender = self.request.get('sender')
        message = self.request.get('message')
        mood = self.request.get('mood')
        #2. Process request (logic & database)

        new_wall_post = WallPost(sender = sender, message = message, mood=mood)
        new_wall_post.put()

        wall_posts = WallPost.query().order(-WallPost.timestamp).fetch(100)
        if new_wall_post not in wall_posts:
            wall_posts.insert(0,new_wall_post)
            
        #3. Render the response.
        template_values = {}
        template_values['wall_posts'] = wall_posts
        template = jinja_environment.get_template('wall.html')
        self.response.out.write(template.render(template_values))

class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        #1. Read request.
        urlsafe = self.request.get('key')
        #1.5 normally you would need to check for errors around here.
        #2. Process request (logic & database)
        wall_post_key = ndb.Key(urlsafe=urlsafe)
        wall_post = wall_post_key.get()
        sender = wall_post.sender
        wall_post_key.delete()
        #3. Render the response.
        self.redirect('/')
        #self.response.write('Deleted a post from : %s' %sender)


routes = [
    ('/', MainHandler),
    ('/delete', DeleteHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
