import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
import webapp2

import os
from google.appengine.ext.webapp import template


class Ghostname(db.Model):

    """Models Ghostname with creator and which user has taken it, if any."""
    ghostname = db.StringProperty(multiline=True)
    creator = db.UserProperty()
    taken_by = db.UserProperty()
    date = db.DateTimeProperty(auto_now_add=True)


class User(db.Model):
    username = db.UserProperty()
    is_admin = db.BooleanProperty()


class MainPage(webapp2.RequestHandler):

    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        ghostnames = db.GqlQuery(
            "SELECT * FROM Ghostname ORDER BY ghostname ASC")

        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_linktext': url_linktext,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


class Get_name(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
        }
        path = os.path.join(os.path.dirname(__file__), 'getname.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


class Results(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getname', Get_name),
    ('/results', Results)
], debug=True)


def main():
    app.RUN()


if __name__ == '__main__':
    main()
