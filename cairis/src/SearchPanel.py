#$URL: svn://edison.comlab.ox.ac.uk/res08/iris/iris/AssetPanel.py $ $Id: AssetPanel.py 330 2010-10-31 15:01:28Z shaf $
import wx
import armid
import DialogClassParametersFactory
from ProjectSettingsDialog import ProjectSettingsDialog
from SearchOptionsPanel import SearchOptionsPanel
from Borg import Borg

class SearchPanel(wx.Panel):
  def __init__(self,parent):
    wx.Panel.__init__(self,parent,armid.SEARCHMODEL_PANEL_ID)
    mainSizer = wx.BoxSizer(wx.VERTICAL)
    b = Borg()
    self.dbProxy = b.dbProxy
    findBox = wx.StaticBox(self,-1,'Find')
    findBoxSizer = wx.StaticBoxSizer(findBox,wx.HORIZONTAL)
    mainSizer.Add(findBoxSizer,0,wx.EXPAND)
    ssCtrl = wx.TextCtrl(self,armid.SEARCHMODEL_TEXTSEARCHSTRING_ID,'')
    findBoxSizer.Add(ssCtrl,1,wx.EXPAND)
    findCtrl = wx.Button(self,armid.SEARCHMODEL_BUTTONFIND_ID,'Find')
    findBoxSizer.Add(findCtrl,0)

    self.spNotebook = wx.Notebook(self,-1)
    
    spPage = wx.Panel(self.spNotebook)
    spPageSizer = wx.BoxSizer(wx.VERTICAL)

    self.listCtrl = wx.ListCtrl(spPage,armid.SEARCHMODEL_LISTRESULTS_ID,style=wx.LC_REPORT)
    self.listCtrl.InsertColumn(0,'Environment')
    self.listCtrl.InsertColumn(1,'Type')
    self.listCtrl.InsertColumn(2,'Name')

    spPageSizer.Add(self.listCtrl,1,wx.EXPAND)
    spPage.SetSizer(spPageSizer)
    self.spNotebook.AddPage(spPage,'Results')

    optPage = wx.Panel(self.spNotebook)
    optPageSizer = wx.BoxSizer(wx.VERTICAL)
    self.optPanel = SearchOptionsPanel(optPage)
    optPageSizer.Add(self.optPanel)
    optPage.SetSizer(optPageSizer)
    self.spNotebook.AddPage(optPage,'Options')

    mainSizer.Add(self.spNotebook,1,wx.EXPAND)


    self.listCtrl.SetColumnWidth(0,150)
    self.listCtrl.SetColumnWidth(1,150)
    self.listCtrl.SetColumnWidth(2,500)
    self.listCtrl.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.onItemActivated)
    self.SetSizer(mainSizer)

  def onItemActivated(self,evt):
    idx = evt.GetIndex()
    envName = (self.listCtrl.GetItem(idx,0)).GetText()
    dimLabel = (self.listCtrl.GetItem(idx,1)).GetText()
    objtName = (self.listCtrl.GetItem(idx,2)).GetText()
    b = Borg()
    reqGrid = b.mainFrame.FindWindowById(armid.ID_REQGRID)
    reqGrid.ClearSelection()

    if (dimLabel == 'Requirement'):
      scName,idx = objtName.split('-')
      gridIdx = int(idx) - 1
      dimName,objtName = self.dbProxy.dimensionNameByShortCode(scName)
      reqPanel = b.mainFrame.FindWindowById(armid.RMPANEL_ID)
      if (dimName == 'asset'):
        reqPanel.updateObjectSelection(objtName)
      else:
        reqPanel.updateEnvironmentSelection(objtName)
      reqGrid.SelectRow(gridIdx) 
    elif (dimLabel == 'Project Settings'):
      pSettings = self.dbProxy.getProjectSettings()
      pDict = self.dbProxy.getDictionary()
      contributors = self.dbProxy.getContributors()
      revisions = self.dbProxy.getRevisions()
      dlg = ProjectSettingsDialog(self,pSettings,pDict,contributors,revisions)
      if (dlg.ShowModal() == armid.PROJECTSETTINGS_BUTTONCOMMIT_ID):
        self.dbProxy.updateSettings(dlg.name(),dlg.background(),dlg.goals(),dlg.scope(),dlg.definitions(),dlg.contributors(),dlg.revisions(),dlg.richPicture(),self.b.fontSize,self.b.fontName)
      dlg.Destroy()
    else:
      dcp,dimName,dimDlg,dlgCode,dimFn = DialogClassParametersFactory.build(dimLabel)
      if (dimDlg != None):
        if (dimName == 'misusecase'):
          dlg = dimDlg(self)
        else:
          dlg = dimDlg(self,dcp)
        dlg.load(self.dbProxy.dimensionObject(objtName,dimName))
        if (dlg.ShowModal() == dlgCode):
          dimFn(dlg.parameters()) 
        dlg.Destroy()