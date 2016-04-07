# -*- coding: utf-8 -*-
# import pdb
# pdb.set_trace()
import cgi
import os
from google.appengine.api import users
from google.appengine.ext import db
import urllib
import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

addedNames = 0


class Ghostname(db.Model):

    """Models Ghostname with creator and which user has taken it, if any."""
    ghostname = db.StringProperty(required=True)
    creator = db.StringProperty(default="Default")
    taken_by = db.StringProperty()
    is_taken = db.BooleanProperty(default=False)
    last_altered_by = db.StringProperty(default="Default")


class User(db.Model):
    username = db.UserProperty()
    is_admin = db.BooleanProperty()


def ghostname_parent_key():
    return db.Key.from_path('Ghostname', 'default_ghostnametable')


def addInitialNames():
    g1 = Ghostname(parent=ghostname_parent_key(),
                   ghostname='Betelgeuse')
    g2 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Bhoot')
    g3 = Ghostname(parent=ghostname_parent_key(),
                   ghostname='Bloody Mary')
    g4 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Bogle')
    g5 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Casper')
    g6 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Chindi')
    g7 = Ghostname(parent=ghostname_parent_key(),
                   ghostname='Cihuateteo')
    g8 = Ghostname(parent=ghostname_parent_key(),
                   ghostname='Clytemnestra')
    g9 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Draugr')
    g10 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Dybbuk')
    g11 = Ghostname(parent=ghostname_parent_key(),
                    key_name='Gjenganger', ghostname='Gjenganger')
    g12 = Ghostname(
        parent=ghostname_parent_key(), ghostname=u'Guĭ')
    g13 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Ibbur')
    g14 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Jima')
    g15 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Jinn')
    g16 = Ghostname(
        parent=ghostname_parent_key(), ghostname='La Llorona')
    g17 = Ghostname(parent=ghostname_parent_key(),
                    ghostname="Moaning Myrtle")
    g18 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Mr. Boogedy')
    g19 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Nachzehrer')
    g20 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Blinky')
    g21 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Pinky')
    g22 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Inky')
    g23 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Clyde')
    g24 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Patrick Swayze')
    g25 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Phi Tai Hong')
    g26 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Pishacha')
    g27 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Poltergeist')
    g28 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Revenant')
    g29 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Ringwraith')
    g30 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Slender Man')
    g31 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Slimer')
    g32 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Space Ghost')
    g33 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Strigoi')
    g34 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Candyman')
    g35 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='The Crypt Keeper')
    g36 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Headless Horseman')
    g37 = Ghostname(
        parent=ghostname_parent_key(), ghostname=u'Tomás')
    g38 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Vetala')
    g39 = Ghostname(parent=ghostname_parent_key(),
                    ghostname=u'Wiedergänger')
    g40 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Xunantunich')
    g41 = Ghostname(
        parent=ghostname_parent_key(), ghostname=u'Yūrei')
    g42 = Ghostname(parent=ghostname_parent_key(),
                    ghostname='Zhong Kui')
    g43 = Ghostname(
        parent=ghostname_parent_key(), ghostname='Zuul')

    db.put([g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22,
            g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33, g34, g35, g36, g37, g38, g39, g40, g41, g42, g43])


class Main_page(webapp2.RequestHandler):

    def get(self):
        adminurl = users.create_login_url(self.request.uri)
        if users.get_current_user():
            url = users.create_logout_url('/')
            url_link_text = 'Sign Out'
            if users.is_current_user_admin():
                adminurl = '/admin'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        global addedNames
        if addedNames == 0:
            addInitialNames()
            addedNames = 1

        ghostnames = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "ORDER BY ghostname ASC",
                                 ghostname_parent_key())

        adminerror = None
        if self.request.get('error') == 'true':
            adminerror = 'Error: You don\'t have administrator rights with this account, please sign out and log in as Administrator'

        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_link_text': url_link_text,
            'get_name_link_text': 'Get a Phantom name',
            'adminurl': adminurl,
            'adminerror': adminerror
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

    def post(self):
        adminurl = users.create_login_url(self.request.uri)
        if users.get_current_user():
            url = users.create_logout_url('/')
            url_link_text = 'Sign Out'
            if users.is_current_user_admin():
                adminurl = '/admin'
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

        ghostname = cgi.escape(self.request.get('ghostname'))
        dbghostnameentity = db.GqlQuery("SELECT * "
                                        "FROM Ghostname "
                                        "WHERE ANCESTOR IS :1 "
                                        "AND ghostname = :2",
                                        ghostname_parent_key(),
                                        ghostname).get()
        ghostnames = Ghostname.all()
        dbghostnameentity.is_taken = True
        dbghostnameentity.taken_by = taken_by
        dbghostnameentity.put()

        ghostnames = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "ORDER BY ghostname ASC",
                                 ghostname_parent_key())
        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_link_text': url_link_text,
            'get_name_link_text': 'Change your current Phantom name',
            'adminurl': adminurl
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Get_name(webapp2.RequestHandler):

    def get(self):
        adminurl = users.create_login_url(self.request.uri)
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
            if users.is_current_user_admin():
                adminurl = '/admin'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        template_values = {
            'url': url,
            'url_link_text': url_link_text,
            'adminurl': adminurl
        }

        template = JINJA_ENVIRONMENT.get_template('getname.html')
        self.response.write(template.render(template_values))


