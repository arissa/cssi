import jinja2
import os
import webapp2 
import logging

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomepageHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('index.html')
    self.response.write(template.render())

class ContactHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('contact.html')
    self.response.write(template.render())
  def post(self):
    template = jinja_environment.get_template('contact.html')
    name = self.request.get('name')
    subject = self.request.get('subject')
    message = self.request.get('message')
    logging.info('%s, %s, %s') %(name, subject, message)
    self.response.write(template.render())



routes = [
    ('/index.*', HomepageHandler),
    ('/contact.*', ContactHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)