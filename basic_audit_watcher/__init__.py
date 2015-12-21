import os
import time


class Watcher(object):
    def __init__(self, conf, logger):
        self.audit_type = None
        self.outfile = None
        self.logger = logger

    def start(self, audit_type):
        filename = "/tmp/%s-%d.auditlog" % (audit_type, os.getpid())
        self.outfile = open(filename, "a")
        self.outfile.write("%.6f started\n" % time.time())
        self.logger.debug("Logging to %s" % filename)

    def see_object(self, object_metadata, policy_index):
        name = object_metadata['name']
        self.outfile.write("%.6f found %s in policy %d\n" % (time.time(), name, policy_index))

    def end(self):
        self.outfile.write("%.6f finished\n" % time.time())
        self.outfile.close()
