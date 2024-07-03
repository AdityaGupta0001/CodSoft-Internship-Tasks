import customtkinter
import os
from random import choice
import string
import pyperclip

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.geometry("400x370")
        self.resizable(False,False)
        self.title("Password Generator")
        self.iconbitmap(self.file_path+'/assets/password.ico')

        my_font = customtkinter.CTkFont(family="Roboto", size=23,weight='normal')
        my_font2 = customtkinter.CTkFont(family="Roboto", size=15,weight='normal')

        self.length_label = customtkinter.CTkLabel(self,width=360,height=20, font=my_font2,text_color="#ffffff",fg_color="transparent",text="Enter password length", anchor="w")
        self.length_label.grid(row=0,column=0,padx=20,pady=(20,0))

        self.length_value = ""
        self.generated_password = ""
        self.length = customtkinter.CTkEntry(self, width=360, height=40, font=my_font, text_color="#ffffff", border_color="#ffffff", fg_color="transparent", placeholder_text_color="#999999", corner_radius=8)
        self.length.grid(row=1,column=0, padx=20, pady=(5,10))

        self.password_indicator_label = customtkinter.CTkLabel(self,width=360,height=20, font=my_font2,text_color="#ffffff",fg_color="transparent",text="Generated Password", anchor="w")
        self.password_indicator_label.grid(row=2,column=0,padx=20,pady=(20,0))
        self.password_label = customtkinter.CTkLabel(self, width=360, height=40, font=my_font, text="", anchor="w", fg_color="#333333",corner_radius=8,text_color="#525252")
        self.password_label.grid(row=3,column=0,padx=20,pady=(5,20))

        self.generate_button = customtkinter.CTkButton(self,width=360,height=40,font=my_font, text_color="#ffffff", text="Generate",anchor="center", state='disabled', fg_color="#48017a",hover_color="#7500c7", command=lambda: generate_password())
        self.generate_button.grid(row=4,column=0,padx=20,pady=(20,20))

        self.copy_button = customtkinter.CTkButton(self,width=360,height=40,font=my_font, text_color="#ffffff", text="Copy Password",anchor="center", state='disabled',hover_color="#7500c7", fg_color="#48017a", command=lambda: copy_password())
        self.copy_button.grid(row=5,column=0,padx=20,pady=(0,0))
        
        self.copy_message = customtkinter.CTkLabel(self,width=360,height=20, font=my_font2,text_color="#9c9c9c",fg_color="transparent",text="", anchor="center")
        self.copy_message.grid(row=6, column=0, padx=20, pady=(10,20))

        def button_press(event):
            self.length_value = ""
            for i in self.length.get():
                if i in "0123456789":
                    self.length_value+=i
            self.length.delete(0,customtkinter.END)
            self.length.insert(0,self.length_value)

            if self.length_value!="":   
                self.generate_button.configure(state='normal')
            else:
                self.generate_button.configure(state='disabled')

        def message_box(message):
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            
            def button_func():
                box.destroy()
            label = customtkinter.CTkLabel(box, text=message, font=("Roboto",15))
            label.pack(pady=30)

            button = customtkinter.CTkButton(box, text="OK", command=button_func,hover_color="#7500c7", fg_color="#48017a")
            button.pack()

            box.transient(self)
            box.grab_set()      
            box.focus_set()


        def copy_password():
            pyperclip.copy(self.generated_password)
            self.copy_message.configure(text="Password copied to clipboard")
        def generate_password():
            if int(self.length_value)<8:
                message_box("Minimum password length: 8")
            elif int(self.length_value)>25:
                message_box("Maximum password length: 25")
            else:
                self.generated_password = ""
                uppercase = list(string.ascii_uppercase)
                lowercase = list(string.ascii_lowercase)
                digits = list(string.digits)
                punctuation = list(string.punctuation)

                for i in range(int(self.length_value)):
                    char_type = choice([uppercase,lowercase,digits,punctuation])
                    char = choice(char_type)
                    self.generated_password+=char
                
                self.password_label.configure(text=self.generated_password, fg_color = "#ffffff")
                self.copy_button.configure(state="normal")

            
            
        self.bind("<Key>",button_press)
app = App()
app.mainloop()