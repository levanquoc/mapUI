#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Feb 18, 2021 02:22:45 AM GMT  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    main_support.set_Tk_var()
    top = Toplevel1 (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    main_support.set_Tk_var()
    top = Toplevel1 (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1920x927+57+70")
        top.minsize(136, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.005, rely=0.019, relheight=0.229
                , relwidth=0.198)
        self.Labelframe1.configure(relief='raised')
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(relief="raised")
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")

        self.Button1 = tk.Button(self.Labelframe1)
        self.Button1.place(relx=0.105, rely=0.042, height=44, width=77
                , bordermode='ignore')
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=main_support.createRFID)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''RFID''')

        self.Button2 = tk.Button(self.Labelframe1)
        self.Button2.place(relx=0.105, rely=0.259, height=44, width=77
                , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=main_support.createLinehorizontal)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''LINE''')

        self.Button3 = tk.Button(self.Labelframe1)
        self.Button3.place(relx=0.105, rely=0.476, height=44, width=77
                , bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=main_support.createLinevertical)
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''LINE''')

        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.421, rely=0.344, height=7, width=43
                , bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#000000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.471, rely=0.476, height=39, width=10
                , bordermode='ignore')
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#000000")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Label''')

        self.Labelframe2 = tk.LabelFrame(self.Labelframe1)
        self.Labelframe2.place(relx=0.421, rely=0.042, relheight=0.241
                , relwidth=0.134, bordermode='ignore')
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(background="#0000a0")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")

        self.Button13 = tk.Button(self.Labelframe1)
        self.Button13.place(relx=0.105, rely=0.736, height=44, width=77
                , bordermode='ignore')
        self.Button13.configure(activebackground="#ececec")
        self.Button13.configure(activeforeground="#000000")
        self.Button13.configure(background="#d9d9d9")
        self.Button13.configure(command=main_support.crossroadLine)
        self.Button13.configure(disabledforeground="#a3a3a3")
        self.Button13.configure(foreground="#000000")
        self.Button13.configure(highlightbackground="#d9d9d9")
        self.Button13.configure(highlightcolor="black")
        self.Button13.configure(pady="0")
        self.Button13.configure(text='''CROSSROAD''')

        self.mapFrame = tk.Canvas(top)
        self.mapFrame.place(relx=0.224, rely=0.012, relheight=0.972
                , relwidth=0.788)
        self.mapFrame.configure(background="#d9d9d9")
        self.mapFrame.configure(borderwidth="2")
        self.mapFrame.configure(highlightbackground="#d9d9d9")
        self.mapFrame.configure(highlightcolor="black")
        self.mapFrame.configure(insertbackground="black")
        self.mapFrame.configure(relief="ridge")
        self.mapFrame.configure(selectbackground="blue")
        self.mapFrame.configure(selectforeground="white")

        self.Labelframe3 = tk.LabelFrame(top)
        self.Labelframe3.place(relx=0.005, rely=0.259, relheight=0.348
                , relwidth=0.197)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''PROPERTY_LINE''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")

        self.lenlineEntry = tk.Entry(self.Labelframe3)
        self.lenlineEntry.place(relx=0.235, rely=0.285, height=27, relwidth=0.196
                , bordermode='ignore')
        self.lenlineEntry.configure(background="white")
        self.lenlineEntry.configure(disabledforeground="#a3a3a3")
        self.lenlineEntry.configure(font="TkFixedFont")
        self.lenlineEntry.configure(foreground="#000000")
        self.lenlineEntry.configure(highlightbackground="#d9d9d9")
        self.lenlineEntry.configure(highlightcolor="black")
        self.lenlineEntry.configure(insertbackground="black")
        self.lenlineEntry.configure(selectbackground="blue")
        self.lenlineEntry.configure(selectforeground="white")

        self.Label1 = tk.Label(self.Labelframe3)
        self.Label1.place(relx=0.026, rely=0.588, height=19, width=54
                , bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Head''')

        self.functionEntry = ttk.Combobox(self.Labelframe3)
        self.functionEntry.place(relx=0.235, rely=0.409, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['None','Line','Hook','Position',]
        self.functionEntry.configure(values=self.value_list)
        self.functionEntry.configure(exportselection="0")
        self.functionEntry.configure(state='readonly')
        self.functionEntry.configure(takefocus="")

        self.Label4 = tk.Label(self.Labelframe3)
        self.Label4.place(relx=0.026, rely=0.706, height=29, width=64
                , bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Rotate type''')

        self.headEntry = ttk.Combobox(self.Labelframe3)
        self.headEntry.place(relx=0.238, rely=0.56, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['Front','Back',]
        self.headEntry.configure(values=self.value_list)
        self.headEntry.configure(state='readonly')
        self.headEntry.configure(takefocus="")

        self.Label5 = tk.Label(self.Labelframe3)
        self.Label5.place(relx=0.026, rely=0.288, height=25, width=44
                , bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Len''')

        self.Label7 = tk.Label(self.Labelframe3)
        self.Label7.place(relx=0.529, rely=0.121, height=22, width=64
                , bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Degree rote''')

        self.Label8 = tk.Label(self.Labelframe3)
        self.Label8.place(relx=0.529, rely=0.279, height=21, width=64
                , bordermode='ignore')
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Command''')

        self.Label9 = tk.Label(self.Labelframe3)
        self.Label9.place(relx=0.529, rely=0.415, height=21, width=54
                , bordermode='ignore')
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Line type''')

        self.Label10 = tk.Label(self.Labelframe3)
        self.Label10.place(relx=0.529, rely=0.588, height=21, width=64
                , bordermode='ignore')
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Speed max''')

        self.Label11 = tk.Label(self.Labelframe3)
        self.Label11.place(relx=0.529, rely=0.734, height=12, width=54
                , bordermode='ignore')
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Wait time''')

        self.Label12 = tk.Label(self.Labelframe3)
        self.Label12.place(relx=0.026, rely=0.412, height=21, width=64
                , bordermode='ignore')
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Fucntion''')

        self.Label13 = tk.Label(self.Labelframe3)
        self.Label13.place(relx=0.053, rely=0.136, height=20, width=29
                , bordermode='ignore')
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Index''')

        self.rotatetypeEntry = ttk.Combobox(self.Labelframe3)
        self.rotatetypeEntry.place(relx=0.238, rely=0.706, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['None','Center','Side',]
        self.rotatetypeEntry.configure(values=self.value_list)
        self.rotatetypeEntry.configure(state='readonly')
        self.rotatetypeEntry.configure(takefocus="")

        self.commandEntry = ttk.Combobox(self.Labelframe3)
        self.commandEntry.place(relx=0.751, rely=0.251, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['None','Center','Left','Right',]
        self.commandEntry.configure(values=self.value_list)
        self.commandEntry.configure(state='readonly')
        self.commandEntry.configure(takefocus="")

        self.linetypeEntry = ttk.Combobox(self.Labelframe3)
        self.linetypeEntry.place(relx=0.741, rely=0.402, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['One','Fork Left','Fork Right','Cross',]
        self.linetypeEntry.configure(values=self.value_list)
        self.linetypeEntry.configure(state='readonly')
        self.linetypeEntry.configure(takefocus="")

        self.speedmaxEntry = ttk.Combobox(self.Labelframe3)
        self.speedmaxEntry.place(relx=0.741, rely=0.585, relheight=0.096
                , relwidth=0.193, bordermode='ignore')
        self.value_list = ['Slow','Normal','High',]
        self.speedmaxEntry.configure(values=self.value_list)
        self.speedmaxEntry.configure(state='readonly')
        self.speedmaxEntry.configure(takefocus="")

        self.waittimeEntry = tk.Entry(self.Labelframe3)
        self.waittimeEntry.place(relx=0.741, rely=0.709, height=27
                , relwidth=0.196, bordermode='ignore')
        self.waittimeEntry.configure(background="white")
        self.waittimeEntry.configure(disabledforeground="#a3a3a3")
        self.waittimeEntry.configure(font="TkFixedFont")
        self.waittimeEntry.configure(foreground="#000000")
        self.waittimeEntry.configure(highlightbackground="#d9d9d9")
        self.waittimeEntry.configure(highlightcolor="black")
        self.waittimeEntry.configure(insertbackground="black")
        self.waittimeEntry.configure(selectbackground="blue")
        self.waittimeEntry.configure(selectforeground="white")

        self.indexLineEntry = tk.Entry(self.Labelframe3)
        self.indexLineEntry.place(relx=0.233, rely=0.124, height=27
                , relwidth=0.196, bordermode='ignore')
        self.indexLineEntry.configure(background="white")
        self.indexLineEntry.configure(disabledforeground="#a3a3a3")
        self.indexLineEntry.configure(font="TkFixedFont")
        self.indexLineEntry.configure(foreground="#000000")
        self.indexLineEntry.configure(highlightbackground="#d9d9d9")
        self.indexLineEntry.configure(highlightcolor="black")
        self.indexLineEntry.configure(insertbackground="black")
        self.indexLineEntry.configure(selectbackground="blue")
        self.indexLineEntry.configure(selectforeground="white")

        self.degreeroteEntry = tk.Entry(self.Labelframe3)
        self.degreeroteEntry.place(relx=0.751, rely=0.124, height=27
                , relwidth=0.169, bordermode='ignore')
        self.degreeroteEntry.configure(background="white")
        self.degreeroteEntry.configure(disabledforeground="#a3a3a3")
        self.degreeroteEntry.configure(font="TkFixedFont")
        self.degreeroteEntry.configure(foreground="#000000")
        self.degreeroteEntry.configure(highlightbackground="#d9d9d9")
        self.degreeroteEntry.configure(highlightcolor="black")
        self.degreeroteEntry.configure(insertbackground="black")
        self.degreeroteEntry.configure(selectbackground="blue")
        self.degreeroteEntry.configure(selectforeground="white")

        self.Labelframe5 = tk.LabelFrame(top)
        self.Labelframe5.place(relx=0.005, rely=0.615, relheight=0.098
                , relwidth=0.198)
        self.Labelframe5.configure(relief='groove')
        self.Labelframe5.configure(foreground="black")
        self.Labelframe5.configure(text='''RFID''')
        self.Labelframe5.configure(background="#d9d9d9")
        self.Labelframe5.configure(highlightbackground="#d9d9d9")
        self.Labelframe5.configure(highlightcolor="black")

        self.Label6 = tk.Label(self.Labelframe5)
        self.Label6.place(relx=0.026, rely=0.549, height=10, width=85
                , bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Name''')

        self.nameRFIDEntry = tk.Entry(self.Labelframe5)
        self.nameRFIDEntry.place(relx=0.316, rely=0.516, height=27
                , relwidth=0.168, bordermode='ignore')
        self.nameRFIDEntry.configure(background="white")
        self.nameRFIDEntry.configure(disabledforeground="#a3a3a3")
        self.nameRFIDEntry.configure(font="TkFixedFont")
        self.nameRFIDEntry.configure(foreground="#000000")
        self.nameRFIDEntry.configure(highlightbackground="#d9d9d9")
        self.nameRFIDEntry.configure(highlightcolor="black")
        self.nameRFIDEntry.configure(insertbackground="black")
        self.nameRFIDEntry.configure(selectbackground="blue")
        self.nameRFIDEntry.configure(selectforeground="white")

        self.Label14 = tk.Label(self.Labelframe5)
        self.Label14.place(relx=0.039, rely=0.22, height=19, width=74
                , bordermode='ignore')
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''Index''')

        self.indexCardEntry = tk.Entry(self.Labelframe5)
        self.indexCardEntry.place(relx=0.316, rely=0.132, height=27
                , relwidth=0.168, bordermode='ignore')
        self.indexCardEntry.configure(background="white")
        self.indexCardEntry.configure(disabledforeground="#a3a3a3")
        self.indexCardEntry.configure(font="TkFixedFont")
        self.indexCardEntry.configure(foreground="#000000")
        self.indexCardEntry.configure(highlightbackground="#d9d9d9")
        self.indexCardEntry.configure(highlightcolor="black")
        self.indexCardEntry.configure(insertbackground="black")
        self.indexCardEntry.configure(selectbackground="blue")
        self.indexCardEntry.configure(selectforeground="white")

        self.Labelframe6 = tk.LabelFrame(top)
        self.Labelframe6.place(relx=0.005, rely=0.723, relheight=0.156
                , relwidth=0.197)
        self.Labelframe6.configure(relief='groove')
        self.Labelframe6.configure(foreground="black")
        self.Labelframe6.configure(text='''Labelframe''')
        self.Labelframe6.configure(background="#d9d9d9")
        self.Labelframe6.configure(highlightbackground="#d9d9d9")
        self.Labelframe6.configure(highlightcolor="black")

        self.Label15 = tk.Label(self.Labelframe6)
        self.Label15.place(relx=0.053, rely=0.4, height=21, width=54
                , bordermode='ignore')
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(background="#d9d9d9")
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(foreground="#000000")
        self.Label15.configure(highlightbackground="#d9d9d9")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''Start''')

        self.Label16 = tk.Label(self.Labelframe6)
        self.Label16.place(relx=0.053, rely=0.552, height=21, width=54
                , bordermode='ignore')
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''End''')

        self.startEntry = tk.Entry(self.Labelframe6)
        self.startEntry.place(relx=0.212, rely=0.414, height=17, relwidth=0.167
                , bordermode='ignore')
        self.startEntry.configure(background="white")
        self.startEntry.configure(disabledforeground="#a3a3a3")
        self.startEntry.configure(font="TkFixedFont")
        self.startEntry.configure(foreground="#000000")
        self.startEntry.configure(highlightbackground="#d9d9d9")
        self.startEntry.configure(highlightcolor="black")
        self.startEntry.configure(insertbackground="black")
        self.startEntry.configure(selectbackground="blue")
        self.startEntry.configure(selectforeground="white")

        self.endEntry = tk.Entry(self.Labelframe6)
        self.endEntry.place(relx=0.209, rely=0.552, height=17, relwidth=0.169
                , bordermode='ignore')
        self.endEntry.configure(background="white")
        self.endEntry.configure(disabledforeground="#a3a3a3")
        self.endEntry.configure(font="TkFixedFont")
        self.endEntry.configure(foreground="#000000")
        self.endEntry.configure(highlightbackground="#d9d9d9")
        self.endEntry.configure(highlightcolor="black")
        self.endEntry.configure(insertbackground="black")
        self.endEntry.configure(selectbackground="blue")
        self.endEntry.configure(selectforeground="white")

        self.Button5 = tk.Button(self.Labelframe6)
        self.Button5.place(relx=0.45, rely=0.759, height=24, width=67
                , bordermode='ignore')
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(command=main_support.send)
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''SEND''')

        self.routeEntry = ttk.Combobox(self.Labelframe6)
        self.routeEntry.place(relx=0.217, rely=0.207, relheight=0.145
                , relwidth=0.14, bordermode='ignore')
        self.value_list = ['1','2','3','4','5','6','7','8','9','10',]
        self.routeEntry.configure(values=self.value_list)
        self.routeEntry.configure(textvariable=main_support.combobox)
        self.routeEntry.configure(takefocus="")

        self.Label17 = tk.Label(self.Labelframe6)
        self.Label17.place(relx=0.085, rely=0.214, height=21, width=44
                , bordermode='ignore')
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(background="#d9d9d9")
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(foreground="#000000")
        self.Label17.configure(highlightbackground="#d9d9d9")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Route''')

        self.Button7 = tk.Button(self.Labelframe6)
        self.Button7.place(relx=0.132, rely=0.759, height=24, width=47
                , bordermode='ignore')
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(command=main_support.setupStep)
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''OK''')

        self.Button8 = tk.Button(self.Labelframe6)
        self.Button8.place(relx=0.291, rely=0.759, height=24, width=47
                , bordermode='ignore')
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(command=main_support.reset)
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''RESET''')

if __name__ == '__main__':
    vp_start_gui()





