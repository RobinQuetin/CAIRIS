#$URL: svn://edison.comlab.ox.ac.uk/res08/iris/iris/ThreatDialog.py $ $Id: ThreatDialog.py 249 2010-05-30 17:07:31Z shaf $
import wx
import armid
import WidgetFactory
import ARM
from Borg import Borg
from ThreatParameters import ThreatParameters
from ThreatPanel import ThreatPanel

class ThreatDialog(wx.Dialog):
  def __init__(self,parent,parameters):
    wx.Dialog.__init__(self,parent,parameters.id(),parameters.label(),style=wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.THICK_FRAME|wx.RESIZE_BORDER,size=(400,500))
    self.theThreatId = -1
    self.theThreatName = ''
    self.theThreatType = ''
    self.theThreatMethod = ''
    self.theEnvironmentProperties = []
    self.panel = 0
    self.buildControls(parameters)
    self.theCommitVerb = 'Add'
    
  def buildControls(self,parameters):
    mainSizer = wx.BoxSizer(wx.VERTICAL)
    self.panel = ThreatPanel(self)
    self.panel.buildControls(parameters.createFlag())
    mainSizer.Add(self.panel,1,wx.EXPAND)
    self.SetSizer(mainSizer)
    wx.EVT_BUTTON(self,armid.THREAT_BUTTONCOMMIT_ID,self.onCommit)


  def load(self,threat):
    self.theThreatId = threat.id() 
    self.panel.loadControls(threat)
    self.theCommitVerb = 'Edit'

  def onCommit(self,evt):
    nameCtrl = self.FindWindowById(armid.THREAT_TEXTNAME_ID)
    typeCtrl = self.FindWindowById(armid.THREAT_THREATTYPE_ID)
    methodCtrl = self.FindWindowById(armid.THREAT_TEXTMETHOD_ID)
    environmentCtrl = self.FindWindowById(armid.THREAT_PANELENVIRONMENT_ID)

    self.theThreatName = nameCtrl.GetValue()
    if (self.theCommitVerb == 'Add'):
      b = Borg()
      try:
        b.dbProxy.nameCheck(self.theThreatName,'threat')
      except ARM.ARMException,errorText:
        dlg = wx.MessageDialog(self,str(errorText),'Add threat',wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()
        return

    self.theThreatType = typeCtrl.GetValue()
    self.theThreatMethod = methodCtrl.GetValue()
    self.theEnvironmentProperties = environmentCtrl.environmentProperties()

    commitLabel = self.theCommitVerb + ' threat'

    if len(self.theThreatName) == 0:
      dlg = wx.MessageDialog(self,'Threat name cannot be empty',commitLabel,wx.OK) 
      dlg.ShowModal()
      dlg.Destroy()
      return
    if len(self.theThreatType) == 0:
      dlg = wx.MessageDialog(self,'Threat type cannot be empty',commitLabel,wx.OK) 
      dlg.ShowModal()
      dlg.Destroy()
      return
    elif len(self.theThreatMethod) == 0:
      dlg = wx.MessageDialog(self,'Method cannot be empty',commitLabel,wx.OK) 
      dlg.ShowModal()
      dlg.Destroy()
      return
    else:
      for environmentProperties in self.theEnvironmentProperties:
        if len(environmentProperties.likelihood()) == 0:
          errorTxt = 'No likelihood associated with environment ' + environmentProperties.name()
          dlg = wx.MessageDialog(self,errorTxt,commitLabel,wx.OK)
          dlg.ShowModal()
          dlg.Destroy()
          return
        if len(environmentProperties.attackers()) == 0:
          errorTxt = 'No attackers associated with environment ' + environmentProperties.name()
          dlg = wx.MessageDialog(self,errorTxt,commitLabel,wx.OK)
          dlg.ShowModal()
          dlg.Destroy()
          return
        if len(environmentProperties.assets()) == 0:
          errorTxt = 'No assets associated with environment ' + environmentProperties.name()
          dlg = wx.MessageDialog(self,errorTxt,commitLabel,wx.OK)
          dlg.ShowModal()
          dlg.Destroy()
          return
        if len(environmentProperties.properties()) == 0:
          errorTxt = 'No security properties associated with environment ' + environmentProperties.name()
          dlg = wx.MessageDialog(self,errorTxt,commitLabel,wx.OK)
          dlg.ShowModal()
          dlg.Destroy()
          return
      self.EndModal(armid.THREAT_BUTTONCOMMIT_ID)

  def parameters(self):
    parameters = ThreatParameters(self.theThreatName,self.theThreatType,self.theThreatMethod,self.theEnvironmentProperties)
    parameters.setId(self.theThreatId)
    return parameters