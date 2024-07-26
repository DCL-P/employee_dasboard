import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import sqlite3

#connection met de database
conn = sqlite3.connect('werknemers_data.db')
c = conn.cursor()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

dashboard = customtkinter.CTk()

dashboard.title("Werknemers Portaal")
dashboard.geometry("900x420")
dashboard.config(bg="#161C25")


font1 = ('Arial', 10,'bold')
font2 = ('Arial', 12,'bold')

employee_number = customtkinter.CTkLabel(dashboard, font=font1, text="Werknemers-ID", text_color='#fff', bg_color='#161C25')
employee_number.place(x=20, y=20)

employee_entry = customtkinter.CTkEntry(dashboard, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
employee_entry.place(x=100, y=20)

name_employee = customtkinter.CTkLabel(dashboard, font=font1, text="Voornaam", text_color='#fff', bg_color='#161C25')
name_employee.place(x=20, y=80)

name_entry = customtkinter.CTkEntry(dashboard, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
name_entry.place(x=100, y=80)

functie_select = customtkinter.CTkLabel(dashboard, font=font1, text="Bedrijfsfunctie",text_color='#fff', bg_color='#161C25')
functie_select.place(x=20, y=140)

functie_entry = customtkinter.CTkEntry(dashboard, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
functie_entry.place(x=100, y=140)

gender_select = customtkinter.CTkLabel(dashboard, font=font1, text="Geslacht", text_color='#fff', bg_color='#161C25')
gender_select.place(x=20,y=200)

options = ["Man", "Vrouw", "Anders", "Zeg ik liever niet."]
variable1 = StringVar()

gender_choices = customtkinter.CTkComboBox(dashboard,font=font1, text_color='#000', fg_color='#fff', dropdown_hover_color='#0C9295', button_color='#0C9295', button_hover_color='#0C9295', border_color='#0C9295', border_width=2, width=180, variable=variable1, values=options, state='readonly')
gender_choices.set(" ")
gender_choices.place(x=100, y=200)

status_options = customtkinter.CTkLabel(dashboard, font=font1, text="Status", text_color='#fff', bg_color='#161C25')
status_options.place(x=20, y=260)

status_entry = customtkinter.CTkEntry(dashboard, font=font1, text_color='#000', fg_color='#fff', border_color='#0C9295', border_width=2, width=180)
status_entry.place(x=100, y=260)

def register_employees():
    werknemersid = employee_entry.get()
    name = name_entry.get()
    functie = functie_entry.get()
    gender = variable1.get()
    status = status_entry.get()

    if not (werknemersid and name and functie and gender and status):
        messagebox.showerror("Foutief", "Vul alle velden in")
        return
    with open('werknemers.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([werknemersid, name, functie, gender, status])

    c.execute(f"INSERT INTO users VALUES(:werknemersid, :name, :functie, :gender, :status)",{'werknemersid':werknemersid, 'name':name, 'functie':functie, 'gender':gender, 'status':status} )
    conn.commit()

    messagebox.showinfo("Succes", "Werknemer succesvol doorgevoerd in systeem.")

    employee_entry.delete(0, END)
    name_entry.delete(0, END)
    functie_entry.delete(0, END)
    variable1.set(" ")
    status_entry.delete(0, END)


add_button = customtkinter.CTkButton(dashboard, font=font1, text_color='#fff', text="Registreer Werknemer", fg_color="#05A312", hover_color='#00850B', bg_color='#161C25', cursor="hand2", corner_radius=15, width=260, command=register_employees)
add_button.place(x=20, y=310)
dashboard.mainloop()
