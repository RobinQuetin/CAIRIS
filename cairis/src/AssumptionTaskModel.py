#$URL: svn://edison.comlab.ox.ac.uk/res08/iris/iris/AssumptionPersonaModel.py $ $Id: AssumptionPersonaModel.py 330 2010-10-31 15:01:28Z shaf $

import DotTrace
import pydot
import wx
import os
import ARM
import gtk
from Borg import Borg

class AssumptionTaskModel:
  def __init__(self,tlinks):
    self.theTraceLinks = tlinks
    b = Borg()
    self.dbProxy = b.dbProxy
    self.fontName = b.fontName
    self.fontSize = b.apFontSize
    self.theGraph = pydot.Dot()
    if (os.name == 'nt'):
      self.theGraphName = 'C:\\arm\\at.dot'
    elif (os.uname()[0] == 'Linux'):
      self.theGraphName = os.environ['IRIS_SCRATCH'] + '/at.dot'
    elif (os.uname()[0] == 'Darwin'):
      self.theGraphName = os.environ['IRIS_SCRATCH'] + '/at.dot'
    else :
      raise ARM.UnsupportedOperatingSystem(os.name)
    self.theGraph.set_graph_defaults(rankdir='LR')

    self.theNodeLookup = {}

  def buildGraph(self):
    self.buildGraph()
 
  def size(self):
    return len(self.theTraceLinks)

  def buildNode(self,dimName,objtName):
    objtUrl = dimName + '#' + str(objtName)
    if (dimName == 'task'):
      self.theGraph.add_node(pydot.Node(objtName,shape='ellipse',fontname=self.fontName,fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'task_characteristic'):
      self.theGraph.add_node(pydot.Node(objtName,shape='record',fontname=self.fontName,style='filled',fillcolor='green',fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'rebuttal'):
      self.theGraph.add_node(pydot.Node(objtName,shape='record',fontname=self.fontName,style='filled',fillcolor='red',fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'qualifier'):
      self.theGraph.add_node(pydot.Node(objtName,shape='rectangle',fontname=self.fontName,style='dashed',fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'warrant'):
      self.theGraph.add_node(pydot.Node(objtName,shape='record',fontname=self.fontName,style='filled',fillcolor='darkslategray3',fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'backing'):
      self.theGraph.add_node(pydot.Node(objtName,shape='record',fontname=self.fontName,style='filled',fillcolor='gray95',fontsize=self.fontSize,URL=objtUrl))
    elif (dimName == 'grounds'):
      self.theGraph.add_node(pydot.Node(objtName,shape='record',fontname=self.fontName,fontsize=self.fontSize,URL=objtUrl))
    else: 
      self.theGraph.add_node(pydot.Node(objtName,shape='point',fontname=self.fontName,label='',fontsize=self.fontSize,URL=objtUrl))

  def graph(self):
    self.nodeNameSet = set([])
    self.dimNameSet = set([])
    self.taskNames = set([])
    self.taskCharacteristics = set([])
    edges = set([])

    for fromName,fromDim,toName,toDim,taskName,tcName in self.theTraceLinks:
      self.taskNames.add(taskName)
      self.taskCharacteristics.add(tcName)

      self.dimNameSet.add(fromDim)
      if (fromName not in self.nodeNameSet):
        self.buildNode(fromDim,fromName)
        self.nodeNameSet.add(fromName)
        self.theNodeLookup[fromName] = fromDim + ' ' + fromName
      self.dimNameSet.add(toDim)
      if (toName not in self.nodeNameSet):
        self.buildNode(toDim,toName)
        self.nodeNameSet.add(toName)
        self.theNodeLookup[toName] = toDim + ' ' + toName
      if ((fromName,toName) not in edges):
        edges.add((fromName,toName)) 
        edge = pydot.Edge(str(fromName),str(toName),URL=fromDim + '#' + toDim)
        self.theGraph.add_edge(edge)
    return self.layout()

  def layout(self,renderer = 'dot'):
    self.theGraph.write_xdot(self.theGraphName,prog=renderer)
    return open(self.theGraphName).read()

  def tasks(self):
    return self.listStore(self.taskNames)

  def characteristics(self):
    return self.listStore(self.taskCharacteristics)

  def listStore(self,unsortedSet):
    modelList = list(unsortedSet)
    modelList.sort(key=str.lower) 
    model = gtk.ListStore(str)
    model.append([''])
    for dim in modelList:
      model.append([dim])
    return model