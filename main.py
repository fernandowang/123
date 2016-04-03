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
#
import webapp2
import os
import logging
import jinja2   


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/index.html")
        path = self.request.path
        self.response.write(template.render({"title": "Home", "path":path}))

class ProjectHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/projects.html")
        path = self.request.path
        self.response.write(template.render({"title": "Projects", "path":path}))

class ResumeHandler(webapp2.RequestHandler):

     def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/resume.html")
        path = self.request.path
        self.response.write(template.render({"title": "Resume", "path":path}))

class ContactmeHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template("templates/contactme.html")
        path = self.request.path
        self.response.write(template.render({"title": "Contact", "path":path}))
            


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html',MainHandler),
    ('/projects.html',ProjectHandler),
    ('/resume.html',ResumeHandler),
    ('/contactme.html',ContactmeHandler)

], debug=True)
