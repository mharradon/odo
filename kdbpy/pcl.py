""" pcl top-level managemenet """
import logging
from kdbpy import kdb, web, lib

class PCL(object):

    def __init__(self, start_kdb=True, start_web=False):
        self.kdb = None
        self.web = None

        if start_kdb:
            self.start_kdb()
        if self.start_web:
            self.start_web()

    def start_kdb(self):
        """ start up kdb/q process and connect server """
        cred = kdb.get_credentials()
        kdb.q_start_process(cred)
        self.kdb = lib.KDB(cred).start()

    def stop_kdb(self):
        """ terminate kdb/q process and connecting server """
        if self.kdb is not None:
            self.kdb.stop()
            self.kdb = None
        kdb.q_stop_process()

    @property
    def is_kdb(self):
        """ return boolean if kdb is started """
        return self.kdb is not None and self.kdb.is_initialized

    def start_web(self):
        """ start up web service """
        self.web = web.Web().start()

    def stop_web(self):
        """ terminate web service """
        if self.web is not None:
            self.web.stop()
            self.web = None

    @property
    def is_web(self):
        """ return boolean if web service is started """
        return self.web is not None and self.web.is_initialized

    def stop(self):
        """ all stop """
        self.stop_web()
        self.stop_kdb()
