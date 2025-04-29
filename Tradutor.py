import customtkinter as ctk
from deep_translator import GoogleTranslator
from tkinter import filedialog, messagebox
import os
import PyPDF2


idiomas = {
    'Espanhol': 'es',
    'Português': 'pt',
    'Inglês': 'en',
    'Francês': 'fr'
}

def traduzir_texto():
    comando_origem_texto = comando_origem.get("1.0", "end-1c")  
    if comando_origem_texto.strip() != "":  
        idioma_origem = selecionar_origem.get()
        idioma_destino = selecionar_destino.get() 
        
        
        if idioma_origem not in idiomas or idioma_destino not in idiomas:
            messagebox.showerror("Erro", "Idioma selecionado não suportado.")
            return
        
        
        try:
            translator = GoogleTranslator(source=idiomas[idioma_origem], target=idiomas[idioma_destino])
            traducao = translator.translate(comando_origem_texto)
            
            comando_destino.configure(state=ctk.NORMAL)  
            comando_destino.delete("1.0", "end")  
            comando_destino.insert(ctk.END, traducao) 
            comando_destino.configure(state=ctk.DISABLED)  
        except Exception as e:
            messagebox.showerror("Erro de tradução", f"Ocorreu um erro ao traduzir o texto: {str(e)}")
    else:
        messagebox.showwarning("Entrada vazia", "Por favor, insira algum texto para traduzir.")

def desabilitar_escrita():
    selecionar_origem.configure(state="readonly")  

def traduzir_pdf():
    arquivo_pdf = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if not arquivo_pdf:
        return
    try:
        with open(arquivo_pdf, "rb") as arquivo:
            leitor_pdf = PyPDF2.PdfReader(arquivo)
            texto = ""
            for pagina in leitor_pdf.pages:
                texto += pagina.extract_text() or ""
        if texto.strip():
            comando_origem.delete("1.0", "end")
            comando_origem.insert(ctk.END, texto)
        else:
            messagebox.showwarning("Erro", "Não foi possível carregar o PDF. Verifique se ele não é uma imagem.")
    except Exception as e:
        messagebox.showerror("Erro ao abrir o PDF", f"Ocorreu um erro: {str(e)}")
            

app = ctk.CTk()
app.title('Tradutor')
app.geometry('1500x1000')

app = ctk.CTk()
app.title('Tradutor')
app.geometry('1000x500')
app.iconbitmap(r"C:\Users\Gabriel\Documents\Projetos\Tradutor\traduzir.ico")
app.resizable(False, False)

label_origem = ctk.CTkLabel(app, text='Texto Origem', height=30, width=300, font=("Arial", 20, "bold"))
label_origem.place(relx=0.20, rely=0.07, anchor="center")

label_destino = ctk.CTkLabel(app, text='Texto Traduzido', height=30, width=300, font=("Arial", 20, "bold"))
label_destino.place(relx=0.80, rely=0.07, anchor="center")

comando_origem = ctk.CTkTextbox(app, width=430, height=300)
comando_origem.place(relx=0.25, rely=0.60, anchor="center")

comando_destino = ctk.CTkTextbox(app, width=430, height=300)
comando_destino.place(relx=0.75, rely=0.60, anchor="center")

selecionar_origem = ctk.CTkComboBox(app, values=['Português', 'Inglês', 'Espanhol', 'Francês'], width=130, height=30, font=("Arial", 15), text_color="gray")
selecionar_origem.place(relx=0.40, rely=0.15, anchor="center")
selecionar_origem.set('Selecionar')
desabilitar_escrita()

selecionar_destino = ctk.CTkComboBox(app, values=['Português', 'Inglês', 'Espanhol', 'Francês'], width=130, height=30, font=("Arial", 15), text_color="gray")
selecionar_destino.set('Selecionar')
selecionar_destino.place(relx=0.60, rely=0.15, anchor="center")

botao_pdf = ctk.CTkButton(app, text="Carregar PDF" , command= traduzir_pdf)
botao_pdf.pack(pady=10)

botao_traduzir_texto = ctk.CTkButton(app, text="Traduzir Texto", command=traduzir_texto)
botao_traduzir_texto.pack(pady=65)




app.mainloop()
