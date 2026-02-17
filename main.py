import tkinter as tk

def verificar():
    idade_digitada = entrada_idade.get()
    
    idade = int(idade_digitada)
    
    if idade >= 18:
        resultado.config(text="Status: Pode beber", fg="green")
    else:
        resultado.config(text="Status: Não pode beber!", fg="red")
        
app = tk.Tk()
app.title("Verificador de idade")
app.geometry("300x200")

tk.Label(app, text="Digite sua idade: ").pack(pady=10)

entrada_idade = tk.Entry(app)
entrada_idade.pack(pady=5)

tk.Button(app, text="Verificar", command=verificar).pack(pady=10)

resultado = tk.Label(app, text="Status: Esperando..")
resultado.pack(pady=20)

app.mainloop()