#$URL: svn://edison.comlab.ox.ac.uk/res08/iris/iris/TaskCharacteristicsDialog.py $ $Id: TaskCharacteristicsDialog.py 249 2010-05-30 17:07:31Z shaf $
import wx
import armid
import TaskCharacteristic
from TaskCharacteristicDialog import TaskCharacteristicDialog
from DialogClassParameters import DialogClassParameters
from TaskCharacteristicDialogParameters import TaskCharacteristicDialogParameters
import ARM
from DimensionBaseDialog import DimensionBaseDialog

class TaskCharacteristicsDialog(DimensionBaseDialog):
  def __init__(self,parent):
    DimensionBaseDialog.__init__(self,parent,armid.TASKCHARACTERISTICS_ID,'Task Characteristics',(930,300),'task.png')
    self.theMainWindow = parent
    idList = [armid.TASKCHARACTERISTICS_CHARLIST_ID,armid.TASKCHARACTERISTICS_BUTTONADD_ID,armid.TASKCHARACTERISTICS_BUTTONDELETE_ID]
    columnList = ['Task','Characteristic']
    self.buildControls(idList,columnList,self.dbProxy.getTaskCharacteristics,'task_characteristic')
    listCtrl = self.FindWindowById(armid.TASKCHARACTERISTICS_CHARLIST_ID)
    listCtrl.SetColumnWidth(0,100)
    listCtrl.SetColumnWidth(1,700)


  def addObjectRow(self,listCtrl,listRow,objt):
    listCtrl.InsertStringItem(listRow,objt.task())
    listCtrl.SetStringItem(listRow,1,objt.characteristic())

  def onAdd(self,evt):
    try:
      addParameters = DialogClassParameters(armid.TASKCHARACTERISTIC_ID,'Add Task Characteristic',TaskCharacteristicDialog,armid.TASKCHARACTERISTIC_BUTTONCOMMIT_ID,self.dbProxy.addTaskCharacteristic,True)
      self.addObject(addParameters)
    except ARM.ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Add task characteristic',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy()
      return

  def onUpdate(self,evt):
    selectedObjt = self.objts[self.deprecatedLabel()]
    objtId = selectedObjt.id()
    try:
      updateParameters = TaskCharacteristicDialogParameters(armid.TASKCHARACTERISTIC_ID,'Edit Task Characteristic',TaskCharacteristicDialog,armid.TASKCHARACTERISTIC_BUTTONCOMMIT_ID,self.dbProxy.updateTaskCharacteristic,False,selectedObjt.task())
      self.updateObject(selectedObjt,updateParameters)
    except ARM.ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Edit task characteristic',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy

  def onDelete(self,evt):
    try:
      self.deleteObject('No task characteristic','Delete task characteristic',self.dbProxy.deleteTaskCharacteristic)
    except ARM.ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Delete task characteristic',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy

  def deprecatedLabel(self):
    listCtrl = self.FindWindowById(armid.TASKCHARACTERISTICS_CHARLIST_ID)
    pItem = listCtrl.GetItem(self.selectedIdx,0)
    pTxt = pItem.GetText()
    charItem = listCtrl.GetItem(self.selectedIdx,1)
    charTxt = charItem.GetText()
    pcLabel = pTxt + '/' + charTxt
    return pcLabel