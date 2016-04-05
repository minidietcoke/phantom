# -*- coding: utf-8 -*-
import cgi
import datetime
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
import webapp2

import os
from google.appengine.ext.webapp import template
# from oauth2client.client import flow_from_clientsecrets

# flow = flow_from_clientsecrets(os.path.join(os.path.dirname(__file__), 'client_secrets.json'),
#                             scope='https://www.googleapis.com/auth/userinfo.email',
#                             redirect_uri='http:localhost:8080')

# try:
#     import googleclouddebugger
#     googleclouddebugger.AttachDebugger()
# except ImportError:
#     pass


class Ghostname(db.Model):

    """Models Ghostname with creator and which user has taken it, if any."""
    ghostname = db.StringProperty(multiline=True)
    creator = db.StringProperty()
    taken_by = db.StringProperty()
    is_taken = db.BooleanProperty(default=False)


class User(db.Model):
    username = db.UserProperty()
    is_admin = db.BooleanProperty()


def addInitialNames():
    g1 = Ghostname(key_name='Betelgeuse', creator='Default', ghostname='Betelgeuse')
    g2 = Ghostname(key_name='Bhoot', creator='Default', ghostname='Bhoot')
    g3 = Ghostname(key_name='Bloody Mary', creator='Default', ghostname='Bloody Mary')
    g4 = Ghostname(key_name='Bogle', creator='Default', ghostname='Bogle')
    g5 = Ghostname(key_name='Casper', creator='Default', ghostname='Casper')
    g6 = Ghostname(key_name='Chindi', creator='Default', ghostname='Chindi')
    g7 = Ghostname(key_name='Cihuateteo', creator='Default', ghostname='Cihuateteo')
    g8 = Ghostname(key_name='Clytemnestra', creator='Default', ghostname='Clytemnestra')
    g9 = Ghostname(key_name='Draugr', creator='Default', ghostname='Draugr')
    g10 = Ghostname(key_name='Dybbuk', creator='Default', ghostname='Dybbuk')
    g11 = Ghostname(key_name='Gjenganger', creator='Default', ghostname='Gjenganger')
    g12 = Ghostname(key_name=u'Guĭ', creator='Default', ghostname=u'Guĭ')
    g13 = Ghostname(key_name='Ibbur', creator='Default', ghostname='Ibbur')
    g14 = Ghostname(key_name='Jima', creator='Default', ghostname='Jima')
    g15 = Ghostname(key_name='Jinn', creator='Default', ghostname='Jinn')
    g16 = Ghostname(key_name='La Llorona', creator='Default', ghostname='La Llorona')
    g17 = Ghostname(key_name='Moaning Myrtle', creator='Default', ghostname='Moaning Myrtle')
    g18 = Ghostname(key_name='Mr. Boogedy', creator='Default', ghostname='Mr. Boogedy')
    g19 = Ghostname(key_name='Nachzehrer', creator='Default', ghostname='Nachzehrer')
    g20 = Ghostname(key_name='Blinky', creator='Default', ghostname='Blinky')
    g21 = Ghostname(key_name='Pinky', creator='Default', ghostname='Pinky')
    g22 = Ghostname(key_name='Inky', creator='Default', ghostname='Inky')
    g23 = Ghostname(key_name='Clyde', creator='Default', ghostname='Clyde')
    g24 = Ghostname(key_name='Patrick Swayze', creator='Default', ghostname='Patrick Swayze')
    g25 = Ghostname(key_name='Phi Tai Hong', creator='Default', ghostname='Phi Tai Hong')
    g26 = Ghostname(key_name='Pishacha', creator='Default', ghostname='Pishacha')
    g27 = Ghostname(key_name='Poltergeist', creator='Default', ghostname='Poltergeist')
    g28 = Ghostname(key_name='Revenant', creator='Default', ghostname='Revenant')
    g29 = Ghostname(key_name='Ringwraith', creator='Default', ghostname='Ringwraith')
    g30 = Ghostname(key_name='Slender Man', creator='Default', ghostname='Slender Man')
    g31 = Ghostname(key_name='Slimer', creator='Default', ghostname='Slimer')
    g32 = Ghostname(key_name='Space Ghost', creator='Default', ghostname='Space Ghost')
    g33 = Ghostname(key_name='Strigoi', creator='Default', ghostname='Strigoi')
    g34 = Ghostname(key_name='Candyman', creator='Default', ghostname='Candyman')
    g35 = Ghostname(key_name='The Crypt Keeper', creator='Default', ghostname='The Crypt Keeper')
    g36 = Ghostname(key_name='Headless Horseman', creator='Default', ghostname='Headless Horseman')
    g37 = Ghostname(key_name=u'Tomás', creator='Default', ghostname=u'Tomás')
    g38 = Ghostname(key_name='Vetala', creator='Default', ghostname='Vetala')
    g39 = Ghostname(key_name=u'Wiedergänger', creator='Default', ghostname=u'Wiedergänger')
    g40 = Ghostname(key_name='Xunantunich', creator='Default', ghostname='Xunantunich')
    g41 = Ghostname(key_name=u'Yūrei', creator='Default', ghostname=u'Yūrei')
    g42 = Ghostname(key_name='Zhong Kui', creator='Default', ghostname='Zhong Kui')
    g43 = Ghostname(key_name='Zuul', creator='Default', ghostname='Zuul')

    db.put([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33, g34, g35, g36, g37, g38, g39, g40, g41, g42, g43])


class MainPage(webapp2.RequestHandler):

    # flow = client.flow_from_clientsecrets(
    # 'client_secrets.json',
    # scope='https://www.googleapis.com/auth/drive.metadata.readonly',
    # redirect_uri='http://www.example.com/oauth2callback')

    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        addInitialNames()

        ghostnames = Ghostname.all()

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

    # def post(self):
    #     if users.get_current_user():
    #         url = users.create_logout_url(self.request.uri)
    #         url_linktext = 'Sign Out'
    #     else:
    #         url = users.create_login_url(self.request.uri)
    #         url_linktext = 'Login'

    #     template_values = {
    #         'url': url,
    #         'url_linktext': url_linktext,
    #     }
    #     path = os.path.join(os.path.dirname(__file__), 'results.html')
    #     self.response.out.write(template.render(path, template_values))


class Results(webapp2.RequestHandler):
    def post(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        ghostnames = Ghostname.all()
        ghostnames = ghostnames.filter("is_taken =", False)
        ghostnames = ghostnames.run(limit=3)

        firstname = cgi.escape(self.request.get('firstname'))
        surname = cgi.escape(self.request.get('surname'))

        template_values = {
            'url': url,
            'url_linktext': url_linktext,
            'ghostnames': ghostnames,
            'firstname': firstname,
            'surname': surname
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/getname', Get_name),
    ('/results', Results)
], debug=True)


def main():
    try:
      import googleclouddebugger
      googleclouddebugger.AttachDebugger()
    except ImportError:
      pass
    app.RUN()


if __name__ == '__main__':
    main()
