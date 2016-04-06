# -*- coding: utf-8 -*-
import cgi
# import datetime
# import urllib
# import wsgiref.handlers

# import pdb
# pdb.set_trace()

import os
from google.appengine.api import users
from google.appengine.ext import db

import jinja2
import webapp2


# from google.appengine.ext.webapp import template
# from oauth2client.client import flow_from_clientsecrets

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class Ghostname(db.Model):

    """Models Ghostname with creator and which user has taken it, if any."""
    ghostname = db.StringProperty(required=True)
    creator = db.StringProperty(required=True)
    taken_by = db.StringProperty()
    is_taken = db.BooleanProperty(default=False)


class User(db.Model):
    username = db.UserProperty()
    is_admin = db.BooleanProperty()


# def ghostnameparent_key():
#     return db.Key.from_path('Ghostname', 'default_ghostnametable')


def ghostname_key():
    return db.Key.from_path('Ghostname', 'default_ghostnametable')


def addInitialNames():
    g1 = Ghostname(parent=ghostname_key(),
                   creator='Default', ghostname='Betel geuse')
    g2 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Bhoot')
    g3 = Ghostname(parent=ghostname_key(),
                   creator='Default', ghostname='Bloody Mary')
    g4 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Bogle')
    g5 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Casper')
    g6 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Chindi')
    g7 = Ghostname(parent=ghostname_key(),
                   creator='Default', ghostname='Cihuateteo')
    g8 = Ghostname(parent=ghostname_key(),
                   creator='Default', ghostname='Clytemnestra')
    g9 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Draugr')
    g10 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Dybbuk')
    g11 = Ghostname(parent=ghostname_key(),
                    key_name='Gjenganger', creator='Default', ghostname='Gjenganger')
    g12 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname=u'Guĭ')
    g13 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Ibbur')
    g14 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Jima')
    g15 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Jinn')
    g16 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='La Llorona')
    g17 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname="Moaning Myrtle")
    g18 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Mr. Boogedy')
    g19 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Nachzehrer')
    g20 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Blinky')
    g21 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Pinky')
    g22 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Inky')
    g23 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Clyde')
    g24 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Patrick Swayze')
    g25 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Phi Tai Hong')
    g26 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Pishacha')
    g27 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Poltergeist')
    g28 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Revenant')
    g29 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Ringwraith')
    g30 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Slender Man')
    g31 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Slimer')
    g32 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Space Ghost')
    g33 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Strigoi')
    g34 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Candyman')
    g35 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='The Crypt Keeper')
    g36 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Headless Horseman')
    g37 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname=u'Tomás')
    g38 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Vetala')
    g39 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname=u'Wiedergänger')
    g40 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Xunantunich')
    g41 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname=u'Yūrei')
    g42 = Ghostname(parent=ghostname_key(),
                    creator='Default', ghostname='Zhong Kui')
    g43 = Ghostname(
        parent=ghostname_key(), creator='Default', ghostname='Zuul')

    db.put([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22,
            g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33, g34, g35, g36, g37, g38, g39, g40, g41, g42, g43])


class MainPage(webapp2.RequestHandler):

    # flow = client.flow_from_clientsecrets(
    # 'client_secrets.json',
    # scope='https://www.googleapis.com/auth/drive.metadata.readonly',
    # redirect_uri='http://www.example.com/oauth2callback')

    def get(self):
        # flow = flow_from_clientsecrets(os.path.join(os.path.dirname(__file__), 'client_secrets.json'),
        #                     scope='https://www.googleapis.com/auth/userinfo.email',
        #                     redirect_uri='http://localhost:8080')
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        addInitialNames()

        # ghostnames = Ghostname.all()
        ghostnames = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "ORDER BY ghostname ASC",
                                 ghostname_key())
        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_link_text': url_link_text,
            'get_name_link_text': 'Get a Phantom name'
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

        # path = os.path.join(os.path.dirname(__file__), 'index.html')
        # self.response.out.write(template.render(path, template_values))

    def post(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        taken_by = cgi.escape(self.request.get('taken_by'))
        num_ghostnames_taken_by_user = Ghostname.all().filter(
            "taken_by =", taken_by).count()

        if num_ghostnames_taken_by_user > 0:
            dbprevghostname = Ghostname.all().filter(
                "taken_by =", taken_by).get()
            dbprevghostname.is_taken = False
            dbprevghostname.taken_by = None
            dbprevghostname.put()

        ghostname = self.request.get('ghostname').decode('utf-8')
        dbghostnameentity = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "AND ghostname = :2",
                                 ghostname_key(),
                                 ghostname).get()
        ghostnames = Ghostname.all()
        dbghostnameentity.is_taken = True
        dbghostnameentity.taken_by = taken_by
        dbghostnameentity.put()

        ghostnames = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "ORDER BY ghostname ASC",
                                 ghostname_key())
        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_link_text': url_link_text,
            'get_name_link_text': 'Change your current Phantom name'
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

        # path = os.path.join(os.path.dirname(__file__), 'index.html')
        # self.response.out.write(template.render(path, template_values))


class Get_name(webapp2.RequestHandler):

    def get(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        template_values = {
            'url': url,
            'url_link_text': url_link_text,
        }

        template = JINJA_ENVIRONMENT.get_template('getname.html')
        self.response.write(template.render(template_values))
        # path = os.path.join(os.path.dirname(__file__), 'getname.html')
        # self.response.out.write(template.render(path, template_values))


class Results(webapp2.RequestHandler):

    def post(self):
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        ghostnames = Ghostname.all().filter("is_taken =", False).run(limit=3)
        firstname = cgi.escape(self.request.get('firstname'))
        surname = cgi.escape(self.request.get('surname'))

        template_values = {
            'url': url,
            'url_link_text': url_link_text,
            'ghostnames': ghostnames,
            'firstname': firstname,
            'surname': surname,
        }
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render(template_values))
        # path = os.path.join(os.path.dirname(__file__), 'results.html')
        # self.response.out.write(template.render(path, template_values))

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
