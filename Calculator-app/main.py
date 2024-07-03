import customtkinter
import os
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.file_path = os.path.dirname(os.path.realpath(__file__))

        self.geometry("340x545")
        self.resizable(False,False)
        self.title("Calculator")
        self.iconbitmap(self.file_path+'/assets/calculator.ico')


        self.calculation_str = ""


        my_font = customtkinter.CTkFont(family="Roboto", size=22,weight='normal')
        my_font2 = customtkinter.CTkFont(family="Roboto", size=50,weight='bold')
        my_font3 = customtkinter.CTkFont(family="Roboto", size=25,weight='normal')

        # View and Entry Frame and Objects
        self.my_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.my_frame.configure(width=310,height=200)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew",ipady=10)

        self.my_frame.label = customtkinter.CTkLabel(self.my_frame,text="",height=90, width=300,corner_radius=5,fg_color="transparent",anchor="e",font=my_font3)
        self.my_frame.label.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

        self.my_frame.entry = customtkinter.CTkLabel(self.my_frame,text="0",height=90,width=300,fg_color='transparent',anchor="e",font=my_font2,textvariable=self.calculation_str)
        self.my_frame.entry.grid(row=1,column=0,padx=10)

        # Button Frame and Objects
        self.button_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.button_frame.configure(width=310,height=310)
        self.button_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.button_frame.button_ce = customtkinter.CTkButton(self.button_frame,text="CE",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("CE"))
        self.button_frame.button_ce.grid(row=0,column=0,pady=10,padx=10)

        self.button_frame.button_del = customtkinter.CTkButton(self.button_frame,text="DEL",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("BackSpace"))
        self.button_frame.button_del.grid(row=0,column=1,pady=10)

        self.button_frame.button_div = customtkinter.CTkButton(self.button_frame,text="/",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("slash"))
        self.button_frame.button_div.grid(row=0,column=2,pady=10,padx=10)
        
        self.button_frame.button_mul = customtkinter.CTkButton(self.button_frame,text="*",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("asterisk"))
        self.button_frame.button_mul.grid(row=0,column=3,pady=10)

        self.button_frame.button_7 = customtkinter.CTkButton(self.button_frame,text="7",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("7"))
        self.button_frame.button_7.grid(row=1,column=0)

        self.button_frame.button_8 = customtkinter.CTkButton(self.button_frame,text="8",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("8"))
        self.button_frame.button_8.grid(row=1,column=1)

        self.button_frame.button_9 = customtkinter.CTkButton(self.button_frame,text="9",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("9"))
        self.button_frame.button_9.grid(row=1,column=2)
        
        self.button_frame.button_min = customtkinter.CTkButton(self.button_frame,text="-",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("minus"))
        self.button_frame.button_min.grid(row=1,column=3)

        self.button_frame.button_4 = customtkinter.CTkButton(self.button_frame,text="4",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("4"))
        self.button_frame.button_4.grid(row=2,column=0,pady=10)

        self.button_frame.button_5 = customtkinter.CTkButton(self.button_frame,text="5",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("5"))
        self.button_frame.button_5.grid(row=2,column=1,pady=10)

        self.button_frame.button_6 = customtkinter.CTkButton(self.button_frame,text="6",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("6"))
        self.button_frame.button_6.grid(row=2,column=2,pady=10)
        
        self.button_frame.button_plus = customtkinter.CTkButton(self.button_frame,text="+",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("plus"))
        self.button_frame.button_plus.grid(row=2,column=3,pady=10)

        self.button_frame.button_1 = customtkinter.CTkButton(self.button_frame,text="1",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("1"))
        self.button_frame.button_1.grid(row=3,column=0)

        self.button_frame.button_2 = customtkinter.CTkButton(self.button_frame,text="2",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("2"))
        self.button_frame.button_2.grid(row=3,column=1)

        self.button_frame.button_3 = customtkinter.CTkButton(self.button_frame,text="3",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("3"))
        self.button_frame.button_3.grid(row=3,column=2)

        self.button_frame.button_mod = customtkinter.CTkButton(self.button_frame,text="%",corner_radius=10,width=66,height=45,font=my_font,fg_color="#828282",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("percent"))
        self.button_frame.button_mod.grid(row=3,column=3)
        
        self.button_frame.button_equals = customtkinter.CTkButton(self.button_frame,text="=",corner_radius=10,width=66,height=45,font=my_font,fg_color="#e87d48",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("="))
        self.button_frame.button_equals.grid(row=4,column=3)
        
        self.button_frame.button_0 = customtkinter.CTkButton(self.button_frame,text="0",corner_radius=10,width=130,anchor="center",height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("0"))
        self.button_frame.button_0.grid(row=4,column=0,columnspan=2,pady=10)

        self.button_frame.button_dot = customtkinter.CTkButton(self.button_frame,text=".",corner_radius=10,width=66,height=45,font=my_font,fg_color="#4E4E4E",text_color="#ffffff",hover_color="#000000", command=lambda: button_click("period"))
        self.button_frame.button_dot.grid(row=4,column=2,pady=10)


        def button_press(event):
            
            if event.keysym == "Escape":
                self.calculation_str=""
                self.my_frame.entry.configure(text="0",font=my_font2)
                self.my_frame.label.configure(text="")
            
            if event.keysym == "Return":
                if self.calculation_str!="":
                    try:
                        res = eval(self.calculation_str)
                        if len(str(res))>10:
                            self.my_frame.entry.configure(font=customtkinter.CTkFont(family="Roboto", size=30,weight='bold'))
                        if len(str(res))>16:
                            self.my_frame.entry.configure(font=customtkinter.CTkFont(family="Roboto", size=20,weight='bold'))
                        if "." in str(res):
                            res=round(res,5)
                        self.my_frame.entry.configure(text=str(res))
                        if len(self.calculation_str)>17:
                            self.my_frame.label.configure(text="Result=")
                        else:
                            self.my_frame.label.configure(text=self.calculation_str+"=")
                        self.calculation_str=str(res)
                    except:
                        self.my_frame.label.configure(text=self.calculation_str+"=")
                        self.my_frame.entry.configure(text="Error")
            
            if event.keysym == "BackSpace":
                self.calculation_str=self.calculation_str[0:(len(self.calculation_str)-1)]
                try:
                    self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])
                except:
                    self.my_frame.entry.configure(text="0",font=my_font2)
                    self.my_frame.label.configure(text="")

            if event.keysym in ["0","1","2","3","4","5","6","7","8","9"]:
                self.calculation_str+=event.keysym
                self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])

            data = {"period":".","plus":"+","minus":"-","asterisk":"*","slash":"/","percent":"%"}

            if event.keysym in data.keys():
                if self.my_frame.entry.cget("text")!="":
                    if self.calculation_str[-1] not in data.values():
                        self.calculation_str+=data[event.keysym]
                        self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])
        
        def button_click(value):
            if value=="CE":
                self.calculation_str=""
                self.my_frame.entry.configure(text="0",font=my_font2)
                self.my_frame.label.configure(text="")

            if value=="=":
                if self.calculation_str!="":
                    try:
                        res = eval(self.calculation_str)
                        if len(str(res))>10:
                            self.my_frame.entry.configure(font=customtkinter.CTkFont(family="Roboto", size=30,weight='bold'))
                        if len(str(res))>16:
                            self.my_frame.entry.configure(font=customtkinter.CTkFont(family="Roboto", size=20,weight='bold'))
                        if "." in str(res):
                            res=round(res,5)
                        self.my_frame.entry.configure(text=str(res))
                        if len(self.calculation_str)>17:
                            self.my_frame.label.configure(text="Result=")
                        else:
                            self.my_frame.label.configure(text=self.calculation_str+"=")
                        self.calculation_str=str(res)
                    except:
                        self.my_frame.label.configure(text=self.calculation_str+"=")
                        self.my_frame.entry.configure(text="Error")

            if value == "BackSpace":
                self.calculation_str=self.calculation_str[0:(len(self.calculation_str)-1)]
                try:
                    self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])
                except:
                    self.my_frame.entry.configure(text="0",font=my_font2)
                    self.my_frame.label.configure(text="")

            if value in ["0","1","2","3","4","5","6","7","8","9"]:
                self.calculation_str+=value
                self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])
            
            data = {"period":".","plus":"+","minus":"-","asterisk":"*","slash":"/","percent":"%"}
            
            if value in data.keys():
                if self.my_frame.entry.cget("text")!="":
                    if self.calculation_str[-1] not in data.values():
                        self.calculation_str+=data[value]
                        self.my_frame.entry.configure(text=self.calculation_str[-10:-1]+self.calculation_str[-1])

        self.bind("<Key>",button_press)

app = App()
app.mainloop()