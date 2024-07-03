import customtkinter
from PIL import Image
import os
from random import choice

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.file_path = os.path.dirname(os.path.realpath(__file__))
        self.geometry("400x500")
        self.resizable(False,False)
        self.title("Rock Paper Scissors")
        self.iconbitmap(self.file_path+'/assets/rock-paper-scissors.ico')

        my_font = customtkinter.CTkFont(family="Roboto", size=70,weight='bold')
        my_font3 = customtkinter.CTkFont(family="Roboto", size=15,weight='normal')
        
        self.user_score = 0
        self.computer_score = 0
        
        
        self.rock = customtkinter.CTkImage(Image.open(self.file_path+"/assets/stone.png"),size=(35,35))
        self.paper = customtkinter.CTkImage(Image.open(self.file_path+"/assets/paper.png"),size=(35,35))
        self.scissors = customtkinter.CTkImage(Image.open(self.file_path+"/assets/scissors.png"),size=(35,35))
        self.score = customtkinter.CTkImage(Image.open(self.file_path+"/assets/score.png"),size=(30,30))

        self.my_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.my_frame.configure(width=350,height=25)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10, columnspan = 2)

        self.my_frame.label = customtkinter.CTkLabel(self.my_frame,text="Press Play",height=20,width=360, corner_radius=5,fg_color="transparent",font=my_font3)
        self.my_frame.label.grid(row=0,column=0,pady=10,padx=10)

        self.label = customtkinter.CTkLabel(self,text="",height=20,width=360, corner_radius=5,fg_color="transparent",anchor="center",font=my_font3)
        self.label.grid(row=1,column=0,pady=10,padx=10, columnspan = 2)


        self.user_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.user_frame.configure(width=180,height=125)
        self.user_frame.grid(row=2, column=0, padx=10, pady=10)

        self.user_frame.label = customtkinter.CTkLabel(self.user_frame,text="You",height=20,width=160, corner_radius=5,fg_color="transparent",font=my_font3)
        self.user_frame.label.grid(row=0,column=0, padx=10, pady=10)
        self.user_frame.rock = customtkinter.CTkButton(self.user_frame,image=self.rock,text="   Rock     ",width=160,height=20,font=my_font3, fg_color="#240257", anchor="center", hover_color="#6502fa", compound="right", text_color="#ffffff", command=lambda: users_choice("Rock"))
        self.user_frame.rock.grid(row=1,column=0, padx=10, pady=10)
        self.user_frame.paper = customtkinter.CTkButton(self.user_frame,image=self.paper,text="   Paper    ",width=160,height=20,font=my_font3, fg_color="#240257", anchor="center", hover_color="#6502fa", compound="right", text_color="#ffffff", command=lambda: users_choice("Paper"))
        self.user_frame.paper.grid(row=2,column=0, padx=10, pady=10)
        self.user_frame.scissors = customtkinter.CTkButton(self.user_frame,image=self.scissors,text="   Scissors ",width=160,height=20,font=my_font3, fg_color="#240257", anchor="center", hover_color="#6502fa", compound="right", text_color="#ffffff", command=lambda: users_choice("Scissors"))
        self.user_frame.scissors.grid(row=3,column=0, padx=10, pady=10)

        self.computer_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.computer_frame.configure(width=180,height=125)
        self.computer_frame.grid(row=2, column=1, padx=10, pady=10)

        self.computer_frame.label = customtkinter.CTkLabel(self.computer_frame,text="Computer",height=20,width=160, corner_radius=5,fg_color="transparent",font=my_font3)
        self.computer_frame.label.grid(row=0,column=0, padx=10, pady=10)
        self.computer_frame.rock = customtkinter.CTkButton(self.computer_frame,image=self.rock,text="   Rock     ",width=160,height=20,font=my_font3, fg_color="#820309", anchor="center", hover_color="#ff0000", compound="right", state="disabled", text_color_disabled="#ffffff")
        self.computer_frame.rock.grid(row=1,column=0, padx=10, pady=10)
        self.computer_frame.paper = customtkinter.CTkButton(self.computer_frame,image=self.paper,text="   Paper    ",width=160,height=20,font=my_font3, fg_color="#820309", anchor="center", hover_color="#ff0000", compound="right", state="disabled", text_color_disabled="#ffffff")
        self.computer_frame.paper.grid(row=2,column=0, padx=10, pady=10)
        self.computer_frame.scissors = customtkinter.CTkButton(self.computer_frame,image=self.scissors,text="   Scissors ",width=160,height=20,font=my_font3, fg_color="#820309", anchor="center", hover_color="#ff0000", compound="right", state="disabled", text_color_disabled="#ffffff")
        self.computer_frame.scissors.grid(row=3,column=0, padx=10, pady=10)

        self.score_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.score_frame.configure(width=380,height=35)
        self.score_frame.grid(row=3, column=0, padx=10, pady=10, columnspan = 2)
        self.score_frame.label = customtkinter.CTkLabel(self.score_frame,text="Score ",height=35,width=60, corner_radius=5,fg_color="#383838",anchor="w",font=my_font3, image=self.score, compound="right")
        self.score_frame.label.grid(row=0,column=0,pady=10,padx=10,ipady=2)
        self.score_frame.label_you = customtkinter.CTkLabel(self.score_frame,text=f"You: {self.user_score}",height=25,width=60, corner_radius=5,fg_color="#240257",anchor="w",font=my_font3)
        self.score_frame.label_you.grid(row=0,column=1,pady=10,padx=10)
        self.score_frame.label_computer = customtkinter.CTkLabel(self.score_frame,text=f"Computer: {self.computer_score}",height=25,width=60, corner_radius=5,fg_color="#820309",anchor="w",font=my_font3)
        self.score_frame.label_computer.grid(row=0,column=2,pady=10,padx=10)

        self.my_frame3 = MyFrame(master=self,border_width=0,border_color="#ffffff",fg_color = "transparent")
        self.my_frame3.configure(width=380,height=40)
        self.my_frame3.grid(row=4, column=0, padx=10, columnspan=2)

        self.my_frame3.reset = customtkinter.CTkButton(self.my_frame3,text="Play",width=170,height=35,font=my_font3, fg_color="#FF8C00", hover_color="#FFA500", command=lambda: play(self.round))
        self.my_frame3.reset.grid(row=0, column=0, pady=10, padx=10)
        
        self.my_frame3.exit = customtkinter.CTkButton(self.my_frame3,text="Exit",width=170,height=35,font=my_font3, fg_color="#b50404", hover_color="#fc3030", command=lambda: exit())
        self.my_frame3.exit.grid(row=0, column=1, pady=10, padx=10)

        self.user_choice = " "
        self.computer_choice = " "
        self.round = 1

        def update_scores():
            self.score_frame.label_you.configure(text = f"You: {self.user_score}")
            self.score_frame.label_computer.configure(text = f"Computer: {self.computer_score}")

        def waithere(sec):
            var = customtkinter.IntVar()
            app.after(sec, var.set, 1)
            app.wait_variable(var)

        def exit():
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            box.iconbitmap(self.file_path+'/assets/rock-paper-scissors.ico')

            label = customtkinter.CTkLabel(box, text="Are you sure you want to exit the app?", font=my_font3, anchor="center")
            label.grid(row=0,column=0,pady=30, columnspan=2, padx=25)

            button = customtkinter.CTkButton(box, text="Cancel", command=box.destroy, width=120)
            button.grid(row=1,column=0,padx=10)
            button2 = customtkinter.CTkButton(box, text="Exit", command=self.destroy,width=120, fg_color="#b50404", hover_color="#fc3030")
            button2.grid(row=1,column=1,padx=10)

            box.transient(self)
            box.grab_set()      
            box.focus_set()

        def clear_choices():
            self.user_frame.rock.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff" )
            self.user_frame.paper.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            self.user_frame.scissors.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")

            self.computer_frame.rock.configure(fg_color = "#820309")
            self.computer_frame.paper.configure(fg_color = "#820309")
            self.computer_frame.scissors.configure(fg_color = "#820309")

            self.user_choice = " "
            self.computer_choice = " "
        
        def message_box(message):
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            box.iconbitmap(self.file_path+'/assets/rock-paper-scissors.ico')
            
            def button_func():
                reset()
                box.destroy()
            label = customtkinter.CTkLabel(box, text=message, font=my_font3)
            label.pack(pady=30)

            button = customtkinter.CTkButton(box, text="OK", command=button_func)
            button.pack()

            box.transient(self)
            box.grab_set()      
            box.focus_set()

        def game_over():
            if self.user_score>self.computer_score:
                message_box("You win!!")
            elif self.user_score<self.computer_score:
                message_box("Computer Wins!!")
            else:
                message_box("Its a tie")
        
        def users_choice(value):
            self.user_choice = value
            if self.user_choice == "Rock":
                self.user_frame.rock.configure(fg_color = "#6502fa", state = "disabled", text_color_disabled="#ffffff" )
                self.user_frame.paper.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
                self.user_frame.scissors.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            elif self.user_choice == "Paper":
                self.user_frame.rock.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
                self.user_frame.paper.configure(fg_color = "#6502fa", state = "disabled", text_color_disabled="#ffffff")
                self.user_frame.scissors.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            elif self.user_choice == "Scissors":
                self.user_frame.rock.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
                self.user_frame.paper.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
                self.user_frame.scissors.configure(fg_color = "#6502fa", state = "disabled", text_color_disabled="#ffffff")

            self.computer_choice = choice(["Rock","Paper","Scissors"])

            if self.computer_choice == "Rock":
                self.computer_frame.rock.configure(fg_color = "#ff0000")
            elif self.computer_choice == "Paper":
                self.computer_frame.paper.configure(fg_color = "#ff0000")
            elif self.computer_choice == "Scissors":
                self.computer_frame.scissors.configure(fg_color = "#ff0000")

            round_win = [("Rock","Scissors"),("Paper","Rock"),("Scissors","Paper")]
            round_draw = [("Rock","Rock"),("Paper","Paper"),("Scissors","Scissors")]

            if (self.user_choice,self.computer_choice) in round_win:
                self.user_score+=1
            elif (self.computer_choice,self.user_choice) in round_win:
                self.computer_score+=1
            elif (self.user_choice,self.computer_choice) in round_draw or (self.computer_choice,self.user_choice) in round_draw:
                pass

            self.round+=1
            update_scores()

            waithere(4000)

            if self.round<=5:
                clear_choices()
                play(self.round)
            else:
                game_over()

        def play(round):
            if round==5:
                self.my_frame.label.configure(text = f"Final Round")    
            else:
                self.my_frame.label.configure(text = f"Round {round}")
            ctr = 3
            self.user_frame.rock.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            self.user_frame.paper.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            self.user_frame.scissors.configure(fg_color = "#240257", state = "disabled", text_color_disabled="#ffffff")
            while ctr!=-1:
                waithere(1000)
                if ctr==0:
                    self.label.configure(text=f"Make your choice NOW!!")
                    self.user_frame.rock.configure(fg_color = "#240257", state = "normal", text_color_disabled="#ffffff" )
                    self.user_frame.paper.configure(fg_color = "#240257", state = "normal", text_color_disabled="#ffffff" )
                    self.user_frame.scissors.configure(fg_color = "#240257", state = "normal", text_color_disabled="#ffffff")
                else:
                    self.label.configure(text=f"Make your choice in {ctr}")
                ctr-=1
                
        def reset():
            self.user_score = 0
            self.computer_score = 0
            self.user_choice = " "
            self.computer_choice = " "
            self.round = 1

            self.my_frame.label.configure(text = f"Press Play to restart")
            self.label.configure(text = "")

            clear_choices()


app = App()
app.mainloop()