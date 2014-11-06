import webapp2

hello_form = '''
<form action = '/hello' method = 'post'>
    <input name = 'first' placeholder = 'Enter your first name' >
    <input name = 'last' placeholder = 'Enter your last name' >
    <button>Submit</button>
</form>
'''
class HelloHandler(webapp2.RequestHandler):
    #get will add a query string, ideal for searches
    def get(self):
        self.response.write(hello_form)
    #post will not add a query string, ideal for logins (like facebook) since it won't show your login info
    def post(self):
        first = self.request.get('first').capitalize()
        last = self.request.get('last').capitalize()

        if first and last:
            full_name = '%s %s' %(first, last)
            self.response.write('')
            self.response.write('Hello, %s!' % (full_name))
        self.response.write(hello_form)

class ErrorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('404 Not Found')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Goodbye!')     

routes = [
    ('/hello', HelloHandler),
    ('/goodbye', GoodbyeHandler),
    ('/.*', ErrorHandler),
]

app = webapp2.WSGIApplication(routes, debug=True)