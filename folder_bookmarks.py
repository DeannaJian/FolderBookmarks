# -*- coding: utf-8 -*-
# Last modified: June 26, 2020

import wx
import wx.adv
import settings_dlg
import pickle
import os

MAX_FOLDER_NUMBER = 5
favorate_folders = []


class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = 'bookmarks_16px.ico'
    TITLE = 'Folder Bookmarks'
    ID_EXIT, ID_SETTINGS = wx.NewIdRef(count=2)
    id_folder = [0] * MAX_FOLDER_NUMBER

    def __init__(self):
        super().__init__()

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
        self.settingsdlg.m_dirPicker1.SetFocus()
        self.settingsdlg.SetSettingsDialog()
        self.settingsdlg.Show(True)

    def OnMenu(self, Event, index):
        """
        Open the selected folder in Explorer.
        """
        os.startfile(favorate_folders[index])

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

        MenuAttrs.append(('设置', self.ID_SETTINGS))
        MenuAttrs.append(('退出', self.ID_EXIT))
        return MenuAttrs


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        FolderBookmarkTaskBarIcon()


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


class MySettingsDlg(settings_dlg.SettingsDialog):
    """
        Dialog for picking favorate folders.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.pickers = (self.m_dirPicker1, self.m_dirPicker2,
                        self.m_dirPicker3, self.m_dirPicker4,
                        self.m_dirPicker5)

    def SetSettingsDialog(self):
        """
           Read current favorates from file.
        """
        for ii in range(0, MAX_FOLDER_NUMBER):
            self.pickers[ii].SetPath(favorate_folders[ii])

    def SaveSelection(self, event):
        """
            Save current selection as favorate folders.
        """
        favorate_folders.clear()

        for ii in range(0, MAX_FOLDER_NUMBER):
            folder_path = self.pickers[ii].GetPath()
            if (os.path.exists(folder_path)):
                favorate_folders.append(folder_path)
            else:
                wx.MessageBox('目录不存在：%s。 不保存该目录。' % folder_path,
                              '提示', wx.OK | wx.ICON_INFORMATION)
                favorate_folders.append('')

        with open('favorate_folders.pkl', 'wb') as ff:
            pickle.dump(favorate_folders, ff)

        self.Show(False)

    def CancelSaving(self, event):
        self.Show(False)

    def move_item_down(self, item_index, direction):
        """
            Move item content (folder path) up or down.
        """
        assert direction in ('down', 'up')

        if direction == 'down':
            dir_picker_a = self.pickers[item_index - 1]
            dir_picker_b = self.pickers[item_index]
        else:
            dir_picker_a = self.pickers[item_index - 1]
            dir_picker_b = self.pickers[item_index - 2]

        temp_path = dir_picker_a.GetPath()
        dir_picker_a.SetPath(dir_picker_b.GetPath())
        dir_picker_b.SetPath(temp_path)

    def item1_down(self, event):
        self.move_item_down(1, 'down')

    def item2_down(self, event):
        self.move_item_down(2, 'down')

    def item3_down(self, event):
        self.move_item_down(3, 'down')

    def item4_down(self, event):
        self.move_item_down(4, 'down')

    def item2_up(self, event):
        self.move_item_down(2, 'up')

    def item3_up(self, event):
        self.move_item_down(3, 'up')

    def item4_up(self, event):
        self.move_item_down(4, 'up')

    def item5_up(self, event):
        self.move_item_down(5, 'up')


if __name__ == "__main__":
    # Initialize the favorate folder list
    settings_file = 'favorate_folders.pkl'

    if not (os.path.exists(settings_file)):
        current_path = os.getcwd()
        favorate_folders = [current_path] * MAX_FOLDER_NUMBER
    else:
        with open(settings_file, 'rb') as ff:
            favorate_folders = pickle.load(ff)
        for ii in range(0, MAX_FOLDER_NUMBER):
            if not (os.path.exists(favorate_folders[ii])):
                favorate_folders[ii] = ''

    app = MyApp()
    app.MainLoop()
