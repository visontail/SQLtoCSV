import wx

import wx.grid


class DatabaseViewer(wx.Frame):
    def __init__(self, parent, title, tables):
        super(DatabaseViewer, self).__init__(parent, title=title, size=(400, 300))
        self.panel = wx.Panel(self)
        
        # Táblázat létrehozása
        self.grid = wx.grid.Grid(self.panel)
        self.grid.CreateGrid(len(tables), 1)

        # Táblák neveinek beállítása
        for i, table in enumerate(tables):
            self.grid.SetCellValue(i, 0, table[0])

        # Grid elrendezése
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)

    def on_close(self, event):
        # Kapcsolat bezárása a program leállításakor
        self.db.disconnect()
        self.Destroy()