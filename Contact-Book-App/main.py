import customtkinter
import webbrowser
from CTkTable import CTkTable
import service
import middleware
import pyperclip
import os
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.file_path = os.path.dirname(os.path.realpath(__file__))
        
        self.title("BuddyBook")
        self.geometry(f"{1100}x{580}")
        self.resizable(False,False)
        self.iconbitmap(self.file_path + "/assets/contacts.ico")
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.my_font = customtkinter.CTkFont(family="Manrope", size=35,weight='bold')
        self.my_font2 = customtkinter.CTkFont(family="Manrope", size=18,weight='normal')
        self.my_font3 = customtkinter.CTkFont(family="Manrope", size=30,weight='bold')

        def redirect(link):
            if link=="GitHub":
                webbrowser.open("https://github.com/AdityaGupta0001")
            elif link=="LinkedIn":
                webbrowser.open("https://www.linkedin.com/in/aditya-gupta-475328252/")

        def home_page():
            destroy()
            self.welcome = customtkinter.CTkScrollableFrame(self, width=400, height=480, corner_radius=10, fg_color="#393939")
            self.welcome.grid(row=0,column=1,sticky="nsew", padx=20, pady=30, rowspan=2)
        
            self.welcome.label = customtkinter.CTkLabel(self.welcome, fg_color="transparent",text_color="#ffffff",text = "Welcome to Book Buddy!", width=380, height=30,anchor="w", font=self.my_font, wraplength=380, justify = "left")
            self.welcome.label.grid(row=0,column=0,pady=10,padx=10)

            self.welcome.label2 = customtkinter.CTkLabel(self.welcome, fg_color="transparent",text_color="#ffffff",text = "We're thrilled to have you join our 1 million+ users who trust Book Buddy for all their contact management needs. Here's what you can do with Book Buddy:\n\n\nAdd Contacts: Effortlessly create new entries for friends, family, and colleagues with our user-friendly interface.\n\nUpdate Details: Keep your contacts' information up-to-date with just a few taps, ensuring you're always in the loop.\n\nView Contacts: Access your entire contact list quickly from our secure database, now spanning over 50 countries.\n\nDelete Contacts: Easily remove outdated or duplicate entries, keeping your address book clean and organized.\n\nSearch Functionality: Instantly find any contact using our powerful search tool, capable of sifting through millions of entries in seconds.\n\n\nThank you for being part of the Book Buddy community! With over 5 million downloads, our app is designed to make your life easier and more connected. Explore the features and enjoy seamless contact management at your fingertips.", width=380, height=30,anchor="w", font=self.my_font2, wraplength=380, justify = "left")
            self.welcome.label2.grid(row=1,column=0,pady=10,padx=10)

            self.about = customtkinter.CTkScrollableFrame(self, width=400, height=220, corner_radius=10, fg_color="#393939")
            self.about.grid(row=0,column=2,sticky="nsew", padx=10, pady=30)

            self.about.label = customtkinter.CTkLabel(self.about, fg_color="transparent",text_color="#ffffff",text = "Updates & News:", width=380, height=30,anchor="w", font=self.my_font3, wraplength=380, justify = "left")
            self.about.label.grid(row=0,column=0,pady=10,padx=10)

            self.about.label2 = customtkinter.CTkLabel(self.about, fg_color="transparent",text_color="#ffffff",text = "Version 2.1 Coming Soon: Get ready for exciting new features and improvements!\n\nCommunity Spotlight: Highlighting stories from our amazing users.\n\nSecurity Enhancements: Learn about the latest updates to keep your data safe.", width=380, height=30,anchor="w", font=self.my_font2, wraplength=380, justify = "left")
            self.about.label2.grid(row=1,column=0,pady=10,padx=10)

            self.about.label3 = customtkinter.CTkLabel(self.about, fg_color="transparent",text_color="#ffffff",text = "\nTips & Tricks:", width=380, height=30,anchor="w", font=self.my_font3, wraplength=380, justify = "left")
            self.about.label3.grid(row=2,column=0,pady=10,padx=10)

            self.about.label4 = customtkinter.CTkLabel(self.about, fg_color="transparent",text_color="#ffffff",text = "Speed Up Entry: Use voice input to quickly add new contacts.\n\nImport Contacts: Easily import contacts from other platforms and services.\n\nMerge Duplicates: Clean up your address book by merging duplicate contacts.", width=380, height=30,anchor="w", font=self.my_font2, wraplength=380, justify = "left")
            self.about.label4.grid(row=3,column=0,pady=10,padx=10)

            self.me = customtkinter.CTkFrame(self, width=400, height=220, corner_radius=10, fg_color="#393939")
            self.me.grid(row=1,column=2,sticky="nsew", padx=10, pady=30)

            self.me.label = customtkinter.CTkLabel(self.me, fg_color="transparent",text_color="#ffffff",text = "\n   Made By: Aditya Gupta", width=380, height=30, font=self.my_font3, wraplength=380)
            self.me.label.grid(row=0,column=0,pady=10,padx=10, columnspan=2)

            self.me.github = customtkinter.CTkButton(self.me,text_color="#ffffff",text = "GitHub", width=155, height=30, command=lambda: redirect("GitHub"), fg_color="#0000ff", hover_color="#0202bf")
            self.me.github.grid(row=1,column=0,padx=30)

            self.me.linkedin = customtkinter.CTkButton(self.me,text_color="#ffffff",text = "LinkedIn", width=155, height=30, command=lambda: redirect("LinkedIn"), fg_color="#0000ff", hover_color="#0202bf")
            self.me.linkedin.grid(row=1,column=1)

        def add_page():
            destroy()

            def insert_contact(name,phone,email,address,city,state,country):
                if name=="" or phone=="" or email=="" or address=="" or city=="" or state=="" or country=="":
                    message_box("Please enter all the details")
                else:
                    if not middleware.checkPhoneNumberValidity(phone):
                        message_box("Invalid Phone Number")
                    elif not middleware.checkEmailValidity(email):
                        message_box("Invalid Email")
                    else:
                        try:
                            service.add_data(name.title(),phone,email.lower(),address,city.title(),state.title(),country.title())
                            message_box("Buddy added successfully!!")
                        except:
                            message_box("Buddy could not be added")


            self.add = customtkinter.CTkFrame(self, width=860, height=480, corner_radius=10, fg_color="#393939")
            self.add.grid(row=0,column=1,sticky="nsew", padx=30, pady=30, columnspan=3)

            self.add.label = customtkinter.CTkLabel(self.add, fg_color="transparent",text_color="#ffffff",text = "Add a Buddy", width=380, height=30,anchor="w", font=self.my_font,justify="left")
            self.add.label.grid(row=0,column=0,pady=(20,0),padx=20, sticky="nsew", columnspan=3)

            self.add.label2 = customtkinter.CTkLabel(self.add, fg_color="transparent",text_color="#ffffff",text = "Effortlessly add new contacts with our streamlined input process.", width=380, height=30,anchor="w", font=self.my_font2, justify = "left")
            self.add.label2.grid(row=1,column=0,padx=20, sticky = "nsew", pady=(0,20), columnspan=3)

            self.add.name = customtkinter.CTkEntry(self.add, placeholder_text="Name", width=820,height=30)
            self.add.name.grid(row=2, column=0, padx=20, pady=(20, 20), sticky="nsew", columnspan=3)

            self.add.phone = customtkinter.CTkEntry(self.add, placeholder_text="Phone Number", width=820,height=30)
            self.add.phone.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="nsew", columnspan=3)

            self.add.email = customtkinter.CTkEntry(self.add, placeholder_text="Email", width=820,height=30)
            self.add.email.grid(row=4, column=0, padx=20, pady=(0, 20), sticky="nsew", columnspan=3)

            self.add.address = customtkinter.CTkEntry(self.add, placeholder_text="Address Line 1", width=820,height=30)
            self.add.address.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="nsew", columnspan=3)

            self.add.city = customtkinter.CTkEntry(self.add, placeholder_text="City", width=25,height=30)
            self.add.city.grid(row=6, column=0, padx=20, pady=(0, 40), sticky="nsew")

            self.add.state = customtkinter.CTkEntry(self.add, placeholder_text="State", width=25,height=30)
            self.add.state.grid(row=6, column=1, padx=20, pady=(0, 40), sticky="nsew")

            self.add.country = customtkinter.CTkEntry(self.add, placeholder_text="Country", width=25,height=30)
            self.add.country.grid(row=6, column=2, padx=20, pady=(0, 40), sticky="nsew")

            self.add.submit = customtkinter.CTkButton(self.add,text="Add Buddy", width=820, height=50, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf", font=self.my_font2, command=lambda: insert_contact(self.add.name.get(),self.add.phone.get(),self.add.email.get(),self.add.address.get(),self.add.city.get(),self.add.state.get(),self.add.country.get()))
            self.add.submit.grid(row=7, column=0, padx=20, pady=(40, 20), sticky="nsew", columnspan= 3)


        def update_page():
            destroy()

            self.update_allowed = False

            def clear_fields():
                self.update_.name.delete(0,customtkinter.END)
                self.update_.phone.delete(0,customtkinter.END)
                self.update_.email.delete(0,customtkinter.END)
                self.update_.address.delete(0,customtkinter.END)
                self.update_.city.delete(0,customtkinter.END)
                self.update_.state.delete(0,customtkinter.END)
                self.update_.country.delete(0,customtkinter.END)
                self.update_.name.configure(state="disabled", placeholder_text="Name")
                self.update_.phone.configure(state="disabled", placeholder_text="Phone Number")
                self.update_.email.configure(state="disabled", placeholder_text="Email")
                self.update_.address.configure(state="disabled", placeholder_text="Address Line 1")
                self.update_.city.configure(state="disabled", placeholder_text="City")
                self.update_.state.configure(state="disabled", placeholder_text="State")
                self.update_.country.configure(state="disabled", placeholder_text="Country")
                self.update_.submit.configure(state="disabled")

            def find_contact(contact):
                if middleware.checkEmailValidity(contact) or middleware.checkPhoneNumberValidity(contact):
                    if service.buddyexists(contact):
                        buddy_data = service.search_data(contact)[1]
                        clear_fields()
                        self.update_.name.configure(state="normal", placeholder_text="Name")
                        self.update_.name.insert(0,buddy_data[0])
                        self.update_.phone.configure(state="normal", placeholder_text="Phone Number")
                        self.update_.phone.insert(0,buddy_data[1])
                        self.update_.email.configure(state="normal", placeholder_text="Email")
                        self.update_.email.insert(0,buddy_data[2])
                        self.update_.address.configure(state="normal", placeholder_text="Address Line 1")
                        self.update_.address.insert(0,buddy_data[3])
                        self.update_.city.configure(state="normal", placeholder_text="City")
                        self.update_.city.insert(0,buddy_data[4])
                        self.update_.state.configure(state="normal", placeholder_text="State")
                        self.update_.state.insert(0,buddy_data[5])
                        self.update_.country.configure(state="normal", placeholder_text="Country")
                        self.update_.country.insert(0,buddy_data[6])
                        self.update_.submit.configure(state="normal")

                        self.update_allowed = True

                    else:
                        clear_fields()
                        message_box("Buddy does not exist")
                else:
                    clear_fields()
                    message_box("Invalid Phone/Email")

            def update_contact(contact, name, phone, email, address, city, state, country):
                if "" in (name, phone, email, address, city, state, country):
                    message_box("Please enter all the details")
                elif not middleware.checkPhoneNumberValidity(phone):
                    message_box("Invalid Phone Number")
                elif not middleware.checkEmailValidity(email):
                    message_box("Invalid Email")
                else:
                    new_contact_data = {'name': name, 'phone': phone, 'email': email, 'address': address, 'city': city, 'state': state, 'country': country}
                    try:
                        service.update_data(contact,new_contact_data)
                        message_box("Buddy updated successfully!!")
                        clear_fields()
                    except:
                        message_box("Buddy could not be updated")
            self.update_ = customtkinter.CTkFrame(self, width=860, height=480, corner_radius=10, fg_color="#393939")
            self.update_.grid(row=0,column=1,sticky="nsew", padx=30, pady=30, columnspan=3)

            self.update_.label = customtkinter.CTkLabel(self.update_, fg_color="transparent",text_color="#ffffff",text = "Update a Buddy", width=380, height=30,anchor="w", font=self.my_font,justify="left")
            self.update_.label.grid(row=0,column=0,pady=(20,0),padx=20, sticky="nsew", columnspan=3)

            self.update_.label2 = customtkinter.CTkLabel(self.update_, fg_color="transparent",text_color="#ffffff",text = "Effortlessly add new contacts with our streamlined input process.", width=380, height=30,anchor="w", font=self.my_font2, justify = "left")
            self.update_.label2.grid(row=1,column=0,padx=20, sticky = "nsew", pady=(0,20), columnspan=3)

            self.update_.find_name = customtkinter.CTkEntry(self.update_, placeholder_text="Enter phone or email of buddy", width=720,height=30, text_color="#ffffff")
            self.update_.find_name.grid(row=2, column=0, padx=(20,20), pady=(20, 10), sticky="nsew",columnspan=3)

            self.update_.find = customtkinter.CTkButton(self.update_,text="Find", width=820, height=15, font=self.my_font2, fg_color="#0000ff", hover_color="#0202bf", command=lambda: find_contact(self.update_.find_name.get()))
            self.update_.find.grid(row=3, column=0, padx=20,pady=(0,20), columnspan=3)

            self.update_.name = customtkinter.CTkEntry(self.update_, placeholder_text="Name", width=820,height=30, state="disabled")
            self.update_.name.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="nsew", columnspan=3)

            self.update_.phone = customtkinter.CTkEntry(self.update_, placeholder_text="Phone Number", width=820,height=30, state="disabled")
            self.update_.phone.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="nsew", columnspan=3)

            self.update_.email = customtkinter.CTkEntry(self.update_, placeholder_text="Email", width=820,height=30, state="disabled")
            self.update_.email.grid(row=6, column=0, padx=20, pady=(0, 10), sticky="nsew", columnspan=3)

            self.update_.address = customtkinter.CTkEntry(self.update_, placeholder_text="Address Line 1", width=820,height=30, state="disabled")
            self.update_.address.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="nsew", columnspan=3)

            self.update_.city = customtkinter.CTkEntry(self.update_, placeholder_text="City", width=25,height=30, state="disabled")
            self.update_.city.grid(row=8, column=0, padx=20, sticky="nsew")

            self.update_.state = customtkinter.CTkEntry(self.update_, placeholder_text="State", width=25,height=30, state="disabled")
            self.update_.state.grid(row=8, column=1, padx=20, sticky="nsew")

            self.update_.country = customtkinter.CTkEntry(self.update_, placeholder_text="Country", width=25,height=30, state="disabled")
            self.update_.country.grid(row=8, column=2, padx=20, sticky="nsew")

            self.update_.submit = customtkinter.CTkButton(self.update_,text="Update Buddy", width=820, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf", height=50, font=self.my_font2, state="disabled" ,command=lambda: update_contact(self.update_.find_name.get(), self.update_.name.get(), self.update_.phone.get(), self.update_.email.get(), self.update_.address.get(), self.update_.city.get(), self.update_.state.get(), self.update_.country.get()))
            self.update_.submit.grid(row=9, column=0, padx=20, pady=(20, 20), sticky="nsew", columnspan= 3)


        def remove_page():
            destroy()

            self.remove = customtkinter.CTkFrame(self, width=860, height=480, corner_radius=10, fg_color="#393939")
            self.remove.grid(row=0,column=1,sticky="nsew", padx=30, pady=30)

            self.remove.check_var = "off"

            def checkbox_event():
                if self.remove.check_var == "off":
                    self.remove.check_var = "on"
                else:
                    self.remove.check_var = "off"
            def delete_contact(contact):
                if middleware.checkEmailValidity(contact) or middleware.checkPhoneNumberValidity(contact):  
                    if self.remove.check_var=="off":
                        message_box("Please check the checkbox")
                    else:
                        if service.buddyexists(contact):
                            service.delete_data(contact)
                            message_box("Buddy removed successfully!!")
                        else:
                            message_box("Buddy does not exist")
                else:
                    message_box("Invalid Phone/Email")

            self.remove.label = customtkinter.CTkLabel(self.remove, fg_color="transparent",text_color="#ffffff",text = "Remove a Buddy", width=380, height=30,anchor="w", font=self.my_font,justify="left")
            self.remove.label.grid(row=0,column=0,pady=(20,0),padx=20, sticky="nsew")

            self.remove.label2 = customtkinter.CTkLabel(self.remove, fg_color="transparent",text_color="#ffffff",text = "Remove old or duplicate contacts with a simple swipe.", width=380, height=30,anchor="w", font=self.my_font2, justify = "left")
            self.remove.label2.grid(row=1,column=0,padx=20, sticky = "nsew", pady=(0,20))

            self.remove.find_name = customtkinter.CTkEntry(self.remove, placeholder_text="Enter phone or email of buddy", width=820,height=30)
            self.remove.find_name.grid(row=2, column=0, padx=(20,20), pady=(20, 10), sticky="nsew")

            self.remove.check = customtkinter.CTkCheckBox(self.remove, text="I understand that this contact will be permanently deleted and cannot be recovered.",command=checkbox_event, fg_color="#0000ff")
            self.remove.check.grid(row=3,column=0,sticky="nsew",padx=20)

            self.remove.submit = customtkinter.CTkButton(self.remove,text="Remove Buddy", text_color="#ffffff", width=820, height=50, font=self.my_font2, fg_color="#0000ff", hover_color="#0202bf", command=lambda: delete_contact(self.remove.find_name.get()))
            self.remove.submit.grid(row=9, column=0, padx=20, pady=(250, 20), sticky="nsew", columnspan= 3)

        def search_page():
            destroy()
            table_data = service.get_data()

            def search_contact(contact):
                if contact=="":
                    self.search.table_frame.table.configure(values = table_data)
                elif not service.buddyexists(contact):
                    message_box("Buddy does not exist")
                else:
                    search_results = service.search_data(contact)
                    if len(search_results)>1:
                        self.search.table_frame.table.configure(values = search_results)
            
            self.search = customtkinter.CTkFrame(self, width=860, height=480, corner_radius=10, fg_color="#393939")
            self.search.grid(row=0,column=1,sticky="nsew", padx=30, pady=30)

            self.search.label = customtkinter.CTkLabel(self.search, fg_color="transparent",text_color="#ffffff",text = "Search a Buddy", width=380, height=30,anchor="w", font=self.my_font,justify="left")
            self.search.label.grid(row=0,column=0,pady=(20,0),padx=20, sticky="nsew")

            self.search.label2 = customtkinter.CTkLabel(self.search, fg_color="transparent",text_color="#ffffff",text = "Find any contact instantly with our powerful search tool.", width=380, height=30,anchor="w", font=self.my_font2, justify = "left")
            self.search.label2.grid(row=1,column=0,padx=20, sticky = "nsew", pady=(0,20))

            self.search.find_name = customtkinter.CTkEntry(self.search, placeholder_text="Enter phone or email of buddy", width=820,height=30)
            self.search.find_name.grid(row=2, column=0, padx=(20,20), pady=(20, 10), sticky="nsew")
            
            self.search.table_frame = customtkinter.CTkScrollableFrame(self.search, fg_color="transparent", width=800, height=250)
            self.search.table_frame.grid(row=3, column=0, padx=20,pady=(0,0), columnspan=3)

            self.search.table_frame.table = CTkTable(self.search.table_frame, values=table_data, width=100, height=30, hover_color="#0000ff")
            self.search.table_frame.table.grid(row=0, column=0, padx=10,pady=(20,20))

            self.search.submit = customtkinter.CTkButton(self.search,text="Search Buddy", text_color="#ffffff", width=820, height=50, font=self.my_font2, fg_color="#0000ff", hover_color="#0202bf", command=lambda: search_contact(self.search.find_name.get()))
            self.search.submit.grid(row=4, column=0, padx=20, pady=(10, 30), sticky="nsew", columnspan= 3)


        def mybook_page():
            destroy()

            def on_cell_click(cell_data):
                value = cell_data["value"]
                pyperclip.copy(value)
            self.mybook = customtkinter.CTkFrame(self, width=860, height=480, corner_radius=10, fg_color="#393939")
            self.mybook.grid(row=0,column=1,sticky="nsew", padx=30, pady=30)

            self.mybook.label = customtkinter.CTkLabel(self.mybook, fg_color="transparent",text_color="#ffffff",text = "My Buddies", width=380, height=30,anchor="w", font=self.my_font,justify="left")
            self.mybook.label.grid(row=0,column=0,pady=(20,0),padx=20, sticky="nsew")

            self.mybook.label2 = customtkinter.CTkLabel(self.mybook, fg_color="transparent",text_color="#ffffff",text = "Quickly access and view all your saved contacts in one place.", width=380, height=30,anchor="w", font=self.my_font2, justify = "left")
            self.mybook.label2.grid(row=1,column=0,padx=20, sticky = "nsew", pady=(0,20))          

            table_data = service.get_data()
            
            self.mybook.table_frame = customtkinter.CTkScrollableFrame(self.mybook, fg_color="transparent", width=800, height=370)
            self.mybook.table_frame.grid(row=2, column=0, padx=20,pady=(0,40), columnspan=3)

            self.mybook.table_frame.table = CTkTable(self.mybook.table_frame, values=table_data, width=100, height=30, hover_color="#0000ff", header_color="#000000", command=on_cell_click)
            self.mybook.table_frame.table.grid(row=0, column=0, padx=10,pady=(20,50))

        def destroy():
            frames = self.winfo_children()

            for i in range(len(frames)):
                if i==0:
                    continue
                else:
                    frames[i].destroy()

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(11, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Buddy Book", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_home = customtkinter.CTkButton(self.sidebar_frame, text = "Home", command=home_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_home.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_mybook = customtkinter.CTkButton(self.sidebar_frame, text="My Book", command=mybook_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_mybook.grid(row=2, column=0, padx=20)
        self.sidebar_add = customtkinter.CTkButton(self.sidebar_frame, text= "Add Buddy", command=add_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_add.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_update = customtkinter.CTkButton(self.sidebar_frame, text= "Update Buddy", command=update_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_update.grid(row=4, column=0, padx=20)
        self.sidebar_delete = customtkinter.CTkButton(self.sidebar_frame, text= "Remove Buddy", command=remove_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_delete.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_search = customtkinter.CTkButton(self.sidebar_frame, text= "Search Buddy", command=search_page, text_color="#ffffff", fg_color="#0000ff", hover_color="#0202bf")
        self.sidebar_search.grid(row=6, column=0, padx=20)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(130, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], fg_color="#0000ff",
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20)
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], fg_color="#0000ff",
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20)

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        def message_box(message):
            box = customtkinter.CTkToplevel(self)
            box.title("Game Over")
            box.geometry("300x150")
            box.resizable(False, False)
            
            def button_func():
                box.destroy()
            label = customtkinter.CTkLabel(box, text=message, font=("Roboto",15))
            label.pack(pady=30)

            button = customtkinter.CTkButton(box, text="OK", command=button_func)
            button.pack()

            box.transient(self)
            box.grab_set()      
            box.focus_set()

        home_page()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()