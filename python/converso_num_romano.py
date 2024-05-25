from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Conversor:

    def __init__(self, master=None):
        self.master = master
        self.master.title('Conversor Decimal -> Romano')
        self.master.geometry('400x700')
        self.master.configure(bg='#ffffff')

        self.frame = Frame(master, padx=20, pady=20, bg='#ffffff')
        self.frame.pack(expand=True)

        # Adiciona a logo da faculdade
        self.logo = PhotoImage(file='C:/Users/dti/Desktop/Curso-python/Imagens/logo-nassau.png')  # Altere para o caminho do arquivo da sua logo
        self.logo_label = Label(self.frame, image=self.logo, bg='#ffffff')
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.texto1 = Label(self.frame, text='DECIMAL', bg='#ffffff', font=('Arial', 12, 'bold'))
        self.texto1.grid(row=1, column=0, padx=5, pady=(10, 5))

        self.texto2 = Label(self.frame, text='ROMANO', bg='#ffffff', font=('Arial', 12, 'bold'))
        self.texto2.grid(row=1, column=1, padx=5, pady=(10, 5))

        self.entry_var = StringVar()
        self.ed = Entry(self.frame, textvariable=self.entry_var, font=('Arial', 12), justify='center', width=15)
        self.ed.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.ed.bind("<Return>", self.enter_pressed)
        self.ed.config(validate="key", validatecommand=(self.ed.register(self.validate_input), "%S"))

        self.bt = Button(self.frame, width=10, text='Calcular', command=self.int_to_roman, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
        self.bt.grid(row=3, column=0, columnspan=2, padx=5, pady=20)

        self.res = StringVar()
        self.lb = Label(self.frame, textvariable=self.res, bg='#ffffff', font=('Arial', 12, 'bold'))
        self.lb.grid(row=4, column=0, columnspan=2, padx=5, pady=(10, 0))

        # Botão para exibir as imagens dos professores
        self.bt_imagem = Button(self.frame, width=25, text='Exibir Professores felizes :3 !!', command=self.exibir_imagens, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
        self.bt_imagem.grid(row=5, column=0, columnspan=2, padx=5, pady=20)

        # Frame para conter as imagens dos professores
        self.frame_imagens = None

        # Adiciona o texto de copyright
        self.copyright_text = Label(self.master, text='© 2024 Daniel Fernando dos Santos', bg='#ffffff', font=('Arial', 8))
        self. copyright_text.pack(side=BOTTOM, pady=5)

        # Lista com os caminhos das imagens dos professores
        self.caminhos_imagens = [
            "C:/Users/dti/Desktop/Curso-python/Imagens/marcos.png",
            "C:/Users/dti/Desktop/Curso-python/Imagens/cicero.png",
            "C:/Users/dti/Desktop/Curso-python/Imagens/flavio.png"
        ]

    def enter_pressed(self, event):
        self.int_to_roman()

    def validate_input(self, char):
        return char.isdigit() or char == ""

    def int_to_roman(self):
        n1 = self.ed.get()
        try:
            n1 = int(n1)
        except ValueError:
            messagebox.showerror("Erro", "Digite um número!")
            return

        if not 0 < n1 < 4000:
            messagebox.showerror("Erro", "Os números romanos só são suportados até 3999")
            return

        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []

        for i in range(len(ints)):
            count = int(n1 / ints[i])
            result.append(nums[i] * count)
            n1 -= ints[i] * count

        self.res.set(''.join(result))

    def exibir_imagens(self):
        if self.frame_imagens is not None:
            self.frame_imagens.destroy()

        # Cria um frame para as imagens dos professores
        self.frame_imagens = Frame(self.frame, bg='#ffffff')
        self.frame_imagens.grid(row=6, column=0, columnspan=2, padx=5, pady=20)

        # Carrega e exibe as imagens dos professores
        for idx, caminho in enumerate(self.caminhos_imagens):
            imagem_professor = Image.open(caminho)
            imagem_professor = imagem_professor.resize((100, 100))
            imagem_tk = ImageTk.PhotoImage(imagem_professor)

            # Cria um label para exibir cada imagem
            imagem_label = Label(self.frame_imagens, image=imagem_tk)
            imagem_label.image = imagem_tk
            imagem_label.grid(row=0, column=idx, padx=10)

        # Atualiza o layout da janela
        self.master.update()

# Cria a janela principal do Tkinter
i = Tk()

# Inicializa a classe Conversor com a janela principal
Conversor(i)

# Inicia o loop principal do Tkinter
i.mainloop()
