import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Game(ndb.Model):
	user = ndb.UserProperty()
	x = ndb.IntegerProperty()
	y = ndb.IntegerProperty()
	steps = ndb.IntegerProperty()
	direction = ndb.IntegerProperty()


MAZE = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
       ]

def check_walls(maze,game):
	pass
	#TODO: define how to get walls so you can render them. return [] of walls

class MoveHandler(webapp2.RequestHandler):
	def post(self):
		move = self.request.get('move')
		user = users.get_current_user()
		game = Game.query(Game.user == user).get()
		#TODO: Based on the move and the game, update the game.
		#if move==forward and game.direction=0: game.y += 1
		game.put()
		self.redirect('/')
class MainHandler(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	if user:
    		game = Game.query(Game.user == user).get()
    		if not game:
    			game = Game(user=user, x=1, y=4, direction=0, steps=0)
    			game.put()

    		walls = check_walls(MAZE, game)
        template_values = {'walls':walls}
    	template = jinja_environment.get_template('maze.html')
    	self.response.out.write(template.render(template_values))
class MoveHandler(webapp2.RequestHandler):
	def post(self):
		pass
routes = [
    ('/', MainHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
