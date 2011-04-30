#!/usr/bin/env python
import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import datetime
import locale
import gobject
#import logging

#logging.basicConfig(filename="/home/tudor/logg",format='%(levelname)s:%(message)s', level=logging.DEBUG)

class DeathClock(gnomeapplet.Applet):

    def __init__(self,applet,iid):
        self.timeout_interval = 1000
        self.applet = applet
        self.label = gtk.Label("")
        self.applet.add(self.label)
        self.applet.show_all()
        gobject.timeout_add(self.timeout_interval, self.refresh_seconds)
        return gtk.TRUE

    def get_remaining_seconds(self):
        date1 = datetime.datetime.today()
        date2 = datetime.datetime(2063, 12, 01)
        timed = date2 - date1
        return timed.seconds + timed.days * 86400 # 3600secs x 24h

    def format_seconds(self,secs):
        return locale.format('%d', secs, True)

    def refresh_seconds(self):
        self.label.set_text(self.format_seconds(self.get_remaining_seconds()))
        return gtk.TRUE

gobject.type_register(DeathClock)

def sample_factory(applet, iid):
    DeathClock(applet,iid)
    return gtk.TRUE

if __name__ == '__main__':
    gnomeapplet.bonobo_factory("OAFIID:GNOME_DeathClock", 
                               gnomeapplet.Applet.__gtype__, 
                               "hello", "0", sample_factory)
