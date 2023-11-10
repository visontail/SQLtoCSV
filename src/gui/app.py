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
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)
        # TODO - onclose event megcsinálása
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)

    def on_close(self, event):
        self.db.disconnect()
        self.Destroy()