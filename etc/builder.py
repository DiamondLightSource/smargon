
from iocbuilder import Xml
from iocbuilder import Substitution, AutoSubstitution, SetSimulation, Device, records, Architecture, IocDataStream
from iocbuilder.arginfo import *
from iocbuilder import iocinit, configure
from iocbuilder.modules.motor import *
from iocbuilder.modules.pmac import *
from iocbuilder.modules.motor import MotorLib, basic_asyn_motor, MotorRecord


class smargonBasicTemplate(AutoSubstitution):
    TemplateFile = 'smargonBase.db'

class smargonMotors(Xml):
    TemplateFile = "smargonMotors.xml"

class smargon(Device,):
    Dependencies = (MotorLib, )
    def __init__(self,P,PPMAC_PORT, SSH_PORT, PPMAC_NO,IP_ADDRESS,UNAME = "root",PASSWORD = "deltatau", CS_NO = 1,PROG_NO = 10):
        self.__super.__init__()
        self.P = P
        self.PPMAC_NO = PPMAC_NO

        # Derive the prefix for the power pmac releated templates from the module prefix, 
        # eg, BL03I-MO-SGON-01 becomes BL03I-MO-PPMAC-XX depending on value of PMAC_NO.
        if PPMAC_NO < 10:
            self.PPMAC_PREFIX = P[0:9] + "PPMAC-0" + str(PPMAC_NO)
        else:
            self.PPMAC_PREFIX = P[0:9] + "PPMAC-" + str(PPMAC_NO)

        # New variable PPMAC
        self.PPMAC_PORT = PPMAC_PORT
        self.SSH_PORT = SSH_PORT
        self.IP_ADDRESS = IP_ADDRESS
        self.UNAME = UNAME
        self.PASSWORD = PASSWORD
        self.CS_NO = CS_NO
        self.PROG_NO = PROG_NO
        self.CS_PORT = "CS" + str(CS_NO)
        smargonMotors(P=self.P, PPMAC_PORT=self.PPMAC_PORT,PPMAC_PREFIX=self.PPMAC_PREFIX,SSH_PORT=self.SSH_PORT,CS_NO=self.CS_NO,CS_PORT=self.CS_PORT)
        #smargonBasicTemplate(P=self.P, PORT=self.PPMAC_PORT, PPMAC_PREFIX = self.PPMAC_PREFIX, CS_PORT= self.CS_PORT) 
 # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        P = Simple("Device Prefix", str),
        PPMAC_PORT = Simple("Power pmac port name", str),
        SSH_PORT = Simple("Low leve SSH port name", str),
        PPMAC_NO = Simple("Power pmac number", int),
        IP_ADDRESS = Simple("PPMAC_NO IP address", str),
        UNAME = Simple("SSH username", str),
        PASSWORD = Simple("SSH password", str),
        CS_NO = Simple("Coordinate system number", int),
        PROG_NO = Simple("Motion program number", int),
    )
    # Device attributes
    LibFileList = ['smargon']
    DbdFileList = ['smargon']

    
    def Initialise(self):

        print '# Start of Smargon Power Pmac driver configuration #\n'
        print '# Create SSH Port (PortName, IPAddress, Username, Password, Priority, DisableAutoConnect, noProcessEos)'
        print 'drvAsynPowerPMACPortConfigure("%s","%s","%s","%s", 0,0,0)\n' %(self.SSH_PORT,self.IP_ADDRESS,self.UNAME,self.PASSWORD)

        print ' Configure Model 3 Controller Driver (ControlerPort, LowLevelDriverPort, Address, Axes, MovingPoll, IdlePoll)'
        print 'pmacCreateController("%s","%s", 0, 8, 100, 1000)\n' %(self.PPMAC_PORT,self.SSH_PORT)

        print '# Configure Model 3 Axes Driver (Controler Port, Axis Count)'
        print 'pmacCreateAxes("%s", 8)\n' %(self.PPMAC_PORT)

        print '# Create CS (CSPortName, ControllerPort, CSNumber, ProgramNumber)'
        print 'pmacCreateCS("%s", "%s", "%d", "%d")\n' %(self.CS_PORT,self.PPMAC_PORT,self.CS_NO,self.PROG_NO)
        
        print '# Configure Model 3 CS Axes Driver (CSPortName, CSAxisCount)'
        print 'pmacCreateCSAxes("%s", 9)' %(self.CS_PORT)
        print '# End of Smargon Power Pmac driver configuration #\n'
        
    

        
        

