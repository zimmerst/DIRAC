""" The SLS_Command class is a command class to properly interrogate the SLS
"""

from DIRAC.ResourceStatusSystem.Client.Command.Command import Command
from DIRAC.ResourceStatusSystem.Utilities.Exceptions import *
from DIRAC.ResourceStatusSystem.Utilities.Utils import *

#############################################################################

def _getSESLSName(name):

  splitted = name.split('_', 1)

  if len(splitted) == 1:
    toSplit = splitted[0]
    shortSiteName = toSplit.split('-')[0]
    tokenName = toSplit.split('-')[1]
  else:
    shortSiteName = splitted[0]
    tokenName = splitted[1]
  
  if shortSiteName == 'NIKHEF':
    shortSiteName = 'SARA'
  
  SLSName = shortSiteName + '-' + 'LHCb_' + tokenName
  
  return SLSName
      
#############################################################################

def _getServiceSLSName(name):
  #TBD
  
  return name

#############################################################################

class SLSStatus_Command(Command):
  
  def doCommand(self, args, clientIn=None):
    """ Return getStatus from SLS Client
    
       :params:
         :attr:`args`: 
           - args[0]: string: should be a ValidRes
      
           - args[1]: string: should be the (DIRAC) name of the ValidRes
    """

    if not isinstance(args, tuple):
      raise TypeError, where(self, self.doCommand)
    
    if args[0] not in ValidRes:
      raise InvalidRes, where(self, self.doCommand)
    
    if clientIn is not None:
      c = clientIn
    else:
      # use standard GOC DB Client
      from DIRAC.ResourceStatusSystem.Client.SLSClient import SLSClient   
      c = SLSClient()
      
    if args[0] == 'StorageElement':
      #know the SLS name of the SE
      SLSName = _getSESLSName(args[1])
      
    elif args[0] == 'Service':
      #know the SLS name of the VO BOX - TBD
      SLSName = _getServiceSLSName(args[1])
    
    else:
      raise InvalidRes, where(self, self.doCommand)
    
    res = c.getStatus(SLSName)
    
    return res

#############################################################################

class SLSLink_Command(Command):
  
  def doCommand(self, args, clientIn=None):
    """ Return getStatus from SLS Client
    
       :params:
         :attr:`args`: 
           - args[0]: string: should be a ValidRes
      
           - args[1]: string: should be the (DIRAC) name of the ValidRes
    """

    if not isinstance(args, tuple):
      raise TypeError, where(self, self.doCommand)
    
    if args[0] not in ValidRes:
      raise InvalidRes, where(self, self.doCommand)
    
    if clientIn is not None:
      c = clientIn
    else:
      # use standard GOC DB Client
      from DIRAC.ResourceStatusSystem.Client.SLSClient import SLSClient   
      c = SLSClient()
      
    if args[0] == 'StorageElement':
      #know the SLS name of the SE
      SLSName = _getSESLSName(args[1])
      
    elif args[0] == 'Service':
      #know the SLS name of the VO BOX - TBD
      SLSName = _getServiceSLSName(args[1])
    
    else:
      raise InvalidRes, where(self, self.doCommand)
    
    res = c.getLink(SLSName)
    
    return res

#############################################################################
