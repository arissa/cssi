import logging
import webapp2
import jinja2
import os
import components

jinja_environment = jinja2.Environment(loader= 
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = jinja_environment.get_template('polymertest.html')
        self.response.out.write(template.render(template_values))

routes = [
    ('/', MainHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
