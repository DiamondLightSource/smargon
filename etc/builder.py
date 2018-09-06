
from iocbuilder import Xml
from iocbuilder import Substitution, AutoSubstitution, SetSimulation, Device, records, Architecture, IocDataStream
from iocbuilder.arginfo import *
from iocbuilder import iocinit, configure
from iocbuilder.modules.motor import *
from iocbuilder.modules.pmac import *
from iocbuilder.modules.motor import MotorLib, basic_asyn_motor, MotorRecord


class _smargonMotors(Xml):
    TemplateFile = "smargonMotors.xml"

class _configOnStartup(Xml):
    TemplateFile = "iocStartupCommands.xml"

class _homingLogic(AutoSubstitution):
    TemplateFile = "smargonHoming.template"

class smargon(Device,):
    Dependencies = (MotorLib, )
    def __init__(self,P,PPMAC_PORT, SSH_PORT, PPMAC_NO,IP_ADDRESS, ZEBRA, UNAME = "root",PASSWORD = "deltatau", CS_NO = 1,PROG_NO = 10):
        self.__super.__init__()
        self.P = P
        self.PPMAC_PORT = PPMAC_PORT
        self.SSH_PORT = SSH_PORT
        self.PPMAC_NO = PPMAC_NO
        self.IP_ADDRESS = IP_ADDRESS
        self.ZEBRA = ZEBRA
        self.UNAME = UNAME
        self.PASSWORD = PASSWORD
        self.CS_NO = CS_NO
        self.PROG_NO = PROG_NO
        # Derive the prefix for the power pmac releated templates from the module prefix, 
        # eg, BL03I-MO-SGON-01 becomes BL03I-MO-PPMAC-XX depending on value of PMAC_NO.
        if PPMAC_NO < 10:
            self.PPMAC_PREFIX = P[0:9] + "PPMAC-0" + str(PPMAC_NO)
        else:
            self.PPMAC_PREFIX = P[0:9] + "PPMAC-" + str(PPMAC_NO)
        
        # Create new variable CS_PORT and generate a name for it (eg,CS1)
        self.CS_PORT = "CS" + str(CS_NO)

        # Instatiate the motors and motor controller
        _smargonMotors(P=self.P, PPMAC_PORT=self.PPMAC_PORT,PPMAC_PREFIX=self.PPMAC_PREFIX,SSH_PORT=self.SSH_PORT,CS_NO=self.CS_NO,CS_PORT=self.CS_PORT)
        _configOnStartup(P=self.P,PPMAC_PORT=self.PPMAC_PORT,PPMAC_PREFIX=self.PPMAC_PREFIX)
        _homingLogic(P=self.P,PPMAC_PORT=self.PPMAC_PORT,ZEBRA=self.ZEBRA)
    # __init__ arguments
    ArgInfo = makeArgInfo(__init__,
        P = Simple("Device Prefix", str),
        PPMAC_PORT = Simple("Power pmac port name", str),
        SSH_PORT = Simple("Low leve SSH port name", str),
        PPMAC_NO = Simple("Power pmac number", int),
        IP_ADDRESS = Simple("PPMAC_NO IP address", str),
        ZEBRA = Simple("Base PV for zebra", str),
        UNAME = Simple("SSH username", str),
        PASSWORD = Simple("SSH password", str),
        CS_NO = Simple("Coordinate system number", int),
        PROG_NO = Simple("Motion program number", int),
    )
    # Device attributes
    LibFileList = ['smargon']
    DbdFileList = ['smargon']

        
    

        
        

