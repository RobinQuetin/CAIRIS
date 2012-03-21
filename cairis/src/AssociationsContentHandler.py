#$Id: AssociationsContentHandler.py 568 2012-03-14 11:51:45Z shaf $

from xml.sax.handler import ContentHandler
from GoalAssociationParameters import GoalAssociationParameters
from DependencyParameters import DependencyParameters
from Borg import Borg

def a2s(aStr):
  if aStr == 'a':
    return '*'
  elif aStr == '1..a':
    return '1..*'
  else:
    return aStr

def u2s(aStr):
  outStr = ''
  for c in aStr:
    if (c == '_'):
      outStr += ' '
    else:
      outStr += c
  return outStr
  
class AssociationsContentHandler(ContentHandler):
  def __init__(self):
    b = Borg()
    self.dbProxy = b.dbProxy
    self.theManualAssociations = []
    self.theGoalAssociations = []
    self.theDependencyAssociations = []

    self.resetManualAssociationAttributes()
    self.resetGoalAssociationAttributes()
    self.resetDependencyAssociationAttributes()

  def resolveEntity(self,publicId,systemId):
    return "/home/irisuser/iris/iris/config/associations.dtd"

  def manualAssociations(self):
    return self.theManualAssociations

  def goalAssociations(self):
    return self.theGoalAssociations

  def dependencyAssociations(self):
    return self.theDependencyAssociations

  def resetManualAssociationAttributes(self):
    self.theFromName = ''
    self.theFromDim = ''
    self.theToName = ''
    self.theToDim = ''
    self.theReferenceType = ''

  def resetGoalAssociationAttributes(self):
    self.theEnvironmentName = ''
    self.theGoalName = ''
    self.theGoalDim = ''
    self.theReferenceType = ''
    self.theSubGoalName = ''
    self.theSubGoalDim = ''
    self.isAlternative = 0
    self.inRationale = 0
    self.theRationale = ''

  def resetDependencyAssociationAttributes(self):
    self.theDepender = ''
    self.theDependee = ''
    self.theDepType = ''
    self.theDependency = ''
    self.theEnvironmentName = ''
    self.inRationale = 0
    self.theRationale = ''

  def startElement(self,name,attrs):
    self.currentElementName = name
    if name == 'manual_association':
      self.theFromName = attrs['from_name']
      self.theFromDim = attrs['from_dim']
      self.theToName = attrs['to_name']
      self.theToDim = attrs['to_dim']
      if (self.theFromDim == 'requirement') and (self.theToDim == 'task' or self.theToDim == 'usecase'):
        try:
          self.theReferenceType = attrs['ref_type']
        except KeyError:
          self.theReferenceType = 'and'

      if (self.theFromDim == 'requirement') and (self.theToDim == 'requirement'):
        try:
          self.theReferenceType = attrs['label']
        except KeyError:
          self.theReferenceType = ''

    elif name == 'goal_association':
      self.theEnvironmentName = attrs['environment']
      self.theGoalName = attrs['goal_name']
      self.theGoalDim = attrs['goal_dim']
      self.theReferenceType = attrs['ref_type']
      self.theSubGoalName = attrs['subgoal_name']
      self.theSubGoalDim = attrs['subgoal_dim']
      self.isAlternative = attrs['alternative_id']
    elif name == 'dependency':
      self.theDepender = attrs['depender']
      self.theDependee = attrs['dependee']
      self.theDepType = attrs['dependency_type']
      self.theDependency = attrs['dependency']
      self.theEnvironmentName = attrs['environment']
    elif name == 'rationale':
      self.inRationale = 1
      self.theRationale = ''

  def characters(self,data):
    if self.inRationale:
      self.theRationale += data

  def endElement(self,name):
    if name == 'manual_association':
      fromId = self.dbProxy.getDimensionId(self.theFromName,self.theFromDim)
      toId = self.dbProxy.getDimensionId(self.theToName,self.theToDim)
      self.theManualAssociations.append((self.theFromDim + '_' + self.theToDim,fromId,toId,self.theReferenceType))
      self.resetManualAssociationAttributes()
    elif name == 'goal_association':
      p = GoalAssociationParameters(self.theEnvironmentName,self.theGoalName,self.theGoalDim,self.theReferenceType,self.theSubGoalName,self.theSubGoalDim,self.isAlternative,self.theRationale)
      self.theGoalAssociations.append(p)
      self.resetGoalAssociationAttributes()
    elif name == 'dependency':
      p = DependencyParameters(self.theEnvironmentName,self.theDepender,self.theDependee,self.theDepType,self.theDependency,self.theRationale)
      self.theDependencyAssociations.append(p)
      self.resetDependencyAssociationAttributes()
    elif name == 'rationale':
      self.inRationale = 0