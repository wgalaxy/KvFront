 #   Copyright (C) 2017-2022  Gavin W
 #   This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
 #   the Free Software Foundation, either version 3 of the License, or
 #   (at your option) any later version.

 #   This program is distributed in the hope that it will be useful,
 #   but WITHOUT ANY WARRANTY; without even the implied warranty of
 #   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 #   GNU General Public License for more details.

 #   You should have received a copy of the GNU General Public License
 #   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
from gi.repository import Gtk
from KvFront.config import *
from KvFront.conninfo import *
from KvFront.redis_conninfo import *

class Connection(object):

    def __init__(self, parentwindow, pparent):
        self.pparent = pparent
        self.builderAddConn = Gtk.Builder()
        self.builderAddConn.add_from_file(FILE_UI_ADDSERVER)
        self.builder = Gtk.Builder()
        self.builder.add_from_file(FILE_UI_MAIN)
        self.dlgAddServer = self.builderAddConn.get_object("AddServerDlg")
        self.dlgAddServer.set_transient_for(parentwindow)
        
        self.builderAddConn.get_object("btnSaveConnection").connect("clicked", self.btnSaveConnection_clicked_cb)
        self.builderAddConn.get_object("btnClear").connect("clicked", self.btnClear_clicked_cb)
        self.cfg = Config()
        self.dlgAddServer.show_all()
        
    def btnClear_clicked_cb(self,button):
        self.builderAddConn.get_object("nameentry").set_text("")
        self.builderAddConn.get_object("hostsentry").set_text("")
        
        
    def btnSaveConnection_clicked_cb(self, button):
        print("add connection")
        name = self.builderAddConn.get_object("nameentry").get_text()
        host = self.builderAddConn.get_object("hostsentry").get_text()
        category = self.builderAddConn.get_object("categorycbt").get_active_text()
        password = self.builderAddConn.get_object("pwdentry").get_text()
        addret = self.cfg.addServer(name, host, category, password)
        if addret==0:
             msgdlg = Gtk.MessageDialog(self.builder.get_object("window1"), 0, Gtk.MessageType.INFO,
                                               Gtk.ButtonsType.CLOSE, "the server name is existed.")
             msgdlg.run()
             msgdlg.destroy()
        else:
            if category == "Memcached":
                p = Conninfo()
                p.name = name + "(" + category +")"
                p.hosts = host
                p.category = category
                p.password = password
            
                view =  self.pparent.builder.get_object("treeview2")
                model = view.get_model()
                model.append(None, (p,))
                self.dlgAddServer.destroy()
            elif category == "Redis Standalone" or category == "Redis Cluster":
                p = Conninfo()
                p.name = name + "(" + category +")"
                p.hosts = host
                p.category = category
                p.password = password

                view =  self.pparent.builder.get_object("treeview2")
                model = view.get_model()
                tp = model.append(None, (p,))
                for db_sn in range(0,16):
                    rp = RedisConninfo()
                    rp.name = "db" + str(db_sn)
                    rp.db_sn = db_sn
                    rp.hosts = host
                    rp.category = category
                    rp.password = password
                    model.append(tp,(rp,))
                self.dlgAddServer.destroy()