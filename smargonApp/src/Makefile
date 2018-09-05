TOP=../..

include $(TOP)/configure/CONFIG

LIBRARY_IOC = smargon

# smargon.dbd will be installed into <top>/dbd
DBD += smargon.dbd

# smargon.dbd will be created from these files
smargon_DBD += base.dbd
#smargon_DBD += xxx.dbd

# smargon_registerRecordDeviceDriver.cpp will be created
# smargon.dbd
smargon_SRCS += smargon_registerRecordDeviceDriver.cpp

# We need to link this IOC Application against the EPICS Base libraries
smargon_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
