import logging
log = logging.getLogger(__name__)

from .slaveinfo import Slave

def reboot(name):
    slave = Slave(name)
    slave.load_inventory_info()
    slave.load_bug_info()
    print slave.bug.depends
    print slave.bug.id_
    # update bugzilla during all of these
    # can we update bugzilla with a log handler?
    # try to do an ssh reboot
    # try to do an oob reboot
    # try to do a pdu reboot
    # file IT bug

    # is there anything with oob AND pdu?
