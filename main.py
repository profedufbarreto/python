import tkinter as tk

def say_hello():
    print("Olá! Fazendo teste!")
    
window = tk.Tk()
window.title("Meu primeiro APP")
window.geometry("300x200")

label = tk.Label(window, text="Bem-vindo ao Tkinter!")
label.pack(pady=10)

button = tk.Button(window, text="Clique aqui", command=say_hello)
button.pack(pady=10)

window.mainloop()