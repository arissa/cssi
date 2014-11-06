import logging
import jinja2
import webapp2
import os
import random

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {'count':0}
        template = jinja_environment.get_template('zoltar.html')
        self.response.out.write(template.render(template_values))


    def post(self):
        count = self.request.get('count')
        logging.info('COUNT: %s' % count)

        if count:
            count = int(count)
        else:
            count = -1


        count += 1

        fortune1 = 'You will live long and prosper'
        fortune2 = 'You will find true happiness'
        fortune3 = 'You will not be able to find any dessert tonight'
        fortune4 = 'You will spill all over yourself'

        fortunes = [fortune1,fortune2, fortune3, fortune4]
        random_fortune = random.choice(fortunes)

        template_values = {'fortune':random_fortune, 'count':count}
        template = jinja_environment.get_template('zoltar.html')
        self.response.out.write(template.render(template_values))

routes = [
    ('/', MainHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
