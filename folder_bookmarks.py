# -*- coding: utf-8 -*-
# Last modified: Aug 6, 2020

import wx
import wx.adv
import settings_dlg
import pickle

MAX_FOLDER_NUMBER = 5
favorate_folders = []


class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = 'bookmarks_16px.ico'
    TITLE = 'Folder Bookmarks'
    ID_EXIT, ID_SETTINGS = wx.NewIdRef(count=2)
    id_folder = [0] * MAX_FOLDER_NUMBER

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)

        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onSettings, id=self.ID_SETTINGS)
        for ii in range(0, MAX_FOLDER_NUMBER):
            self.id_folder[ii] = wx.NewIdRef(count=1)
            self.Bind(wx.EVT_MENU, lambda evt, temp=ii: self.OnMenu(evt, temp),
                      id=self.id_folder[ii])

    def onExit(self, event):
        wx.Exit()

    def onSettings(self, event):
        '''
        dlg = MySettingsDlg(None)
        dlg.ShowSettingsDialog()
        dlg.Show(True)
        '''
        pass

    def OnMenu(self, Event, index):
        """
        Open the selected folder in Explorer.
        """
        msg = u"打开目录#" + str(index)
        wx.MessageBox(msg)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    def getMenuAttrs(self):
        """
        Generate menu items from file.
        If the file is empty or corrupted, open Settings dialog.
        """
        MenuAttrs = []
        for ii in range(0, MAX_FOLDER_NUMBER):
            MenuAttrs.append((u'打开目录#' + str(ii), self.id_folder[ii]))

        MenuAttrs.append(('设置', self.ID_EXIT))
        MenuAttrs.append(('退出', self.ID_EXIT))
        return MenuAttrs


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        FolderBookmarkTaskBarIcon()


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


class MySettingsDlg(settings_dlg.SettingsDialog):
    """
        Dialog for picking favorate folders.
    """

    def ShowSettingsDialog(self):
        """
           Read current favorates from file.
        """
        self.m_dirPicker1.SetPath(favorate_folders[0])
        self.m_dirPicker2.SetPath(favorate_folders[1])
        self.m_dirPicker3.SetPath(favorate_folders[2])
        self.m_dirPicker4.SetPath(favorate_folders[3])
        self.m_dirPicker5.SetPath(favorate_folders[4])

    def SaveSelection(self, event):
        """
            Save current selection as favorate folders.
        """
        temp_favorates = []
        temp_favorates.append(self.m_dirPicker1.GetPath())
        temp_favorates.append(self.m_dirPicker2.GetPath())
        temp_favorates.append(self.m_dirPicker3.GetPath())
        temp_favorates.append(self.m_dirPicker4.GetPath())
        temp_favorates.append(self.m_dirPicker5.GetPath())

        with open('favorate_folders.pkl', 'wb') as ff:
            pickle.dump(temp_favorates, ff)

        self.Show(False)

    def CancelSaving(self, event):
        self.Show(False)


if __name__ == "__main__":
    '''Debug Main Frame'''
    app = MyApp()
    with open('favorate_folders.pkl', 'rb') as ff:
        favorate_folders = pickle.load(ff)

    '''
    app = wx.App(False)
    dlg = MySettingsDlg(None)
    dlg.ShowSettingsDialog()
    dlg.Show(True)
    '''

    #start the applications 
    app.MainLoop()
