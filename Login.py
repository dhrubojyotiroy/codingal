import tkinter as tk
from tkinter import messagebox

uc = {"abc":"1234" , "user1":"pass1" , "user2":"pass2" , "user3":"pass3" , "user4":"pass4"}
def login():
  username = entry_username.get()
  password = entry_password.get()
  if username in uc and uc[username] == password:
    messagebox.showinfo("Login Ststus","Login Successful")
  else:
    messagebox.showerror("Login Status","Invalid Username or Password")
def clearfield():
  entry_username.delete(0,tk.END)
  entry_password.delete(0,tk.END)


root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

labelusername = tk.Label(root,text="Username")
labelusername.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

labelpassword = tk.Label(root,text="Password")
labelpassword.pack(pady=5)

entry_password = tk.Entry(root,show="*")
entry_password.pack(pady=5)

buttonlogin = tk.Button(root,text="Login",command=login)
buttonlogin.pack(pady=5)
buttonclear = tk.Button(root,text="Clear",command=clearfield)
buttonclear.pack(pady=5)

root.mainloop()
