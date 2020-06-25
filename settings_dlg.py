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
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"请选择你的常用目录", pos = wx.DefaultPosition, size = wx.Size( 461,306 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, u" ", u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer3.Add( self.m_dirPicker1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer4.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer4.Add( self.m_button3, 0, wx.ALL, 5 )

        self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer4.Add( self.m_dirPicker2, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button4 = wx.Button( self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer5.Add( self.m_button4, 0, wx.ALL, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer5.Add( self.m_button5, 0, wx.ALL, 5 )

        self.m_dirPicker3 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer5.Add( self.m_dirPicker3, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button6 = wx.Button( self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer6.Add( self.m_button6, 0, wx.ALL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"↓", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer6.Add( self.m_button7, 0, wx.ALL, 5 )

        self.m_dirPicker4 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer6.Add( self.m_dirPicker4, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button8 = wx.Button( self, wx.ID_ANY, u"↑", wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        bSizer7.Add( self.m_button8, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,32 ), 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer7.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_dirPicker5 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.Size( 400,-1 ), wx.DIRP_DEFAULT_STYLE )
        bSizer7.Add( self.m_dirPicker5, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )

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

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.item1_down )
        self.m_button2.Bind( wx.EVT_BUTTON, self.item2_up )
        self.m_button3.Bind( wx.EVT_BUTTON, self.item2_down )
        self.m_button4.Bind( wx.EVT_BUTTON, self.item3_up )
        self.m_button5.Bind( wx.EVT_BUTTON, self.item3_down )
        self.m_button6.Bind( wx.EVT_BUTTON, self.item4_up )
        self.m_button7.Bind( wx.EVT_BUTTON, self.item4_down )
        self.m_button8.Bind( wx.EVT_BUTTON, self.item5_up )
        self.m_buttonSave.Bind( wx.EVT_BUTTON, self.SaveSelection )
        self.m_buttonCancel.Bind( wx.EVT_BUTTON, self.CancelSaving )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def item1_down( self, event ):
        pass

    def item2_up( self, event ):
        pass

    def item2_down( self, event ):
        pass

    def item3_up( self, event ):
        pass

    def item3_down( self, event ):
        pass

    def item4_up( self, event ):
        pass

    def item4_down( self, event ):
        pass

    def item5_up( self, event ):
        pass

    def SaveSelection( self, event ):
        pass

    def CancelSaving( self, event ):
        pass


