import os
import wx

class MyPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.my_text = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        btn0 = wx.Button(self, label='Open File')
        btn0.Bind(wx.EVT_BUTTON, self.onOpen)
        btn1 = wx.Button(self, label='Save File')
        btn1.Bind(wx.EVT_BUTTON, self.OnSaveAs)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.my_text, 1, wx.ALL|wx.EXPAND)
        sizer.Add(btn0, 0, wx.ALL|wx.CENTER, 5)
        sizer.Add(btn1, 0, wx.ALL|wx.CENTER, 5)

        self.SetSizer(sizer)

    def onOpen(self, event):
        wildcard = "All files (*.*)|*.*"
        dialog = wx.FileDialog(self, "Open File", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return

        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as fobj:
                for line in fobj:
                    self.my_text.WriteText(line)

    def OnSaveAs(self, event):
        with wx.FileDialog(self, "Save my file", wildcard="All files (*.*)|*.cl",
                        style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    file.write(self.my_text.GetValue())
                    file.close()
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)

class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='Proyecto#1 de Compiladores')

        panel = MyPanel(self)

        self.Show()

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()