class Results(webapp2.RequestHandler):

    def get(self):
        self.redirect('/getname')

    def post(self):
        adminurl = users.create_login_url(self.request.uri)
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_link_text = 'Sign Out'
            if users.is_current_user_admin():
                adminurl = '/admin'
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Login'

        ghostnames = Ghostname.all().filter(
            "is_taken =", False).order('ghostname')
        # .run(limit=3)
        firstname = cgi.escape(self.request.get('firstname'))
        surname = cgi.escape(self.request.get('surname'))

        template_values = {
            'url': url,
            'url_link_text': url_link_text,
            'ghostnames': ghostnames,
            'firstname': firstname,
            'surname': surname,
            'adminurl': adminurl
        }
        template = JINJA_ENVIRONMENT.get_template('results.html')
        self.response.write(template.render(template_values))


class Admin(webapp2.RequestHandler):

    def get(self):
        global addedNames
        if addedNames == 0:
            addInitialNames()
            addedNames = 1
        current_user = users.get_current_user()
        adminurl = users.create_login_url(self.request.uri)
        if current_user:
            url = users.create_logout_url('/')
            url_link_text = 'Sign Out'
            current_user = users.get_current_user().nickname()
            if users.is_current_user_admin():
                adminurl = '/admin'
            else:
                self.redirect("/?%s" % urllib.urlencode(dict(error="true")))
        else:
            url = users.create_login_url(self.request.uri)
            url_link_text = 'Sign in'
            self.redirect(url)

        ghostnames = db.GqlQuery("SELECT * "
                                 "FROM Ghostname "
                                 "WHERE ANCESTOR IS :1 "
                                 "ORDER BY ghostname ASC",
                                 ghostname_parent_key())
        template_values = {
            'ghostnames': ghostnames,
            'url': url,
            'url_link_text': url_link_text,
            'get_name_link_text': 'Get a Phantom name',
            'adminurl': adminurl,
            'current_user': current_user
        }

        template = JINJA_ENVIRONMENT.get_template('admin.html')
        self.response.write(template.render(template_values))


class Save(webapp2.RequestHandler):

    def post(self):
        oldghostname = self.request.get('oldghostname')
        newname = self.request.get('newghostname')

        dbghostnameentitynumber = db.GqlQuery("SELECT * "
                                              "FROM Ghostname "
                                              "WHERE ANCESTOR IS :1 "
                                              "AND ghostname = :2",
                                              ghostname_parent_key(),
                                              newname).count()
        if dbghostnameentitynumber == 0:
            if oldghostname == '':
                newghost = Ghostname(parent=ghostname_parent_key(),
                                     creator=users.get_current_user().nickname(), ghostname=newname, last_altered_by=users.get_current_user().nickname())
                newghost.put()
            else:
                dbghostnameentity = db.GqlQuery("SELECT * "
                                                "FROM Ghostname "
                                                "WHERE ANCESTOR IS :1 "
                                                "AND ghostname = :2",
                                                ghostname_parent_key(),
                                                oldghostname).get()
                dbghostnameentity.ghostname = newname
                dbghostnameentity.last_altered_by = users.get_current_user(
                ).nickname()
                dbghostnameentity.put()
        self.redirect('/admin')


class Delete(webapp2.RequestHandler):

    def post(self):
        ghostname = self.request.get('ghostname')
        dbghostnameentity = db.GqlQuery("SELECT * "
                                        "FROM Ghostname "
                                        "WHERE ANCESTOR IS :1 "
                                        "AND ghostname = :2",
                                        ghostname_parent_key(),
                                        ghostname).get()
        dbghostnameentity.delete()
        self.redirect('/admin')


app = webapp2.WSGIApplication([
    ('/', Main_page),
    ('/getname', Get_name),
    ('/results', Results),
    ('/admin', Admin),
    ('/save', Save),
    ('/delete', Delete)
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
