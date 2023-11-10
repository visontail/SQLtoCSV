import wx

import wx.grid


class TableViewer(wx.Frame):
    def __init__(self, parent, title, tables):
        super(TableViewer, self).__init__(parent, title=title, size=(400, 300))
        self.panel = wx.Panel(self)
        
        # create table
        self.grid = wx.grid.Grid(self.panel, -1)
        self.grid.CreateGrid(len(tables), 2)
        # set Tables' Name
        for i, table in enumerate(tables):
            self.grid.SetCellValue(i, 1, table[0])
            # align center
            self.grid.SetCellAlignment(i, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # first column for checkbox
        for i in range (len(tables)):
            self.grid.SetCellRenderer(i, 0, wx.grid.GridCellBoolRenderer())
            self.grid.SetCellEditor(i, 0, wx.grid.GridCellBoolEditor())
            # align center
            self.grid.SetCellAlignment(i, 0, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # grid arrangement
        grid_sizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer.Add(self.grid, 1, wx.EXPAND)
        # add save button
        save_button = wx.Button(self.panel, label="Save")
        save_button.Bind(wx.EVT_BUTTON, self.on_save)
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.AddStretchSpacer()
        button_sizer.Add(save_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)
        
        # window arrengement
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid_sizer, 1, wx.EXPAND)
        sizer.Add(button_sizer, 0, wx.EXPAND)
        self.panel.SetSizer(sizer)
        # TODO - onclose event
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)

    def on_save(self, event):
        # TODO - onsave event megcsinálni
        pass

    def on_close(self, event):
        # TODO - onclose event megcsinálni
        self.db.disconnect()
        self.Destroy()