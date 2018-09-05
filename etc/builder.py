
from iocbuilder import Xml
from iocbuilder import Substitution, AutoSubstitution, SetSimulation, Device, records, Architecture, IocDataStream
from iocbuilder.arginfo import *
from iocbuilder import iocinit, configure

class smargonBasicTemplate(AutoSubstitution):
    TemplateFile = 'smargonBase.db'

class smargon(Device,):
    #Dependencies = (ADCore,)
    #TemplateFile = "sem.template"
    def __init__(self,P,PPMAC,PORT_NAME,IP_ADDRESS,UNAME = "root",PASSWORD = "deltatau", CS_NO = 1,PROG_NO = 10):
        self.__super.__init__()
        self.P = P
        self.PPMAC = PPMAC
        self.PORT_NAME = PORT_NAME
        self.IP_ADDRESS = IP_ADDRESS
        self.UNAME = UNAME
        self.PASSWORD = PASSWORD
        self.CS_NO = CS_NO
        self.PROG_NO = PROG_NO
        self.CS_NAME = "CS" + str(CS_NO)
        smargonBasicTemplate(P = self.P,)
    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        P = Simple("Device Prefix", str),
        PPMAC = Simple("Power pmac name", str),
        PORT_NAME = Simple("SSH port name", str),
        IP_ADDRESS = Simple("PPMAC IP address", str),
        UNAME = Simple("SSH username", str),
        PASSWORD = Simple("SSH password", str),
        CS_NO = Simple("Coordinate system number", int),
        PROG_NO = Simple("Motion program number", int),
    )
    # Device attributes
    #LibFileList = ['ADJeol_JSM-IT100']
    #DbdFileList = ['semDetectorSupport']

    
    def Initialise(self):

        print '# Start of Smargon Power Pmac driver configuration #\n'
        print '# Create SSH Port (PortName, IPAddress, Username, Password, Priority, DisableAutoConnect, noProcessEos)'
        print 'drvAsynPowerPMACPortConfigure("%s","%s","%s","%s", 0,0,0)\n' %(self.PORT_NAME,self.IP_ADDRESS,self.UNAME,self.PASSWORD)

        print ' Configure Model 3 Controller Driver (ControlerPort, LowLevelDriverPort, Address, Axes, MovingPoll, IdlePoll)'
        print 'pmacCreateController("%s","%s", 0, 8, 100, 1000)\n' %(self.PPMAC,self.PORT_NAME)

        print '# Configure Model 3 Axes Driver (Controler Port, Axis Count)'
        print 'pmacCreateAxes("%s", 8)\n' %(self.PPMAC)

        print '# Create CS (CSPortName, ControllerPort, CSNumber, ProgramNumber)'
        print 'pmacCreateCS("%s", "%s", "%d", "%d")\n' %(self.CS_NAME,self.PORT_NAME,self.CS_NO,self.PROG_NO)
        
        print '# Configure Model 3 CS Axes Driver (CSPortName, CSAxisCount)'
        print 'pmacCreateCSAxes("%s", 9)' %(self.CS_NAME)
        print 'pmacSetCoordStepsPerUnit("%s", 1, 1)' %(self.CS_NAME)
        print 'pmacSetCoordStepsPerUnit("%s", 2, 1)\n' %(self.CS_NAME)
        print '# End of Smargon Power Pmac driver configuration #\n'
        
    

        
        

