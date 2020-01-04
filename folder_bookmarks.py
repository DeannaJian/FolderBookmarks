# -*- coding: utf-8 -*-
# Last modified: Aug 6, 2020

import wx
import wx.adv
import settings_dlg


MAX_FOLDER_NUMBER = 5


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


if __name__ == "__main__":
    '''Debug Main Frame'''
    #app = MyApp()
    
    '''Debug settings dialog'''
    app = wx.App(False)
    dlg = settings_dlg.SettingsDialog(None)
    dlg.Show(True)

    #start the applications 
    app.MainLoop()
