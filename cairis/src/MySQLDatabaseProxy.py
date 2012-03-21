#$URL: svn://edison.comlab.ox.ac.uk/res08/iris/iris/MySQLDatabaseProxy.py $ $Id: MySQLDatabaseProxy.py 579 2012-03-19 16:20:12Z shaf $
from Borg import Borg
import MySQLdb
import RequirementFactory
from Environment import Environment
from ARM import *
import _mysql_exceptions 
import Attacker
import Asset
import Threat
import Vulnerability
import Persona
import MisuseCase
import Task
import Risk
import Response
import ClassAssociation
import DatabaseProxy
from AttackerParameters import AttackerParameters
from PersonaParameters import PersonaParameters
from GoalParameters import GoalParameters
from ObstacleParameters import ObstacleParameters
from AssetParameters import AssetParameters
from TemplateAssetParameters import TemplateAssetParameters
from SecurityPatternParameters import SecurityPatternParameters
from ThreatParameters import ThreatParameters
from VulnerabilityParameters import VulnerabilityParameters
from RiskParameters import RiskParameters
from ResponseParameters import ResponseParameters
from RoleParameters import RoleParameters
from ResponsibilityParameters import ResponsibilityParameters
import ObjectFactory
from TaskParameters import TaskParameters
from MisuseCaseParameters import MisuseCaseParameters
from DomainPropertyParameters import DomainPropertyParameters
import TraceParameters
import UpdateTraceParameters
import Trace
import armid
from DotTraceParameters import DotTraceParameters
from EnvironmentParameters import EnvironmentParameters
from Target import Target
from AttackerEnvironmentProperties import AttackerEnvironmentProperties
from AssetEnvironmentProperties import AssetEnvironmentProperties
from ThreatEnvironmentProperties import ThreatEnvironmentProperties
from VulnerabilityEnvironmentProperties import VulnerabilityEnvironmentProperties
from AcceptEnvironmentProperties import AcceptEnvironmentProperties
from TransferEnvironmentProperties import TransferEnvironmentProperties
from MitigateEnvironmentProperties import MitigateEnvironmentProperties
from CountermeasureEnvironmentProperties import CountermeasureEnvironmentProperties
from CountermeasureParameters import CountermeasureParameters
from PersonaEnvironmentProperties import PersonaEnvironmentProperties
from TaskEnvironmentProperties import TaskEnvironmentProperties
from MisuseCaseEnvironmentProperties import MisuseCaseEnvironmentProperties
from RoleEnvironmentProperties import RoleEnvironmentProperties
from ClassAssociationParameters import ClassAssociationParameters
from GoalAssociationParameters import GoalAssociationParameters
from DependencyParameters import DependencyParameters
from GoalEnvironmentProperties import GoalEnvironmentProperties
from ObstacleEnvironmentProperties import ObstacleEnvironmentProperties
from DomainParameters import DomainParameters
from DomainAssociation import DomainAssociation
from ValueTypeParameters import ValueTypeParameters
from ExternalDocumentParameters import ExternalDocumentParameters
from DocumentReferenceParameters import DocumentReferenceParameters
from ConceptReferenceParameters import ConceptReferenceParameters
from PersonaCharacteristicParameters import PersonaCharacteristicParameters
from TaskCharacteristicParameters import TaskCharacteristicParameters
from UseCaseParameters import UseCaseParameters
from UseCase import UseCase
from UseCaseEnvironmentProperties import UseCaseEnvironmentProperties
from UseCaseParameters import UseCaseParameters
from Step import Step
from Steps import Steps
from ReferenceSynopsis import ReferenceSynopsis
from ReferenceContribution import ReferenceContribution
from ConceptMapAssociationParameters import ConceptMapAssociationParameters
import string
import os

from numpy import *

LABEL_COL = 0
ID_COL = 1
NAME_COL = 2
DESCRIPTION_COL = 3
PRIORITY_COL = 4
RATIONALE_COL = 5
FITCRITERION_COL = 6
ORIGINATOR_COL = 7
VERSION_COL = 8
TYPE_COL = 9
ASSET_COL = 10

ENVIRONMENTID_COL = 0
ENVIRONMENTNAME_COL = 1
ENVIRONMENTSHORTCODE_COL = 2
ENVIRONMENTDESC_COL = 3

ATTACKERS_ID_COL = 0
ATTACKERS_NAME_COL = 1
ATTACKERS_DESCRIPTION_COL = 2
ATTACKERS_IMAGE_COL = 3

ASSETS_ID_COL = 0
ASSETS_NAME_COL = 1
ASSETS_SHORTCODE_COL = 2
ASSETS_DESCRIPTION_COL = 3
ASSETS_SIGNIFICANCE_COL = 4
ASSETS_TYPE_COL = 5
ASSETS_CRITICAL_COL = 6
ASSETS_CRITICALRATIONALE_COL = 7
TEMPLATEASSETS_CPROPERTY_COL = 8
TEMPLATEASSETS_IPROPERTY_COL = 9
TEMPLATEASSETS_AVPROPERTY_COL = 10
TEMPLATEASSETS_ACPROPERTY_COL = 11
TEMPLATEASSETS_ANPROPERTY_COL = 12
TEMPLATEASSETS_PANPROPERTY_COL = 13
TEMPLATEASSETS_UNLPROPERTY_COL = 14
TEMPLATEASSETS_UNOPROPERTY_COL = 15

CLASSASSOCIATIONS_ID_COL = 0
CLASSASSOCIATIONS_ENV_COL = 1
CLASSASSOCIATIONS_HEAD_COL = 2
CLASSASSOCIATIONS_HEADDIM_COL = 3
CLASSASSOCIATIONS_HEADNAV_COL = 4
CLASSASSOCIATIONS_HEADTYPE_COL = 5
CLASSASSOCIATIONS_HEADMULT_COL = 6
CLASSASSOCIATIONS_HEADROLE_COL = 7
CLASSASSOCIATIONS_TAILROLE_COL = 8
CLASSASSOCIATIONS_TAILMULT_COL = 9
CLASSASSOCIATIONS_TAILTYPE_COL = 10
CLASSASSOCIATIONS_TAILNAV_COL = 11
CLASSASSOCIATIONS_TAILDIM_COL = 12
CLASSASSOCIATIONS_TAIL_COL = 13
CLASSASSOCIATIONS_RATIONALE_COL =14

GOALASSOCIATIONS_ID_COL = 0
GOALASSOCIATIONS_ENV_COL = 1
GOALASSOCIATIONS_GOAL_COL = 2
GOALASSOCIATIONS_GOALDIM_COL = 3
GOALASSOCIATIONS_TYPE_COL = 4
GOALASSOCIATIONS_SUBGOAL_COL = 5
GOALASSOCIATIONS_SUBGOALDIM_COL = 6
GOALASSOCIATIONS_ALTERNATIVE_COL = 7
GOALASSOCIATIONS_RATIONALE_COL = 8

DEPENDENCIES_ID_COL = 0
DEPENDENCIES_ENV_COL = 1
DEPENDENCIES_DEPENDER_COL = 2
DEPENDENCIES_DEPENDEE_COL = 3
DEPENDENCIES_DTYPE_COL = 4
DEPENDENCIES_DEPENDENCY_COL = 5
DEPENDENCIES_RATIONALE_COL = 6

THREAT_ID_COL = 0
THREAT_NAME_COL = 1
THREAT_TYPE_COL = 2
THREAT_METHOD_COL = 3
THREAT_LIKELIHOOD_COL = 4

VULNERABILITIES_ID_COL = 0
VULNERABILITIES_NAME_COL = 1
VULNERABILITIES_DESCRIPTION_COL = 2
VULNERABILITIES_TYPE_COL = 3

DIM_ID_COL = 0
DIM_NAME_COL = 1

HIGH_VALUE = 3
MEDIUM_VALUE = 2
LOW_VALUE = 1

PERSONAS_ID_COL = 0
PERSONAS_NAME_COL = 1
PERSONAS_ACTIVITIES_COL = 2
PERSONAS_ATTITUDES_COL = 3
PERSONAS_APTITUDES_COL = 4
PERSONAS_MOTIVATIONS_COL = 5
PERSONAS_SKILLS_COL = 6
PERSONAS_IMAGE_COL = 7
PERSONAS_ASSUMPTION_COL = 8
PERSONAS_TYPE_COL = 9

TASKS_ID_COL = 0
TASKS_NAME_COL = 1
TASKS_SHORTCODE_COL = 2
TASKS_OBJECTIVE_COL = 3
TASKS_ASSUMPTION_COL = 4
TASKS_AUTHOR_COL = 5

MISUSECASES_ID_COL = 0
MISUSECASES_NAME_COL = 1

TASK_USECASE_TYPE = 0
TASK_MISUSECASE_TYPE = 1
TASK_VALUTASK_TYPE = 2

RISKS_ID_COL = 0
RISKS_NAME_COL = 1
RISKS_THREATNAME_COL = 2
RISKS_VULNAME_COL = 3

RESPONSES_ID_COL = 0
RESPONSES_NAME_COL = 1
RESPONSES_MITTYPE_COL = 2
RESPONSES_RISK_COL = 3

INCONSISTENCIES_ID_COL = 0
INCONSISTENCIES_PROPERTY_COL = 1
INCONSISTENCIES_FROMASSET_COL = 2
INCONSISTENCIES_FROMVALUE_COL = 3
INCONSISTENCIES_TOASSET_COL = 4
INCONSISTENCIES_TOVALUE_COL = 5

DETECTION_TYPE_ID = 2
REACTION_TYPE_ID = 3

FROM_OBJT_COL = 0
FROM_ID_COL = 1
TO_OBJT_COL = 2
TO_ID_COL = 3

COUNTERMEASURES_ID_COL = 0
COUNTERMEASURES_NAME_COL = 1
COUNTERMEASURES_DESCRIPTION_COL = 2
COUNTERMEASURES_TYPE_COL = 3

GOALS_ID_COL = 0
GOALS_NAME_COL = 1
GOALS_ORIGINATOR_COL = 2
GOALS_COLOUR_COL = 3

OBSTACLES_ID_COL = 0
OBSTACLES_NAME_COL = 1
OBSTACLES_ORIG_COL = 2

SECURITYPATTERN_ID_COL = 0
SECURITYPATTERN_NAME_COL = 1
SECURITYPATTERN_CONTEXT_COL = 2
SECURITYPATTERN_PROBLEM_COL = 3
SECURITYPATTERN_SOLUTION_COL = 4

EXTERNALDOCUMENT_ID_COL = 0
EXTERNALDOCUMENT_NAME_COL = 1
EXTERNALDOCUMENT_VERSION_COL = 2
EXTERNALDOCUMENT_PUBDATE_COL = 3
EXTERNALDOCUMENT_AUTHORS_COL = 4
EXTERNALDOCUMENT_DESCRIPTION_COL = 5

DOCUMENTREFERENCE_ID_COL = 0
DOCUMENTREFERENCE_NAME_COL = 1
DOCUMENTREFERENCE_DOCNAME_COL = 2
DOCUMENTREFERENCE_CNAME_COL = 3
DOCUMENTREFERENCE_EXCERPT_COL = 4

CONCEPTREFERENCE_ID_COL = 0
CONCEPTREFERENCE_NAME_COL = 1
CONCEPTREFERENCE_DIMNAME_COL = 2
CONCEPTREFERENCE_OBJTNAME_COL = 3
CONCEPTREFERENCE_DESCRIPTION_COL = 4

PERSONACHARACTERISTIC_ID_COL = 0
PERSONACHARACTERISTIC_PERSONANAME_COL = 1
PERSONACHARACTERISTIC_BVAR_COL = 2
PERSONACHARACTERISTIC_QUAL_COL = 3
PERSONACHARACTERISTIC_PDESC_COL = 4

TASKCHARACTERISTIC_ID_COL = 0
TASKCHARACTERISTIC_TASKNAME_COL = 1
TASKCHARACTERISTIC_QUAL_COL = 2
TASKCHARACTERISTIC_TDESC_COL = 3

REFERENCE_NAME_COL = 0
REFERENCE_TYPE_COL = 1
REFERENCE_DESC_COL = 2
REFERENCE_DIM_COL = 3

collectedIds = set([])

