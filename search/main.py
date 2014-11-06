import webapp2
import jinja2
import os
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import logging


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

#class Link(ndb.Model)

class MainHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = jinja_environment.get_template('hello.html')
    self.response.out.write(template.render(template_values))

class SearchHandler(webapp2.RequestHandler):
    def post(self):
        url = self.request.get('user-url')
        result = urlfetch.fetch(url)
        if result.status_code == 200:
            html = result.content
            num_links = html.count('href')


            template_values = {'num_chars':len(html), 'num_links':num_links}
            template = jinja_environment.get_template('results.html')
            self.response.out.write(template.render(template_values))

            self.response.out.write(html)

#class LinksHandler(webapp2.RequestHandler):
    #def post(self):


routes = [
    ('/', MainHandler),
    ('/results', SearchHandler),
    #('/links', LinksHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
