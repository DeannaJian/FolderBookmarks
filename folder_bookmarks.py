# -*- coding: utf-8 -*-
# Last modified: June 25, 2020

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

        self.settingsdlg = MySettingsDlg(None)

        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.onSettings, id=self.ID_SETTINGS)
        for ii in range(0, MAX_FOLDER_NUMBER):
            self.id_folder[ii] = wx.NewIdRef(count=1)
            self.Bind(wx.EVT_MENU, lambda evt, temp=ii: self.OnMenu(evt, temp),
                      id=self.id_folder[ii])

    def onExit(self, event):
        wx.Exit()

    def onSettings(self, event):
        self.settingsdlg.SetSettingsDialog()
        self.settingsdlg.Show(True)

    def OnMenu(self, Event, index):
        """
        Open the selected folder in Explorer.
        """
        import os

        os.system("start explorer %s" % favorate_folders[index])

    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    def StripPathString(self, path):
        if len(path) > 20:
            len_last_part = min(path.rfind('\\'), 10)
            path = path[0:(22 - len_last_part)] + '...' + path[-len_last_part:]

        return path

    def getMenuAttrs(self):
        """
        Generate menu items.
        """
        MenuAttrs = []
        for ii in range(0, MAX_FOLDER_NUMBER):
            if favorate_folders[ii]:
                MenuAttrs.append((self.StripPathString(favorate_folders[ii]),
                                  self.id_folder[ii]))
                # print(self.StripPathString(favorate_folders[ii]))

        MenuAttrs.append(('设置', self.ID_SETTINGS))
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

    def SetSettingsDialog(self):
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
        favorate_folders.clear()
        favorate_folders.append(self.m_dirPicker1.GetPath())
        favorate_folders.append(self.m_dirPicker2.GetPath())
        favorate_folders.append(self.m_dirPicker3.GetPath())
        favorate_folders.append(self.m_dirPicker4.GetPath())
        favorate_folders.append(self.m_dirPicker5.GetPath())

        with open('favorate_folders.pkl', 'wb') as ff:
            pickle.dump(favorate_folders, ff)

        self.Show(False)

    def CancelSaving(self, event):
        self.Show(False)


if __name__ == "__main__":
    with open('favorate_folders.pkl', 'rb') as ff:
        favorate_folders = pickle.load(ff)

    app = MyApp()
    app.MainLoop()
