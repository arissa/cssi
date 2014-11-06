#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#in app engine, follow the flow
#
import logging
import webapp2
from google.appengine.api import urlfetch
import jinja2
import os
from google.appengine.ext import ndb

#jinja_environment is a global variable. two variables can use the environment
jinja_environment = jinja2.Environment(loader= 
    jinja2.FileSystemLoader(os.path.dirname(__file__)))
    
class ALink(ndb.Model): #WallPost is a type of ndb model. it extends the ndb model
    aLink = ndb.StringProperty()
    
class FormHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        #url = "http://www.google.com/"
        myUrl = self.request.get('typeUrl')
        #result = urlfetch.fetch(myUrl)
        template_values = {}
        #if result.status_code == 200:
          #self.response.out.write(template.render((result.content))  
        template = jinja_environment.get_template('user.html')
        self.response.out.write(template.render(template_values))  
        #self.response.out.write(result.content)

class UrlHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world!')
        
        
        myUrls = self.request.get('typeUrl')
        myUrls = myUrls.split()
        #result = urlfetch.fetch(url)
        for url in myUrls:
            
            result = urlfetch.fetch(url)
        template_values = {}
        
        if result.status_code == 200:
          #self.response.out.write(template.render((result.content))  
          template = jinja_environment.get_template('results.html')
          #self.response.out.write(len(result.content))
          #template['length of content': len(result.content)]
          #self.response.out.write(len(result.content))
          
          template_values['length'] = len(result.content)
          self.response.out.write(template.render(template_values)) 
          self.response.out.write(result.content)
class DataHandler(webapp2.RequestHandler):#THIS WORKS, YEAH MAN
    def get(self):
        allLinks = self.request.get('allLinks')
        linksList = allLinks.split()
        for link in linksList:
            logging.info('This is what one link looks like:' + str(link))
            aLink = ALink( aLink = link)
            aLink.put()
        self.redirect('/display')
        
class getDataHandler(webapp2.RequestHandler):
    def get(self):
        links = ALink.query().fetch(100)
        for link in links:
            self.response.out.write(link)
        template_values = {} #makes the code dynamic. accepts data. insert anything dynamic into the pattern
        template_values['links'] = links
        template = jinja_environment.get_template('display.html') #this file is the template you've just loaded
        self.response.out.write(template.render(template_values))#this is what you're adding in
        

app = webapp2.WSGIApplication([
     ('/', FormHandler), ('/url', UrlHandler), ('/data', DataHandler), ('/display', getDataHandler)
], debug=True)
