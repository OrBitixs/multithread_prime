import math
import wx
import multiprocessing as mp

def prime_number(num: int) -> bool:
    i = 2
    while(i <= math.floor(math.sqrt(num))):
        if (num%i==0):
            return False
        i += 1
    return True


class MyFrame(wx.Frame):

    def __init__(self):
        super(MyFrame, self).__init__(parent=None, title = "No title")


    def InitUI(self, prime: bool, num: int):
        txt = str(num) + " is "
        if prime:
            txt=txt+"a prime"
        else:
            txt=txt+"not a prime"

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        font = wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)

        st1 = wx.StaticText(pnl, label=txt, style=wx.ALIGN_LEFT)

        st1.SetFont(font)

        vbox.Add(st1, flag=wx.ALL, border=15)

        pnl.SetSizer(vbox)

        self.SetTitle('Bittersweet')
        self.Centre()

def display(num: int):
    app = wx.App()
    frame = MyFrame()
    frame.InitUI(prime_number(num), num)
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    while(True):
        inp = int(input())
        p = mp.Process(target=display, args=(inp,))
        p.start()
        p.join(0.1)
#        print(p.exitcode)
