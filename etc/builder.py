import subprocess
from iocbuilder import Device, AutoSubstitution, Xml
from iocbuilder.modules.asyn import AsynIP
from iocbuilder.modules.streamDevice import AutoProtocol
from iocbuilder.arginfo import *

class smargonLib(Device):
    LibFileList = ['smargon']
    DbdFileList = ['smargon']
    AutoInstantiate = True

#class smargonXmlTemplate(Xml):
#       TemplateFile = "smargonTemplate.xml"

class Smargon(Device, ):
    #Dependencies = (ADCore,)
    def __init__(self, PORTNAME = "SSHP", IP_ADDRESS = "", UNAME = "root", PASSWORD = "deltatau", **args):

    # __init__ arguments
    ArgInfo =
            makeArgInfo(__init__,
        P = Simple("Device Prefix", str),
        PORTNAME = Simple('Portname', str),
        IP_ADDRESS = Simple('IP Address of power pmac', str),
        UNAME = Simple('SSH username for power pmac', str),
        PASSWORD = Simple('SSH password for power pmac', str))

    # Device attributes
    #LibFileList = ['smargon']
    #DbdFileList = ['smargon']

    def Initialise(self):
        print '# Create SSH Port (PortName, IPAddress, Username, Password, Priority, DisableAutoConnect, noProcessEos) ' \
        print 'drvAsynPowerPMACPortConfigure("%(PORTNAME)s", "%(IP_ADDRESS)s", ' \
            '%(UNAME)s, %(PASSWORD)s, 0, 0, 0)'  % self.__dict__

