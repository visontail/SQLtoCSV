import os
import wx
import wx.grid
import csv


class TableViewer(wx.Frame):
    def __init__(self, parent, title, database):
        super(TableViewer, self).__init__(parent, title=title, size=(400, 400))
        self.panel = wx.Panel(self)
        # pass database to self.db
        self.db = database
        # connect to database
        self.db.connect()
        # gets tables from database
        tables = self.db.select_tables()
        # creates grid window
        self.grid = wx.grid.Grid(self.panel, -1)
        self.grid.CreateGrid(len(tables), 2)
        # set tables' name in window
        for i, table in enumerate(tables):
            self.grid.SetCellValue(i, 1, table[0])
            # align center
            self.grid.SetCellAlignment(i, 1, wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        # set tables column size
        self.grid.SetColSize(1, 140)
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
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Show(True)
    
    # Function to handle Save button event
    def on_save(self, event):
        # goes through the grid, checks if box is checked
        selected_tables = [i for i in range(self.grid.GetNumberRows()) if self.grid.GetCellValue(i, 0) == '1']
        # if no tables was selected gives a warning
        if not selected_tables:
            wx.MessageBox("No table selected for saving!", "Warning", wx.OK | wx.ICON_WARNING)
            return
        # create a folder to store csv files if it doesn't exist
        csv_folder = 'csv-files'
        os.makedirs(csv_folder, exist_ok=True)
        # goes through selected tables
        for i in selected_tables:
            # gets table name from grid
            table_name = self.grid.GetCellValue(i, 1)
            # gets content of the table
            content = self.db.select_content(table_name)
            # if there's content writes it in the csv file
            if content:
                # file name is the table's name + .csv
                file_name = f"{table_name}.csv"
                file_path = os.path.join(csv_folder, file_name)
                with open(file_path, 'w', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerows(content)
            else:
                wx.MessageBox(f"Table '{table_name}' has no content!", "Warning", wx.OK | wx.ICON_WARNING)
        wx.MessageBox("Saved successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
        # set all checkboxes to unchecked after saving
        for i in range(self.grid.GetNumberRows()):
            self.grid.SetCellValue(i, 0, '0')
    
    # Function to handle on close event
    def on_close(self, event):
        self.db.disconnect()
        wx.MessageBox("Application closing down", "Goodbye", wx.OK | wx.ICON_INFORMATION)
        self.Destroy()