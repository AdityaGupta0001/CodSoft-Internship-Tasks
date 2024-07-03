import customtkinter
from random import choice, randint
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
        self.geometry("400x540")
        self.resizable(False,False)
        self.title("Tic Tac Toe")
        self.iconbitmap(self.file_path+'/assets/ttt.ico')

        self.difficulty_level = ""
        self.positions = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}
        self.game_mode = ""
        self.player_toggle_value = "X"
        self.single_gamemode_positions = [0,1,2,3,4,5,6,7,8]
        self.single_gamemode_counter = 0

        my_font = customtkinter.CTkFont(family="Roboto", size=70,weight='bold')
        my_font3 = customtkinter.CTkFont(family="Roboto", size=15,weight='normal')

        self.my_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.my_frame.configure(width=380,height=25)
        self.my_frame.grid(row=0, column=0, padx=10, pady=10)

        self.my_frame.label = customtkinter.CTkLabel(self.my_frame,text="Difficulty: ",height=20, corner_radius=5,fg_color="transparent",anchor="w",font=my_font3)
        self.my_frame.label.grid(row=0,column=0,pady=10,padx=10)
        
        radio_var = customtkinter.StringVar(value="")
        self.my_frame.radio_easy = customtkinter.CTkRadioButton(self.my_frame, text="Easy",command=lambda: toggle_difficulty(), variable= radio_var, value="Easy", width=72, border_color="#20e637", fg_color="#ffffff", hover_color="#ffffff", border_width_checked=5)
        self.my_frame.radio_easy.grid(row=0,column=1,pady=10,padx=10)
        self.my_frame.radio_medium = customtkinter.CTkRadioButton(self.my_frame, text="Medium",command=lambda: toggle_difficulty(), variable= radio_var, value="Medium", width=72, border_color="#ffd103", fg_color="#ffffff", hover_color="#ffffff", border_width_checked=5)
        self.my_frame.radio_medium.grid(row=0,column=2,pady=10,padx=10)
        self.my_frame.radio_hard = customtkinter.CTkRadioButton(self.my_frame, text="Hard",command=lambda: toggle_difficulty(), variable= radio_var, value="Hard", width=72, border_color="#ff0303", fg_color="#ffffff", hover_color="#ffffff", border_width_checked=5)
        self.my_frame.radio_hard.grid(row=0,column=3,pady=10,padx=10)   

        self.my_frame2 = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.my_frame2.configure(width=380,height=40)
        self.my_frame2.grid(row=1, column=0, padx=10, pady=10)

        self.my_frame2.single_player = customtkinter.CTkButton(self.my_frame2,text="Single Player",width=170,height=25,font=my_font3, fg_color="#240257", hover_color="#6502fa", command=lambda: toggle_game_mode("single"))
        self.my_frame2.single_player.grid(row=0, column=0, pady=10, padx=10)

        self.my_frame2.multi_player = customtkinter.CTkButton(self.my_frame2,text="Multi Player",width=170,height=25, font=my_font3, fg_color="#240257", hover_color="#6502fa", command=lambda: toggle_game_mode("multi"))
        self.my_frame2.multi_player.grid(row=0, column=1, pady=10, padx=10)

        self.game_frame = MyFrame(master=self,border_width=1,border_color="#ffffff")
        self.game_frame.configure(width=310,height=320)
        self.game_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.game_frame.button_0 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(0))
        self.game_frame.button_0.grid(row=0,column=0,pady=10,padx=10)
        self.game_frame.button_1 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(1))
        self.game_frame.button_1.grid(row=0,column=1,pady=10)
        self.game_frame.button_2 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(2))
        self.game_frame.button_2.grid(row=0,column=2,pady=10,padx=10)
        self.game_frame.button_3 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(3))
        self.game_frame.button_3.grid(row=1,column=0)
        self.game_frame.button_4 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(4))
        self.game_frame.button_4.grid(row=1,column=1)
        self.game_frame.button_5 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(5))
        self.game_frame.button_5.grid(row=1,column=2)
        self.game_frame.button_6 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(6))
        self.game_frame.button_6.grid(row=2,column=0,pady=10)
        self.game_frame.button_7 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(7))
        self.game_frame.button_7.grid(row=2,column=1,pady=10)
        self.game_frame.button_8 = customtkinter.CTkButton(self.game_frame,text="",corner_radius=10,width=113,height=93,font=my_font,fg_color="transparent",text_color="#ffffff",border_width=2,border_color="#ffffff",hover_color="#000000", command=lambda: game_play(8))
        self.game_frame.button_8.grid(row=2,column=2,pady=10)
        
        self.my_frame3 = MyFrame(master=self,border_width=0,border_color="#ffffff",fg_color = "transparent")
        self.my_frame3.configure(width=380,height=40)
        self.my_frame3.grid(row=3, column=0, padx=10)

        self.my_frame3.reset = customtkinter.CTkButton(self.my_frame3,text="Reset",width=170,height=35,font=my_font3, fg_color="#FF8C00", hover_color="#FFA500", command=lambda: reset())
        self.my_frame3.reset.grid(row=0, column=0, pady=10, padx=10)
        
        self.my_frame3.exit = customtkinter.CTkButton(self.my_frame3,text="Exit",width=170,height=35,font=my_font3, fg_color="#b50404", hover_color="#fc3030", command=lambda: exit())
        self.my_frame3.exit.grid(row=0, column=1, pady=10, padx=10)

        self.buttons = [self.game_frame.button_0,self.game_frame.button_1,self.game_frame.button_2,self.game_frame.button_3,self.game_frame.button_4,self.game_frame.button_5,self.game_frame.button_6,self.game_frame.button_7,self.game_frame.button_8]

        def toggle_game_mode(mode):
            self.game_mode = mode
            if self.game_mode == "single":
                self.my_frame2.single_player.configure(fg_color = "#6502fa")
                self.my_frame2.multi_player.configure(fg_color = "#240257")
            else:
                self.my_frame2.single_player.configure(fg_color = "#240257")
                self.my_frame2.multi_player.configure(fg_color = "#6502fa")
                
        def toggle_difficulty():
            self.difficulty_level = radio_var.get()

        def exit():
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            box.iconbitmap(self.file_path+'/assets/ttt.ico')

            label = customtkinter.CTkLabel(box, text="Are you sure you want to exit the app?", font=my_font3, anchor="center")
            label.grid(row=0,column=0,pady=30, columnspan=2, padx=25)

            button = customtkinter.CTkButton(box, text="Cancel", command=box.destroy, width=120)
            button.grid(row=1,column=0,padx=10)
            button2 = customtkinter.CTkButton(box, text="Exit", command=self.destroy,width=120, fg_color="#b50404", hover_color="#fc3030")
            button2.grid(row=1,column=1,padx=10)

            box.transient(self)
            box.grab_set()      
            box.focus_set()

        def reset():
            for i in self.buttons:
                i.configure(text = "", state="normal")
            self.positions = {0:" ", 1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" "}
            self.player_toggle_value = "X"
            self.single_gamemode_positions = [0,1,2,3,4,5,6,7,8]
            self.single_gamemode_counter = 0

        def waithere():
            var = customtkinter.IntVar()
            app.after(1000, var.set, 1)
            app.wait_variable(var)

        def check_win():
            winning_combinations = [
                (0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6)
            ]
            
            for combo in winning_combinations:
                if self.positions[combo[0]]!=" " and self.positions[combo[1]]!=" " and self.positions[combo[2]]!=" ":
                    if self.positions[combo[0]] == self.positions[combo[1]] and self.positions[combo[1]] == self.positions[combo[2]] and self.positions[combo[0]] == self.positions[combo[2]]:
                        if self.positions[combo[0]] == "X":
                            return "Win X"
                        else:
                            return "Win O"
            if " " not in self.positions.values():
                return "Draw"
            
            return "Continue"

        def minimax(board, depth, isMaximizing):
            result = check_win()
            if result == "Win X":
                return -1
            elif result == "Win O":
                return 1
            elif result == "Draw":
                return 0

            if isMaximizing:
                bestScore = -float("inf")
                for key in board.keys():
                    if board[key] == " ":
                        board[key] = "O"
                        score = minimax(board, depth + 1, False)
                        board[key] = " "
                        if score > bestScore:
                            bestScore = score
                return bestScore
            else:
                bestScore = float("inf")
                for key in board.keys():
                    if board[key] == " ":
                        board[key] = "X"
                        score = minimax(board, depth + 1, True)
                        board[key] = " "
                        if score < bestScore:
                            bestScore = score
                return bestScore

        def playComputer():
            self.single_gamemode_counter += 1
            bestScore = -float("inf")
            bestMove = None

            for key in self.positions.keys():
                if self.positions[key] == " ":
                    self.positions[key] = "O"
                    score = minimax(self.positions, 0, False)
                    self.positions[key] = " "
                    if score > bestScore:
                        bestScore = score
                        bestMove = key
            if bestMove is not None:
                self.positions[bestMove] = "O"
                self.buttons[bestMove].configure(text="O", state="disabled", text_color_disabled="#ffffff")

        def random_move():
            available_positions = [key for key, value in self.positions.items() if value == " "]
            if available_positions:
                move = choice(available_positions)
                self.positions[move] = "O"
                self.buttons[move].configure(text="O", state="disabled", text_color_disabled="#ffffff")


        def message_box(message):
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            box.iconbitmap(self.file_path+'/assets/ttt.ico')
            
            label = customtkinter.CTkLabel(box, text=message, font=my_font3)
            label.pack(pady=30)

            button = customtkinter.CTkButton(box, text="OK", command=box.destroy)
            button.pack()

            box.transient(self)
            box.grab_set()      
            box.focus_set()    

        def game_play(val):
            if self.game_mode=="":
                message_box("Please select game mode")

            elif self.game_mode == "multi":

                self.buttons[val].configure(text=self.player_toggle_value)
                self.buttons[val].configure(state = "disabled",text_color_disabled="#ffffff")
                self.positions[val] = self.player_toggle_value
                
                if self.player_toggle_value=="X":
                    self.player_toggle_value = "O"
                else:
                    self.player_toggle_value = "X"
                
                if check_win() == "Win X":
                    message_box("Player 1 is the winner!!")
                    reset()
                if check_win() == "Win O":
                    message_box("Player 2 is the winner!!")
                    reset()
                elif check_win() == "Draw":
                    message_box("Its a draw!!")
                    reset()

            elif self.game_mode == "single":

                if self.difficulty_level == "":
                    message_box("Please select difficulty level")

                elif self.difficulty_level == "Easy":
                    self.buttons[val].configure(text=self.player_toggle_value)
                    self.buttons[val].configure(state = "disabled",text_color_disabled="#ffffff")
                    self.positions[val] = self.player_toggle_value
                    self.single_gamemode_positions.remove(val)
                    self.single_gamemode_counter+=1
                    
                    if self.player_toggle_value=="X":
                        self.player_toggle_value = "O"
                    else:
                        self.player_toggle_value = "X"
                    
                    if self.single_gamemode_positions!=[]:
                        comp = choice(self.single_gamemode_positions)
                        waithere()
                        self.buttons[comp].configure(text=self.player_toggle_value)
                        self.buttons[comp].configure(state = "disabled",text_color_disabled="#ffffff")
                        self.positions[comp] = self.player_toggle_value
                        self.single_gamemode_positions.remove(comp)
                        self.single_gamemode_counter+=1

                    if self.single_gamemode_counter<=9:
                        if self.player_toggle_value=="X":
                            self.player_toggle_value = "O"
                        else:
                            self.player_toggle_value = "X"

                    if check_win() == "Win X":
                        message_box("You are the winner!!")
                        reset()
                    if check_win() == "Win O":
                        message_box("Computer is the winner!!")
                        reset()
                    elif check_win() == "Draw":
                        message_box("Its a draw!!")
                        reset()

                elif self.difficulty_level == "Medium":
                    self.buttons[val].configure(text=self.player_toggle_value)
                    self.buttons[val].configure(state="disabled", text_color_disabled="#ffffff")
                    self.positions[val] = self.player_toggle_value
                    self.single_gamemode_counter += 1
                    waithere()

                    if self.single_gamemode_counter <= 9:
                        if randint(0, 1) == 0:
                            random_move()
                        else:
                            playComputer()

                    if check_win() == "Win X":
                        message_box("You are the winner!!")
                        reset()
                    if check_win() == "Win O":
                        message_box("Computer is the winner!!")
                        reset()
                    elif check_win() == "Draw":
                        message_box("Its a draw!!")
                        reset()

                elif self.difficulty_level == "Hard":
                    self.buttons[val].configure(text=self.player_toggle_value)
                    self.buttons[val].configure(state = "disabled",text_color_disabled="#ffffff")
                    self.positions[val] = self.player_toggle_value
                    self.single_gamemode_counter+=1
                    waithere()

                    if self.single_gamemode_counter<=9:
                        playComputer()
                    
                    if check_win() == "Win X":
                        message_box("You are the winner!!")
                        reset()
                    if check_win() == "Win O":
                        message_box("Computer is the winner!!")
                        reset()
                    elif check_win() == "Draw":
                        message_box("Its a draw!!")
                        reset()

app = App()
app.mainloop()