class MySQLDatabaseProxy(DatabaseProxy.DatabaseProxy):
  def __init__(self):
    DatabaseProxy.DatabaseProxy.__init__(self)
    self.theGrid = 0
    try:
      b = Borg()
      self.conn = MySQLdb.connect(host=b.dbHost,port=b.dbPort,user=b.dbUser,passwd=b.dbPasswd,db=b.dbName)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error connecting to the IRIS database on host ' + b.dbHost + ' at port ' + str(b.dbPort) + ' with user ' + b.dbUser + ' (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
    self.theDimIdLookup, self.theDimNameLookup = self.buildDimensionLookup()

  def reconnect(self):
    try:
      self.conn.close()
      b = Borg()
      self.conn = MySQLdb.connect(host=b.dbHost,port=b.dbPort,user=b.dbUser,passwd=b.dbPasswd,db=b.dbName)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error connecting to the IRIS database on host ' + b.dbHost + ' at port ' + str(b.dbPort) + ' with user ' + b.dbUser + ' (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
    self.theDimIdLookup, self.theDimNameLookup = self.buildDimensionLookup()


  def associateGrid(self,gridObjt): self.theGrid = gridObjt
    
  def buildDimensionLookup(self):
    idLookup  = {}
    nameLookup = {}
    try:
      curs = self.conn.cursor()
      curs.execute('call traceDimensions()')
      if (curs.rowcount == -1):
        exceptionText = 'Error building dimension lookup tables'
        raise DatabaseProxyException(exceptionText) 
      for row in curs.fetchall():
        row = list(row)
        idLookup[row[0]] = row[1]
        nameLookup[row[1]] = row[0]
      curs.close()
      return (idLookup, nameLookup)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error building dimension lookup tables (id:' + str(id) + ',message:' + msg
    
  def close(self):
    self.conn.close()

  def getRequirements(self,constraintId = '',isAsset = 1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRequirements(%s,%s)',(constraintId,isAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Undefined error while loading the requirements environment'
        raise DatabaseProxyException(exceptionText) 
      reqDict = {}
      for row in curs.fetchall():
        row = list(row)
        reqId = row[ID_COL]
        reqLabel = row[LABEL_COL]
        reqName = row[NAME_COL]
        reqDesc = row[DESCRIPTION_COL]
        priority = row[PRIORITY_COL]
        rationale = row[RATIONALE_COL]
        fitCriterion = row[FITCRITERION_COL]
        originator = row[ORIGINATOR_COL]
        reqType = row[TYPE_COL]
        reqVersion = row[VERSION_COL]
        reqDomain = row[ASSET_COL]
        r = RequirementFactory.build(reqId,reqLabel,reqName,reqDesc,priority,rationale,fitCriterion,originator,reqType,reqDomain,reqVersion)
        reqDict[reqDesc] = r
      curs.close()
      return reqDict
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error loading requirements (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def getRequirement(self,reqId):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRequirement(%s)',(reqId))
      if (curs.rowcount == -1):
        exceptionText = 'Undefined error while loading the requirements environment'
        raise DatabaseProxyException(exceptionText) 
      reqDict = {}
      for row in curs.fetchall():
        row = list(row)
        reqId = row[ID_COL]
        reqLabel = row[LABEL_COL]
        reqName = row[NAME_COL]
        reqDesc = row[DESCRIPTION_COL]
        priority = row[PRIORITY_COL]
        rationale = row[RATIONALE_COL]
        fitCriterion = row[FITCRITERION_COL]
        originator = row[ORIGINATOR_COL]
        reqType = row[TYPE_COL]
        reqVersion = row[VERSION_COL]
        r = RequirementFactory.build(reqId,reqLabel,reqName,reqDesc,priority,rationale,fitCriterion,originator,reqType,reqVersion)
        reqDict[reqDesc] = r
      curs.close()
      return reqDict
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error loading requirements (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def getDomains(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDomains(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Undefined error while getting domains'
        raise DatabaseProxyException(exceptionText) 
      domains = []
      for row in curs.fetchall():
        row = list(row)
        domainId = row[0]
        domainName = row[1]
        shortCode = row[2]
        domainDesc = row[3]
        domainType = row[4]
        givenIndicator = row[5]
        domains.append((domainId,domainName,shortCode,domainDesc,domainType,givenIndicator))
      curs.close()
      domDict = {}
      for domainId,domainName,shortCode,domainDesc,domainType,givenIndicator in domains:
        domainAssociations = self.getDomainAssociations(domainId)
        domParameters = DomainParameters(domainName,shortCode,domainDesc,domainType,givenIndicator,domainAssociations)
        dom = ObjectFactory.build(domainId,domParameters)
        domDict[domainName] = dom
      return domDict
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error loading requirement module ' + modName + ' (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def getDomainAssociations(self,domainId):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDomainAssociations(%s)',(domainId))
      if (curs.rowcount == -1):
        exceptionText = 'Undefined error while getting domains associated with domain id ' + str(domainId)
        raise DatabaseProxyException(exceptionText) 
      domains = []
      for row in curs.fetchall():
        row = list(row)
        domainAssociation = DomainAssociation('domain','domainname','domain',row[0],row[1])
        domains.append(domainAssociation)
      curs.close()
      return domains
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting domains associated with domain id ' + str(domainId) + ' (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def getOrderedRequirements(self,constraintId = '',isAsset = True):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRequirements(%s,%s)',(constraintId,isAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Undefined error while loading the requirements environment'
        raise DatabaseProxyException(exceptionText) 
      reqList = []
      for row in curs.fetchall():
        row = list(row)
        reqId = row[ID_COL]
        reqLabel = row[LABEL_COL]
        reqName = row[NAME_COL]
        reqDesc = row[DESCRIPTION_COL]
        priority = row[PRIORITY_COL]
        rationale = row[RATIONALE_COL]
        fitCriterion = row[FITCRITERION_COL]
        originator = row[ORIGINATOR_COL]
        reqType = row[TYPE_COL]
        reqDomain = row[ASSET_COL]
        reqVersion = row[VERSION_COL]
        r = RequirementFactory.build(reqId,reqLabel,reqName,reqDesc,priority,rationale,fitCriterion,originator,reqType,reqDomain,reqVersion)
        reqList.append(r)
      curs.close()
      return reqList
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error loading requirements (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
  
  
  def lastId(self):
    try: 
      curs = self.conn.cursor()
      curs.execute('call lastId()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting last id'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      return row[0]
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting latest identifier (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def newId(self):
    try: 
      curs = self.conn.cursor()
      curs.execute('call newId()',())
      if (curs.rowcount == -1):
        exceptionText = 'Error getting last id'
        raise DatabaseProxyException(exceptionText) 
      results = curs.fetchone()
      newId = results[0]
      curs.close()
      return newId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting new identifier (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
  
  def addRequirement(self,r,assetName,isAsset = True):
    try:
      curs = self.conn.cursor()
      curs.execute('call addRequirement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(r.label(),r.id(), r.version(), r.name(),r.description(), r.rationale(), r.originator(), r.fitCriterion(), r.priority(),r.type(),assetName,isAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Error inserting new requirement ' + str(r.id())
        raise DatabaseProxyException(exceptionText)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL adding new requirement ' + str(r.id()) + '(id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def updateRequirement(self,r):
    try:
      curs = self.conn.cursor()
      curs.execute('call updateRequirement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(r.label(),r.id(), r.version(), r.name(),r.description(), r.rationale(), r.originator(), r.fitCriterion(), r.priority(),r.type()))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating requirement ' + str(r.id())
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL adding updating requirement ' + str(r.id()) + '(id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def addValueTensions(self,envId,tensions):
    for vtKey in tensions:
      spValue = vtKey[0]
      prValue = vtKey[1]
      vt = tensions[vtKey]
      vtValue = vt[0]
      vtRationale = vt[1]
      self.addValueTension(envId,spValue,prValue,vtValue,vtRationale)

  def addValueTension(self,envId,spId,prId,tId,tRationale):
    try:
      curs = self.conn.cursor()
      curs.execute('call addValueTension(%s,%s,%s,%s,%s)',(envId,spId,prId,tId,tRationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding value tension for environment id ' + str(envId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL adding value tension for environment id ' + str(envId) + '(id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def addEnvironment(self,parameters):
    environmentId = self.newId()
    environmentName = parameters.name()
    environmentShortCode = parameters.shortCode()
    environmentDescription = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call addEnvironment(%s,%s,%s,%s)',(environmentId,environmentName,environmentShortCode,environmentDescription))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      if (len(parameters.environments()) > 0):
        for c in parameters.environments():
          curs.execute('call addCompositeEnvironment(%s,%s)',(environmentId,c))
          if (curs.rowcount == -1):
            exceptionText = 'Error associating environment ' + c + ' with composite environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
        self.addCompositeEnvironmentProperties(environmentId,parameters.duplicateProperty(),parameters.overridingEnvironment())

      assetValues = parameters.assetValues()
      if (assetValues != None):
        for v in assetValues:
          self.updateValueType(v)

      self.addValueTensions(environmentId,parameters.tensions())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addCompositeEnvironmentProperties(self,environmentId,duplicateProperty,overridingEnvironment):
    try:
      curs = self.conn.cursor()
      curs.execute('call addCompositeEnvironmentProperties(%s,%s,%s)',(environmentId,duplicateProperty,overridingEnvironment))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding duplicate properties for environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding duplicate properties for environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskEnvironments(self,threatName,vulName):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskEnvironments(%s,%s)',(threatName,vulName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting environments associated with threat ' + threatName + ' and vulnerability ' + vulName
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append(row[0])
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments associated with threat ' + threatName + ' and vulnerability ' + vulName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateEnvironment(self,parameters):
    environmentId = parameters.id()
    environmentName = parameters.name()
    environmentShortCode = parameters.shortCode()
    environmentDescription = parameters.description()

    try:
      curs = self.conn.cursor()
      curs.execute('call deleteEnvironmentComponents(%s)',(parameters.id()))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateEnvironment(%s,%s,%s,%s)',(environmentId,environmentName,environmentShortCode,environmentDescription))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding updating environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      if (len(parameters.environments()) > 0):
        for c in parameters.environments():
          curs.execute('call addCompositeEnvironment(%s,%s)',(environmentId,c))
          if (curs.rowcount == -1):
            exceptionText = 'Error associating environment ' + c + ' with composite environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
      if (len(parameters.duplicateProperty()) > 0):
        self.addCompositeEnvironmentProperties(environmentId,parameters.duplicateProperty(),parameters.overridingEnvironment())
      self.addValueTensions(environmentId,parameters.tensions())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteRequirement(self,r):
    self.deleteObject(r,'requirement')
    self.conn.commit()

  def getEnvironments(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getEnvironments(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining requirement environment list'
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

    environments = {}
    envRows = []
    for row in curs.fetchall():
      row = list(row)
      environmentId = row[ENVIRONMENTID_COL]
      environmentName = row[ENVIRONMENTNAME_COL]
      environmentShortCode = row[ENVIRONMENTSHORTCODE_COL]
      environmentDesc = row[ENVIRONMENTDESC_COL]
      envRows.append((environmentId,environmentName,environmentShortCode,environmentDesc))
    curs.close()
    for environmentId,environmentName,environmentShortCode,environmentDesc in envRows:
      cc = self.compositeEnvironments(environmentId)
      duplicateProperty = 'None'
      overridingEnvironment = ''
      if (len(cc) > 0):
        duplicateProperty,overridingEnvironment = self.duplicateProperties(environmentId)
      tensions = self.environmentTensions(environmentName)
      p = EnvironmentParameters(environmentName,environmentShortCode,environmentDesc,cc,duplicateProperty,overridingEnvironment,tensions)
      cn = ObjectFactory.build(environmentId,p)
      environments[environmentName] = cn 
    return environments

  def compositeEnvironments(self,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call compositeEnvironments(%s)',(environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining composite environments for environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append(row[0])
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error environments associated with composite environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def compositeEnvironmentIds(self,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call compositeEnvironmentIds(%s)',(environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining composite environments for environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append(row[0])
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error environments associated with composite environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def duplicateProperties(self,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call duplicateProperties(%s)',(environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining duplicate property for composite environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        duplicateProperty = row[0] 
        overridingEnvironment = row[1]
        curs.close()   
        return (duplicateProperty,overridingEnvironment) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error environments associated with composite environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getAttackers(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getAttackers(%s)',(constraintId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining attackers'
        raise DatabaseProxyException(exceptionText) 
      attackers = {}
      attackerRows = []
      for row in curs.fetchall():
        row = list(row)
        attackerId = row[ATTACKERS_ID_COL]
        attackerName = row[ATTACKERS_NAME_COL]
        attackerDesc = row[ATTACKERS_DESCRIPTION_COL]
        attackerImage = row[ATTACKERS_IMAGE_COL]
        attackerRows.append((attackerId,attackerName,attackerDesc,attackerImage))
      curs.close()
      for attackerId,attackerName,attackerDesc,attackerImage in attackerRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(attackerId,'attacker'):
          roles = self.dimensionRoles(attackerId,environmentId,'attacker')
          capabilities = self.attackerCapabilities(attackerId,environmentId)
          motives = self.attackerMotives(attackerId,environmentId)
          properties = AttackerEnvironmentProperties(environmentName,roles,motives,capabilities)
          environmentProperties.append(properties) 
        p = AttackerParameters(attackerName,attackerDesc,attackerImage,environmentProperties)
        attacker = ObjectFactory.build(attackerId,p)
        attackers[attackerName] = attacker
      return attackers
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting attackers (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
  
  def dimensionEnvironments(self,dimId,dimTable):
    try:
      curs = self.conn.cursor()
      sqlTxt = 'call ' + dimTable + '_environments(%s)'
      curs.execute(sqlTxt,(dimId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining getting environments for ' + dimTable + ' id ' + str(dimId)
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append((row[0],row[1]))
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments for ' + dimTable + ' id ' + str(dimId) +  ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def attackerMotives(self,attackerId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call attacker_motivation(%s,%s)',(attackerId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining attacker motives'
        raise DatabaseProxyException(exceptionText) 
      motives = []
      for row in curs.fetchall():
        row = list(row)
        motives.append(row[0])
      curs.close()
      return motives
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting motives for atttacker id ' + str(attackerId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def threatLikelihood(self,threatId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select threat_likelihood(%s,%s)',(threatId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining likelihood for threat id ' + str(threatId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      lhood = row[0] 
      curs.close()
      return lhood
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting likelihood for threat id ' + str(threatId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def vulnerabilitySeverity(self,vulId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select vulnerability_severity(%s,%s)',(vulId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining severity for vulnerability id ' + str(vulId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      sev = row[0] 
      curs.close()
      return sev
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting severity for vulnerability id ' + str(vulId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def attackerCapabilities(self,attackerId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call attacker_capability(%s,%s)',(attackerId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining attacker capabilities'
        raise DatabaseProxyException(exceptionText) 
      capabilities = []
      for row in curs.fetchall():
        row = list(row)
        capabilities.append((row[0],row[1]))
      curs.close()
      return capabilities
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting capabilities for atttacker id ' + str(attackerId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addAttacker(self,parameters):
    try:
      attackerId = self.newId()
      attackerName = parameters.name()
      attackerDesc = parameters.description()
      attackerImage = parameters.image()
      curs = self.conn.cursor()
      curs.execute("call addAttacker(%s,%s,%s,%s)",(attackerId,attackerName,attackerDesc,attackerImage))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding attacker ' + attackerName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(attackerId,'attacker',environmentName)
        self.addAttackerMotives(attackerId,environmentName,environmentProperties.motives())
        self.addAttackerCapabilities(attackerId,environmentName,environmentProperties.capabilities())
        self.addDimensionRoles(attackerId,'attacker',environmentName,environmentProperties.roles())
      self.conn.commit()
      curs.close()
      return attackerId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding attacker ' + str(attackerId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDimensionEnvironment(self,dimId,table,environmentName):
    try:
      curs = self.conn.cursor()
      sqlTxt = 'call add_' + table + '_environment(%s,%s)'
      curs.execute(sqlTxt,(dimId,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating ' + table + ' id ' + str(dimId) + ' with environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating ' + table + ' id ' + str(dimId) + ' with environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addAttackerMotives(self,attackerId,environmentName,motives):
    try:
      curs = self.conn.cursor()
      for motive in motives:
        curs.execute('call addAttackerMotive(%s,%s,%s)',(attackerId,environmentName,motive))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating attacker id ' + str(attackerId) + ' with motive ' + motive
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating attacker id ' + str(attackerId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addAttackerCapabilities(self,attackerId,environmentName,capabilities):
    try:
      curs = self.conn.cursor()
      for name,value in capabilities:
        curs.execute('call addAttackerCapability(%s,%s,%s,%s)',(attackerId,environmentName,name,value))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating attacker id ' + str(attackerId) + ' with capabilities'
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating attacker id ' + str(attackerId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
  
  def updateAttacker(self,parameters):
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteAttackerComponents(%s)',(parameters.id()))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating attacker ' + attackerName
        raise DatabaseProxyException(exceptionText) 

      attackerId = parameters.id()
      attackerName = parameters.name()
      attackerDesc = parameters.description()
      attackerImage = parameters.image()
      curs = self.conn.cursor()
      curs.execute("call updateAttacker(%s,%s,%s,%s)",(attackerId,attackerName,attackerDesc,attackerImage))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating attacker ' + attackerName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(attackerId,'attacker',environmentName)
        self.addAttackerMotives(attackerId,environmentName,environmentProperties.motives())
        self.addAttackerCapabilities(attackerId,environmentName,environmentProperties.capabilities())
        self.addDimensionRoles(attackerId,'attacker',environmentName,environmentProperties.roles())
      self.conn.commit()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating attacker id ' + str(parameters.id()) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteAttacker(self,attackerId):
    self.deleteObject(attackerId,'attacker')
    self.conn.commit()

  def deleteObject(self,objtId,tableName):
    try: 
      curs = self.conn.cursor()
      sqlTxt = 'call delete_' + tableName + '(%s)'
      curs.execute(sqlTxt,(objtId))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting ' + tableName + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.IntegrityError, e:
      id,msg = e
      exceptionText = 'Cannot remove ' + tableName + ' due to dependent data.  Check the environment model for further information  (id:' + str(id) + ',message:' + msg + ')'
      raise IntegrityException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting ' + tableName + 's (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addAsset(self,parameters):
    assetId = self.newId()
    assetName = parameters.name()
    shortCode = parameters.shortCode()
    assetDesc = parameters.description()
    assetSig = parameters.significance()
    assetType = parameters.type()
    assetCriticality = parameters.critical()
    assetCriticalRationale = parameters.criticalRationale()
    try:
      curs = self.conn.cursor()
      curs.execute('call addAsset(%s,%s,%s,%s,%s,%s,%s,%s)',(assetId,assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new asset ' + assetName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(assetId,'asset',environmentName)
        self.addAssetAssociations(assetId,assetName,environmentName,cProperties.associations())
        self.addSecurityProperties('asset',assetId,environmentName,cProperties.properties(),cProperties.rationale())
      self.conn.commit()
      curs.close()
      return assetId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding asset ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateAsset(self,parameters):
    assetId = parameters.id()
    assetName = parameters.name()
    shortCode = parameters.shortCode()
    assetDesc = parameters.description()
    assetSig = parameters.significance()
    assetType = parameters.type()
    assetCriticality = parameters.critical()
    assetCriticalRationale = parameters.criticalRationale()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteAssetComponents(%s)',(assetId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating asset ' + assetName
        raise DatabaseProxyException(exceptionText) 

      curs.execute('call updateAsset(%s,%s,%s,%s,%s,%s,%s,%s)',(assetId,assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating asset ' + assetName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(assetId,'asset',environmentName)
        self.addAssetAssociations(assetId,assetName,environmentName,cProperties.associations())
        self.addSecurityProperties('asset',assetId,environmentName,cProperties.properties(),cProperties.rationale())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating asset ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addSecurityProperties(self,dimTable,objtId,environmentName,securityProperties,pRationale):
    sqlTxt = 'call add_' + dimTable + '_properties(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
      curs = self.conn.cursor()
      curs.execute(sqlTxt,(objtId,environmentName,securityProperties[armid.C_PROPERTY],securityProperties[armid.I_PROPERTY],securityProperties[armid.AV_PROPERTY],securityProperties[armid.AC_PROPERTY],securityProperties[armid.AN_PROPERTY],securityProperties[armid.PAN_PROPERTY],securityProperties[armid.UNL_PROPERTY],securityProperties[armid.UNO_PROPERTY],pRationale[armid.C_PROPERTY],pRationale[armid.I_PROPERTY],pRationale[armid.AV_PROPERTY],pRationale[armid.AC_PROPERTY],pRationale[armid.AN_PROPERTY],pRationale[armid.PAN_PROPERTY],pRationale[armid.UNL_PROPERTY],pRationale[armid.UNO_PROPERTY]))
      if (curs.rowcount == -1):
        exceptionText = 'Error setting security properties for ' + dimTable + ' id ' + str(objtId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding security properties for ' + dimTable + ' id ' + str(objtId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateSecurityProperties(self,dimTable,objtId,securityProperties,pRationale):
    sqlTxt = ''
    if (dimTable == 'threat'):
      sqlTxt += 'update threat_property set property_value_id=%s, property_rationale=%s where environment_id = ' + str(self.environmentId) + ' and threat_id = %s and property_id = %s'
    else:
      sqlTxt += 'update ' + dimTable + '_property set property_value_id=%s, property_rationale=%s where ' + dimTable + '_id = %s and property_id = %s'
    try:
      curs = self.conn.cursor()
      curs.execute(sqlTxt,(securityProperties[armid.C_PROPERTY],pRationale[armid.C_PROPERTY],objtId,armid.C_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating confidentiality property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.I_PROPERTY],pRationale[armid.I_PROPERTY],objtId,armid.I_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating integrity property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.AV_PROPERTY],pRationale[armid.AV_PROPERTY],objtId,armid.AV_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating availability property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.AC_PROPERTY],pRationale[armid.AC_PROPERTY],objtId,armid.AC_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating accountability property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.AN_PROPERTY],pRationale[armid.AN_PROPERTY],objtId,armid.AN_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating anonymity property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.PAN_PROPERTY],pRationale[armid.PAN_PROPERTY],objtId,armid.PAN_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating pseudonymity property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.UNL_PROPERTY],pRationale[armid.UNL_PROPERTY],objtId,armid.UNL_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating unlinkability property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.execute(sqlTxt,(securityProperties[armid.UNO_PROPERTY],pRationale[armid.UNO_PROPERTY],objtId,armid.UNO_PROPERTY))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating unobservability property for ' + dimTable + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating security properties for ' + dimTable + ' id ' + str(objtId) +  ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteAsset(self,assetId):
    self.deleteObject(assetId,'asset')
    self.conn.commit()

  def dimensionObject(self,constraintName,dimensionTable):
    if (dimensionTable != 'requirement'):
      constraintId = self.getDimensionId(constraintName,dimensionTable)
    objts = {}
    if (dimensionTable == 'goalassociation'):
      objts = self.getGoalAssociations(constraintId)
    if (dimensionTable == 'asset'):
      objts = self.getAssets(constraintId)
    if (dimensionTable == 'template_asset'):
      objts = self.getTemplateAssets(constraintId)
    if (dimensionTable == 'securitypattern'):
      objts = self.getSecurityPatterns(constraintId)
    if (dimensionTable == 'classassociation'):
      objts = self.getClassAssociations(constraintId)
    if (dimensionTable == 'goal'):
      objts = self.getGoals(constraintId)
    if (dimensionTable == 'obstacle'):
      objts = self.getObstacles(constraintId)
    elif (dimensionTable == 'attacker'):
      objts = self.getAttackers(constraintId)
    elif (dimensionTable == 'threat'):
      objts = self.getThreats(constraintId)
    elif (dimensionTable == 'vulnerability'):
      objts = self.getVulnerabilities(constraintId)
    elif (dimensionTable == 'risk'):
      objts = self.getRisks(constraintId)
    elif (dimensionTable == 'response'):
      objts = self.getResponses(constraintId)
    elif (dimensionTable == 'countermeasure'):
      objts = self.getCountermeasures(constraintId)
    elif (dimensionTable == 'persona'):
      objts = self.getPersonas(constraintId)
    elif (dimensionTable == 'task'):
      objts = self.getTasks(constraintId)
    elif (dimensionTable == 'usecase'):
      objts = self.getUseCases(constraintId)
    elif (dimensionTable == 'misusecase'):
      objts = self.getMisuseCases(constraintId)
    elif (dimensionTable == 'requirement'):
      objts = self.getRequirement(constraintName)
    elif (dimensionTable == 'environment'):
      objts = self.getEnvironments(constraintId)
    elif (dimensionTable == 'role'):
      objts = self.getRoles(constraintId)
    elif (dimensionTable == 'domainproperty'):
      objts = self.getDomainProperties(constraintId)
    elif (dimensionTable == 'domain'):
      objts = self.getDomains(constraintId)
    elif (dimensionTable == 'document_reference'):
      objts = self.getDocumentReferences(constraintId)
    elif (dimensionTable == 'concept_reference'):
      objts = self.getConceptReferences(constraintId)
    elif (dimensionTable == 'persona_characteristic'):
      objts = self.getPersonaCharacteristics(constraintId)
    elif (dimensionTable == 'task_characteristic'):
      objts = self.getTaskCharacteristics(constraintId)
    elif (dimensionTable == 'external_document'):
      objts = self.getExternalDocuments(constraintId)
    elif (dimensionTable == 'reference_synopsis'):
      objts = self.getReferenceSynopsis(constraintId)
    elif (dimensionTable == 'reference_contribution'):
      objts = self.getReferenceContributions(constraintId)

    return (objts.values())[0]

  def getAssets(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getAssets(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining assets'
        raise DatabaseProxyException(exceptionText) 
      assets = {}
      assetRows = []
      for row in curs.fetchall():
        row = list(row)
        assetName = row[ASSETS_NAME_COL]
        shortCode = row[ASSETS_SHORTCODE_COL]
        assetId = row[ASSETS_ID_COL]
        assetDesc = row[ASSETS_DESCRIPTION_COL]
        assetSig = row[ASSETS_SIGNIFICANCE_COL]
        assetType = row[ASSETS_TYPE_COL]
        assetCriticality = row[ASSETS_CRITICAL_COL]
        assetCriticalRationale = row[ASSETS_CRITICALRATIONALE_COL]
        assetRows.append((assetName,assetId,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale))
      curs.close()
      for assetName,assetId,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale in assetRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(assetId,'asset'):
          syProperties,pRationale = self.relatedProperties('asset',assetId,environmentId)
          assetAssociations = self.assetAssociations(assetId,environmentId)
          properties = AssetEnvironmentProperties(environmentName,syProperties,pRationale,assetAssociations)
          environmentProperties.append(properties) 
        parameters = AssetParameters(assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale,environmentProperties)
        asset = ObjectFactory.build(assetId,parameters)
        assets[assetName] = asset
      return assets
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assets (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getThreats(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getThreats(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining threats'
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting threats (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

    threats = {}
    threatRows = []
    for row in curs.fetchall():
      row = list(row)
      threatId = row[THREAT_ID_COL]
      threatName = row[THREAT_NAME_COL]
      threatType = row[THREAT_TYPE_COL]
      thrMethod = row[THREAT_METHOD_COL]
      threatRows.append((threatId,threatName,threatType,thrMethod))
    curs.close()
    for threatId,threatName,threatType,thrMethod in threatRows: 
      environmentProperties = []
      for environmentId,environmentName in self.dimensionEnvironments(threatId,'threat'):
        likelihood = self.threatLikelihood(threatId,environmentId)
        assets = self.threatenedAssets(threatId,environmentId) 
        attackers = self.threatAttackers(threatId,environmentId)
        syProperties,pRationale = self.relatedProperties('threat',threatId,environmentId)
        properties = ThreatEnvironmentProperties(environmentName,likelihood,assets,attackers,syProperties,pRationale)
        environmentProperties.append(properties)
      parameters = ThreatParameters(threatName,threatType,thrMethod,environmentProperties)
      threat = ObjectFactory.build(threatId,parameters)
      threats[threatName] = threat
    return threats

  def getDimensionId(self,dimensionName,dimensionTable):
    if (dimensionTable == 'trace_dimension'):
      return self.theDimNameLookup[dimensionName]
    if dimensionTable == 'linkand':
      dimensionTable = 'goalassociation'
    try:
      curs = self.conn.cursor()
      sqlText = ''
      if ((dimensionTable == 'classassociation') or (dimensionTable == 'goalassociation')):
        associationComponents = dimensionName.split('/')
        if (dimensionTable == 'goalassociation'):
          curs.execute('select goalAssociationId(%s,%s,%s,%s,%s)',(associationComponents[0],associationComponents[1],associationComponents[2],associationComponents[3],associationComponents[4]))
        elif (dimensionTable == 'classassociation'):
          curs.execute('select classAssociationId(%s,%s,%s)',(associationComponents[0],associationComponents[1],associationComponents[2]))
      else:
        curs.execute('call dimensionId(%s,%s)',(dimensionName,dimensionTable))

      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining '
        exceptionText += dimensionTable + ' details'
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        exceptionText = 'No identifier associated with '
        exceptionText += dimensionTable + ' object ' + dimensionName
        raise DatabaseProxyException(exceptionText) 

      row = curs.fetchone()
      dimId = row[0]
      if (dimId == None and dimensionTable == 'requirement'):
        curs.execute('select requirementNameId(%s)',(dimensionName))
        if (curs.rowcount == -1):
          exceptionText = 'Error obtaining '
          exceptionText += dimensionTable + ' details'
          raise DatabaseProxyException(exceptionText) 
        else:
          row = curs.fetchone()
          dimId = row[0]
      curs.close()
      return dimId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting '
      exceptionText += dimensionTable + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getDimensions(self,dimensionTable,idConstraint=-1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDimensions(%s,%s)',(dimensionTable,idConstraint))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining ' + dimensionTable + 's'
        raise DatabaseProxyException(exceptionText) 
      dimensions = {}
      for row in curs.fetchall():
        row = list(row)
        dimensionName = row[DIM_NAME_COL]
        dimensionId = row[DIM_ID_COL]
        dimensions[dimensionName] = dimensionId
      curs.close()
      return dimensions
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting '
      exceptionText += dimensionTable + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getDimensionNames(self,dimensionTable,currentEnvironment = ''):
    try:
      dimensions = []
      curs = self.conn.cursor()
      if (dimensionTable != 'template_asset'):
        sqlText = 'call ' + dimensionTable + 'Names(%s)' 
        curs.execute(sqlText,(currentEnvironment))
      else:
        curs.execute('call template_assetNames()')
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining ' + dimensionTable + 's'
        raise DatabaseProxyException(exceptionText) 
      for row in curs.fetchall():
        row = list(row)
        dimensionName = str(row[0])
        dimensions.append(dimensionName)
      curs.close()
      return dimensions
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting '
      exceptionText += dimensionTable + 's (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getEnvironmentNames(self):
    try:
      dimensions = []
      curs = self.conn.cursor()
      sqlText = 'call nonCompositeEnvironmentNames()' 
      curs.execute(sqlText)
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining environments'
        raise DatabaseProxyException(exceptionText) 
      for row in curs.fetchall():
        row = list(row)
        dimensionName = str(row[0])
        dimensions.append(dimensionName)
      curs.close()
      return dimensions
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments (id:' + str(id) + ', message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addThreat(self,parameters,update = False):
    threatId = self.newId()
    threatName = parameters.name()
    threatType = parameters.type()
    threatMethod = parameters.method()
    try:
      curs = self.conn.cursor()
      curs.execute("call addThreat(%s,%s,%s,%s)",(threatId,threatName,threatType,threatMethod))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new threat ' + threatName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(threatId,'threat',environmentName)
        curs.execute("call addThreatLikelihood(%s,%s,%s)",(threatId,environmentName,cProperties.likelihood()))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
        self.addSecurityProperties('threat',threatId,environmentName,cProperties.properties(),cProperties.rationale())

        for assetName in cProperties.assets():
          curs.execute("call addAssetThreat(%s,%s,%s)",(threatId,environmentName,assetName))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
        for attacker in cProperties.attackers():
          curs.execute("call addThreatAttacker(%s,%s,%s)",(threatId,environmentName,attacker))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return threatId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding threat ' + threatName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def updateThreat(self,parameters):
    threatId = parameters.id()
    threatName = parameters.name()
    threatType = parameters.type()
    threatMethod = parameters.method()

    try:
      curs = self.conn.cursor()
      curs.execute('call deleteThreatComponents(%s)',(threatId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating threat ' + threatName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateThreat(%s,%s,%s,%s)',(threatId,threatName,threatType,threatMethod))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating threat ' + threatName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(threatId,'threat',environmentName)
        curs.execute("call addThreatLikelihood(%s,%s,%s)",(threatId,environmentName,cProperties.likelihood()))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
        self.addSecurityProperties('threat',threatId,environmentName,cProperties.properties(),cProperties.rationale())

        for assetName in cProperties.assets():
          curs.execute("call addAssetThreat(%s,%s,%s)",(threatId,environmentName,assetName))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
        for attacker in cProperties.attackers():
          curs.execute("call addThreatAttacker(%s,%s,%s)",(threatId,environmentName,attacker))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating threat ' + threatName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getVulnerabilities(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getVulnerabilities(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining vulnerabilities'
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting vulnerabilities (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

    vulnerabilities = {}
    vulRows = []
    for row in curs.fetchall():
      row = list(row)
      vulnerabilityId = row[VULNERABILITIES_ID_COL]
      vulnerabilityName = row[VULNERABILITIES_NAME_COL]
      vulnerabilityDescription = row[VULNERABILITIES_DESCRIPTION_COL]
      vulnerabilityType = row[VULNERABILITIES_TYPE_COL]
      vulRows.append((vulnerabilityId,vulnerabilityName,vulnerabilityDescription,vulnerabilityType))
    curs.close()
    for vulnerabilityId,vulnerabilityName,vulnerabilityDescription,vulnerabilityType in vulRows:
      environmentProperties = []
      for environmentId,environmentName in self.dimensionEnvironments(vulnerabilityId,'vulnerability'):
        severity = self.vulnerabilitySeverity(vulnerabilityId,environmentId)
        assets = self.vulnerableAssets(vulnerabilityId,environmentId)
        properties = VulnerabilityEnvironmentProperties(environmentName,severity,assets)
        environmentProperties.append(properties)
      parameters = VulnerabilityParameters(vulnerabilityName,vulnerabilityDescription,vulnerabilityType,environmentProperties)
      vulnerability = ObjectFactory.build(vulnerabilityId,parameters)
      vulnerabilities[vulnerabilityName] = vulnerability
    return vulnerabilities

  def deleteVulnerability(self,vulId):
    self.deleteObject(vulId,'vulnerability')
    self.conn.commit()

  def addVulnerability(self,parameters):
    vulName = parameters.name()
    vulDesc = parameters.description()
    vulType = parameters.type()
    try:
      vulId = self.newId()
      curs = self.conn.cursor()
      curs.execute('call addVulnerability(%s,%s,%s,%s)',(vulId,vulName,vulDesc,vulType))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new vulnerability ' + vulName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(vulId,'vulnerability',environmentName)
        curs.execute("call addVulnerabilitySeverity(%s,%s,%s)",(vulId,environmentName,cProperties.severity()))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding new vulnerability ' + vulName + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
        for assetName in cProperties.assets():
          curs.execute("call addAssetVulnerability(%s,%s,%s)",(vulId,environmentName,assetName))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding new threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return vulId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding vulnerability ' + vulName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateVulnerability(self,parameters):
    vulId = parameters.id()
    vulName = parameters.name()
    vulDesc = parameters.description()
    vulType = parameters.type()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteVulnerabilityComponents(%s)',(vulId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating vulnerability ' + vulName
        raise DatabaseProxyException(exceptionText)
      curs.execute('call updateVulnerability(%s,%s,%s,%s)',(vulId,vulName,vulDesc,vulType))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding updating vulnerability ' + vulName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(vulId,'vulnerability',environmentName)
        curs.execute("call addVulnerabilitySeverity(%s,%s,%s)",(vulId,environmentName,cProperties.severity()))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding vulnerability ' + vulName + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
        for assetName in cProperties.assets():
          curs.execute("call addAssetVulnerability(%s,%s,%s)",(vulId,environmentName,assetName))
          if (curs.rowcount == -1):
            exceptionText = 'Error adding threat ' + threatName + ' to environment ' + environmentName
            raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating vulnerability (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def relatedProperties(self,dimTable,objtId,environmentId):
    try:
        curs = self.conn.cursor()
        sqlTxt = 'call ' + dimTable + 'Properties (%s,%s)'
        curs.execute(sqlTxt,(objtId,environmentId))
        if (curs.rowcount == -1):
          exceptionText = 'Error getting ' + dimTable + ' properties in environment id ' + str(environmentId)
          raise DatabaseProxyException(exceptionText) 
        properties = []
        row = curs.fetchone()
        properties =  array((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])).astype(int32) 
        pRationale =  [row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15]]
        curs.close()
        return (properties,pRationale)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting ' + dimTable + ' properties in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonas(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getPersonas(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining personas'
        raise DatabaseProxyException(exceptionText) 

      personaRows = []
      for row in curs.fetchall():
        row = list(row)
        personaId = row[PERSONAS_ID_COL]
        personaName = row[PERSONAS_NAME_COL]
        activities = row[PERSONAS_ACTIVITIES_COL]
        attitudes = row[PERSONAS_ATTITUDES_COL]
        aptitudes = row[PERSONAS_APTITUDES_COL]
        motivations = row[PERSONAS_MOTIVATIONS_COL]
        skills = row[PERSONAS_SKILLS_COL]
        image = row[PERSONAS_IMAGE_COL]
        isAssumption = row[PERSONAS_ASSUMPTION_COL]
        pType = row[PERSONAS_TYPE_COL]
        personaRows.append((personaId,personaName,activities,attitudes,aptitudes,motivations,skills,image,isAssumption,pType))
      curs.close()

      personas = {}
      for personaId,personaName,activities,attitudes,aptitudes,motivations,skills,image,isAssumption,pType in personaRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(personaId,'persona'):
          personaDesc = self.personaNarrative(personaId,environmentId)
          directFlag = self.personaDirect(personaId,environmentId)
          roles = self.dimensionRoles(personaId,environmentId,'persona')
          properties = PersonaEnvironmentProperties(environmentName,directFlag,personaDesc,roles)
          environmentProperties.append(properties)
        parameters = PersonaParameters(personaName,activities,attitudes,aptitudes,motivations,skills,image,isAssumption,pType,environmentProperties)
        persona = ObjectFactory.build(personaId,parameters)
        personas[personaName] = persona
      return personas
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting personas (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def dimensionRoles(self,dimId,environmentId,table):
    try:
      curs = self.conn.cursor() 
      sqlTxt = 'call ' + table + '_roles(%s,%s)'
      curs.execute(sqlTxt,(dimId,environmentId))
      if (curs.rowcount == -1):
        curs.close() 
        exceptionText = 'Error getting roles for ' + table + ' id ' + str(dimId)
        raise DatabaseProxyException(exceptionText) 
      else:
        roles = []
        for row in curs.fetchall():
          row = list(row)
          roles.append(row[0])
        curs.close() 
        return roles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting roles for ' + table + ' id ' + str(personaId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def personaGoals(self,personaId,environmentId):
    try:
      curs = self.conn.cursor() 
      curs.execute('call personaGoals(%s,%s)',(personaId,environmentId))
      if (curs.rowcount == -1):
        curs.close() 
        exceptionText = 'Error getting goals for persona id ' + str(personaId)
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close() 
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals for persona id ' + str(personaId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def threatAttackers(self,threatId,environmentId):
    try:
      curs = self.conn.cursor() 
      curs.execute('call threat_attacker(%s,%s)',(threatId,environmentId))
      if (curs.rowcount == -1):
        curs.close() 
        exceptionText = 'Error getting attackers for threat id ' + str(threatId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      else:
        attackers = []
        for row in curs.fetchall():
          row = list(row)
          attackers.append(row[0])
        curs.close() 
        return attackers
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting attackers for threat id ' + str(threatId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addPersona(self,parameters):
    try:
      personaId = self.newId()
      personaName = parameters.name()
      activities = parameters.activities()
      attitudes = parameters.attitudes()
      aptitudes = parameters.aptitudes()
      motivations = parameters.motivations()
      skills = parameters.skills()
      image = parameters.image()
      isAssumption = parameters.assumption()
      pType = parameters.type()

      curs = self.conn.cursor()
      curs.execute('call addPersona(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(personaId,personaName,activities.encode('utf-8'),attitudes.encode('utf-8'),aptitudes.encode('utf-8'),motivations.encode('utf-8'),skills.encode('utf-8'),image,isAssumption,pType))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new persona ' + personaName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(personaId,'persona',environmentName)
        self.addPersonaNarrative(personaId,environmentName,environmentProperties.narrative().encode('utf-8'))
        self.addPersonaDirect(personaId,environmentName,environmentProperties.directFlag())
        self.addDimensionRoles(personaId,'persona',environmentName,environmentProperties.roles())
      self.conn.commit()
      curs.close()
      return personaId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding persona (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDimensionRoles(self,personaId,table,environmentName,roles):
    try:
      curs = self.conn.cursor()
      for role in roles:
        sqlTxt = 'call add_' + table + '_role (%s,%s,%s)'
        curs.execute(sqlTxt,(personaId,environmentName,role)) 
        if (curs.rowcount == -1):
          exceptionText = 'Error associating role ' + role + ' with ' + table + ' id ' + str(personaId)
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding roles to ' + table + ' id ' + str(personaId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updatePersona(self,parameters):
    personaId = parameters.id()
    personaName = parameters.name()
    activities = parameters.activities()
    attitudes = parameters.attitudes()
    aptitudes = parameters.aptitudes()
    motivations = parameters.motivations()
    skills = parameters.skills()
    image = parameters.image()
    isAssumption = parameters.assumption()
    pType = parameters.type()
    try:
      curs = self.conn.cursor()
      curs.execute('call deletePersonaComponents(%s)',(personaId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating persona ' + personaName
        raise DatabaseProxyException(exceptionText) 

      curs.execute('call updatePersona(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(personaId,personaName,activities.encode('utf-8'),attitudes.encode('utf-8'),aptitudes.encode('utf-8'),motivations.encode('utf-8'),skills.encode('utf-8'),image,isAssumption,pType))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating persona ' + personaName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(personaId,'persona',environmentName)
        self.addPersonaNarrative(personaId,environmentName,environmentProperties.narrative().encode('utf-8'))
        self.addPersonaDirect(personaId,environmentName,environmentProperties.directFlag())
        self.addDimensionRoles(personaId,'persona',environmentName,environmentProperties.roles())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating persona (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deletePersona(self,personaId):
    self.deleteObject(personaId,'persona')
    self.conn.commit()

  def getTasks(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getTasks(%s)',(constraintId));
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining tasks'
        raise DatabaseProxyException(exceptionText) 

      tasks = {} 
      taskRows = []
      for row in curs.fetchall():
        row = list(row)
        taskId = row[TASKS_ID_COL]
        taskName = row[TASKS_NAME_COL]
        taskShortCode = row[TASKS_SHORTCODE_COL]
        taskObjective = row[TASKS_OBJECTIVE_COL]
        isAssumption = row[TASKS_ASSUMPTION_COL]
        taskAuthor = row[TASKS_AUTHOR_COL]
        taskRows.append((taskId,taskName,taskShortCode,taskObjective,isAssumption,taskAuthor))
      curs.close()

      for taskId,taskName,taskShortCode,taskObjective,isAssumption,taskAuthor in taskRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(taskId,'task'):
          dependencies = self.taskDependencies(taskId,environmentId)
          personas = self.taskPersonas(taskId,environmentId)
          assets = self.taskAssets(taskId,environmentId)
          narrative = self.taskNarrative(taskId,environmentId)
          consequences = self.taskConsequences(taskId,environmentId)
          benefits = self.taskBenefits(taskId,environmentId)
          concernAssociations = self.taskConcernAssociations(taskId,environmentId)
          properties = TaskEnvironmentProperties(environmentName,dependencies,personas,assets,concernAssociations,narrative,consequences,benefits)
          environmentProperties.append(properties)
          parameters = TaskParameters(taskName,taskShortCode,taskObjective,isAssumption,taskAuthor,environmentProperties)
          task = ObjectFactory.build(taskId,parameters)
          tasks[taskName] = task
      return tasks
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting tasks (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getMisuseCases(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getMisuseCases(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining Misuse Cases'
        raise DatabaseProxyException(exceptionText) 
      if (curs.rowcount == 0):
        return None
      else:
        mcs = {}
        mcRows = []
        for row in curs.fetchall():
          mcId = row[MISUSECASES_ID_COL]
          mcName = row[MISUSECASES_NAME_COL]
          mcRows.append((mcId,mcName))
        curs.close()
        for mcId,mcName in mcRows:
          risk = self.misuseCaseRisk(mcId)
          environmentProperties = []
          for environmentId,environmentName in self.dimensionEnvironments(mcId,'misusecase'):
            narrative = self.misuseCaseNarrative(mcId,environmentId)
            properties = MisuseCaseEnvironmentProperties(environmentName,narrative)
            environmentProperties.append(properties)
          parameters = MisuseCaseParameters(mcName,environmentProperties,risk)
          mc = ObjectFactory.build(mcId,parameters)
          mcs[mcName] = mc
      return mcs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting misuse case (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskMisuseCase(self,riskId):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskMisuseCase(%s)',(riskId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining tasks'
        raise DatabaseProxyException(exceptionText) 

      if (curs.rowcount == 0):
        return None
      else:
        row = curs.fetchone()
        mcId = row[MISUSECASES_ID_COL]
        mcName = row[MISUSECASES_NAME_COL]
        curs.close()
        risk = self.misuseCaseRisk(mcId)
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(mcId,'misusecase'):
          narrative = self.misuseCaseNarrative(mcId,environmentId)
          properties = MisuseCaseEnvironmentProperties(environmentName,narrative)
          environmentProperties.append(properties)
        parameters = MisuseCaseParameters(mcName,environmentProperties,risk)
        mc = ObjectFactory.build(mcId,parameters)
      return mc
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting misuse case (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 



  def misuseCaseRisk(self,mcId):
    try:
      curs = self.conn.cursor()
      curs.execute('select misuseCaseRisk(%s)',(mcId))
      rowCount = curs.rowcount
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error getting risk for misuse case id ' + str(mcId)
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        riskName = row[0]
        curs.close()
        return riskName
    except _mysql_exceptions.DatabaseError, e:
     id,msg = e
     exceptionText = 'MySQL error getting risk for misuse case id ' + str(mcId) + ' (id:' + str(id) + ',message:' + msg + ')'
     raise DatabaseProxyException(exceptionText) 



  def taskPersonas(self,taskId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskPersonas(%s,%s)',(taskId,environmentId))
      rowCount = curs.rowcount
      personas = []
      if (rowCount == -1):
        exceptionText = 'Error obtaining task personas for environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      elif (rowCount > 0):
        for row in curs.fetchall():
          row = list(row)
          personas.append((row[0],row[1],row[2],row[3],row[4]))
      curs.close()
      return personas 
    except _mysql_exceptions.DatabaseError, e:
     id,msg = e
     exceptionText = 'MySQL error getting task personas for environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
     raise DatabaseProxyException(exceptionText) 

  def taskAssets(self,taskId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskAssets(%s,%s)',(taskId,environmentId))
      rowCount = curs.rowcount
      assets = []
      if (rowCount == -1):
        exceptionText = 'Error obtaining task assets for environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      elif (rowCount > 0):
        for row in curs.fetchall():
          row = list(row)
          assets.append(row[0])
      curs.close()
      return assets 
    except _mysql_exceptions.DatabaseError, e:
     id,msg = e
     exceptionText = 'MySQL error getting task assets for environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
     raise DatabaseProxyException(exceptionText) 

  def addTask(self,parameters):
    taskName = self.conn.escape_string(parameters.name())
    taskShortCode = self.conn.escape_string(parameters.shortCode())
    taskObjective = self.conn.escape_string(parameters.objective())
    isAssumption = parameters.assumption()
    taskAuthor = parameters.author()
    try:
      taskId = self.newId()
      curs = self.conn.cursor()
      curs.execute('call addTask(%s,%s,%s,%s,%s,%s)',(taskId,taskName,taskShortCode,taskObjective,isAssumption,taskAuthor))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new task ' + taskName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(taskId,'task',environmentName)
        self.addTaskDependencies(taskId,cProperties.dependencies(),environmentName)
        taskAssets = cProperties.assets()
        if (len(taskAssets) > 0):
          self.addTaskAssets(taskId,taskAssets,environmentName)
        self.addTaskPersonas(taskId,cProperties.personas(),environmentName)
        self.addTaskConcernAssociations(taskId,environmentName,cProperties.concernAssociations())
        self.addTaskNarrative(taskId,cProperties.narrative().encode('utf-8'),cProperties.consequences().encode('utf-8'),cProperties.benefits().encode('utf-8'),environmentName)
      self.conn.commit()
      curs.close()
      return taskId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding task ' + taskName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addMisuseCase(self,parameters):
    mcName = parameters.name()
    try:
      mcId = self.newId()
      curs = self.conn.cursor()
      curs.execute('call addMisuseCase(%s,%s)',(mcId,mcName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new task ' + scName
        raise DatabaseProxyException(exceptionText) 
      self.addMisuseCaseRisk(mcId,parameters.risk())
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(mcId,'misusecase',environmentName)
        self.addMisuseCaseNarrative(mcId,cProperties.narrative().encode('utf-8'),environmentName)
      self.conn.commit()
      curs.close()
      return mcId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding misuse case ' + mcName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def updateTask(self,parameters):
    taskId = parameters.id()
    taskName = parameters.name()
    taskShortCode = parameters.shortCode()
    taskObjective = parameters.objective()
    isAssumption = parameters.assumption()
    taskAuthor = parameters.author()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteTaskComponents(%s)',(taskId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating task ' + taskName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateTask(%s,%s,%s,%s,%s,%s)',(taskId,taskName,taskShortCode,taskObjective,isAssumption,taskAuthor))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating task ' + taskName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(taskId,'task',environmentName)
        self.addTaskDependencies(taskId,cProperties.dependencies(),environmentName)
        self.addTaskConcernAssociations(taskId,environmentName,cProperties.concernAssociations())
        self.addTaskPersonas(taskId,cProperties.personas(),environmentName)
        taskAssets = cProperties.assets()
        if (len(taskAssets) > 0):
          self.addTaskAssets(taskId,taskAssets,environmentName)
        self.addTaskNarrative(taskId,cProperties.narrative().encode('utf-8'),cProperties.consequences().encode('utf-8'),cProperties.benefits().encode('utf-8'),environmentName)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding task ' + taskName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateMisuseCase(self,parameters):
    mcId = parameters.id()
    mcName = parameters.name()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteMisuseCaseComponents(%s)',(mcId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating misuse case ' + mcName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateMisuseCase(%s,%s)',(mcId,mcName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating misuse case ' + mcName
        raise DatabaseProxyException(exceptionText) 
      self.addMisuseCaseRisk(mcId,parameters.risk())
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(mcId,'misusecase',environmentName)
        self.addMisuseCaseNarrative(mcId,cProperties.narrative().encode('utf-8'),environmentName)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding misuse case ' + mcName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def addTaskPersonas(self,taskId,personas,environmentName):
    try:
      curs = self.conn.cursor()
      for persona,duration,frequency,demands,goalsupport in personas:
        curs.execute('call addTaskPersona(%s,%s,%s,%s,%s,%s,%s)',(taskId,persona,duration,frequency,demands,goalsupport,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding task persona ' + persona + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating personas with environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTaskAssets(self,taskId,assets,environmentName):
    try:
      curs = self.conn.cursor()
      for asset in assets:
        curs.execute('call addTaskAsset(%s,%s,%s)',(taskId,asset,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding task asset ' + asset + ' to environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating assets with environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addMisuseCaseRisk(self,mcId,riskName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addMisuseCaseRisk(%s,%s)',(mcId,riskName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating risk ' + mcName + ' with misuse case ' + str(mcId)
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating risk ' + riskName + ' with misuse case id ' + str(mcId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteTask(self,taskId):
    self.deleteObject(taskId,'task')
    self.conn.commit()

  def deleteThreat(self,objtId):
    self.deleteObject(objtId,'threat')
    self.conn.commit()

  def deleteResponse(self,responseId):
    self.deleteObject(responseId,'response')
    self.conn.commit()

  def getTraceDimensions(self,dimName,isFrom):
    return self.traceDimensionList(self.getDimensionId(dimName,'trace_dimension'),isFrom)

  def traceDimensionList(self,dimId,isFrom):
    try:
      curs = self.conn.cursor()
      curs.execute('call traceDimensionList(%s,%s)',(dimId,isFrom))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting trace dimensions ' + str(vulId)
        raise DatabaseProxyException(exceptionText) 
      dimensions = []
      for row in curs.fetchall():
        row = list(row)
        dimensions.append(row[0])
      curs.close()
      return dimensions 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting trace dimensions (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRisks(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRisks(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining risks'
        raise DatabaseProxyException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting risks (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
    risks = {}
    parameterList = []
    for row in curs.fetchall():
      row = list(row)
      riskId = row[RISKS_ID_COL]
      riskName = row[RISKS_NAME_COL]
      threatName = row[RISKS_THREATNAME_COL]
      vulName = row[RISKS_VULNAME_COL]
      parameterList.append((riskId,riskName,threatName,vulName))
    curs.close()

    for parameters in parameterList:
      riskId = parameters[0]
      mc = self.riskMisuseCase(riskId)
      parameters = RiskParameters(parameters[1],parameters[2],parameters[3],mc)
      risk = ObjectFactory.build(riskId,parameters)
      risks[risk.name()] = risk
    return risks

  def addRisk(self,parameters):
    try:
      threatName = parameters.threat()
      vulName = parameters.vulnerability()
      riskId = self.newId()
      riskName = parameters.name()
      curs = self.conn.cursor()
      curs.execute('call addRisk(%s,%s,%s,%s)',(threatName,vulName,riskId,riskName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new risk ' + str(riskId)
        raise DatabaseProxyException(exceptionText) 
      mc = parameters.misuseCase()
      mcParameters = MisuseCaseParameters(mc.name(),mc.environmentProperties(),mc.risk())
      self.addMisuseCase(mcParameters)
      self.conn.commit()
      curs.close()
      return riskId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding risk (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateRisk(self,parameters):
    try:
      riskId = parameters.id()
      threatName = parameters.threat()
      vulName = parameters.vulnerability()
      riskName = parameters.name()
      curs = self.conn.cursor()
      curs.execute('call updateRisk(%s,%s,%s,%s)',(threatName,vulName,riskId,riskName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating risk ' + str(riskId)
        raise DatabaseProxyException(exceptionText) 
      mc = parameters.misuseCase()
      mcParameters = MisuseCaseParameters('Exploit ' + riskName,mc.environmentProperties(),riskName)
      mcParameters.setId(mc.id())
      self.updateMisuseCase(mcParameters)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating risk ' + riskId + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteRisk(self,riskId):
    self.deleteObject(riskId,'risk')
    self.conn.commit()

  def deleteMisuseCase(self,mcId):
    self.deleteObject(mcId,'misusecase')
    self.conn.commit()

  def getResponses(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getResponses(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining responses'
        raise DatabaseProxyException(exceptionText) 

      responses = {}
      responseRows = []
      for row in curs.fetchall():
        row = list(row)
        respId = row[RESPONSES_ID_COL]
        respName = row[RESPONSES_NAME_COL]
        respType = row[RESPONSES_MITTYPE_COL]
        respRisk = row[RESPONSES_RISK_COL]
        responseRows.append((respId,respName,respType,respRisk))
      curs.close()
      for respId,respName,respType,respRisk in responseRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(respId,'response'):
          if (respType == 'Accept'):
            respCost = self.responseCost(respId,environmentId)
            respDescription = self.responseDescription(respId,environmentId)
            properties = AcceptEnvironmentProperties(environmentName,respCost,respDescription)
            environmentProperties.append(properties) 
          elif (respType == 'Transfer'):
            respDescription = self.responseDescription(respId,environmentId)
            respRoles = self.responseRoles(respId,environmentId)
            properties = TransferEnvironmentProperties(environmentName,respDescription,respRoles)
            environmentProperties.append(properties) 
          else:
            mitType = self.mitigationType(respId,environmentId)
            detPoint = ''
            detMechs = []
            if (mitType == 'Detect'):
              detPoint = self.detectionPoint(respId,environmentId)
            elif (mitType == 'React'):
              detMechs = self.detectionMechanisms(respId,environmentId)
            properties = MitigateEnvironmentProperties(environmentName,mitType,detPoint,detMechs)
            environmentProperties.append(properties) 
         
        parameters = ResponseParameters(respName,respRisk,environmentProperties,respType)
        response = ObjectFactory.build(respId,parameters)
        responses[respName] = response
      return responses
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting responses (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def responseCost(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select responseCost(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining cost associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      costName = row[0]
      curs.close()
      return costName
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting cost associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def responseDescription(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select responseDescription(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining description associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      respDesc = row[0]
      curs.close()
      return respDesc
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting description associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def responseRoles(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call responseRoles(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining roles associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      roles = []
      for row in curs.fetchall():
        row = list(row)
        roles.append((row[0],row[1]))
      curs.close()
      return roles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting roles associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def mitigationType(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select mitigationType(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining mitigation type associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      mitType = row[0]
      curs.close()
      return mitType
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error obtainining mitigation type associated with response id ' + str(responseId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def riskComponents(self,riskName):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskComponents(%s)',(riskName))  
      if (curs.rowcount == -1):
        exceptionText = 'Error geting components of risk ' + riskName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      threatName = row[0]
      vulName = row[1]
      curs.close()
      return [threatName,vulName]
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting components of risk ' + riskName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addResponse(self,parameters):
    try:
      respName = parameters.name()
      respRisk = parameters.risk()
      respType = parameters.responseType()
      respId = self.newId()
      curs = self.conn.cursor()
      curs.execute('call addResponse(%s,%s,%s,%s)',(respId,respName,respType,respRisk))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new response ' + mitName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(respId,'response',environmentName)
        if (respType == 'Accept'):
          self.addResponseCost(respId,cProperties.cost(),environmentName)
          self.addResponseDescription(respId,cProperties.description(),environmentName)
        elif (respType == 'Transfer'):
          self.addResponseDescription(respId,cProperties.description(),environmentName)
          self.addResponseRoles(respId,cProperties.roles(),environmentName,cProperties.description())
        else:
          mitType = cProperties.type()
          self.addMitigationType(respId,mitType,environmentName)
          if (mitType == 'Detect'):    
            self.addDetectionPoint(respId,cProperties.detectionPoint(),environmentName)
          elif (mitType == 'React'):
           for detMech in cProperties.detectionMechanisms():
             self.addReactionDetectionMechanism(respId,detMech,environmentName)

      self.conn.commit()
      curs.close()
      return respId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addMitigationType(self,responseId,mitType,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_response_mitigate(%s,%s,%s)',(responseId,environmentName,mitType))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating mitigation type ' + mitType + ' with response ' + str(responseId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating mitigation type ' + mitType + ' with response ' + str(responseId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)


  def addResponseCost(self,responseId,costName,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addResponseCost(%s,%s,%s)',(responseId,costName,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating cost ' + costName + ' with response ' + str(responseId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating cost ' + costName + ' with response ' + str(responseId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addResponseDescription(self,responseId,descriptionText,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addResponseDescription(%s,%s,%s)',(responseId,descriptionText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating description with response ' + str(responseId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating description with response ' + str(responseId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addResponseRoles(self,responseId,roles,environmentName,respDesc):
    try:
      curs = self.conn.cursor()
      for role,cost in roles:
        curs.execute('call addResponseRole(%s,%s,%s,%s,%s)',(responseId,role,cost,environmentName,respDesc))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating role ' + role + ' with response ' + str(responseId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating roles with response ' + str(responseId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def updateResponse(self,parameters):
    respName = parameters.name()
    respRisk = parameters.risk()
    respType = parameters.responseType()
    respId = parameters.id()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteResponseComponents(%s)',(respId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating response ' + respName
        raise DatabaseProxyException(exceptionText) 

      curs.execute('call updateResponse(%s,%s,%s,%s)',(respId,respName,respType,respRisk))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding updating response ' + respName
        raise DatabaseProxyException(exceptionText) 
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(respId,'response',environmentName)
        if (respType == 'Accept'):
          self.addResponseCost(respId,cProperties.cost(),environmentName)
          self.addResponseDescription(respId,cProperties.description(),environmentName)
        elif (respType == 'Transfer'):
          self.addResponseDescription(respId,cProperties.description(),environmentName)
          self.addResponseRoles(respId,cProperties.roles(),environmentName,cProperties.description())
        else:
          mitType = cProperties.type()
          self.addMitigationType(respId,mitType,environmentName)
          if (mitType == 'Detect'):    
            self.addDetectionPoint(respId,cProperties.detectionPoint(),environmentName)
          elif (mitType == 'React'):
           for detMech in cProperties.detectionMechanisms():
             self.addReactionDetectionMechanism(respId,detMech,environmentName)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def detectionPoint(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select mitigatePoint(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting detection point for detection response id ' + str(mitId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      detectionPointName = row[0]
      curs.close()
      return detectionPointName
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting detection point for detection response id ' + str(responseId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDetectionPoint(self,mitId,detPoint,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_mitigate_point(%s,%s,%s)',(mitId,environmentName,detPoint))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating detection point ' + detPoint + ' for response id ' + str(mitId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close() 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating detection point ' + detPoint + ' for response id ' + str(mitId) + 'in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addReactionDetectionMechanism(self,mitId,detMech,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_reaction_detection_mechanism(%s,%s,%s)',(mitId,detMech,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating detection mechanism ' + detMech + ' with reaction id ' + str(mitId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close() 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating detection mechanism ' + detMech + ' with reaction id ' + str(mitId) + 'in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def detectionMechanisms(self,responseId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call detectionMechanisms(%s,%s)',(responseId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting detection mechanisms'
        raise DatabaseProxyException(exceptionText) 
      detectionMechanisms = []
      for row in curs.fetchall():
        row = list(row)
        detectionMechanisms.append(row[0])
      curs.close()
      return detectionMechanisms
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting detection mechanisms (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskAnalysisModel(self,environmentName,dimensionName='',objectName=''):
    if (dimensionName == 'risk' and objectName !='') or (objectName != '' and self.isRisk(objectName)):
      return self.riskModel(environmentName,objectName)

    try:
      curs = self.conn.cursor()
      curs.execute('call riskAnalysisModel(%s)',(environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting traceability links '
        raise DatabaseProxyException(exceptionText) 
      traces = []
      for traceRow in curs.fetchall():
        traceRow = list(traceRow)
        fromObjt = traceRow[FROM_OBJT_COL]
        fromName = traceRow[FROM_ID_COL]
        toObjt = traceRow[TO_OBJT_COL]
        toName = traceRow[TO_ID_COL]
        if (dimensionName != ''):
          if (fromObjt != dimensionName) and (toObjt != dimensionName):
            continue
        if (objectName != ''):
          if (fromName != objectName) and (toName != objectName):
            continue
        parameters = DotTraceParameters(fromObjt,fromName,toObjt,toName)
        traces.append(ObjectFactory.build(-1,parameters))
      curs.close() 
      return traces
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting risk analysis model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def removableTraces(self,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call viewRemovableTraces(%s)',(environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting removeable trace relations'
        raise DatabaseProxyException(exceptionText) 
      traces = []
      for traceRow in curs.fetchall():
        traceRow = list(traceRow)
        fromObjt = traceRow[FROM_OBJT_COL]
        fromName = traceRow[FROM_ID_COL]
        toObjt = traceRow[TO_OBJT_COL]
        toName = traceRow[TO_ID_COL]
        traces.append((fromObjt,fromName,toObjt,toName))
      curs.close() 
      return traces
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting removeable trace relations (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def allowableTraceDimension(self,fromId,toId):
    try:
      curs = self.conn.cursor()
      curs.execute('call allowableTraceDimension(%s,%s)',(fromId,toId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting allowable trace dimensions for from_id ' + str(fromId) + ' and to_id ' + str(toId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      isAllowable = row[0]
      curs.close()
      return isAllowable
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting allowable trace dimensions for from_id ' + str(fromId) + ' and to_id ' + str(toId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def reportDependencies(self,dimName,objtId):
    try:
      curs = self.conn.cursor()
      curs.execute('call reportDependents(%s,%s)',(objtId,dimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting dependencies for ' + dimName + ' id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        return []
      else:
        deps = []
        for row in curs.fetchall():
          row = list(row)
          deps.append((row[0],row[1],row[2]))
        curs.close()
        return deps
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting dependencies for ' + dimName + ' id ' + str(objtId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteDependencies(self,deps):
    for dep in deps:
      dimName = dep[0]
      objtId = dep[1]
      self.deleteObject(objtId,dimName)
    self.conn.commit()

  def threatenedAssets(self,threatId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call threat_asset(%s,%s)',(threatId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining getting assets associated with threat id ' + str(threatId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      assetNames  = []
      for row in curs.fetchall():
        row = list(row)
        assetNames.append(row[0])
      curs.close()
      return assetNames
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assets associated with threat id ' + str(threatId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def vulnerableAssets(self,vulId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call vulnerability_asset(%s,%s)',(vulId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining getting assets associated with vulnerability id ' + str(vulId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      assetNames  = []
      for row in curs.fetchall():
        row = list(row)
        assetNames.append(row[0])
      curs.close()
      return assetNames
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assets associated with vulnerability id ' + str(vulId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def addTrace(self,traceTable,fromId,toId,contributionType = 'and'):
    try:
      curs = self.conn.cursor()
     
      if (traceTable != 'requirement_task' and traceTable != 'requirement_usecase' and traceTable != 'requirement_requirement'):
        sqlText = 'insert into ' + traceTable + ' values(%s,%s)'
        curs.execute(sqlText,(fromId,toId)) 
      elif (traceTable == 'requirement_requirement'):
        sqlText = 'insert into ' + traceTable + ' values(%s,%s,%s)'
        curs.execute(sqlText,(fromId,toId,contributionType)) 
      else:
        refTypeId = self.getDimensionId(contributionType,'reference_type')
        sqlText = 'insert into ' + traceTable + ' values(%s,%s,%s)'
        curs.execute(sqlText,(fromId,toId,refTypeId)) 
      if (curs.rowcount == -1):
        exceptionText = 'Error adding fromId ' + str(fromId) + ' and toId ' + str(toId) + ' to link table ' + traceTable
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding fromId ' + str(fromId) + ' and toId ' + str(toId) + ' to link table ' + traceTable + ' (id: ' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteEnvironment(self,environmentId):
    self.deleteObject(environmentId,'environment')
    self.conn.commit()

  def riskRating(self,thrName,vulName,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskRating(%s,%s,%s)',(thrName,vulName,environmentName))
      if (curs.rowcount == -1):
        riskName = thrName + '/' + vulName
        exceptionText = 'MySQL error rating risk ' + riskName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      riskRating = row[0]
      curs.close()
      return riskRating
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      riskName = thrName + '/' + vulName
      exceptionText = 'MySQL error rating risk ' + riskName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def riskScore(self,threatName,vulName,environmentName,riskName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskScore(%s,%s,%s,%s)',(threatName,vulName,environmentName,riskName))
      if (curs.rowcount == -1):
        riskName = threatName + '/' + vulName
        exceptionText = 'MySQL calculating score for risk ' + riskName
        raise DatabaseProxyException(exceptionText) 
      else:
        scoreDetails = []
        for row in curs.fetchall():
          row = list(row)
          riskResponse = row[0]
          prmScore = row[1]
          pomScore = row[2]
          detailsBuf = row[3]
          scoreDetails.append((riskResponse,prmScore,pomScore,detailsBuf))
        curs.close()
        return scoreDetails
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error calculating score for risk ' + riskName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def targetNames(self,reqList,envName):
    targetDict = {}
    for reqLabel in reqList:
      reqTargets = self.reqTargetNames(reqLabel,envName)
      for target in reqTargets:
        if target in targetDict:
          for x in reqTargets:
            targetDict[target].add(x)
        else:
          targetDict[target] = reqTargets[target]
    return targetDict

  def reqTargetNames(self,reqLabel,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call targetNames(%s,%s)',(reqLabel,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting target names'
        raise DatabaseProxyException(exceptionText) 
      targets = {}
      for row in curs.fetchall():
        row = list(row)
        targetName = row[0]
        responseName = row[1]
        if (targetName in targets):
          targets[targetName].add(responseName)
        else:
          targets[targetName] = set([responseName])
      curs.close() 
      return targets
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting target names (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRoles(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRoles(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining roles'
        raise DatabaseProxyException(exceptionText) 
      roles = {}
      roleRows = []
      for row in curs.fetchall():
        row = list(row)
        roleId = row[0]
        roleName = row[1]
        roleType = row[2]
        shortCode = row[3]
        roleDescription = row[4]
        roleRows.append((roleId,roleName,roleType,shortCode,roleDescription))
      curs.close() 
      for roleId,roleName,roleType,shortCode,roleDescription in roleRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(roleId,'role'):
          roleResponses = self.roleResponsibilities(roleId,environmentId)
          roleCountermeasures = self.roleCountermeasures(roleId,environmentId)
          properties = RoleEnvironmentProperties(environmentName,roleResponses,roleCountermeasures)
          environmentProperties.append(properties)
        parameters = RoleParameters(roleName,roleType,shortCode,roleDescription,environmentProperties)
        role = ObjectFactory.build(roleId,parameters)
        roles[roleName] = role
      return roles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting roles (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addRole(self,parameters):
    roleId = self.newId()
    roleName = parameters.name()
    roleType = parameters.type()
    shortCode = parameters.shortCode()
    roleDesc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call addRole(%s,%s,%s,%s,%s)',(roleId,roleName,roleType,shortCode,roleDesc))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error adding new role ' + roleName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return roleId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding role ' + roleName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateRole(self,parameters):
    roleId = parameters.id()
    roleName = parameters.name()
    roleType = parameters.type()
    shortCode = parameters.shortCode()
    roleDesc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateRole(%s,%s,%s,%s,%s)',(roleId,roleName,roleType,shortCode,roleDesc))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error updating role ' + roleName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return roleId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating role ' + roleName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteRole(self,roleId):
    self.deleteObject(roleId,'role')
    self.conn.commit()

  def roleResponsibilities(self,roleId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call roleResponses(%s,%s)',(roleId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining responses for role id ' + str(roleId) + ' in environment ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        curs.close()
        return []
      else:
        responsibilities = []
        for row in curs.fetchall():
          row = list(row)
          responsibilities.append((row[0],row[1]))
        curs.close()
        return responsibilities
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting responses for role id ' + str(roleId) + 'in environment ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def roleCountermeasures(self,roleId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call roleCountermeasures(%s,%s)',(roleId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining countermeasures for role id ' + str(roleId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        curs.close()
        return []
      else:
        responsibilities = []
        for row in curs.fetchall():
          row = list(row)
          responsibilities.append(row[0])
        curs.close()
        return responsibilities
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting countermeasures for role id ' + str(roleId) + ' in environment ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'

  def getCountermeasures(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getCountermeasures(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining countermeasures'
        raise DatabaseProxyException(exceptionText) 
      countermeasures = {}
      cmRows = []
      for row in curs.fetchall():
        row = list(row)
        cmId = row[COUNTERMEASURES_ID_COL]
        cmName = row[COUNTERMEASURES_NAME_COL]
        cmDesc = row[COUNTERMEASURES_DESCRIPTION_COL]
        cmType = row[COUNTERMEASURES_TYPE_COL]
        cmRows.append((cmId,cmName,cmDesc,cmType))
      curs.close()
      for cmId,cmName,cmDesc,cmType in cmRows:
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(cmId,'countermeasure'):
          reqs,targets = self.countermeasureTargets(cmId,environmentId)
          properties,pRationale = self.relatedProperties('countermeasure',cmId,environmentId)
          cost = self.countermeasureCost(cmId,environmentId)
          roles = self.countermeasureRoles(cmId,environmentId)
          personas = self.countermeasurePersonas(cmId,environmentId)
          properties = CountermeasureEnvironmentProperties(environmentName,reqs,targets,properties,pRationale,cost,roles,personas)
          environmentProperties.append(properties) 
        parameters = CountermeasureParameters(cmName,cmDesc,cmType,environmentProperties)
        countermeasure = ObjectFactory.build(cmId,parameters)
        countermeasures[cmName] = countermeasure
      return countermeasures
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting countermeasures (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasureCost(self,cmId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select countermeasureCost(%s,%s)',(cmId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining cost associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      costName = row[0]
      curs.close()
      return costName
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting cost associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasureTargets(self,cmId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call countermeasureRequirements(%s,%s)',(cmId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining requirements associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      reqs = []
      for row in curs.fetchall():
        row = list(row)
        reqs.append(row[0])
      curs.close()
      curs = self.conn.cursor()
      curs.execute('call countermeasureTargets(%s,%s)',(cmId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining targets associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      targets = []
      for row in curs.fetchall():
        row = list(row)
        targets.append(Target(row[0],row[1],row[2]))
      curs.close()
      return (reqs,targets)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting targets associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasureRoles(self,cmId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call countermeasureRoles(%s,%s)',(cmId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining roles associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      roles = []
      for row in curs.fetchall():
        row = list(row)
        roles.append(row[0])
      curs.close()
      return roles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting roles associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasurePersonas(self,cmId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call countermeasurePersonas(%s,%s)',(cmId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining task personas associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      personas = []
      for row in curs.fetchall():
        row = list(row)
        taskName = row[0]
        personaName = row[1]
        duration = row[2]
        frequency = row[3]
        demands = row[4]
        goalSupport = row[5]
        personas.append((taskName,personaName,duration,frequency,demands,goalSupport))
      curs.close()
      return personas
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting personas associated with countermeasure id ' + str(cmId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def addCountermeasure(self,parameters):
    cmName = parameters.name()
    cmDesc = parameters.description()
    cmType = parameters.type()
    cmId = self.newId()
    try:
      curs = self.conn.cursor()
      curs.execute('call addCountermeasure(%s,%s,%s,%s)',(cmId,cmName,cmDesc,cmType))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new countermeasure ' + cmName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(cmId,'countermeasure',environmentName)
        self.addCountermeasureTargets(cmId,cProperties.requirements(),cProperties.targets(),environmentName)
        self.addSecurityProperties('countermeasure',cmId,environmentName,cProperties.properties(),cProperties.rationale())
        self.addCountermeasureCost(cmId,cProperties.cost(),environmentName)
        self.addCountermeasureRoles(cmId,cProperties.roles(),environmentName)
        self.addCountermeasurePersonas(cmId,cProperties.personas(),environmentName)
        self.addRequirementRoles(cmName,cProperties.roles(),cProperties.requirements(),environmentName)
      self.conn.commit()
      curs.close()
      return cmId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding countermeasure ' + cmName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def updateCountermeasure(self,parameters):
    cmName = parameters.name()
    cmDesc = parameters.description()
    cmType = parameters.type()
    cmId = parameters.id()
    environmentProperties = parameters.environmentProperties()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteCountermeasureComponents(%s)',(cmId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating response ' + respName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateCountermeasure(%s,%s,%s,%s)',(cmId,cmName,cmDesc,cmType))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating countermeasure ' + cmName
        raise DatabaseProxyException(exceptionText) 

      for cProperties in environmentProperties:
        environmentName = cProperties.name()
        self.addDimensionEnvironment(cmId,'countermeasure',environmentName)
        self.updateCountermeasureTargets(cmId,cProperties.requirements(),cProperties.targets(),environmentName)
        self.addSecurityProperties('countermeasure',cmId,environmentName,cProperties.properties(),cProperties.rationale())
        self.addCountermeasureCost(cmId,cProperties.cost(),environmentName)
        self.addCountermeasureRoles(cmId,cProperties.roles(),environmentName)
        self.addCountermeasurePersonas(cmId,cProperties.personas(),environmentName)
        self.updateRequirementRoles(cmName,cProperties.roles(),cProperties.requirements(),environmentName)
      self.conn.commit()
      curs.close()
      return cmId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating countermeasure ' + cmName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addCountermeasureTargets(self,cmId,reqs,targets,environmentName):
    try:
      curs = self.conn.cursor()
      for reqLabel in reqs:
        curs.execute('call addCountermeasureRequirement(%s,%s,%s)',(cmId,reqLabel,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating requirement ' + reqLabel + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
      for target in targets:
        curs.execute('call addCountermeasureTarget(%s,%s,%s,%s,%s)',(cmId,target.name(),target.effectiveness(),target.rationale(),environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating target ' + target.name() + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
#        for responseName in target.responses():
#          curs.execute('call addCountermeasureTargetResponse(%s,%s,%s,%s)',(cmId,target.name(),responseName,environmentName))
#          if (curs.rowcount == -1):
#            exceptionText = 'Error associating target ' + target.name() + ' and response ' + response + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
#            raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating targets with countermeasure ' + str(cmId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def updateCountermeasureTargets(self,cmId,reqs,targets,environmentName):
    try:
      curs = self.conn.cursor()
      for reqLabel in reqs:
        curs.execute('call updateCountermeasureRequirement(%s,%s,%s)',(cmId,reqLabel,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating requirement ' + reqLabel + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
      for target in targets:
        curs.execute('call addCountermeasureTarget(%s,%s,%s,%s,%s)',(cmId,target.name(),target.effectiveness(),target.rationale(),environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating target ' + target.name() + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
#        for responseName in target.responses():
#          curs.execute('call addCountermeasureTargetResponse(%s,%s,%s,%s)',(cmId,target.name(),responseName,environmentName))
#          if (curs.rowcount == -1):
#            exceptionText = 'Error associating target ' + target.name() + ' and response ' + response + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating targets with countermeasure ' + str(cmId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)


  def addRequirementRoles(self, cmName,roles, requirements, environmentName):
    for role in roles:
      for requirement in requirements:
        self.addRequirementRole(cmName,role,requirement,environmentName)

  def updateRequirementRoles(self, cmName,roles, requirements, environmentName):
    for role in roles:
      for requirement in requirements:
        self.updateRequirementRole(cmName,role,requirement,environmentName)
          
  def deleteRequirementRoles(self, roles, requirements, environmentName):
    for role in roles:
      for requirement in requirements:
        self.deleteRequirementRole(role,requirement,environmentName)

  def addRequirementRole(self,cmName,roleName,reqName,envName):
    associationId = self.newId()
    try:
      curs = self.conn.cursor()
      curs.execute('call addRequirementRole(%s,%s,%s,%s,%s)',(associationId,cmName,roleName,reqName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + envName + ' - response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def updateRequirementRole(self,cmName,roleName,reqName,envName):
    associationId = self.newId()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateRequirementRole(%s,%s,%s,%s,%s)',(associationId,cmName,roleName,reqName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + envName + ' - response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def deleteRequirementRole(self,roleName,reqName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteRequirementRole(%s,%s,%s)',(roleName,reqName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error de-associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error de-associating requirement ' + reqName + ' with role ' + roleName + ' in environment ' + environmentName + ' - response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addCountermeasureCost(self,cmId,costName,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addCountermeasureCost(%s,%s,%s)',(cmId,costName,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating cost ' + costName + ' with response ' + str(cmId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating cost ' + costName + ' with response ' + str(cmId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addCountermeasureRoles(self,cmId,roles,environmentName):
    try:
      curs = self.conn.cursor()
      for role in roles:
        curs.execute('call addCountermeasureRole(%s,%s,%s)',(cmId,role,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating role ' + role + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating role ' + role + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addCountermeasurePersonas(self,cmId,personas,environmentName):
    try:
      curs = self.conn.cursor()
      for task,persona,duration,frequency,demands,goalSupport in personas:
        curs.execute('call addCountermeasurePersona(%s,%s,%s,%s,%s,%s,%s,%s)',(cmId,persona,task,duration,frequency,demands,goalSupport,environmentName))
        if (curs.rowcount == -1):
          exceptionText = 'Error associating persona ' + persona + ' with countermeasure ' + str(cmId) + ' in environment ' + environmentName
          raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating personas with countermeasure ' + str(cmId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def personaNarrative(self,scId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select personaNarrative(%s,%s)',(scId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining narrative associated with persona id ' + str(scId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      desc = row[0]
      curs.close()
      return desc
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting narrative associated with persona id ' + str(scId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def personaDirect(self,scId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select personaDirect(%s,%s)',(scId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining direct flag associated with persona id ' + str(scId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      directFlag = row[0]
      directValue = 'False'
      if (directFlag == 1):
        directValue = 'True'
      curs.close()
      return directValue
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting directFlag associated with persona id ' + str(scId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addPersonaNarrative(self,stId,environmentName,descriptionText):
    try:
      curs = self.conn.cursor()
      curs.execute('call addPersonaNarrative(%s,%s,%s)',(stId,descriptionText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating narrative with persona ' + str(stId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating narrative with persona ' + str(stId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addPersonaDirect(self,stId,environmentName,directText):
    try:
      curs = self.conn.cursor()
      curs.execute('call addPersonaDirect(%s,%s,%s)',(stId,directText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating direct flag with persona ' + str(stId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating direct flag with persona ' + str(stId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def taskNarrative(self,scId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select taskNarrative(%s,%s)',(scId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining narrative associated with task id ' + str(scId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      narrative = row[0]
      curs.close()
      return narrative
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting narrative associated with task id ' + str(scId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskConsequences(self,scId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select taskConsequences(%s,%s)',(scId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining consequences associated with task id ' + str(scId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      consequences = row[0]
      curs.close()
      return consequences
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting consequences associated with task id ' + str(scId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskBenefits(self,scId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select taskBenefits(%s,%s)',(scId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining benefits associated with task id ' + str(scId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      benefits = row[0]
      curs.close()
      return benefits
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting benefits associated with task id ' + str(scId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTaskNarrative(self,scId,narrativeText,cText,bText,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addTaskNarrative(%s,%s,%s,%s,%s)',(scId,narrativeText,cText,bText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating narrative with task ' + str(scId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating narrative with task ' + str(scId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def misuseCaseNarrative(self,mcId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select misuseCaseNarrative(%s,%s)',(mcId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining narrative associated with misuse case id ' + str(mcId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      narrative = row[0]
      curs.close()
      return narrative
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting narrative associated with misuse case id ' + str(mcId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addMisuseCaseNarrative(self,mcId,narrativeText,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addMisuseCaseNarrative(%s,%s,%s)',(mcId,narrativeText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating narrative with misuse case ' + str(mcId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating narrative with misuse case ' + str(mcId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def riskEnvironmentNames(self,riskName):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskEnvironmentNames(%s)',(riskName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining getting environments associated with risk ' + riskName
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append(row[0])
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments associated with risk ' + riskName + ' id ' + str(dimId) +  ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def threatVulnerabilityEnvironmentNames(self,threatName,vulName):
    try:
      curs = self.conn.cursor()
      curs.execute('call threatVulnerabilityEnvironmentNames(%s,%s)',(threatName,vulName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining getting environments associated with threat ' + threatName + ' and vulnerability ' + vulName
        raise DatabaseProxyException(exceptionText) 
      environments = []
      for row in curs.fetchall():
        row = list(row)
        environments.append(row[0])
      curs.close()
      return environments
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments associated with threat ' + threatName  + ' and vulnerability ' + vulName + ' id ' + str(dimId) +  ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskDependencies(self,tId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select taskDependencies(%s,%s)',(tId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining dependencies associated with task id ' + str(tId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      dependencies = row[0]
      curs.close()
      return dependencies
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting dependencies associated with task id ' + str(tId) + ' in environment id ' + str(environmentId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTaskDependencies(self,tId,depsText,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addTaskDependencies(%s,%s,%s)',(tId,depsText,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating dependencies with task ' + str(tId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating objective with task ' + str(tId) + ' in environment ' + environmentName + ' response (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def requirementLabelId(self,reqLabel):
    try:
      curs = self.conn.cursor()
      curs.execute('select requirementLabelId(%s)',(reqLabel))
      if (curs.rowcount <= 0):
        exceptionText = 'Error getting id for requirement label ' + reqLabel
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        reqId = row[0]
        curs.close()
        return reqId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting id for requirement label ' + reqLabel + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def requirementLabel(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('select requirementLabel(%s)',(reqName))
      if (curs.rowcount <= 0):
        exceptionText = 'Error getting id for requirement name ' + reqName
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        reqLabel = row[0]
        curs.close()
        return reqLabel
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting id for requirement name ' + reqName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def requirementLabelById(self,reqId):
    try:
      curs = self.conn.cursor()
      curs.execute('select requirementLabelById(%s)',(reqId))
      if (curs.rowcount <= 0):
        exceptionText = 'Error getting id for requirement label for id ' + str(reqId)
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        reqLabel = row[0]
        curs.close()
        return reqLabel
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting id for requirement label for id ' + str(reqId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)


  def requirementNameId(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('select requirementNameId(%s)',(reqName))
      if (curs.rowcount <= 0):
        exceptionText = 'Error getting id for requirement name ' + reqName
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        reqId = row[0]
        curs.close()
        return reqId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting id for requirement name ' + reqName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def mitigatedRisks(self,cmId):
    try:
      curs = self.conn.cursor()
      curs.execute('call mitigatedRisks(%s)',(cmId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting risks mitigated by countermeasure id ' + str(cmId)
        raise DatabaseProxyException(exceptionText) 
      else:
        risks = []
        for row in curs.fetchall():
          row = list(row)
          risks.append(row[0])
        curs.close()
        return risks
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting risks mitigated by countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def deleteTrace(self,fromObjt,fromName,toObjt,toName):
    try:
      curs = self.conn.cursor()
      curs.execute('call delete_trace(%s,%s,%s,%s)',(fromObjt,fromName,toObjt,toName))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting trace relation: (' + fromObjt + ',' + fromName + ',' + toObjt + ',' + toName + ')'
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting trace relation: (' + fromObjt + ',' + fromName + ',' + toObjt + ',' + toName + ') (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def deleteCountermeasure(self,cmId):
    self.deleteObject(cmId,'countermeasure')
    self.conn.commit()

  def addGoal(self,parameters):
    goalId = self.newId()
    goalName = parameters.name()
    goalOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoal(%s,%s,%s)',(goalId,goalName,goalOrig))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new goal ' + goalName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(goalId,'goal',environmentName)
        self.addGoalDefinition(goalId,environmentName,environmentProperties.definition())
        self.addGoalCategory(goalId,environmentName,environmentProperties.category())
        self.addGoalPriority(goalId,environmentName,environmentProperties.priority())
        self.addGoalFitCriterion(goalId,environmentName,environmentProperties.fitCriterion())
        self.addGoalIssue(goalId,environmentName,environmentProperties.issue())
        self.addGoalRefinements(goalId,goalName,environmentName,environmentProperties.goalRefinements(),environmentProperties.subGoalRefinements())
        self.addGoalConcerns(goalId,environmentName,environmentProperties.concerns())
        self.addGoalConcernAssociations(goalId,environmentName,environmentProperties.concernAssociations())
      self.conn.commit()
      curs.close()
      return goalId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding goal ' + goalName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateGoal(self,parameters):
    goalId = parameters.id()
    goalName = parameters.name()
    goalOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteGoalComponents(%s)',(goalId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating goal ' + goalName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateGoal(%s,%s,%s)',(goalId,goalName,goalOrig))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating goal ' + goalName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(goalId,'goal',environmentName)
        self.addGoalDefinition(goalId,environmentName,environmentProperties.definition())
        self.addGoalCategory(goalId,environmentName,environmentProperties.category())
        self.addGoalPriority(goalId,environmentName,environmentProperties.priority())
        self.addGoalFitCriterion(goalId,environmentName,environmentProperties.fitCriterion())
        self.addGoalIssue(goalId,environmentName,environmentProperties.issue())
        self.addGoalRefinements(goalId,goalName,environmentName,environmentProperties.goalRefinements(),environmentProperties.subGoalRefinements())
        self.addGoalConcerns(goalId,environmentName,environmentProperties.concerns())
        self.addGoalConcernAssociations(goalId,environmentName,environmentProperties.concernAssociations())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating goal ' + goalName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getGoals(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getGoals(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goals'
        raise DatabaseProxyException(exceptionText) 
      goals = {}
      goalRows = []
      for row in curs.fetchall():
        row = list(row)
        goalId = row[GOALS_ID_COL]
        goalName = row[GOALS_NAME_COL]
        goalOrig = row[GOALS_ORIGINATOR_COL]
        goalRows.append((goalId,goalName,goalOrig))
      curs.close()

      for goalId,goalName,goalOrig in goalRows:
        environmentProperties = self.goalEnvironmentProperties(goalId)
        parameters = GoalParameters(goalName,goalOrig,self.goalEnvironmentProperties(goalId))
        goal = ObjectFactory.build(goalId,parameters)
        goals[goalName] = goal
      return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getColouredGoals(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getColouredGoals(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goals'
        raise DatabaseProxyException(exceptionText) 
      goals = {}
      goalRows = []
      for row in curs.fetchall():
        row = list(row)
        goalId = row[GOALS_ID_COL]
        goalName = row[GOALS_NAME_COL]
        goalOrig = row[GOALS_ORIGINATOR_COL]
        goalColour = row[GOALS_COLOUR_COL]
        goalRows.append((goalId,goalName,goalOrig,goalColour))
      curs.close()

      for goalId,goalName,goalOrig,goalColour in goalRows:
        environmentProperties = self.goalEnvironmentProperties(goalId)
        parameters = GoalParameters(goalName,goalOrig,self.goalEnvironmentProperties(goalId))
        goal = ObjectFactory.build(goalId,parameters)
        goal.setColour(goalColour)
        goals[goalName] = goal
      return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def goalEnvironmentProperties(self,goalId):
    try:
      environmentProperties = []
      for environmentId,environmentName in self.dimensionEnvironments(goalId,'goal'):
        goalLabel = self.goalLabel(goalId,environmentId)
        goalDef = self.goalDefinition(goalId,environmentId)
        goalType = self.goalCategory(goalId,environmentId)
        goalPriority = self.goalPriority(goalId,environmentId)
        goalFitCriterion = self.goalFitCriterion(goalId,environmentId)
        goalIssue = self.goalIssue(goalId,environmentId) 
        goalRefinements,subGoalRefinements = self.goalRefinements(goalId,environmentId)
        concerns = self.goalConcerns(goalId,environmentId)
        concernAssociations = self.goalConcernAssociations(goalId,environmentId)
        properties = GoalEnvironmentProperties(environmentName,goalLabel,goalDef,goalType,goalPriority,goalFitCriterion,goalIssue,goalRefinements,subGoalRefinements,concerns,concernAssociations)
        environmentProperties.append(properties) 
      return environmentProperties
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goal environment properties for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteGoal(self,goalId):
    self.deleteObject(goalId,'goal')
    self.conn.commit()

  def roleTasks(self,environmentName,roles):
    try:
      curs = self.conn.cursor()
      tpSet = set([])
      for role in roles:
        curs.execute('call countermeasureTaskPersonas(%s,%s)',(role,environmentName))
        for row in curs.fetchall():
          row = list(row)
          taskName = row[0]
          personaName = row[1]
          tpSet.add((taskName,personaName))
      curs.close()
      tpDict = {}
      for taskName,personaName in tpSet:
        tpDict[(taskName,personaName)] = ['None','None','None','None']
      return tpDict
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting tasks associated with environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskUsabilityScore(self,taskName,environmentName):
    try:
      curs = self.conn.cursor()
      curs.execute('select task_usability(%s,%s)',(taskName,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining usability score for task ' + taskName + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        taskUsabilityScore = int(row[0])
        curs.close()
        return taskUsabilityScore
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task usability associated with environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskLoad(self,taskId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select usability_score(%s,%s)',(taskId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining task load for task id ' + str(taskId) + ' in environment ' + environmentId
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        taskLoad = row[0]
        curs.close()
        return taskLoad
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task load with environment id ' + str(taskId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasureLoad(self,taskId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select hindrance_score(%s,%s)',(taskId,environmentId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining countermeasure load for task id ' + str(taskId) + ' in environment ' + environmentId
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        taskLoad = row[0]
        curs.close()
        return taskLoad
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task countermeasure load with environment id ' + str(taskId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentAssets(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call assetNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining assets for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        assets = []
        for row in curs.fetchall():
          row = list(row)
          assets.append(row[0])
        curs.close()
        return assets
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assets associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentGoals(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goals for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentObstacles(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call obstacleNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining obstacles for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        obstacles = []
        for row in curs.fetchall():
          row = list(row)
          obstacles.append(row[0])
        curs.close()
        return obstacles 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting obstacles associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentDomainProperties(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call domainPropertyNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining domain properties for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting domain properties associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentCountermeasures(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call countermeasureNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining countermeasures for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting countermeasures associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentTasks(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining tasks for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting tasks associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentThreats(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call threatNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining threats for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting threats associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentVulnerabilities(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call vulnerabilityNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining vulnerabilities for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting vulnerabilities associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalModelElements(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalModelElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goal model elements for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goal model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleModelElements(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call obstacleModelElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining obstacle model elements for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting obstacle model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def responsibilityModelElements(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call responsibilityModelElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining responsibility model elements for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting responsibility model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskModelElements(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskModelElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining task model elements for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def classModelElements(self,envName,hideConcerns = False):
    try:
      curs = self.conn.cursor()
      if (hideConcerns == True):
        curs.execute('call concernlessClassModelElements(%s)',(envName))
      else:
        curs.execute('call classModelElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining class model elements for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting class model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def classModel(self,envName,asName = '',hideConcerns = False):
    if (hideConcerns == True):
      if (asName == ''):
        return self.classAssociations('call concernlessClassModel(%s)',envName)
      else:
        return self.classTreeAssociations('call concernlessClassTree(%s,%s)',asName,envName)
    else:
      if (asName == ''):
        return self.classAssociations('call classModel(%s)',envName)
      else:
        return self.classTreeAssociations('call classTree(%s,%s)',asName,envName)


  def getClassAssociations(self,constraintId = ''):
    return self.classAssociations('call classAssociationNames(%s)',constraintId)

  def classAssociations(self,procName,constraintId = ''):
    try:
      curs = self.conn.cursor()
      curs.execute(procName,(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining class associations'
        raise DatabaseProxyException(exceptionText) 
      associations = {}
      for row in curs.fetchall():
        row = list(row)
        associationId = row[CLASSASSOCIATIONS_ID_COL]
        envName = row[CLASSASSOCIATIONS_ENV_COL]
        headName = row[CLASSASSOCIATIONS_HEAD_COL]
        headDim  = row[CLASSASSOCIATIONS_HEADDIM_COL]
        headNav =  row[CLASSASSOCIATIONS_HEADNAV_COL]
        headType = row[CLASSASSOCIATIONS_HEADTYPE_COL]
        headMult = row[CLASSASSOCIATIONS_HEADMULT_COL]
        headRole = row[CLASSASSOCIATIONS_HEADROLE_COL]
        tailRole = row[CLASSASSOCIATIONS_TAILROLE_COL]
        tailMult = row[CLASSASSOCIATIONS_TAILMULT_COL]
        tailType = row[CLASSASSOCIATIONS_TAILTYPE_COL]
        tailNav =  row[CLASSASSOCIATIONS_TAILNAV_COL]
        tailDim  = row[CLASSASSOCIATIONS_TAILDIM_COL]
        tailName = row[CLASSASSOCIATIONS_TAIL_COL]
        rationale = row[CLASSASSOCIATIONS_RATIONALE_COL]
        parameters = ClassAssociationParameters(envName,headName,headDim,headNav,headType,headMult,headRole,tailRole,tailMult,tailType,tailNav,tailDim,tailName,rationale)
        association = ObjectFactory.build(associationId,parameters)
        asLabel = envName + '/' + headName + '/' + tailName
        associations[asLabel] = association
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting class associations (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def classTreeAssociations(self,procName,assetName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute(procName,(assetName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining class associations'
        raise DatabaseProxyException(exceptionText) 
      associations = {}
      for row in curs.fetchall():
        row = list(row)
        associationId = row[CLASSASSOCIATIONS_ID_COL]
        envName = row[CLASSASSOCIATIONS_ENV_COL]
        headName = row[CLASSASSOCIATIONS_HEAD_COL]
        headDim  = row[CLASSASSOCIATIONS_HEADDIM_COL]
        headNav =  row[CLASSASSOCIATIONS_HEADNAV_COL]
        headType = row[CLASSASSOCIATIONS_HEADTYPE_COL]
        headMult = row[CLASSASSOCIATIONS_HEADMULT_COL]
        headRole = row[CLASSASSOCIATIONS_HEADROLE_COL]
        tailRole = row[CLASSASSOCIATIONS_TAILROLE_COL]
        tailMult = row[CLASSASSOCIATIONS_TAILMULT_COL]
        tailType = row[CLASSASSOCIATIONS_TAILTYPE_COL]
        tailNav =  row[CLASSASSOCIATIONS_TAILNAV_COL]
        tailDim  = row[CLASSASSOCIATIONS_TAILDIM_COL]
        tailName = row[CLASSASSOCIATIONS_TAIL_COL]
        rationale = row[CLASSASSOCIATIONS_RATIONALE_COL]
        parameters = ClassAssociationParameters(envName,headName,headDim,headNav,headType,headMult,headRole,tailRole,tailMult,tailType,tailNav,tailDim,tailName,rationale)
        association = ObjectFactory.build(associationId,parameters)
        asLabel = envName + '/' + headName + '/' + tailName
        associations[asLabel] = association
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting class associations (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addClassAssociation(self,parameters):
    associationId = self.newId()
    envName = parameters.environment()
    headAsset = parameters.headAsset()
    headType = parameters.headType()
    headNav = parameters.headNavigation()
    headMult = parameters.headMultiplicity()
    headRole = parameters.headRole()
    tailRole = parameters.tailRole()
    tailMult = parameters.tailMultiplicity()
    tailNav = parameters.tailNavigation()
    tailType = parameters.tailType()
    tailAsset = parameters.tailAsset()

    try:
      curs = self.conn.cursor()
      curs.execute('call addClassAssociation(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(associationId,envName,headAsset,headType,headNav,headMult,headRole,tailRole,tailMult,tailNav,tailType,tailAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new class association ' + envName + '/' + headAsset + '/' + tailAsset
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return associationId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding class association ' + envName + '/' + headAsset + '/' + tailAsset + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateClassAssociation(self,parameters):
    associationId = parameters.id()
    envName = parameters.environment()
    headAsset = parameters.headAsset()
    headType = parameters.headType()
    headNav = parameters.headNavigation()
    headMult = parameters.headMultiplicity()
    headRole = parameters.headRole()
    tailRole = parameters.tailRole()
    tailMult = parameters.tailMultiplicity()
    tailNav = parameters.tailNavigation()
    tailType = parameters.tailType()
    tailAsset = parameters.tailAsset()

    try:
      curs = self.conn.cursor()
      curs.execute('call updateClassAssociation(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(associationId,envName,headAsset,headType,headNav,headMult,headRole,tailRole,tailMult,tailNav,tailType,tailAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating class association ' + envName + '/' + headAsset + '/' + tailAsset
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating class association ' + envName + '/' + headAsset + '/' + tailAsset + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteClassAssociation(self,associationId):
    self.deleteObject(associationId,'classassociation')
    self.conn.commit()

  def goalModel(self,envName,goalName = '',topLevelGoals = 0,caseFilter = 0):
    if (goalName == ''):
      return self.goalAssociations('call goalModel(%s)',envName)
    else:
      return self.goalTreeAssociations('call goalTree(%s,%s,%s,%s)',goalName,envName,topLevelGoals,caseFilter)
   

  def responsibilityModel(self,envName,roleName = ''):
    if (roleName == ''):
      return self.goalAssociations('call responsibilityModel(%s)',envName)
    else:
      return self.goalTreeAssociations('call subResponsibilityModel(%s,%s)',envName,roleName)
 
  def obstacleModel(self,envName,goalName = '',topLevelGoals = 0):
    if (goalName == ''):
      return self.goalAssociations('call obstacleModel(%s)',envName)
    else:
      return self.goalTreeAssociations('call obstacleTree(%s,%s,%s,%s)',goalName,envName,topLevelGoals)
 
  def taskModel(self,envName,taskName = '',mcFilter=False):
    if (taskName == ''):
      return self.goalAssociations('call taskModel(%s)',envName)
    else:
      if (mcFilter == True):
        return self.goalTreeAssociations('call subMisuseCaseModel(%s,%s)',taskName,envName)
      else:
        return self.goalTreeAssociations('call subTaskModel(%s,%s)',taskName,envName)

  def getGoalAssociations(self,constraintId = ''):
    return self.goalAssociations('call goalAssociationNames(%s)',constraintId)

  def goalAssociations(self,procName,constraintId = ''):
    try:
      curs = self.conn.cursor()
      curs.execute(procName,(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goal associations'
        raise DatabaseProxyException(exceptionText) 
      associations = {}
      for row in curs.fetchall():
        row = list(row)
        associationId = row[GOALASSOCIATIONS_ID_COL]
        envName = row[GOALASSOCIATIONS_ENV_COL]
        goalName = row[GOALASSOCIATIONS_GOAL_COL]
        goalDimName = row[GOALASSOCIATIONS_GOALDIM_COL]
        aType = row[GOALASSOCIATIONS_TYPE_COL]
        subGoalName = row[GOALASSOCIATIONS_SUBGOAL_COL]
        subGoalDimName = row[GOALASSOCIATIONS_SUBGOALDIM_COL]
        alternativeId = row[GOALASSOCIATIONS_ALTERNATIVE_COL]
        rationale = row[GOALASSOCIATIONS_RATIONALE_COL]
        parameters = GoalAssociationParameters(envName,goalName,goalDimName,aType,subGoalName,subGoalDimName,alternativeId,rationale)
        association = ObjectFactory.build(associationId,parameters)
        asLabel = envName + '/' + goalName + '/' + subGoalName + '/' + aType
        associations[asLabel] = association
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goal associations (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalTreeAssociations(self,procName,goalName,envName,topLevelGoals = 0,caseFilter = 0):
    try:
      curs = self.conn.cursor()
      if (procName == 'call goalTree(%s,%s,%s,%s)') or (procName == 'call obstacleTree(%s,%s,%s,%s)'):
        curs.execute(procName,(goalName,envName,topLevelGoals,caseFilter))
      else:
        curs.execute(procName,(goalName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining sub-goal associations'
        raise DatabaseProxyException(exceptionText) 
      associations = {}
      for row in curs.fetchall():
        row = list(row)
        associationId = row[GOALASSOCIATIONS_ID_COL]
        envName = row[GOALASSOCIATIONS_ENV_COL]
        goalName = row[GOALASSOCIATIONS_GOAL_COL]
        goalDimName = row[GOALASSOCIATIONS_GOALDIM_COL]
        aType = row[GOALASSOCIATIONS_TYPE_COL]
        subGoalName = row[GOALASSOCIATIONS_SUBGOAL_COL]
        subGoalDimName = row[GOALASSOCIATIONS_SUBGOALDIM_COL]
        alternativeId = row[GOALASSOCIATIONS_ALTERNATIVE_COL]
        rationale = row[GOALASSOCIATIONS_RATIONALE_COL]
        parameters = GoalAssociationParameters(envName,goalName,goalDimName,aType,subGoalName,subGoalDimName,alternativeId,rationale)
        association = ObjectFactory.build(associationId,parameters)
        asLabel = envName + '/' + goalName + '/' + subGoalName + '/' + aType
        associations[asLabel] = association
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting sub-goal associations (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def addGoalAssociation(self,parameters):
    associationId = self.newId()
    envName = parameters.environment()
    goalName = parameters.goal()
    if (goalName == ''):
      return
    goalDimName = parameters.goalDimension()
    aType = parameters.type()
    subGoalName = parameters.subGoal()
    subGoalDimName = parameters.subGoalDimension()
    alternativeId = parameters.alternative()
    rationale = parameters.rationale()
    try:
      curs = self.conn.cursor()
#      print 'call addGoalAssociation(',associationId,',',envName,',',goalName,',',goalDimName,',',aType,',',subGoalName,',',subGoalDimName,',',alternativeId,',',rationale,')'
      curs.execute('call addGoalAssociation(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(associationId,envName,goalName,goalDimName,aType,subGoalName,subGoalDimName,alternativeId,rationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new goal association ' + envName + '/' + goalName + '/' + subGoalName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return associationId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding goal association ' + envName + '/' + goalName + '/' + subGoalName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateGoalAssociation(self,parameters):
    associationId = parameters.id()
    envName = parameters.environment()
    goalName = parameters.goal()
    goalDimName = parameters.goalDimension()
    aType = parameters.type()
    subGoalName = parameters.subGoal()
    subGoalDimName = parameters.subGoalDimension()
    alternativeId = parameters.alternative()
    rationale = parameters.rationale()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateGoalAssociation(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(associationId,envName,goalName,goalDimName,aType,subGoalName,subGoalDimName,alternativeId,rationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating goal association ' + envName + '/' + goalName + '/' + subGoalName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating goal association ' + envName + '/' + goalName + '/' + subGoalName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteGoalAssociation(self,associationId,goalDimName,subGoalDimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call delete_goalassociation(%s,%s,%s)',(associationId,goalDimName,subGoalDimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting goal association id ' + str(objtId)
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.IntegrityError, e:
      id,msg = e
      exceptionText = 'Cannot remove goal association due to dependent data.  Check the goal model model for further information  (id:' + str(id) + ',message:' + msg + ')'
      raise IntegrityException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting goal association (id:' + str(id) + ',message:' + msg + ')'


  def addGoalDefinition(self,goalId,environmentName,goalDef):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalDefinition(%s,%s,%s)',(goalId,environmentName,goalDef))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating goal id ' + str(goalId) + ' with definition:' + goalDef
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalCategory(self,goalId,environmentName,goalCat):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalCategory(%s,%s,%s)',(goalId,environmentName,goalCat))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating goal id ' + str(goalId) + ' with category ' + goalCat
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalPriority(self,goalId,environmentName,goalPri):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalPriority(%s,%s,%s)',(goalId,environmentName,goalPri))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating goal id ' + str(goalId) + ' with priority ' + goalPri
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalFitCriterion(self,goalId,environmentName,goalFC):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalFitCriterion(%s,%s,%s)',(goalId,environmentName,goalFC))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating goal id ' + str(goalId) + ' with fit criterion: ' + goalFC
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalIssue(self,goalId,environmentName,goalIssue):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalIssue(%s,%s,%s)',(goalId,environmentName,goalIssue))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating goal id ' + str(goalId) + ' with issue: ' + goalIssue
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalRefinements(self,goalId,goalName,environmentName,goalAssociations,subGoalAssociations):
    for goal,goalDim,refinement,altName,rationale in subGoalAssociations:
      alternativeId = 0
      if (altName == 'Yes'):
        alternativeId = 1
      parameters = GoalAssociationParameters(environmentName,goalName,'goal',refinement,goal,goalDim,alternativeId,rationale)
      self.addGoalAssociation(parameters) 
    for goal,goalDim,refinement,altName,rationale in goalAssociations:
      alternativeId = 0
      if (altName == 'Yes'):
        alternativeId = 1
      parameters = GoalAssociationParameters(environmentName,goal,'goal',refinement,goalName,'goal',alternativeId,rationale)
      self.addGoalAssociation(parameters) 

  def addGoalConcernAssociations(self,goalId,environmentName,associations):
    for source,sourceMultiplicity,link,target,targetMultiplicity in associations:
      self.addGoalConcernAssociation(goalId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity) 

  def addGoalConcernAssociation(self,goalId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity):
    try:
      curs = self.conn.cursor()
      curs.execute('call addGoalConcernAssociation(%s,%s,%s,%s,%s,%s,%s)',(goalId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating concern with goal id ' + str(goalId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating concern with goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTaskConcernAssociations(self,taskId,environmentName,associations):
    for source,sourceMultiplicity,link,target,targetMultiplicity in associations:
      self.addTaskConcernAssociation(taskId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity) 

  def addTaskConcernAssociation(self,taskId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity):
    try:
      curs = self.conn.cursor()
      curs.execute('call addTaskConcernAssociation(%s,%s,%s,%s,%s,%s,%s)',(taskId,environmentName,source,sourceMultiplicity,link,target,targetMultiplicity))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating concern with task id ' + str(taskId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating concern with task id ' + str(taskId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addObstacleRefinements(self,goalId,goalName,environmentName,goalAssociations,subGoalAssociations):
    for goal,goalDim,refinement,altName,rationale in subGoalAssociations:
      alternativeId = 0
      if (altName == 'Yes'):
        alternativeId = 1
      parameters = GoalAssociationParameters(environmentName,goalName,'obstacle',refinement,goal,goalDim,alternativeId,rationale)
      self.addGoalAssociation(parameters) 
    for goal,goalDim,refinement,altName,rationale in goalAssociations:
      alternativeId = 0
      if (altName == 'Yes'):
        alternativeId = 1
      parameters = GoalAssociationParameters(environmentName,goal,goalDim,refinement,goalName,'obstacle',alternativeId,rationale)
      self.addGoalAssociation(parameters) 

  def addObstacleConcerns(self,obsId,environmentName,concerns):
    for concern in concerns:
      self.addObstacleConcern(obsId,environmentName,concern)

  def addObstacleConcern(self,obsId,environmentName,concern):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_obstacle_concern(%s,%s,%s)',(obsId,environmentName,concern))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error adding concern ' + concern + ' to obstacle id ' + str(obsId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding concern ' + concern + ' to obstacle id ' + str(obsId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addGoalConcerns(self,goalId,environmentName,concerns):
    for concern in concerns:
      if concern != '':
        self.addGoalConcern(goalId,environmentName,concern)

  def addGoalConcern(self,goalId,environmentName,concern):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_goal_concern(%s,%s,%s)',(goalId,environmentName,concern))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error adding concern ' + concern + ' to goal id ' + str(goalId) + ' in environment ' + environmentName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding concern ' + concern + ' to goal id ' + str(goalId) + ' in environment ' + environmentName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addAssetAssociations(self,assetId,assetName,environmentName,assetAssociations):
    for headNav,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailNav,tailAsset in assetAssociations:
      parameters = ClassAssociationParameters(environmentName,assetName,'asset',headNav,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailNav,'asset',tailAsset)
      self.addClassAssociation(parameters) 

  def addDomainAssociations(self,domainId,domainAssociations):
    for toDomain,domPhen,cDom in domainAssociations:
      self.addDomainAssociation(domainId,toDomain,domPhen,cDom) 

  def addDomainAssociation(self,domainId,toDomainName,domPhen,cDom):
    try:
      curs = self.conn.cursor()
      curs.execute('call add_domain_association(%s,%s,%s,%s)',(domainId,toDomainName,domPhen,cDom))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error adding domain association from domain id ' + str(domainId) + ' to domain ' + toDomainName
        raise DatabaseProxyException(exceptionText) 
      curs.close()

    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding domain association from domain id ' + str(domainId) + ' to domain ' + toDomainName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalLabel(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_label(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining label for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting label for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalDefinition(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_definition(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining definition for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting definition for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalCategory(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_category(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining category for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting category for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalPriority(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_priority(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining priority for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting priority for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalFitCriterion(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_fitcriterion(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining fit criterion for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting fit criterion for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalIssue(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select goal_issue(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining issue for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting issue for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalRefinements(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalRefinements(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining sub goal associations for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      goalRefinements = []
      for row in curs.fetchall():
        row = list(row)
        goalName = row[GOALASSOCIATIONS_GOAL_COL]
        aType = row[GOALASSOCIATIONS_TYPE_COL]
        goalDimName = row[GOALASSOCIATIONS_GOALDIM_COL]
        alternativeId = row[GOALASSOCIATIONS_ALTERNATIVE_COL]
        rationale = row[GOALASSOCIATIONS_RATIONALE_COL]
        altName = 'No'
        if (alternativeId == 1):
          altName = 'Yes'
        goalRefinements.append((goalName,goalDimName,aType,altName,rationale))
      curs.close()
      curs = self.conn.cursor()
      curs.execute('call subGoalRefinements(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining sub goal associations for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      subGoalRefinements = []
      for row in curs.fetchall():
        row = list(row)
        goalName = row[GOALASSOCIATIONS_SUBGOAL_COL]
        aType = row[GOALASSOCIATIONS_TYPE_COL]
        goalDimName = row[GOALASSOCIATIONS_SUBGOALDIM_COL]
        alternativeId = row[GOALASSOCIATIONS_ALTERNATIVE_COL]
        rationale = row[GOALASSOCIATIONS_RATIONALE_COL]
        altName = 'No'
        if (alternativeId == 1):
          altName = 'Yes'
        subGoalRefinements.append((goalName,goalDimName,aType,altName,rationale))
      curs.close()
      return goalRefinements,subGoalRefinements 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting sub goal associations for goal id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def assetAssociations(self,assetId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('call assetAssociations(%s,%s)',(assetId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining sub goal associations for goal id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      associations = []
      for row in curs.fetchall():
        row = list(row)
        headType = row[CLASSASSOCIATIONS_HEADTYPE_COL]
        headNav = row[CLASSASSOCIATIONS_HEADNAV_COL]
        headMult = row[CLASSASSOCIATIONS_HEADMULT_COL]
        headRole = row[CLASSASSOCIATIONS_HEADROLE_COL]
        tailRole = row[CLASSASSOCIATIONS_TAILROLE_COL]
        tailMult = row[CLASSASSOCIATIONS_TAILMULT_COL]
        tailNav = row[CLASSASSOCIATIONS_TAILNAV_COL]
        tailType = row[CLASSASSOCIATIONS_TAILTYPE_COL]
        tailName = row[CLASSASSOCIATIONS_TAIL_COL]
        associations.append((headNav,headType,headMult,headRole,tailRole,tailMult,tailType,tailNav,tailName))
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting associations for asset id ' + str(assetId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getDomainProperties(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDomainProperties(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining domainProperties'
        raise DatabaseProxyException(exceptionText) 
      dps = {}
      for row in curs.fetchall():
        row = list(row)
        dpId = row[0]
        dpName = row[1]
        dpDesc = row[2]
        dpType = row[3]
        dpOrig = row[4]
        parameters = DomainPropertyParameters(dpName,dpDesc,dpType,dpOrig)
        dp = ObjectFactory.build(dpId,parameters)
        dps[dpName] = dp
      curs.close() 
      return dps
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting domain properties (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDomainProperty(self,parameters):
    dpId = self.newId()
    dpName = parameters.name()
    dpDesc = parameters.description()
    dpType = parameters.type()
    dpOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call addDomainProperty(%s,%s,%s,%s,%s)',(dpId,dpName,dpDesc,dpType,dpOrig))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error adding new domain property ' + dpName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return dpId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding domain property ' + dpName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateDomainProperty(self,parameters):
    dpId = parameters.id()
    dpName = parameters.name()
    dpDesc = parameters.description()
    dpType = parameters.type()
    dpOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateDomainProperty(%s,%s,%s,%s,%s)',(dpId,dpName,dpDesc,dpType,dpOrig))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error updating domain property ' + dpName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return dpId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating domain property ' + dpName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteDomainProperty(self,dpId):
    self.deleteObject(dpId,'domainproperty')
    self.conn.commit()

  def getObstacles(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getObstacles(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining obstacles'
        raise DatabaseProxyException(exceptionText) 
      obstacles = {}
      obstacleRows = []
      for row in curs.fetchall():
        row = list(row)
        obsId = row[OBSTACLES_ID_COL]
        obsName = row[OBSTACLES_NAME_COL]
        obsOrig = row[OBSTACLES_ORIG_COL]
        obstacleRows.append((obsId,obsName,obsOrig))
      curs.close()

      for obsId,obsName,obsOrig in obstacleRows:
        environmentProperties = self.obstacleEnvironmentProperties(obsId)
        parameters = ObstacleParameters(obsName,obsOrig,environmentProperties)
        obstacle = ObjectFactory.build(obsId,parameters)
        obstacles[obsName] = obstacle
      return obstacles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting obstacles (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleEnvironmentProperties(self,obsId):
    try:
      environmentProperties = []
      for environmentId,environmentName in self.dimensionEnvironments(obsId,'obstacle'):
        obsLabel = self.obstacleLabel(obsId,environmentId)
        obsDef = self.obstacleDefinition(obsId,environmentId)
        obsType = self.obstacleCategory(obsId,environmentId)
        goalRefinements,subGoalRefinements = self.goalRefinements(obsId,environmentId)
        concerns = self.obstacleConcerns(obsId,environmentId)
        properties = ObstacleEnvironmentProperties(environmentName,obsLabel,obsDef,obsType,goalRefinements,subGoalRefinements,concerns)
        environmentProperties.append(properties) 
      return environmentProperties
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environmental properties for obstacle id ' + str(obsId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleDefinition(self,obsId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select obstacle_definition(%s,%s)',(obsId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining definition for obstacle id ' + str(obsId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      obsAttr = row[0] 
      curs.close()
      return obsAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting definition for obstacle id ' + str(obsId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleCategory(self,obsId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select obstacle_category(%s,%s)',(obsId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining category for obstacle id ' + str(obsId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      obsAttr = row[0] 
      curs.close()
      return obsAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting category for obstacle id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addObstacle(self,parameters):
    obsId = self.newId()
    obsName = parameters.name()
    obsOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call addObstacle(%s,%s,%s)',(obsId,obsName,obsOrig))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new obstacle ' + obsName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(obsId,'obstacle',environmentName)
        self.addObstacleDefinition(obsId,environmentName,environmentProperties.definition())
        self.addObstacleCategory(obsId,environmentName,environmentProperties.category())
        self.addObstacleRefinements(obsId,obsName,environmentName,environmentProperties.goalRefinements(),environmentProperties.subGoalRefinements())
        self.addObstacleConcerns(obsId,environmentName,environmentProperties.concerns())
      self.conn.commit()
      curs.close()
      return obsId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding obstacle ' + obsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateObstacle(self,parameters):
    obsId = parameters.id()
    obsName = parameters.name()
    obsOrig = parameters.originator()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteObstacleComponents(%s)',(obsId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating obstacle ' + obsName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateObstacle(%s,%s,%s)',(obsId,obsName,obsOrig))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating obstacle ' + obsName
        raise DatabaseProxyException(exceptionText) 
      for environmentProperties in parameters.environmentProperties():
        environmentName = environmentProperties.name()
        self.addDimensionEnvironment(obsId,'obstacle',environmentName)
        self.addObstacleDefinition(obsId,environmentName,environmentProperties.definition())
        self.addObstacleCategory(obsId,environmentName,environmentProperties.category())
        self.addObstacleRefinements(obsId,obsName,environmentName,environmentProperties.goalRefinements(),environmentProperties.subGoalRefinements())
        self.addObstacleConcerns(obsId,environmentName,environmentProperties.concerns())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating obstacle ' + obsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addObstacleDefinition(self,obsId,environmentName,obsDef):
    try:
      curs = self.conn.cursor()
      curs.execute('call addObstacleDefinition(%s,%s,%s)',(obsId,environmentName,obsDef))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating obstacle id ' + str(obsId) + ' with definition:' + obsDef
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with obstacle id ' + str(obsId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addObstacleCategory(self,obsId,environmentName,obsCat):
    try:
      curs = self.conn.cursor()
      curs.execute('call addObstacleCategory(%s,%s,%s)',(obsId,environmentName,obsCat))
      if (curs.rowcount == -1):
        exceptionText = 'Error associating obstacle id ' + str(obsId) + ' with category ' + obsCat
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating details with obstacle id ' + str(obsId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteObstacle(self,obsId):
    self.deleteObject(obsId,'obstacle')
    self.conn.commit()

  def updateSettings(self, projName, background, goals, scope, definitions, contributors,revisions,richPicture,fontSize = '7.5',fontName = 'Times New Roman'):
    try:
      curs = self.conn.cursor()
      curs.execute('call updateProjectSettings(%s,%s,%s,%s,%s,%s,%s)',(projName,background,goals,scope,richPicture,fontSize,fontName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating project settings'
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call deleteDictionary()')
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting project dictionary'
        raise DatabaseProxyException(exceptionText) 
      for entry in definitions:
        curs.execute('call addDictionaryEntry(%s,%s)',(entry[0],entry[1]))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding entry (' + entry[0] + ',' + entry[1] + ')'
          raise DatabaseProxyException(exceptionText) 
      curs.execute('call deleteContributors()')
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting project contributors'
        raise DatabaseProxyException(exceptionText) 
      for entry in contributors:
        curs.execute('call addContributorEntry(%s,%s,%s,%s)',(entry[0],entry[1],entry[2],entry[3]))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding contributor'
          raise DatabaseProxyException(exceptionText) 
      curs.execute('call deleteRevisions()')
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting project revisions'
        raise DatabaseProxyException(exceptionText) 
      for entry in revisions:
        curs.execute('call addRevision(%s,%s,%s)',(entry[0],entry[1],entry[2]))
        if (curs.rowcount == -1):
          exceptionText = 'Error adding revision'
          raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating project settings (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getProjectSettings(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getProjectSettings()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting project settings'
        raise DatabaseProxyException(exceptionText) 
      pSettings = {}
      for row in curs.fetchall():
        row = list(row)
        pSettings[row[0]] = row[1]
      curs.close()
      return pSettings
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting project settings (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
  
  def getDictionary(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDictionary()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting project naming conventions'
        raise DatabaseProxyException(exceptionText) 
      pDict = {}
      for row in curs.fetchall():
        row = list(row)
        pDict[row[0]] = row[1]
      curs.close()
      return pDict
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting naming conventions (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getContributors(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getContributors()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting project naming conventions'
        raise DatabaseProxyException(exceptionText) 
      contributors = []
      for row in curs.fetchall():
        row = list(row)
        contributors.append((row[0],row[1],row[2],row[3]))
      curs.close()
      return contributors
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting naming conventions (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRevisions(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRevisions()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting project revisions'
        raise DatabaseProxyException(exceptionText) 
      revisions = []
      for row in curs.fetchall():
        row = list(row)
        revisions.append((row[0],row[1],row[2]))
      curs.close()
      return revisions
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting revisions (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRequirementVersions(self,reqId):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRequirementVersions(%s)',(reqId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting requirement versions'
        raise DatabaseProxyException(exceptionText) 
      revisions = []
      for row in curs.fetchall():
        row = list(row)
        revisions.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
      curs.close()
      return revisions
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting requirement versions (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDomain(self,parameters):
    domainId = self.newId()
    modName = parameters.name()
    modShortCode = parameters.shortCode()
    modDesc = parameters.description()
    domType = parameters.type()
    givenIndicator = parameters.given()
    try:
      curs = self.conn.cursor()
      curs.execute('call addDomain(%s,%s,%s,%s,%s,%s)',(domainId,modName,modShortCode,modDesc,domType,givenIndicator))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new requirement module ' + modName
        raise DatabaseProxyException(exceptionText) 
      self.addDomainAssociations(domainId,parameters.domains())
      self.conn.commit()
      curs.close()
      return domainId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding requirement module ' + modName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateDomain(self,parameters):
    domainId = parameters.id()
    modName = parameters.name()
    modShortCode = parameters.shortCode()
    modDesc = parameters.description()
    domType = parameters.type()
    givenIndicator = parameters.given()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteDomainComponents(%s)',(domainId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating domain ' + modName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateDomain(%s,%s,%s,%s,%s,%s)',(domainId,modName,modShortCode,modDesc,domType,givenIndicator))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating requirement module ' + modName
        raise DatabaseProxyException(exceptionText) 
      self.addDomainAssociations(domainId,parameters.domains())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating requirement module ' + modName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteDomain(self,r):
    self.deleteObject(r,'domain')
    self.conn.commit()

  def contextModelElements(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call contextModelElements(%s)',envName)
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining context model elements'
        raise DatabaseProxyException(exceptionText) 
      else:
        elements = []
        for row in curs.fetchall():
          row = list(row)
          elements.append((row[0],row[1]))
        curs.close()
        return elements
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting class model elements associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def exposedDomains(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call exposedDomains(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining domains exposed by environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        doms = []
        for row in curs.fetchall():
          row = list(row)
          doms.append(row[0])
        curs.close()
        return doms
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting domains exposed by environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def existingResponseGoal(self,responseId):
    try:
      curs = self.conn.cursor()
      curs.execute('select existingResponseGoal(%s)',(responseId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goal associated with response id ' + str(responseId)
        raise DatabaseProxyException(exceptionText) 
      else:
        row = curs.fetchone()
        row = list(row)
        isExisting = int(row[0])
        curs.close()
        return isExisting
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting domains exposed by environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getValueTypes(self,dimName,envName = ''):
    try:
      customisableValues = set(['asset_value','threat_value','risk_class','countermeasure_value','capability','motivation','asset_type','threat_type','vulnerability_type','severity','likelihood'])
      if (dimName not in customisableValues):
        exceptionText = 'Values for ' + dimName + ' are not customisable.'
        raise DatabaseProxyException(exceptionText) 
      curs = self.conn.cursor()
      curs.execute('call getCustomisableValues(%s,%s)',(dimName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goal associated with response id ' + str(responseId)
        raise DatabaseProxyException(exceptionText) 
      else:
        values = []
        for row in curs.fetchall():
          row = list(row)
          typeId = row[0]
          typeName = row[1]
          typeDesc = row[2]
          parameters = ValueTypeParameters(typeName,typeDesc,dimName,envName)
          objt = ObjectFactory.build(typeId,parameters)
          values.append(objt)
        curs.close()
        return values
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting customisable values for ' + dimName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteCapability(self,objtId):
    self.deleteObject(objtId,'capability')

  def deleteCapability(self,objtId):
    self.deleteObject(objtId,'capability')
    self.conn.commit()

  def deleteMotivation(self,objtId):
    self.deleteObject(objtId,'motivation')
    self.conn.commit()

  def deleteAssetType(self,objtId):
    self.deleteObject(objtId,'asset_type')
    self.conn.commit()

  def deleteThreatType(self,objtId):
    self.deleteObject(objtId,'threat_type')
    self.conn.commit()

  def deleteVulnerabilityType(self,objtId):
    self.deleteObject(objtId,'vulnerability_type')
    self.conn.commit()

  def addValueType(self,parameters):
    if (parameters.id() != -1):
      valueTypeId = parameters.id()
    else:
      valueTypeId = self.newId()
    vtName = parameters.name()
    vtDesc = parameters.description()
    vtType = parameters.type()
    if ((vtType == 'asset_value') or (vtType == 'threat_value') or (vtType == 'risk_class') or (vtType == 'countermeasure_value')):
      exceptionText = 'Cannot add ' + vtType + 's'
      raise DatabaseProxyException(exceptionText) 

    try:
      curs = self.conn.cursor()
      curs.execute('call addValueType(%s,%s,%s,%s)',(valueTypeId,vtName,vtDesc,vtType))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding ' + vtType + ' ' + vtName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return valueTypeId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding ' + vtType + ' ' + vtName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateValueType(self,parameters):
    valueTypeId = parameters.id()
    vtName = parameters.name()
    vtDesc = parameters.description()
    vtType = parameters.type()
    envName = parameters.environment()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateValueType(%s,%s,%s,%s,%s)',(valueTypeId,vtName,vtDesc,vtType,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating ' + vtType + ' ' + vtName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating ' + vtType + ' ' + vtName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def threatTypes(self,envName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call threatTypes(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting threat types'
        raise DatabaseProxyException(exceptionText) 
      stats = {}
      for row in curs.fetchall():
        row = list(row)
        stats[row[0]] = row[1]
        curs.close()
      return stats
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting threat statistics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskScatter(self,envName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call getRiskElements(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting threat types'
        raise DatabaseProxyException(exceptionText) 
      xPoints = []
      yPoints = []
      riskDetails = []
      for row in curs.fetchall():
        row = list(row)
        riskDetails.append((row[0],row[1],row[2]))
        xPoints.append(row[3])
        yPoints.append(row[4])
        curs.close()

      scores = []
      for risk,threat,vulnerability in riskDetails:
        scoreDetails = self.riskScore(threat,vulnerability,envName,risk)
        highestScore = 0
        for resp,preScore,postScore,details in scoreDetails:
          if (postScore > highestScore):
            highestScore = postScore
        scores.append(highestScore)
      return xPoints,yPoints,scores
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting threat statistics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def inheritedAssetProperties(self,assetId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    syProperties,pRationale = self.relatedProperties('asset',assetId,environmentId)
    assetAssociations = self.assetAssociations(assetId,environmentId)
    return AssetEnvironmentProperties(environmentName,syProperties,pRationale,assetAssociations)

  def inheritedAttackerProperties(self,attackerId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    roles = self.dimensionRoles(attackerId,environmentId,'attacker')
    capabilities = self.attackerCapabilities(attackerId,environmentId)
    motives = self.attackerMotives(attackerId,environmentId)
    return AttackerEnvironmentProperties(environmentName,roles,motives,capabilities)

  def inheritedThreatProperties(self,threatId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    likelihood = self.threatLikelihood(threatId,environmentId)
    assets = self.threatenedAssets(threatId,environmentId) 
    attackers = self.threatAttackers(threatId,environmentId)
    syProperties,pRationale = self.relatedProperties('threat',threatId,environmentId)
    return ThreatEnvironmentProperties(environmentName,likelihood,assets,attackers,syProperties,pRationale)

  def inheritedVulnerabilityProperties(self,vulId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    severity = self.vulnerabilitySeverity(vulId,environmentId)
    assets = self.vulnerableAssets(vulId,environmentId)
    return VulnerabilityEnvironmentProperties(environmentName,severity,assets)

  def inheritedTaskProperties(self,taskId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    dependencies = self.taskDependencies(taskId,environmentId)
    personas = self.taskPersonas(taskId,environmentId)
    assets = self.taskAssets(taskId,environmentId)
    concs = self.taskConcernAssociations(taskId,environmentId)
    narrative = self.taskNarrative(taskId,environmentId)
    return TaskEnvironmentProperties(environmentName,dependencies,personas,assets,concs,narrative)

  def inheritedUseCaseProperties(self,ucId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    preConds,postConds = self.useCaseConditions(ucId,environmentId)
    ucSteps = self.useCaseSteps(ucId,environmentId)
    return UseCaseEnvironmentProperties(environmentName,preConds,ucSteps,postConds)

  def inheritedGoalProperties(self,goalId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    goalDef = self.goalDefinition(goalId,environmentId)
    goalType = self.goalCategory(goalId,environmentId)
    goalPriority = self.goalPriority(goalId,environmentId)
    goalFitCriterion = self.goalFitCriterion(goalId,environmentId)
    goalIssue = self.goalIssue(goalId,environmentId) 
    concs = self.goalConcerns(goalId,environmentId)
    cas = self.goalConcernAssociations(goalId,environmentId)
    goalRefinements,subGoalRefinements = self.goalRefinements(goalId,environmentId)
    return GoalEnvironmentProperties(environmentName,'',goalDef,goalType,goalPriority,goalFitCriterion,goalIssue,goalRefinements,subGoalRefinements,concs,cas)

  def inheritedObstacleProperties(self,obsId,environmentName):
    environmentId = self.getDimensionId(environmentName,'environment')
    obsDef = self.obstacleDefinition(obsId,environmentId)
    obsType = self.obstacleCategory(obsId,environmentId)
    goalRefinements,subGoalRefinements = self.goalRefinements(obsId,environmentId)
    return ObstacleEnvironmentProperties(environmentName,'',obsDef,obsType,goalRefinements,subGoalRefinements)

  def getVulnerabilityDirectory(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getVulnerabilityDirectory()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting vulnerability directory'
        raise DatabaseProxyException(exceptionText) 
      directoryList = []
      for row in curs.fetchall():
        row = list(row)
        vLabel = row[0]
        vName = row[1]
        vDesc = row[2]
        vType = row[3]
        vRef = row[4]
        directoryList.append((vLabel,vName,vDesc,vType,vRef))
      curs.close()
      return directoryList
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting vulnerability directory (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getThreatDirectory(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call getThreatDirectory()')
      if (curs.rowcount == -1):
        exceptionText = 'Error getting threat directory'
        raise DatabaseProxyException(exceptionText) 
      directoryList = []
      for row in curs.fetchall():
        row = list(row)
        directoryList.append((row[0],row[1],row[2],row[3],row[4]))
      curs.close()
      return directoryList
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting threat directory (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def reassociateAsset(self,assetName,envName,reqId):
    try:
      curs = self.conn.cursor()
      curs.execute('call reassociateAsset(%s,%s,%s)',(assetName,envName,reqId))
      if (curs.rowcount == -1):
        exceptionText = 'Error re-associating requirement id ' + str(reqId) + ' with asset ' + assetName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error re-associating requirement id ' + str(reqId) + ' with asset ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleConcerns(self,obsId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call obstacleConcerns(%s,%s)',(obsId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concerns for obstacle id ' + str(obsId) + ' in environment id ' + str(envId)
        raise DatabaseProxyException(exceptionText) 
      else:
        assets = []
        for row in curs.fetchall():
          row = list(row)
          assets.append(row[0])
        curs.close()
        return assets
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concerns for obstacle id ' + str(obsId) + ' in environment id ' + str(envId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalConcerns(self,goalId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalConcerns(%s,%s)',(goalId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concerns for goal id ' + str(goalId) + ' in environment id ' + str(envId)
        raise DatabaseProxyException(exceptionText) 
      else:
        concs = []
        for row in curs.fetchall():
          row = list(row)
          concs.append(row[0])
        curs.close()
        return concs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concerns for goal id ' + str(goalId) + ' in environment id ' + str(envId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalConcernAssociations(self,goalId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalConcernAssociations(%s,%s)',(goalId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concern associations for goal id ' + str(goalId) + ' in environment id ' + str(envId)
        raise DatabaseProxyException(exceptionText) 
      else:
        cas = []
        for row in curs.fetchall():
          row = list(row)
          cas.append((row[0],row[1],row[2],row[3],row[4]))
        curs.close()
        return cas
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concern associations for goal id ' + str(goalId) + ' in environment id ' + str(envId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def taskConcernAssociations(self,taskId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskConcernAssociations(%s,%s)',(taskId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concern associations for task id ' + str(taskId) + ' in environment id ' + str(envId)
        raise DatabaseProxyException(exceptionText) 
      else:
        cas = []
        for row in curs.fetchall():
          row = list(row)
          cas.append((row[0],row[1],row[2],row[3],row[4]))
        curs.close()
        return cas
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concern associations for task id ' + str(taskId) + ' in environment id ' + str(envId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getDependencies(self,constraintId = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDependencies(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining dependencies'
        raise DatabaseProxyException(exceptionText) 
      dependencies = {}
      for row in curs.fetchall():
        row = list(row)
        depId = row[DEPENDENCIES_ID_COL]
        envName = row[DEPENDENCIES_ENV_COL]
        depender = row[DEPENDENCIES_DEPENDER_COL]
        dependee = row[DEPENDENCIES_DEPENDEE_COL]
        dType = row[DEPENDENCIES_DTYPE_COL]
        dependencyName = row[DEPENDENCIES_DEPENDENCY_COL]
        rationale = row[DEPENDENCIES_RATIONALE_COL]
        parameters = DependencyParameters(envName,depender,dependee,dType,dependencyName,rationale)
        dependency = ObjectFactory.build(depId,parameters)
        dLabel = envName + '/' + depender + '/' + dependee + '/' + dependencyName
        dependencies[dLabel] = dependency
      curs.close()
      return dependencies
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting dependencies (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDependency(self,parameters):
    depId = self.newId()
    envName = parameters.environment()
    depender = parameters.depender()
    dependee = parameters.dependee()
    dType = parameters.dependencyType()
    dependencyName = parameters.dependency()
    rationale = parameters.rationale()
    try:
      curs = self.conn.cursor()
#      print 'call addDependency(',depId,',',envName,',',depender,',',dependee,',',dType,',',dependencyName,',',rationale,')'
      curs.execute('call addDependency(%s,%s,%s,%s,%s,%s,%s)',(depId,envName,depender,dependee,dType,dependencyName,rationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new dependency ' + envName + '/' + depender + '/' + dependee
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return depId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding new dependency ' + envName + '/' + depender + '/' + dependee + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def updateDependency(self,parameters):
    depId = parameters.id()
    envName = parameters.environment()
    depender = parameters.depender()
    dependee = parameters.dependee()
    dType = parameters.dependencyType()
    dependencyName = parameters.dependency()
    rationale = parameters.rationale()
    try:
      curs = self.conn.cursor()
#      print 'call updateDependency(',depId,',',envName,',',depender,',',dependee,',',dType,',',dependencyName,',',rationale,')'
      curs.execute('call updateDependency(%s,%s,%s,%s,%s,%s,%s)',(depId,envName,depender,dependee,dType,dependencyName,rationale))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating dependency ' + envName + '/' + depender + '/' + dependee
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating dependency ' + envName + '/' + depender + '/' + dependee + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteDependency(self,depId,depType):
    try:
      curs = self.conn.cursor()
      curs.execute('call delete_dependency(%s,%s)',(depId,depType))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting dependency id ' + str(depId)
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.IntegrityError, e:
      id,msg = e
      exceptionText = 'Cannot remove dependency due to dependent data.  Check the responsibility model for further information  (id:' + str(id) + ',message:' + msg + ')'
      raise IntegrityException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting dependency id ' + str(depId) + ' (id:' + str(id) + ',message:' + msg + ')'

  def getDependencyTable(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call dependencyTable(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting dependency table for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      depRows = []
      for row in curs.fetchall():
        row = list(row)
        depender = row[0]
        dependee = row[1]
        depType = row[2]
        dependency = row[3]
        rationale = row[4]
        depRows.append((depender,dependee,depType,dependency,rationale))
      curs.close()
      return depRows
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error building dependency table for environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'

  def getDependencyTables(self):
    envs = self.getEnvironmentNames()
    deps = {}
    curs = self.conn.cursor()
    for env in envs:
      depRows = self.getDependencyTable(env)
      if (len(depRows) > 0):
        deps[env] = self.getDependencyTable(env)
    return deps

  def reportAssociationDependencies(self,fromAsset,toAsset,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call associationDependencyCheck(%s,%s,%s)',(fromAsset,toAsset,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting association dependencies between ' + fromAsset + ' and ' + toAsset + ' in environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        return []
      else:
        deps = []
        for row in curs.fetchall():
          row = list(row)
          deps.append(row[0])
        curs.close()
        return deps
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting association dependencies between ' + fromAsset + ' and ' + toAsset + ' in environment ' + envName + ' id ' + str(objtId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def reportAssociationTargetDependencies(self,assetProperties,toAsset,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call associationTargetDependencyCheck(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(assetProperties[0],assetProperties[1],assetProperties[2],assetProperties[3],assetProperties[4],assetProperties[5],assetProperties[6],assetProperties[7],toAsset,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting association dependencies between the current asset and ' + toAsset + ' in environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      elif (curs.rowcount == 0):
        return []
      else:
        deps = []
        for row in curs.fetchall():
          row = list(row)
          deps.append(row[0])
        curs.close()
        return deps
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting association dependencies between the current asset and ' + toAsset + ' in environment ' + envName + ' id ' + str(objtId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTemplateAsset(self,parameters):
    assetId = parameters.id()
    if (assetId == -1):
      assetId = self.newId()

    assetName = parameters.name()
    shortCode = parameters.shortCode()
    assetDesc = parameters.description()
    assetSig = parameters.significance()
    assetType = parameters.type()
    assetCriticality = parameters.critical()
    assetCriticalRationale = parameters.criticalRationale()
    cProperty = parameters.confidentialityProperty()
    iProperty = parameters.integrityProperty()
    avProperty = parameters.availabilityProperty()
    acProperty = parameters.accountabilityProperty()
    anProperty = parameters.anonymityProperty()
    panProperty = parameters.pseudonymityProperty()
    unlProperty = parameters.unlinkabilityProperty()
    unoProperty = parameters.unobservabilityProperty()
    try:
      curs = self.conn.cursor()
      curs.execute('call addTemplateAsset(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(assetId,assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale,cProperty,iProperty,avProperty,acProperty,anProperty,panProperty,unlProperty,unoProperty))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new asset ' + assetName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return assetId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding template asset ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateTemplateAsset(self,parameters):
    assetId = parameters.id()
    assetName = parameters.name()
    shortCode = parameters.shortCode()
    assetDesc = parameters.description()
    assetSig = parameters.significance()
    assetType = parameters.type()
    assetCriticality = parameters.critical()
    assetCriticalRationale = parameters.criticalRationale()
    cProperty = parameters.confidentialityProperty()
    iProperty = parameters.integrityProperty()
    avProperty = parameters.availabilityProperty()
    acProperty = parameters.accountabilityProperty()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateTemplateAsset(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(assetId,assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale,cProperty,iProperty,avProperty,acProperty))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new asset ' + assetName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return assetId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating template asset ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getTemplateAssets(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getTemplateAssets(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining assets'
        raise DatabaseProxyException(exceptionText) 
      templateAssets = {}
      for row in curs.fetchall():
        row = list(row)
        assetName = row[ASSETS_NAME_COL]
        shortCode = row[ASSETS_SHORTCODE_COL]
        assetId = row[ASSETS_ID_COL]
        assetDesc = row[ASSETS_DESCRIPTION_COL]
        assetSig = row[ASSETS_SIGNIFICANCE_COL]
        assetType = row[ASSETS_TYPE_COL]
        assetCriticality = row[ASSETS_CRITICAL_COL]
        assetCriticalRationale = row[ASSETS_CRITICALRATIONALE_COL]
        cProperty = row[TEMPLATEASSETS_CPROPERTY_COL]
        iProperty = row[TEMPLATEASSETS_IPROPERTY_COL]
        avProperty = row[TEMPLATEASSETS_AVPROPERTY_COL]
        acProperty = row[TEMPLATEASSETS_ACPROPERTY_COL]
        anProperty = row[TEMPLATEASSETS_ANPROPERTY_COL]
        panProperty = row[TEMPLATEASSETS_PANPROPERTY_COL]
        unlProperty = row[TEMPLATEASSETS_UNLPROPERTY_COL]
        unoProperty = row[TEMPLATEASSETS_UNOPROPERTY_COL]
        parameters = TemplateAssetParameters(assetName,shortCode,assetDesc,assetSig,assetType,assetCriticality,assetCriticalRationale,cProperty,iProperty,avProperty,acProperty,anProperty,panProperty,unlProperty,unoProperty)
        templateAsset = ObjectFactory.build(assetId,parameters)
        templateAssets[assetName] = templateAsset
      return templateAssets
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting template assets (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteTemplateAsset(self,assetId):
    self.deleteObject(assetId,'template_asset')
    self.conn.commit()

  def deleteSecurityPattern(self,patternId):
    self.deleteObject(patternId,'securitypattern')
    self.conn.commit()

  def getSecurityPatterns(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getSecurityPatterns(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining security patterns'
        raise DatabaseProxyException(exceptionText) 
      patterns = {}
      patternRows = []
      for row in curs.fetchall():
        row = list(row)
        patternId = row[SECURITYPATTERN_ID_COL]
        patternName = row[SECURITYPATTERN_NAME_COL]
        patternContext = row[SECURITYPATTERN_CONTEXT_COL]
        patternProblem = row[SECURITYPATTERN_PROBLEM_COL]
        patternSolution = row[SECURITYPATTERN_SOLUTION_COL]
        patternRows.append((patternId,patternName,patternContext,patternProblem,patternSolution))
      curs.close()
      for patternId,patternName,patternContext,patternProblem,patternSolution in patternRows:
        patternStructure = self.patternStructure(patternId)
        patternReqs = self.patternRequirements(patternId)
        parameters = SecurityPatternParameters(patternName,patternContext,patternProblem,patternSolution,patternReqs,patternStructure)
        pattern = ObjectFactory.build(patternId,parameters)
        patterns[patternName] = pattern
      return patterns
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting security patterns (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def patternStructure(self,patternId):
    try:
      curs = self.conn.cursor()
      curs.execute('call getSecurityPatternStructure(%s)',(patternId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining security pattern structure'
        raise DatabaseProxyException(exceptionText) 
      pStruct = []
      for row in curs.fetchall():
        row = list(row)
        pStruct.append((row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
      curs.close()
      return pStruct
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting structure for pattern id ' + str(patternId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def patternRequirements(self,patternId):
    try:
      curs = self.conn.cursor()
      curs.execute('call getSecurityPatternRequirements(%s)',(patternId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining security pattern requirements'
        raise DatabaseProxyException(exceptionText) 
      pStruct = []
      for row in curs.fetchall():
        row = list(row)
        reqType = row[0]
        reqName = row[1]
        reqDesc = row[2]
        reqRationale = row[3]
        reqFc = row[4]
        reqAsset = row[5]
        pStruct.append((reqName,reqDesc,reqType,reqRationale,reqFc,reqAsset))
      curs.close()
      return pStruct
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting requirements for pattern id ' + str(patternId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 



  def addSecurityPattern(self,parameters):
    patternId = parameters.id()
    if (patternId == -1):
      patternId = self.newId()
    patternName = parameters.name()
    patternContext = parameters.context()
    patternProblem = parameters.problem()
    patternSolution = parameters.solution()
    patternStructure = parameters.associations()
    patternRequirements = parameters.requirements()
    try:
      curs = self.conn.cursor()
      curs.execute('call addSecurityPattern(%s,%s,%s,%s,%s)',(patternId,patternName,patternContext,patternProblem,patternSolution))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding security pattern ' + patternName
        raise DatabaseProxyException(exceptionText) 
      self.addPatternStructure(patternId,patternStructure)
      self.addPatternRequirements(patternId,patternRequirements)
      self.conn.commit()
      curs.close()
      return patternId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding security pattern ' + patternName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateSecurityPattern(self,parameters):
    patternId = parameters.id()
    patternName = parameters.name()
    patternContext = parameters.context()
    patternProblem = parameters.problem()
    patternSolution = parameters.solution()
    patternStructure = parameters.associations()
    patternRequirements = parameters.requirements()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteSecurityPatternComponents(%s)',(patternId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating security pattern ' + patternName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateSecurityPattern(%s,%s,%s,%s,%s)',(patternId,patternName,patternContext,patternProblem,patternSolution))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating security pattern ' + patternName
        raise DatabaseProxyException(exceptionText) 
      self.addPatternStructure(patternId,patternStructure)
      self.addPatternRequirements(patternId,patternRequirements)
      self.conn.commit()
      curs.close()
      return patternId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating security pattern  ' + patternName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addPatternStructure(self,patternId,patternStructure):
    for headAsset,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailAsset in patternStructure:
      self.addPatternAssetAssociation(patternId,headAsset,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailAsset)

  def addPatternRequirements(self,patternId,patternRequirements):
    for idx,reqData in enumerate(patternRequirements):
      self.addPatternRequirement(idx+1,patternId,reqData[0],reqData[1],reqData[2],reqData[3],reqData[4],reqData[5])

  def addPatternRequirement(self,reqLabel,patternId,reqName,reqDesc,reqType,reqRationale,reqFC,reqAsset):
    try:
      curs = self.conn.cursor()
      curs.execute('call addSecurityPatternRequirement(%s,%s,%s,%s,%s,%s,%s,%s)',(reqLabel,patternId,reqType,reqName,reqDesc,reqRationale,reqFC,reqAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding requirement to pattern id ' + str(patternId) 
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding requirement to pattern id ' + str(patternId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addPatternAssetAssociation(self,patternId,headAsset,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailAsset):
    assocId = self.newId()
    try:
      curs = self.conn.cursor()
      curs.execute('call addSecurityPatternStructure(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(assocId,patternId,headAsset,headAdornment,headNry,headRole,tailRole,tailNry,tailAdornment,tailAsset))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding structure to pattern id ' + str(patternId) 
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding structure to pattern id ' + str(patternId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def patternAssets(self,patternId):
    try:
      curs = self.conn.cursor()
      curs.execute('call securityPatternAssets(%s)',(patternId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining assets associated with pattern id ' + str(patternId)
        raise DatabaseProxyException(exceptionText) 
      assets = []
      for row in curs.fetchall():
        row = list(row)
        assets.append(row[0])
      curs.close()
      return assets
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assets associated with pattern id ' + str(patternId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addSituatedAssets(self,patternId,assetParametersList):
    for assetParameters in assetParametersList:
      assetId = self.addAsset(assetParameters)
      self.situatePatternAsset(patternId,assetId)

  def situatePatternAsset(self,patternId,assetId):
    try:
      curs = self.conn.cursor()
      curs.execute('call situatePatternAsset(%s,%s)',(assetId,patternId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error situating asset id ' + str(assetId) 
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error situating asset id ' + str(assetId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def isCountermeasureAssetGenerated(self,cmId):
    try:
      curs = self.conn.cursor()
      curs.execute('select isCountermeasureAssetGenerated(%s)',(cmId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error checking assets associated with countermeasure id ' + str(cmId) 
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      isGenerated = row[0]
      curs.close()
      return isGenerated
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error checking assets associated with countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def isCountermeasurePatternGenerated(self,cmId):
    try:
      curs = self.conn.cursor()
      curs.execute('select isCountermeasurePatternGenerated(%s)',(cmId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error checking patterns associated with countermeasure id ' + str(cmId) 
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      isGenerated = row[0]
      curs.close()
      return isGenerated
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error checking patterns associated with countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def exposedCountermeasures(self,parameters):
    objtId = parameters.id()
    expCMs = []
    for cProperties in parameters.environmentProperties():
      envName = cProperties.name()
      expAssets = cProperties.assets()
      for expAsset in expAssets:
        expCMs += self.exposedCountermeasure(envName,expAsset)
    return expCMs

  def exposedCountermeasure(self,envName,assetName):
    try:
      curs = self.conn.cursor()
      curs.execute('call exposedCountermeasure(%s,%s)',(envName,assetName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error get countermeasures exposed by ' + assetName 
        raise DatabaseProxyException(exceptionText) 
      expCMs = []
      for row in curs.fetchall():
        row = list(row)
        expCMs.append((envName,row[0],assetName,row[1]))
      curs.close()
      return expCMs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting countermeasures exposed by ' + assetName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
  
  def updateCountermeasuresEffectiveness(self,objtId,dimName,expCMs):
    for envName,cmName,assetName,cmEffectiveness in expCMs:
      self.updateCountermeasureEffectiveness(objtId,dimName,cmName,assetName,envName,cmEffectiveness) 

  def updateCountermeasureEffectiveness(self,objtId,dimName,cmName,assetName,envName,cmEffectiveness):
    try:
      curs = self.conn.cursor()
      curs.execute('call updateCountermeasureEffectiveness(%s,%s,%s,%s,%s,%s)',(objtId,dimName,cmName,assetName,envName,cmEffectiveness))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error updating effectiveness of countermeasure ' + cmName 
        raise DatabaseProxyException(exceptionText) 
      expCMs = []
      for row in curs.fetchall():
        row = list(row)
        expCMs.append((envName,row[0],assetName,row[1]))
      curs.close()
      return expCMs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating effectiveness of countermeasure ' + cmName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def countermeasurePatterns(self,cmId):
    try:
      curs = self.conn.cursor()
      curs.execute('call countermeasurePatterns(%s)',cmId)
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error getting patterns associated with countermeasure id ' + str(cmId)
        raise DatabaseProxyException(exceptionText) 
      patterns = []
      for row in curs.fetchall():
        row = list(row)
        patterns.append(row[0])
      curs.close()
      return patterns
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting patterns associated with countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteSituatedPattern(self,cmId,patternName):
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteSituatedPattern(%s,%s)',(cmId,patternName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error deletint pattern ' + patternName + ' associated with countermeasure id ' + str(cmId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
      self.conn.commit()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting pattern ' + patternName  + ' associated with countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def candidateCountermeasurePatterns(self,cmId):
    try:
      curs = self.conn.cursor()
      curs.execute('call candidateCountermeasurePatterns(%s)',cmId)
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error getting potential patterns associated with countermeasure id ' + str(cmId)
        raise DatabaseProxyException(exceptionText) 
      patterns = []
      for row in curs.fetchall():
        row = list(row)
        patterns.append(row[0])
      curs.close()
      return patterns
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting potential patterns associated with countermeasure id ' + str(cmId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def associateCountermeasureToPattern(self,cmId,patternName):
    try:
      curs = self.conn.cursor()
      curs.execute('call associateCountermeasureToPattern(%s,%s)',(cmId,patternName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error associating countermeasure id ' + str(cmId) + ' with pattern ' + patternName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating countermeasure id ' + str(cmId) + 'with pattern ' + patternName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def nameCheck(self,objtName,dimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call nameExists(%s,%s)',(objtName,dimName))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error checking existence of ' + dimName + ' ' + objtName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      objtCount = row[0]
      curs.close()
      if (objtCount > 0):
        exceptionText = dimName + ' ' + objtName + ' already exists.'
        raise ARMException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error checking existence of ' + dimName + ' ' + objtName + ' (id:' + str(id) + ',message:' + msg + ')'

  def getExternalDocuments(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getExternalDocuments(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining external documents'
        raise DatabaseProxyException(exceptionText) 
      eDocs = {}
      for row in curs.fetchall():
        row = list(row)
        docId = row[EXTERNALDOCUMENT_ID_COL]
        docName = row[EXTERNALDOCUMENT_NAME_COL]
        docVersion = row[EXTERNALDOCUMENT_VERSION_COL]
        docPubDate = row[EXTERNALDOCUMENT_PUBDATE_COL]
        docAuthors = row[EXTERNALDOCUMENT_AUTHORS_COL]
        docDesc = row[EXTERNALDOCUMENT_DESCRIPTION_COL]
        parameters = ExternalDocumentParameters(docName,docVersion,docPubDate,docAuthors,docDesc)
        eDoc = ObjectFactory.build(docId,parameters)
        eDocs[docName] = eDoc
      return eDocs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting external documents (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getDocumentReferences(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDocumentReferences(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining document references'
        raise DatabaseProxyException(exceptionText) 
      dRefs = {}
      for row in curs.fetchall():
        row = list(row)
        refId = row[DOCUMENTREFERENCE_ID_COL]
        refName = row[DOCUMENTREFERENCE_NAME_COL]
        docName = row[DOCUMENTREFERENCE_DOCNAME_COL]
        cName = row[DOCUMENTREFERENCE_CNAME_COL]
        excerpt = row[DOCUMENTREFERENCE_EXCERPT_COL]
        parameters = DocumentReferenceParameters(refName,docName,cName,excerpt)
        dRef = ObjectFactory.build(refId,parameters)
        dRefs[refName] = dRef
      return dRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting document references (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getExternalDocumentReferences(self,docName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call getDocumentReferencesByExternalDocument(%s)',(docName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining document references for external document ' + docName
        raise DatabaseProxyException(exceptionText) 
      dRefs = {}
      for row in curs.fetchall():
        row = list(row)
        refId = row[DOCUMENTREFERENCE_ID_COL]
        refName = row[DOCUMENTREFERENCE_NAME_COL]
        docName = row[DOCUMENTREFERENCE_DOCNAME_COL]
        cName = row[DOCUMENTREFERENCE_CNAME_COL]
        excerpt = row[DOCUMENTREFERENCE_EXCERPT_COL]
        parameters = DocumentReferenceParameters(refName,docName,cName,excerpt)
        dRef = ObjectFactory.build(refId,parameters)
        dRefs[refName] = dRef
      return dRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting document references for external document ' + docName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonaDocumentReferences(self,personaName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getPersonaDocumentReferences(%s)',(personaName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining document references for persona ' + personaName
        raise DatabaseProxyException(exceptionText) 
      dRefs = []
      for row in curs.fetchall():
        row = list(row)
        refName = row[0]
        docName = row[1]
        excerpt = row[2]
        dRefs.append((refName,docName,excerpt))
      return dRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting document references for persona ' + personaName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonaConceptReferences(self,personaName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getPersonaConceptReferences(%s)',(personaName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining document references for persona ' + personaName
        raise DatabaseProxyException(exceptionText) 
      dRefs = []
      for row in curs.fetchall():
        row = list(row)
        refName = row[0]
        cType = row[1]
        cName = row[2]
        excerpt = row[3]
        dRefs.append((refName,cType,cName,excerpt))
      return dRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting document references for persona ' + personaName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonaExternalDocuments(self,personaName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getPersonaExternalDocuments(%s)',(personaName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining external documents for persona ' + personaName
        raise DatabaseProxyException(exceptionText) 
      edRefs = []
      for row in curs.fetchall():
        row = list(row)
        docName = row[0]
        docVer = row[1]
        docAuthors = row[2]
        docDate = row[3]
        docDesc = row[4]
        edRefs.append((docName,docVer,docAuthors,docDate,docDesc))
      return edRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting external documents for persona ' + personaName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonaCharacteristics(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getPersonaCharacteristics(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining persona characteristics'
        raise DatabaseProxyException(exceptionText) 
      pChars = {}
      pcSumm = []
      for row in curs.fetchall():
        row = list(row)
        pcId = row[PERSONACHARACTERISTIC_ID_COL]
        pName = row[PERSONACHARACTERISTIC_PERSONANAME_COL]
        bvName = row[PERSONACHARACTERISTIC_BVAR_COL]
        qualName = row[PERSONACHARACTERISTIC_QUAL_COL]
        pcDesc = row[PERSONACHARACTERISTIC_PDESC_COL]
        pcSumm.append((pcId,pName,bvName,qualName,pcDesc))
      curs.close()

      for pcId,pName,bvName,qualName,pcDesc in pcSumm:
        grounds,warrant,backing,rebuttal = self.characteristicReferences(pcId,'characteristicReferences')
        parameters = PersonaCharacteristicParameters(pName,qualName,bvName,pcDesc,grounds,warrant,backing,rebuttal)
        pChar = ObjectFactory.build(pcId,parameters)
        pChars[pName + '/' + bvName + '/' + pcDesc] = pChar
      return pChars
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting persona characteristics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def characteristicReferences(self,pcId,spName):
    try:
      curs = self.conn.cursor()
      curs.execute('call ' + spName + '(%s)',(pcId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining characteristic references'
        raise DatabaseProxyException(exceptionText) 
      refDict = {}
      refDict['grounds'] = []
      refDict['warrant'] = []
      refDict['rebuttal'] = []
      for row in curs.fetchall():
        row = list(row)
        refName = row[REFERENCE_NAME_COL]
        typeName = row[REFERENCE_TYPE_COL]
        refDesc = row[REFERENCE_DESC_COL]
        dimName = row[REFERENCE_DIM_COL]
        refDict[typeName].append((refName,refDesc,dimName))
      curs.close()        
      refDict['grounds'].sort()
      refDict['warrant'].sort()
      refDict['rebuttal'].sort()

      pcBacking = self.characteristicBacking(pcId,spName)
      backingList = []
      for backing,concept in pcBacking:
        backingList.append(backing)
      backingList.sort()

      return (refDict['grounds'],refDict['warrant'],backingList,refDict['rebuttal'])
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting persona characteristic references (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteExternalDocument(self,docId = -1):
    self.deleteObject(docId,'external_document')
    self.conn.commit()

  def deleteDocumentReference(self,refId = -1):
    self.deleteObject(refId,'document_reference')
    self.conn.commit()

  def deletePersonaCharacteristic(self,pcId = -1):
    self.deleteObject(pcId,'persona_characteristic')
    self.conn.commit()

  def addExternalDocument(self,parameters):
    docId = self.newId()
    docName = self.conn.escape_string(parameters.name())
    docVersion = parameters.version()
    docDate = self.conn.escape_string(parameters.date())
    docAuthors = self.conn.escape_string(parameters.authors())
    docDesc = self.conn.escape_string(parameters.description())
    try:
      curs = self.conn.cursor()
      curs.execute('call addExternalDocument(%s,%s,%s,%s,%s,%s)',(docId,docName.encode('utf-8'),docVersion.encode('utf-8'),docDate.encode('utf-8'),docAuthors.encode('utf-8'),docDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding external document ' + docName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return docId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding external document ' + docName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def updateExternalDocument(self,parameters):
    docId = parameters.id()
    docName = self.conn.escape_string(parameters.name())
    docVersion = parameters.version()
    docDate = self.conn.escape_string(parameters.date())
    docAuthors = self.conn.escape_string(parameters.authors())
    docDesc = self.conn.escape_string(parameters.description())
    try:
      curs = self.conn.cursor()
      curs.execute('call updateExternalDocument(%s,%s,%s,%s,%s,%s)',(docId,docName.encode('utf-8'),docVersion.encode('utf-8'),docDate.encode('utf-8'),docAuthors.encode('utf-8'),docDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating external document ' + docName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating external document ' + docName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDocumentReference(self,parameters):
    refId = self.newId()
    refName = parameters.name()
    docName = parameters.document()
    cName = parameters.contributor()
    refExc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call addDocumentReference(%s,%s,%s,%s,%s)',(refId,refName.encode('utf-8'),docName.encode('utf-8'),cName.encode('utf-8'),refExc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding document reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return refId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding document reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateDocumentReference(self,parameters):
    refId = parameters.id()
    refName = parameters.name()
    docName = parameters.document()
    cName = parameters.contributor()
    refExc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateDocumentReference(%s,%s,%s,%s,%s)',(refId,refName.encode('utf-8'),docName.encode('utf-8'),cName.encode('utf-8'),refExc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating document reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating document reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addPersonaCharacteristic(self,parameters):
    pcId = self.newId()
    personaName = parameters.persona()
    qualName = parameters.qualifier()
    bVar = parameters.behaviouralVariable()
    cDesc = parameters.characteristic()
    grounds = parameters.grounds()
    warrant = parameters.warrant() 
    rebuttal = parameters.rebuttal()
    try:
      curs = self.conn.cursor()
      curs.execute('call addPersonaCharacteristic(%s,%s,%s,%s,%s)',(pcId,personaName,qualName,bVar,cDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding persona characteristic ' + pDesc
        raise DatabaseProxyException(exceptionText) 

      self.addPersonaCharacteristicReferences(pcId,grounds,warrant,rebuttal)
      self.conn.commit()
      curs.close()
      return pcId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding persona characteristic ' + cDesc + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updatePersonaCharacteristic(self,parameters):
    pcId = parameters.id()
    personaName = parameters.persona()
    qualName = parameters.qualifier()
    bVar = parameters.behaviouralVariable()
    cDesc = parameters.characteristic()
    grounds = parameters.grounds()
    warrant = parameters.warrant() 
    rebuttal = parameters.rebuttal()
    try:
      curs = self.conn.cursor()
      curs.execute('call deletePersonaCharacteristicComponents(%s)',(pcId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating persona characteristic ' + cDesc
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updatePersonaCharacteristic(%s,%s,%s,%s,%s)',(pcId,personaName,qualName,bVar,cDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating persona characteristic ' + cDesc
        raise DatabaseProxyException(exceptionText) 
      self.addPersonaCharacteristicReferences(pcId,grounds,warrant,rebuttal)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating persona characteristic ' + cDesc + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getPersonaBehaviouralCharacteristics(self,pName,bvName):
    try:
      curs = self.conn.cursor()
      curs.execute('call personaBehaviouralCharacteristics(%s,%s)',(pName,bvName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining persona behavioural characteristics'
        raise DatabaseProxyException(exceptionText) 
      pChars = {}
      pcSumm = []
      for row in curs.fetchall():
        row = list(row)
        pcId = row[0]
        qualName = row[1]
        pcDesc = row[2]
        pcSumm.append((pcId,pName,bvName,qualName,pcDesc))
      curs.close()
      for pcId,pName,bvName,qualName,pcDesc in pcSumm:
        grounds,warrant,backing,rebuttal = self.characteristicReferences(pcId,'characteristicReferences')
        parameters = PersonaCharacteristicParameters(pName,qualName,bvName,pcDesc,grounds,warrant,backing,rebuttal)
        pChar = ObjectFactory.build(pcId,parameters)
        pChars[pName + '/' + bvName + '/' + pcDesc] = pChar
      return pChars
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting persona behavioural characteristics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getConceptReferences(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getConceptReferences(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concept references'
        raise DatabaseProxyException(exceptionText) 
      cRefs = {}
      for row in curs.fetchall():
        row = list(row)
        refId = row[CONCEPTREFERENCE_ID_COL]
        refName = row[CONCEPTREFERENCE_NAME_COL]
        dimName = row[CONCEPTREFERENCE_DIMNAME_COL]
        objtName = row[CONCEPTREFERENCE_OBJTNAME_COL]
        cDesc = row[CONCEPTREFERENCE_DESCRIPTION_COL]
        parameters = ConceptReferenceParameters(refName,dimName,objtName,cDesc)
        cRef = ObjectFactory.build(refId,parameters)
        cRefs[refName] = cRef
      return cRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concept references (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addConceptReference(self,parameters):
    refId = self.newId()
    refName = parameters.name()
    dimName = parameters.dimension()
    objtName = parameters.objectName()
    cDesc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call addConceptReference(%s,%s,%s,%s,%s)',(refId,refName,dimName,objtName,cDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding concept reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return refId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding concept reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateConceptReference(self,parameters):
    refId = parameters.id()
    refName = parameters.name()
    dimName = parameters.dimension()
    objtName = parameters.objectName()
    cDesc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateConceptReference(%s,%s,%s,%s,%s)',(refId,refName,dimName,objtName,cDesc.encode('utf-8')))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating concept reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return refId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating concept reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteConceptReference(self,refId,dimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call delete_concept_reference(%s,%s)',(refId,dimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error deleting concept reference id ' + str(refId)
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.IntegrityError, e:
      id,msg = e
      exceptionText = 'Cannot remove concept reference due to dependent data.  (id:' + str(id) + ',message:' + msg + ')'
      raise IntegrityException(exceptionText) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error deleting concept reference (id:' + str(id) + ',message:' + msg + ')'

  def addPersonaCharacteristicReferences(self,pcId,grounds,warrant,rebuttal):
    for g,desc,dim in grounds:
      self.addPersonaCharacteristicReference(pcId,g,'grounds',desc,dim)

    for w,desc,dim in warrant:
      self.addPersonaCharacteristicReference(pcId,w,'warrant',desc,dim)

    for r,desc,dim in rebuttal:
      self.addPersonaCharacteristicReference(pcId,r,'rebuttal',desc,dim)


  def addPersonaCharacteristicReference(self,pcId,refName,crTypeName,refDesc,dimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addPersonaCharacteristicReference(%s,%s,%s,%s,%s)',(pcId,refName,crTypeName,refDesc.encode('utf-8'),dimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding ' + crTypeName + ' ' + refName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding ' + crTypeName + ' ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def referenceDescription(self,dimName,refName):
    try:
      curs = self.conn.cursor()
      curs.execute('call referenceDescription(%s,%s)',(dimName,refName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding ' + dimName + ' ' + refName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      refDesc = row[0]
      curs.close()
      return refDesc
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding ' + crTypeName + ' ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
  
  def documentReferenceNames(self,docName):
    try:
      curs = self.conn.cursor()
      curs.execute('call documentReferenceNames(%s)',(docName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting references for artifact ' + docName
        raise DatabaseProxyException(exceptionText) 
      refNames = []
      for row in curs.fetchall():
        row = list(row)
        refNames.append(row[0])
      curs.close()
      return refNames
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting references for artifact ' + docName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def referenceUse(self,refName,dimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call referenceUse(%s,%s)',(refName,dimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting characteristics associated with ' + dimName + ' ' + refName
        raise DatabaseProxyException(exceptionText) 
      refNames = []
      for row in curs.fetchall():
        row = list(row)
        refNames.append((row[0],row[1],row[2]))
      curs.close()
      return refNames
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting characteristics associated with ' + dimName + ' ' + refName +  ' (id:' + str(id) + ',message:' + msg + ')'

  def characteristicBacking(self,pcId,spName):
    try:
      curs = self.conn.cursor()
      if (spName == 'characteristicReferences'):
        curs.execute('call characteristicBacking(%s)',(pcId))
      else:
        curs.execute('call taskCharacteristicBacking(%s)',(pcId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting backing for characteristic id ' + str(pcId)
        raise DatabaseProxyException(exceptionText) 
      backing = []
      for row in curs.fetchall():
        row = list(row)
        backing.append((row[0],row[1]))
      curs.close()
      return backing
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting backing for characteristic ' + str(pcId) +  ' (id:' + str(id) + ',message:' + msg + ')'

  def assumptionPersonaModel(self,personaName = '',bvName = '',pcName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call assumptionPersonaModel(%s,%s,%s)',(personaName,bvName,pcName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining assumption persona model'
        raise DatabaseProxyException(exceptionText) 
      associations = []
      for row in curs.fetchall():
        row = list(row)
        fromName = row[0]
        fromDim = row[1]
        toName = row[2]
        toDim = row[3]
        personaNameOut = row[4]
        bvNameOut = row[5]
        pcNameOut = row[6]
        associations.append((fromName,fromDim,toName,toDim,personaNameOut,bvNameOut,pcNameOut))
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assumption persona model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getGrounds(self,constraintName):
    return self.getArgReference('Grounds',constraintName)

  def getWarrant(self,constraintName):
    return self.getArgReference('Warrant',constraintName)

  def getRebuttal(self,constraintName):
    return self.getArgReference('Rebuttal',constraintName)

  def getTaskGrounds(self,constraintName):
    return self.getArgReference('TaskGrounds',constraintName)

  def getTaskWarrant(self,constraintName):
    return self.getArgReference('TaskWarrant',constraintName)

  def getTaskRebuttal(self,constraintName):
    return self.getArgReference('TaskRebuttal',constraintName)


  def getArgReference(self,atName,constraintName):
    try:
      curs = self.conn.cursor()
      curs.execute('call get' + atName + '(%s)',(constraintName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining ' + atName + ':' + constraintName
        curs.close()
        raise DatabaseProxyException(exceptionText) 
      else:
# Reference could be used in multiple grounds, warrants, or backings,  so just enumerate the rows and return the results from the final row
        groundsName = ''
        dimName = ''
        objtName = ''
        refDesc = ''
        for row in curs.fetchall():
          row = list(row)
          groundsName = row[0] 
          dimName = row[1]
          objtName = row[2]
          refDesc = row[3]
        curs.close()   
        return (dimName,objtName,refDesc) 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting ' + atName + ':' + constraintName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addThreatDirectory(self,tDir):
    self.addDirectory(tDir,'threat')

  def addVulnerabilityDirectory(self,vDir):
    self.addDirectory(vDir,'vulnerability')

  def addDirectory(self,gDir,dimName):
    try:
      self.deleteObject(-1,dimName + '_directory')
      for dirId,dLabel,dName,dDesc,dType,dRef in gDir:
        dTypeId = self.getDimensionId(dType,dimName + '_type')
        self.addDirectoryEntry(dirId,dLabel,dName,dDesc,dTypeId,dRef,dimName)
      self.conn.commit()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error importing ' + dimName + ' directory (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addDirectoryEntry(self,dirId,dLabel,dName,dDesc,dTypeId,dRef,dimName):
    try:
      dimName = string.upper(dimName[0]) + dimName[1:]
      curs = self.conn.cursor()
      curs.execute('call add' + dimName + 'DirectoryEntry(%s,%s,%s,%s,%s,%s)',(dirId,dLabel,dName,dDesc,dTypeId,dRef))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding ' + dimName + ' directory entry ' + dLabel
        curs.close()
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error importing ' + dimName + ' directory entry ' + dLabel + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def lastRequirementLabel(self,assetName):
    try: 
      curs = self.conn.cursor()
      curs.execute('select lastRequirementLabel(%s)',(assetName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting last requirement label for asset ',assetName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      return row[0]
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting last requirement label for asset ' + assetName + ' (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def getUseCases(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getUseCases(%s)',(constraintId));
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining usecases'
        raise DatabaseProxyException(exceptionText) 

      ucRows = []
      for row in curs.fetchall():
        row = list(row)
        ucId = row[0]
        ucName = row[1]
        ucAuth = row[2]
        ucCode = row[3]
        ucDesc = row[4]
        ucRows.append((ucId,ucName,ucAuth,ucCode,ucDesc))
      curs.close()

      ucs = {} 

      for ucId,ucName,ucAuth,ucCode,ucDesc in ucRows:
        ucRoles = self.useCaseRoles(ucId)
        environmentProperties = []
        for environmentId,environmentName in self.dimensionEnvironments(ucId,'usecase'):
          preConds,postConds = self.useCaseConditions(ucId,environmentId)
          ucSteps = self.useCaseSteps(ucId,environmentId)
          properties = UseCaseEnvironmentProperties(environmentName,preConds,ucSteps,postConds)
          environmentProperties.append(properties)
          parameters = UseCaseParameters(ucName,ucAuth,ucCode,ucRoles,ucDesc,environmentProperties)
          uc = ObjectFactory.build(ucId,parameters)
          ucs[ucName] = uc
      return ucs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting tasks (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def useCaseRoles(self,ucName):
    try:
      curs = self.conn.cursor()
      curs.execute('call useCaseRoles(%s)',(ucName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting actors associated with use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      roles = []
      for row in curs.fetchall():
        row = list(row)
        roles.append(row[0])
      curs.close()
      return roles
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting actors associated with use case ' + ucName +  ' (id:' + str(id) + ',message:' + msg + ')'

  def useCaseConditions(self,ucId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call useCaseConditions(%s,%s)',(ucId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting conditions associated with use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      cond = []
      row = curs.fetchone()
      preCond = row[0]
      postCond = row[1]
      curs.close()
      return (preCond,postCond)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting conditions associated with use case id ' + str(ucId) +  ' (id:' + str(id) + ',message:' + msg + ')'

  def useCaseSteps(self,ucId,envId):
    try:
      curs = self.conn.cursor()
      curs.execute('call useCaseSteps(%s,%s)',(ucId,envId))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting steps associated with use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      stepRows = []
      for row in curs.fetchall():
        row = list(row)
        stepRows.append((row[1],row[2],row[3],row[4]))
      curs.close()
      steps = Steps()
 
      for pos,stepDetails in enumerate(stepRows):
        stepTxt = stepDetails[0]
        stepSyn = stepDetails[1]
        stepActor = stepDetails[2]
        stepActorType = stepDetails[3]
        stepNo = pos + 1  
        excs = self.useCaseStepExceptions(ucId,envId,stepNo) 
        step = Step(stepTxt,stepSyn,stepActor,stepActorType)
        for exc in excs:
          step.addException(exc)
        steps.append(step)
      return steps
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting steps associated with use case id ' + str(ucId) +  ' (id:' + str(id) + ',message:' + msg + ')'

  def useCaseStepExceptions(self,ucId,envId,stepNo):
    try:
      curs = self.conn.cursor()
      curs.execute('call useCaseStepExceptions(%s,%s,%s)',(ucId,envId,stepNo))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting step exceptions associated with use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      excs = []
      for row in curs.fetchall():
        row = list(row)
        excs.append((row[0],row[1],row[2],row[3],row[4]))
      curs.close()
      return excs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting step exceptions associated with use case id ' + str(ucId) +  ' (id:' + str(id) + ',message:' + msg + ')'

  def addUseCase(self,parameters):
    ucName = parameters.name()
    ucAuth = parameters.author()
    ucCode = parameters.code()
    ucActors = parameters.actors()
    ucDesc = parameters.description()
    try:
      ucId = self.newId()
      curs = self.conn.cursor()
      curs.execute('call addUseCase(%s,%s,%s,%s,%s)',(ucId,ucName,ucAuth,ucCode,ucDesc))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding new use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      for actor in ucActors:
        self.addUseCaseRole(ucId,actor)

      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(ucId,'usecase',environmentName)
        self.addUseCaseConditions(ucId,environmentName,cProperties.preconditions(),cProperties.postconditions())
        self.addUseCaseSteps(ucId,environmentName,cProperties.steps())
      self.conn.commit()
      curs.close()
      return ucId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding use case ' + ucName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseRole(self,ucId,actor):
    try:
      curs = self.conn.cursor()
      curs.execute('call addUseCaseRole(%s,%s)',(ucId,actor)) 
      if (curs.rowcount == -1):
        exceptionText = 'Error associating actor ' + actor + ' with use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error associating actor' + actor + ' with use case id ' + str(ucId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseConditions(self,ucId,envName,preCond,postCond):
    try:
      curs = self.conn.cursor()
      curs.execute('call addUseCaseConditions(%s,%s,%s,%s)',(ucId,envName,preCond,postCond)) 
      if (curs.rowcount == -1):
        exceptionText = 'Error adding conditions to use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding conditions to use case id ' + str(ucId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseSteps(self,ucId,envName,steps):
    for pos,step in enumerate(steps.theSteps):
      stepNo = pos + 1
      self.addUseCaseStep(ucId,envName,stepNo,step)

  def addUseCaseStep(self,ucId,envName,stepNo,step):
    try:
      curs = self.conn.cursor()
      synId = self.newId()
      curs.execute('call addUseCaseStep(%s,%s,%s,%s,%s,%s,%s,%s)',(ucId,envName,stepNo,step.text(),synId,step.synopsis(),step.actor(),step.actorType())) 
      if (curs.rowcount == -1):
        exceptionText = 'Error adding step: ' + step.text() + ' to use case id ' + str(ucId)
        raise DatabaseProxyException(exceptionText) 
      curs.close()
      for idx,exc in (step.theExceptions).iteritems():
        self.addUseCaseStepException(ucId,envName,stepNo,exc[0],exc[1],exc[2],exc[3],exc[4])
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding step: ' + step.text() + ' to use case id ' + str(ucId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseStepException(self,ucId,envName,stepNo,exName,dimType,dimName,catName,exDesc):
    try:
      curs = self.conn.cursor()
      curs.execute('call addUseCaseStepException(%s,%s,%s,%s,%s,%s,%s,%s)',(ucId,envName,stepNo,exName,dimType,dimName,catName,exDesc))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding step exception ' + exName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding step exception ' + exName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateUseCase(self,parameters):
    ucId = parameters.id()
    ucName = parameters.name()
    ucAuth = parameters.author()
    ucCode = parameters.code()
    ucActors = parameters.actors()
    ucDesc = parameters.description()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteUseCaseComponents(%s)',(ucId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateUseCase(%s,%s,%s,%s,%s)',(ucId,ucName,ucAuth,ucCode,ucDesc))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      for actor in ucActors:
        self.addUseCaseRole(ucId,actor)
      for cProperties in parameters.environmentProperties():
        environmentName = cProperties.name()
        self.addDimensionEnvironment(ucId,'usecase',environmentName)
        self.addUseCaseConditions(ucId,environmentName,cProperties.preconditions(),cProperties.postconditions())
        self.addUseCaseSteps(ucId,environmentName,cProperties.steps())
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating use case ' + ucName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteUseCase(self,ucId):
    self.deleteObject(ucId,'usecase')
    self.conn.commit()

  def environmentUseCases(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call usecaseNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining use cases for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting use cases associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def environmentMisuseCases(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call misusecaseNames(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining misuse cases for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        mcs = []
        for row in curs.fetchall():
          row = list(row)
          mcs.append(row[0])
        curs.close()
        return mcs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting misuse cases associated with environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskModel(self,environmentName,riskName):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskModel(%s,%s)',(riskName,environmentName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting risk model'
        raise DatabaseProxyException(exceptionText) 
      traces = []
      for traceRow in curs.fetchall():
        traceRow = list(traceRow)
        fromObjt = traceRow[FROM_OBJT_COL]
        fromName = traceRow[FROM_ID_COL]
        toObjt = traceRow[TO_OBJT_COL]
        toName = traceRow[TO_ID_COL]
        parameters = DotTraceParameters(fromObjt,fromName,toObjt,toName)
        traces.append(ObjectFactory.build(-1,parameters))
      curs.close() 
      return traces
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting risk model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def isRisk(self,candidateRiskName):
    try:
      curs = self.conn.cursor()
      curs.execute('select is_risk(%s)',(candidateRiskName))
      if (curs.rowcount == -1):
        exceptionText = 'Error checking if ' + candidateRiskName + ' is a risk'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      return row[0]
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error checking if ' + candateRiskName + 'is a risk (id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
        

  def textualArgumentationModel(self,personaName,bvType):
    try:
      curs = self.conn.cursor()
      curs.execute('call assumptionPersonaModel_textual(%s,%s)',(personaName,bvType))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting ' + bvType + ' argumentation model for ' + personaName
        raise DatabaseProxyException(exceptionText) 
      rows = []
      for row in curs.fetchall():
        listRow = list(row)
        rows.append((row[0],row[1],row[2]))
      curs.close() 
      return rows
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting ' + bvType + ' argumentation model for ' + personaName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def riskAnalysisToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call riskAnalysisToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting risk analysis artifacts to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      roleCount = row[1]
      assetCount = row[2]
      vulCount = row[3]
      attackerCount = row[4]
      threatCount = row[5]
      riskCount = row[6]
      responseCount = row[7]
      rshipCount = row[8]
      curs.close()
      return (xmlBuf,roleCount,assetCount,vulCount,attackerCount,threatCount,riskCount,responseCount,rshipCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting risk analysis artifacts to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalsToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalsToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting goals to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      dpCount = row[1]
      goalCount = row[2]
      obsCount = row[3]
      reqCount = row[4]
      cmCount = row[5]
      curs.close()
      return (xmlBuf,dpCount,goalCount,obsCount,reqCount,cmCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting goals to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def usabilityToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call usabilityToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting usability data to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      personaCount = row[1]
      edCount = row[2]
      drCount = row[3]
      pcCount = row[4]
      taskCount = row[5]
      ucCount = row[6]
      curs.close()
      return (xmlBuf,personaCount,edCount,drCount,pcCount,taskCount,ucCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL usability data to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def associationsToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call associationsToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting association data to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      maCount = row[1]
      gaCount = row[2]
      rrCount = row[3]
      depCount = row[4]
      curs.close()
      return (xmlBuf,maCount,gaCount,rrCount,depCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error exporting association data to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def projectToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call projectToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting project data to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      curs.close()
      return xmlBuf
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error exporting project data to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def modelToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call modelToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting model to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      curs.close()
      return xmlBuf
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error exporting model to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getTaskCharacteristics(self,constraintId = -1):
    try:
      curs = self.conn.cursor()
      curs.execute('call getTaskCharacteristics(%s)',(constraintId))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining task characteristics'
        raise DatabaseProxyException(exceptionText) 
      tChars = {}
      tcSumm = []
      for row in curs.fetchall():
        row = list(row)
        tcId = row[TASKCHARACTERISTIC_ID_COL]
        tName = row[TASKCHARACTERISTIC_TASKNAME_COL]
        qualName = row[TASKCHARACTERISTIC_QUAL_COL]
        tcDesc = row[TASKCHARACTERISTIC_TDESC_COL]
        tcSumm.append((tcId,tName,qualName,tcDesc))
      curs.close()

      for tcId,tName,qualName,tcDesc in tcSumm:
        grounds,warrant,backing,rebuttal = self.characteristicReferences(tcId,'taskCharacteristicReferences')
        parameters = TaskCharacteristicParameters(tName,qualName,tcDesc,grounds,warrant,backing,rebuttal)
        tChar = ObjectFactory.build(tcId,parameters)
        tChars[tName + '/' + tcDesc] = tChar
      return tChars
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task characteristics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText)

  def addTaskCharacteristic(self,parameters):
    tcId = self.newId()
    taskName = self.conn.escape_string(parameters.task())
    qualName = self.conn.escape_string(parameters.qualifier())
    cDesc = self.conn.escape_string(parameters.characteristic())
    grounds = parameters.grounds()
    warrant = parameters.warrant()
    rebuttal = parameters.rebuttal()
    try:
      curs = self.conn.cursor()
      curs.execute('call addTaskCharacteristic(%s,%s,%s,%s)',(tcId,taskName,qualName,cDesc))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding task characteristic ' + cDesc
        raise DatabaseProxyException(exceptionText) 
      self.addTaskCharacteristicReferences(tcId,grounds,warrant,rebuttal)
      self.conn.commit()
      curs.close()
      return tcId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding task characteristic ' + cDesc + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addTaskCharacteristicReferences(self,tcId,grounds,warrant,rebuttal):
    for g,desc,dim in grounds:
      self.addTaskCharacteristicReference(tcId,g,'grounds',desc.encode('utf-8'),dim)

    for w,desc,dim in warrant:
      self.addTaskCharacteristicReference(tcId,w,'warrant',desc.encode('utf-8'),dim)

    for r,desc,dim in rebuttal:
      self.addTaskCharacteristicReference(tcId,r,'rebuttal',desc.encode('utf-8'),dim)


  def addTaskCharacteristicReference(self,tcId,refName,crTypeName,refDesc,dimName):
    try:
      curs = self.conn.cursor()
      curs.execute('call addTaskCharacteristicReference(%s,%s,%s,%s,%s)',(tcId,refName,crTypeName,refDesc,dimName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding ' + crTypeName + ' ' + refName
        raise DatabaseProxyException(exceptionText) 
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding ' + crTypeName + ' ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def updateTaskCharacteristic(self,parameters):
    tcId = parameters.id()
    taskName = parameters.task()
    qualName = parameters.qualifier()
    cDesc = parameters.characteristic()
    grounds = parameters.grounds()
    warrant = parameters.warrant() 
    rebuttal = parameters.rebuttal()
    try:
      curs = self.conn.cursor()
      curs.execute('call deleteTaskCharacteristicComponents(%s)',(tcId))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating task characteristic ' + cDesc
        raise DatabaseProxyException(exceptionText) 
      curs.execute('call updateTaskCharacteristic(%s,%s,%s,%s)',(tcId,taskName,qualName,cDesc))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating task characteristic ' + cDesc
        raise DatabaseProxyException(exceptionText) 
      self.addTaskCharacteristicReferences(tcId,grounds,warrant,rebuttal)
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating task characteristic ' + cDesc + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def deleteTaskCharacteristic(self,pcId = -1):
    self.deleteObject(pcId,'task_characteristic')
    self.conn.commit()

  def assumptionTaskModel(self,taskName = '',tcName = ''):
    try:
      curs = self.conn.cursor()
      curs.execute('call assumptionTaskModel(%s,%s)',(taskName,tcName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining assumption task model'
        raise DatabaseProxyException(exceptionText) 
      associations = []
      for row in curs.fetchall():
        row = list(row)
        fromName = row[0]
        fromDim = row[1]
        toName = row[2]
        toDim = row[3]
        taskNameOut = row[4]
        tcNameOut = row[5]
        associations.append((fromName,fromDim,toName,toDim,taskNameOut,tcNameOut))
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting assumption task model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getTaskSpecificCharacteristics(self,tName):
    try:
      curs = self.conn.cursor()
      curs.execute('call taskSpecificCharacteristics(%s)',(tName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining task specific characteristics'
        raise DatabaseProxyException(exceptionText) 
      tChars = {}
      tcSumm = []
      for row in curs.fetchall():
        row = list(row)
        tcId = row[0]
        qualName = row[1]
        tcDesc = row[2]
        tcSumm.append((tcId,tName,qualName,tcDesc))
      curs.close()
      for tcId,tName,qualName,tcDesc in tcSumm:
        grounds,warrant,backing,rebuttal = self.characteristicReferences(tcId,'taskCharacteristicReferences')
        parameters = TaskCharacteristicParameters(tName,qualName,tcDesc,grounds,warrant,backing,rebuttal)
        tChar = ObjectFactory.build(tcId,parameters)
        tChars[tName + '/' + tcDesc] = tChar
      return tChars
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting task specific characteristics (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def prettyPrintGoals(self,categoryName):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalsPrettyPrint(%s)',(categoryName))
      if (curs.rowcount == -1):
        exceptionText = 'Error pretty printing goals'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      buf = row[0] 
      curs.close()
      return buf
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL pretty printing goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def searchModel(self,inTxt,opts):
    try:
      curs = self.conn.cursor()

      psFlag = opts[0]
      envFlag = opts[1]
      roleFlag = opts[2]
      pcFlag = opts[3]
      tcFlag = opts[4]
      refFlag = opts[5]
      pFlag = opts[6]
      taskFlag = opts[7]
      ucFlag = opts[8]
      dpFlag = opts[9]
      goalFlag = opts[10]
      obsFlag = opts[11]
      reqFlag = opts[12]
      assetFlag = opts[13]
      vulFlag = opts[14]
      attackerFlag = opts[15]
      thrFlag = opts[16]
      riskFlag = opts[17]
      respFlag = opts[18]
      cmFlag = opts[19]

      curs.execute('call grepModel(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(inTxt,psFlag,envFlag,roleFlag,pcFlag,tcFlag,refFlag,pFlag,taskFlag,ucFlag,dpFlag,goalFlag,obsFlag,reqFlag,assetFlag,vulFlag,attackerFlag,thrFlag,riskFlag,respFlag,cmFlag))
      if (curs.rowcount == -1):
        exceptionText = 'Error searching model'
        raise DatabaseProxyException(exceptionText) 
      results = []
      for row in curs.fetchall():
        row = list(row)
        results.append((row[0],row[1],row[2]))
      curs.close()
      return results
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error searching model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getExternalDocumentReferencesByExternalDocument(self,edName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getExternalDocumentReferences(%s)',(edName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining document references for external document ' + edName
        raise DatabaseProxyException(exceptionText) 
      dRefs = []
      for row in curs.fetchall():
        row = list(row)
        refName = row[0]
        docName = row[1]
        excerpt = row[2]
        dRefs.append((refName,docName,excerpt))
      return dRefs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting document references for external document ' + edName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def dimensionNameByShortCode(self,scName):
    try:
      curs = self.conn.cursor()
      curs.execute('call dimensionNameByShortCode(%s)',(scName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining dimension associated with short code ' + scName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      dePair = (row[0],row[1])
      curs.close()
      return dePair
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error obtaining dimension associated with short code ' + scName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def misuseCaseRiskComponents(self,mcName):
    try:
      curs = self.conn.cursor()
      curs.execute('call misuseCaseRiskComponents(%s)',(mcName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining risk components associated with Misuse Case ' + mcName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      cPair = (row[0],row[1])
      curs.close()
      return cPair
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error obtaining risk components associated with Misuse Case ' + mcName + ' (id:' + str(id) + ',message:' + msg + ')'

  def personaToXml(self,pName):
    try:
      curs = self.conn.cursor()
      curs.execute('call personaToXml(%s)',(pName))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting persona to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      edCount = row[1]
      drCount = row[2]
      pcCount = row[3]
      curs.close()
      return (xmlBuf,edCount,drCount,pcCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error exporting persona to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def defaultEnvironment(self):
    try:
      curs = self.conn.cursor()
      curs.execute('select defaultEnvironment()')
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining default environment'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      defaultEnv = row[0]
      curs.close()
      return defaultEnv
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error obtaining default environment (id:' + str(id) + ',message:' + msg + ')'

  def environmentTensions(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call environmentTensions(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting value tensions for environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      vts = {}
      rowIdx = 0
      for row in curs.fetchall():
        row = list(row)
        anTR = row[0]
        anValue,anRationale = anTR.split('#')
        vts[(rowIdx,4)] = (int(anValue),anRationale)
        panTR = row[1]
        panValue,panRationale = panTR.split('#')
        vts[(rowIdx,5)] = (int(panValue),panRationale)
        unlTR = row[2]
        unlValue,unlRationale = unlTR.split('#')
        vts[(rowIdx,6)] = (int(unlValue),unlRationale)
        unoTR = row[3]
        unoValue,unoRationale = unoTR.split('#')
        vts[(rowIdx,7)] = (int(unlValue),unlRationale)
        rowIdx += 1
      curs.close()
      return vts
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting value tensions for environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def getReferenceSynopsis(self,refName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getReferenceSynopsis(%s)',(refName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting synopsis for reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      rsId = row[0]
      synName = row[1]
      dimName = row[2]
      aType = row[3]
      aName = row[4]
      rs = ReferenceSynopsis(rsId,refName,synName,dimName,aType,aName)
      curs.close() 
      return rs 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting synopsis for reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getReferenceContribution(self,charName,refName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getReferenceContribution(%s,%s)',(refName,charName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting contribution for reference ' + refName + ' and characteristic ' + charName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      rsName = row[0]
      csName = row[1]
      me = row[2]
      cont = row[3]
      rc = ReferenceContribution(rsName,csName,me,cont)
      curs.close() 
      return rc
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting contribution for reference ' + refName + ' and characteristic ' + charName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addReferenceContribution(self,rc):
    rsName = rc.source()
    csName = rc.destination()
    meName = rc.meansEnd()
    contName = rc.contribution()
    try:
      curs = self.conn.cursor()
      curs.execute('call addReferenceContribution(%s,%s,%s,%s)',(rsName,csName,meName,contName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding contribution for reference synopsis ' + rsName + ' and contribution synopsis ' + csName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding contribution for reference synopsis ' + rsName + ' and characteristic synopsis ' + csName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateReferenceContribution(self,rc):
    rsName = rc.source()
    csName = rc.destination()
    meName = rc.meansEnd()
    contName = rc.contribution()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateReferenceContribution(%s,%s,%s,%s)',(rsName,csName,meName,contName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating contribution for reference synopsis ' + rsName + ' and contribution synopsis ' + csName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating contribution for reference synopsis ' + rsName + ' and characteristic synopsis ' + csName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addReferenceSynopsis(self,rs):
    rsId = self.newId()
    refName = rs.reference()
    rsName = rs.synopsis()
    rsDim = rs.dimension()
    atName = rs.actorType()
    actorName = rs.actor()
    try:
      curs = self.conn.cursor()
      curs.execute('call addReferenceSynopsis(%s,%s,%s,%s,%s,%s)',(rsId,refName,rsName,rsDim,atName,actorName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding synopsis ' + rsName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
      return rsId
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding synopsis ' + rsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateReferenceSynopsis(self,rs):
    rsId = rs.id()
    refName = rs.reference()
    rsName = rs.synopsis()
    rsDim = rs.dimension()
    atName = rs.actorType()
    actorName = rs.actor()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateReferenceSynopsis(%s,%s,%s,%s,%s,%s)',(rsId,refName,rsName,rsDim,atName,actorName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating synopsis ' + rsName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating synopsis ' + rsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addCharacteristicSynopsis(self,cs):
    cName = cs.reference()
    csName = cs.synopsis()
    csDim = cs.dimension()
    atName = cs.actorType()
    actorName = cs.actor()
    try:
      curs = self.conn.cursor()
      curs.execute('call addCharacteristicSynopsis(%s,%s,%s,%s,%s)',(cName,csName,csDim,atName,actorName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding synopsis ' + csName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding synopsis ' + csName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateCharacteristicSynopsis(self,cs):
    cName = cs.reference()
    csName = cs.synopsis()
    csDim = cs.dimension()
    atName = cs.actorType()
    actorName = cs.actor()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateCharacteristicSynopsis(%s,%s,%s,%s,%s)',(cName,csName,csDim,atName,actorName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating synopsis ' + csName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating synopsis ' + csName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def referenceCharacteristic(self,refName):
    try:
      curs = self.conn.cursor()
      curs.execute('call referenceCharacteristic(%s)',(refName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting reference associated with characteristic ' + refName
        raise DatabaseProxyException(exceptionText) 
      charNames = []
      for row in curs.fetchall():
        row = list(row)
        charNames.append(row[0])
      curs.close()
      return charNames
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting characteristic associated with reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getCharacteristicSynopsis(self,cName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getCharacteristicSynopsis(%s)',(cName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting synopsis for characteristic ' + cName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      synName = row[0]
      dimName = row[1]
      aType = row[2]
      aName = row[3]
      if synName == '':
        synId = -1
      else:
        synId = 0
      rs = ReferenceSynopsis(synId,cName,synName,dimName,aType,aName)
      curs.close() 
      return rs 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting synopsis for characteristic ' + cName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def hasCharacteristicSynopsis(self,charName):
    try:
      curs = self.conn.cursor()
      curs.execute('select hasCharacteristicSynopsis(%s)',(charName))
      if (curs.rowcount == -1):
        exceptionText = 'Error finding synopsis for characteristic ' + charName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      hs = row[0]
      curs.close()
      return hs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error finding synopsis for characteristic ' + charName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def hasReferenceSynopsis(self,refName):
    try:
      curs = self.conn.cursor()
      curs.execute('select hasReferenceSynopsis(%s)',(refName))
      if (curs.rowcount == -1):
        exceptionText = 'Error finding synopsis for reference ' + refName
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      hs = row[0]
      curs.close()
      return hs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error finding synopsis for reference ' + refName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseSynopsis(self,cs):
    cName = cs.reference()
    csName = cs.synopsis()
    csDim = cs.dimension()
    atName = cs.actorType()
    actorName = cs.actor()
    try:
      curs = self.conn.cursor()
      curs.execute('call addUseCaseSynopsis(%s,%s,%s,%s,%s)',(cName,csName,csDim,atName,actorName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding synopsis ' + csName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding synopsis ' + csName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getUseCaseContributions(self,ucName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getUseCaseContributions(%s)',(ucName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting contributions for use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      ucs = {}
      for row in curs.fetchall():
        row = list(row)
        rsName = row[0]
        me = row[1]
        cont = row[2]
        rType = row[3]
        rc = ReferenceContribution(ucName,rsName,me,cont)
        ucs[rsName] = (rc,rType) 
      curs.close() 
      return ucs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting contributions for use case ' + ucName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def addUseCaseContribution(self,rc):
    ucName = rc.source()
    csName = rc.destination()
    meName = rc.meansEnd()
    contName = rc.contribution()
    try:
      curs = self.conn.cursor()
      curs.execute('call addUseCaseContribution(%s,%s,%s,%s)',(ucName,csName,meName,contName))
      if (curs.rowcount == -1):
        exceptionText = 'Error adding contribution for use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error adding contribution for use case ' + ucName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateUseCaseContribution(self,rc):
    ucName = rc.source()
    csName = rc.destination()
    meName = rc.meansEnd()
    contName = rc.contribution()
    try:
      curs = self.conn.cursor()
      curs.execute('call updateUseCaseContribution(%s,%s,%s,%s)',(ucName,csName,meName,contName))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating contribution for use case ' + ucName
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error updating contribution for use case ' + ucName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 


  def pcToGrl(self,pName,tName,envName):
    try:
      curs = self.conn.cursor()
      print 'call pcToGrl(',pName,',',tName,',',envName,')'
      curs.execute('call pcToGrl(%s,%s,%s)',(pName,tName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting persona and task to GRL'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      buf = row[0] 
      curs.close()
      return buf
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting persona and task to GRL (id:' + str(id) + ',message:' + msg + ')'

  def getEnvironmentGoals(self,goalName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getEnvironmentGoals(%s,%s)',(goalName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goals'
        raise DatabaseProxyException(exceptionText) 
      goals = []
      goalRows = []
      for row in curs.fetchall():
        row = list(row)
        goalId = row[GOALS_ID_COL]
        goalName = row[GOALS_NAME_COL]
        goalOrig = row[GOALS_ORIGINATOR_COL]
        goalRows.append((goalId,goalName,goalOrig))
      curs.close()

      for goalId,goalName,goalOrig in goalRows:
        environmentProperties = self.goalEnvironmentProperties(goalId)
        parameters = GoalParameters(goalName,goalOrig,self.goalEnvironmentProperties(goalId))
        goal = ObjectFactory.build(goalId,parameters)
        goals.append(goal)
      return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateEnvironmentGoal(self,g,envName):
    envProps = g.environmentProperty(envName)
    goalDef = envProps.definition()
    goalCat = envProps.category()
    goalPri = envProps.priority()
    goalFc = envProps.fitCriterion()
    goalIssue = envProps.issue()
    
    try:
      curs = self.conn.cursor()
      curs.execute('call updateEnvironmentGoal(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(g.id(),envName,g.name(),g.originator(),goalDef,goalCat,goalPri,goalFc,goalIssue))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating goal ' + str(g.id())
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL adding updating goal ' + str(g.id()) + '(id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 
 
  def getSubGoalNames(self,goalName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call subGoalNames(%s,%s)',(goalName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining goals for environment ' + envName + ' and subgoal ' + goalName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = ['']
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting goals associated with environment ' + envName + ' and subgoal ' + goalName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def dependentLabels(self,goalName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call dependentLabels(%s,%s)',(goalName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining dependent labels for ' + goalName + ' in environment ' + envName
        raise DatabaseProxyException(exceptionText) 
      else:
        goals = []
        for row in curs.fetchall():
          row = list(row)
          goals.append(row[0])
        curs.close()
        return goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting dependent labels for ' + goalName + ' in environment ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def goalEnvironments(self,goalName):
    try:
      curs = self.conn.cursor()
      curs.execute('call goalEnvironments(%s)',(goalName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining environments for goal ' + goalName
        raise DatabaseProxyException(exceptionText) 
      else:
        envs = ['']
        for row in curs.fetchall():
          row = list(row)
          envs.append(row[0])
        curs.close()
        return envs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments associated with goal ' + envName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleEnvironments(self,obsName):
    try:
      curs = self.conn.cursor()
      curs.execute('call obstacleEnvironments(%s)',(obsName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining environments for obstacle ' + obsName
        raise DatabaseProxyException(exceptionText) 
      else:
        envs = ['']
        for row in curs.fetchall():
          row = list(row)
          envs.append(row[0])
        curs.close()
        return envs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting environments associated with obstacle ' + obsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getSubObstacleNames(self,obsName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call subObstacleNames(%s,%s)',(obsName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining obstacles for environment ' + envName + ' and sub-obstacle ' + obsName
        raise DatabaseProxyException(exceptionText) 
      else:
        obs = ['']
        for row in curs.fetchall():
          row = list(row)
          obs.append(row[0])
        curs.close()
        return obs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting obstacles associated with environment ' + envName + ' and sub-obstacle ' + obsName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getEnvironmentObstacles(self,obsName,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getEnvironmentObstacles(%s,%s)',(obsName,envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining obstacles'
        raise DatabaseProxyException(exceptionText) 
      obs = []
      obsRows = []
      for row in curs.fetchall():
        row = list(row)
        obsId = row[GOALS_ID_COL]
        obsName = row[GOALS_NAME_COL]
        obsOrig = row[GOALS_ORIGINATOR_COL]
        obsRows.append((obsId,obsName,obsOrig))
      curs.close()

      for obsId,obsName,obsOrig in obsRows:
        environmentProperties = self.obstacleEnvironmentProperties(obsId)
        parameters = ObstacleParameters(obsName,obsOrig,self.obstacleEnvironmentProperties(obsId))
        obstacle = ObjectFactory.build(obsId,parameters)
        obs.append(obstacle)
      return obs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting obstacles (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def updateEnvironmentObstacle(self,o,envName):
    envProps = o.environmentProperty(envName)
    obsDef = envProps.definition()
    obsCat = envProps.category()
    
    try:
      curs = self.conn.cursor()
      curs.execute('call updateEnvironmentObstacle(%s,%s,%s,%s,%s,%s)',(o.id(),envName,o.name(),o.originator(),obsDef,obsCat))
      if (curs.rowcount == -1):
        exceptionText = 'Error updating obstacle ' + str(g.id())
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL adding updating obstacle ' + str(o.id()) + '(id:' + str(id) + ',message:' + msg
      raise DatabaseProxyException(exceptionText) 

  def relabelGoals(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call relabelGoals(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error relabelling goals'
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting labelled goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def relabelObstacles(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call relabelObstacles(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error relabelling obstacles'
        raise DatabaseProxyException(exceptionText) 
      self.conn.commit()
      curs.close()
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting labelled obstacles (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def obstacleLabel(self,goalId,environmentId):
    try:
      curs = self.conn.cursor()
      curs.execute('select obstacle_label(%s,%s)',(goalId,environmentId))
      if (curs.rowcount == -1):
        curs.close()
        exceptionText = 'Error obtaining label for obstacle id ' + str(goalId) + ' in environment id ' + str(environmentId)
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      goalAttr = row[0] 
      curs.close()
      return goalAttr
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting label for obstacle id ' + str(goalId) + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getLabelledGoals(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call getEnvironmentGoals(%s,%s)',('',envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining labelled goals'
        raise DatabaseProxyException(exceptionText) 
      goals = {}
      goalRows = []
      for row in curs.fetchall():
        row = list(row)
        goalId = row[GOALS_ID_COL]
        goalName = row[GOALS_NAME_COL]
        goalOrig = row[GOALS_ORIGINATOR_COL]
        goalRows.append((goalId,goalName,goalOrig))
      curs.close()
      for goalId,goalName,goalOrig in goalRows:
        environmentProperties = self.goalEnvironmentProperties(goalId)
        parameters = GoalParameters(goalName,goalOrig,self.goalEnvironmentProperties(goalId))
        g = ObjectFactory.build(goalId,parameters)
        lbl = g.label(envName)
        goals[lbl] = g
      lbls = goals.keys()
      lbls.sort(key=lambda x: [int(y) for y in x.split('.')])
      return lbls,goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting labelled goals  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def redmineGoals(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call redmineGoals(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining redmine goals'
        raise DatabaseProxyException(exceptionText) 
      goals = {}
      goalRows = []
      for row in curs.fetchall():
        row = list(row)
        goalId = row[0]
        envId = row[1]
        goalLabel = row[2]
        goalName = row[3]
        goalOrig = row[4]
        goalDef = row[5]
        goalCat = row[6]
        goalPri = row[7]
        goalFC = row[8]
        goalIssue = row[9]
        goalRows.append((goalId,envId,goalLabel,goalName,goalOrig,goalDef,goalCat,goalPri,goalFC,goalIssue))
      curs.close()
      for goalId,envId,goalLabel,goalName,goalOrig,goalDef,goalCat,goalPri,goalFC,goalIssue in goalRows:
        goalRefinements,subGoalRefinements = self.goalRefinements(goalId,envId)
        concerns = self.goalConcerns(goalId,envId)
        concernAssociations = self.goalConcernAssociations(goalId,envId)
        ep = GoalEnvironmentProperties(envName,goalLabel,goalDef,'Maintain',goalPri,goalFC,goalIssue,goalRefinements,subGoalRefinements,concerns,concernAssociations)
        parameters = GoalParameters(goalName,goalOrig,[ep])
        g = ObjectFactory.build(goalId,parameters)
        lbl = g.label(envName)
        goals[lbl] = g
      lbls = goals.keys()
      shortCode = lbls[0].split('-')[0]
      lblNos = []
      for lbl in lbls:
        lblNos.append(lbl.split('-')[1])
      lblNos.sort(key=lambda x: [int(y) for y in x.split('.')])
      lbls = []
      for ln in lblNos:
        lbls.append(shortCode + '-' + ln) 
      return lbls,goals
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting redmine goals  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def redmineUseCases(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call usecasesToRedmine()')
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting usecases to Redmine'
        raise DatabaseProxyException(exceptionText) 
      ucs = []
      for row in curs.fetchall():
        row = list(row)
        ucs.append((row[0],row[1],row[2],row[3]))
      curs.close()
      return ucs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting usecases to Redmine (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def redmineScenarios(self):
    try:
      curs = self.conn.cursor()
      curs.execute('call redmineScenarios()')
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting scenarios to Redmine'
        raise DatabaseProxyException(exceptionText) 
      scenarios = []
      for row in curs.fetchall():
        row = list(row)
        sName = row[0]
        sEnv = row[1]
        sTxt = row[2]
        scenarios.append((row[0],row[1],row[2]))
      curs.close()
      return scenarios
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting scenarios to Redmine (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def tvTypesToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call tvTypesToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting threat and vulnerability types to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      ttCount = row[1]
      vtCount = row[2]
      curs.close()
      return (xmlBuf,ttCount,vtCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting threat and vulnerability types to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def domainValuesToXml(self,includeHeader=True):
    try:
      curs = self.conn.cursor()
      curs.execute('call domainValuesToXml(%s)',(includeHeader))
      if (curs.rowcount == -1):
        exceptionText = 'Error exporting domain values to XML'
        raise DatabaseProxyException(exceptionText) 
      row = curs.fetchone()
      xmlBuf = row[0] 
      tvCount = row[1]
      rvCount = row[2]
      cvCount = row[3]
      svCount = row[4]
      lvCount = row[5]
      curs.close()
      return (xmlBuf,tvCount,rvCount,cvCount,svCount,lvCount)
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL exporting domain values to XML (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def redmineTempGoals(self):
    try:
      curs = self.conn.cursor()
      curs.execute('select originator,environment,priority,definition,fit_criterion from redmine_goal order by 2,1')
      if (curs.rowcount == -1):
        exceptionText = 'Error selecting interim redmine goals'
        raise DatabaseProxyException(exceptionText) 
      rows = []
      for row in curs.fetchall():
        row = list(row)
        orig = row[0]
        env = row[1]
        pri = row[2] 
        defn = row[3]
        fc = row[4]
        rows.append((orig,env,pri,defn,fc))
      curs.close()
      return rows 
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL selecting interim redmine goals (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def clearDatabase(self):
    srcDir = os.environ['IRIS_SRC'] + '/sql'
    initSql = srcDir + '/init.sql'
    procsSql = srcDir + '/procs.sql'
    b = Borg()
    cmd = '/usr/bin/mysql -h ' + b.dbHost + ' -u ' + b.dbUser + ' --password=\'' + b.dbPasswd + '\'' + ' --database ' + b.dbName + ' < ' + initSql
    os.system(cmd)
    cmd = '/usr/bin/mysql -h ' + b.dbHost + ' -u ' + b.dbUser + ' --password=\'' + b.dbPasswd + '\'' + ' --database ' + b.dbName + ' < ' + procsSql
    os.system(cmd)


  def conceptMapModel(self,envName):
    try:
      curs = self.conn.cursor()
      curs.execute('call conceptMapModel(%s)',(envName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining concept map model'
        raise DatabaseProxyException(exceptionText) 
      associations = {}
      for row in curs.fetchall():
        row = list(row)
        fromName = row[0]
        toName = row[1]
        lbl = row[2]
        fromEnv = row[3]
        toEnv = row[4]
        cmLabel = fromName + '#' + toName + '#' + lbl
        assoc = ConceptMapAssociationParameters(fromName,toName,lbl,fromEnv,toEnv)
        associations[cmLabel] = assoc
      curs.close()
      return associations
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting concept map model (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def traceabilityScore(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('select traceabilityScore(%s)',(reqName))
      if (curs.rowcount == -1):
        exceptionText = 'Error obtaining traceability score for ' + reqName
        raise DatabaseProxyException(exceptionText) 
      results = curs.fetchone()
      scoreCode = results[0]
      curs.close()
      return scoreCode
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting traceability score for ' + reqName + ' (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 
   

  def getRedmineRequirements(self):
    try:
      curs = self.conn.cursor()
      curs.execute('select name,originator,priority,comments,description,environment_code,environment from redmine_requirement order by 1');
      if (curs.rowcount == -1):
        exceptionText = 'Error getting requirements'
        raise DatabaseProxyException(exceptionText) 
      reqs = {}
      reqRows = []
      for row in curs.fetchall():
        row = list(row)
        reqName = row[0]
        reqOriginator = row[1]
        reqPriority = row[2]
        reqComments = row[3]
        reqDesc = row[4]
        reqEnvCode = row[5]
        reqEnv = row[6]
        reqRows.append((reqName,reqOriginator,reqPriority,reqComments,reqDesc,reqEnvCode,reqEnv))
      curs.close()

      priorityLookup = {1:'High',2:'Medium',3:'Low'}
      for reqName,reqOriginator,reqPriority,reqComments,reqDesc,reqEnvCode,reqEnv in reqRows:
        reqScs = self.getRequirementScenarios(reqName)
        reqUcs = self.getRequirementUseCases(reqName)
        reqBis = self.getRequirementBacklog(reqName)
        if reqEnv not in reqs:
          reqs[reqEnv] = []
        reqs[reqEnv].append((reqName,reqOriginator,priorityLookup[reqPriority],reqComments,reqDesc,reqEnvCode,reqScs,reqUcs,reqBis))
      return reqs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting requirements  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRequirementScenarios(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('call requirementScenarios(%s)',(reqName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting scenarios associated with requirement ' + reqName
        raise DatabaseProxyException(exceptionText) 
      scs = [] 
      for row in curs.fetchall():
        row = list(row)
        scs.append(row[0])
      curs.close()
      if len(scs) == 0:
        scs.append('None')
      return scs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting scenarios associated with requirement ' + reqName + '  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRequirementUseCases(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('call requirementUseCases(%s)',(reqName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting use cases associated with requirement ' + reqName
        raise DatabaseProxyException(exceptionText) 
      ucs = [] 
      for row in curs.fetchall():
        row = list(row)
        ucs.append(row[0])
      curs.close()
      if len(ucs) == 0:
        ucs.append('None')
      return ucs
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting use cases associated with requirement ' + reqName + '  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 

  def getRequirementBacklog(self,reqName):
    try:
      curs = self.conn.cursor()
      curs.execute('call requirementBacklog(%s)',(reqName))
      if (curs.rowcount == -1):
        exceptionText = 'Error getting backlog items associated with requirement ' + reqName
        raise DatabaseProxyException(exceptionText) 
      bis = [] 
      for row in curs.fetchall():
        row = list(row)
        bis.append(row[0])
      curs.close()
      if len(bis) == 0:
        bis.append('None')
      return bis
    except _mysql_exceptions.DatabaseError, e:
      id,msg = e
      exceptionText = 'MySQL error getting backlog items associated with requirement ' + reqName + '  (id:' + str(id) + ',message:' + msg + ')'
      raise DatabaseProxyException(exceptionText) 