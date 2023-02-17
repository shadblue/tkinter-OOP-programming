
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
# from matplotlib import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import numpy as np

myfont=('verdana',12)

class SeaofBTCapp(tk.Tk):
    def __init__(self,*args, **kwargs) -> None:
        tk.Tk.__init__(self,*args,**kwargs)
        # iconbitmap(self,default='clienticon.ico')
        container=tk.Frame(self)
        container.pack(side='top',fill='both',expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames={}
        
        for F in (StartPage,PageOne,BTCE_Page):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):
    def __init__(self,parent, controller) -> None:
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text="""Alph Bitcoin Trading Application
                       Use at your own risk
                       There is no promise of warranty""",font=myfont)
        label.pack(pady=10,padx=10)
        
        button1=tk.Button(self,text='Agree',command=lambda: controller.show_frame(BTCE_Page))
        button1.pack()
        
        button2=tk.Button(self,text='Disagree',command=quit)
        button2.pack()
        
        

class PageOne(tk.Frame):
    def __init__(self,parent,controller) -> None:
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text='Page One',font=myfont)
        label.pack(pady=10,padx=10)
        
        button=tk.Button(self,text='Back to Home',command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        # button2=tk.Button(self,text='Visit Page 2',command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
                
# class PageTwo(tk.Frame):
#     def __init__(self,parent,controller) -> None:
#         tk.Frame.__init__(self,parent)
#         label=tk.Label(self,text='Page Two',font=myfont)
#         label.pack(pady=10,padx=10)
        
#         button2=tk.Button(self,text='Back to Home',command=lambda: controller.show_frame(StartPage))
#         button2.pack()
        
#         button2=tk.Button(self,text='Page One',command=lambda: controller.show_frame(PageOne))
#         button2.pack()
#         button2=tk.Button(self,text='Graph Page',command=lambda: controller.show_frame(PageThree))
#         button2.pack()
        
class BTCE_Page(tk.Frame):
    def __init__(self,parent,controller) -> None:
        tk.Frame.__init__(self,parent)
        label=tk.Label(self,text='Graph Page',font=myfont)
        label.pack(pady=10,padx=10)
        
        button2=tk.Button(self,text='Back to Home',command=lambda: controller.show_frame(StartPage))
        button2.pack()
        
        button2=tk.Button(self,text='Page One',command=lambda: controller.show_frame(PageOne))
        button2.pack()
        # button3=tk.Button(self,text='Page Two',command=lambda: controller.show_frame(PageTwo))
        # button3.pack()
        
        f=Figure(figsize=(5,5),dpi=100)
        a=f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        
        canvas=FigureCanvasTkAgg(f,self)
        # canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        
app=SeaofBTCapp()
app.mainloop()
        