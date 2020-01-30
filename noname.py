# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialog
###########################################################################

class SettingsDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"请选择你的常用目录", pos = wx.DefaultPosition, size = wx.Size( 406,306 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

        self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_dirPicker2, 0, wx.ALL, 5 )

        self.m_dirPicker3 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_dirPicker3, 0, wx.ALL, 5 )

        self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_dirPicker4, 0, wx.ALL, 5 )

        self.m_dirPicker5 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer1.Add( self.m_dirPicker5, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer2.SetMinSize( wx.Size( 400,-1 ) )

        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_buttonSave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.m_buttonSave.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
        self.m_buttonSave.SetBackgroundColour( wx.Colour( 0, 120, 215 ) )

        bSizer2.Add( self.m_buttonSave, 0, wx.ALIGN_CENTER, 5 )

        self.m_buttonCancel = wx.Button( self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer2.Add( self.m_buttonCancel, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


