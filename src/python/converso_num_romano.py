from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Conversor:

    def __init__(self, master=None):
        """
        Classe para criar uma interface gráfica simples para converter números decimais para romanos
        e exibir imagens dos professores.
        """
        # Configurações iniciais da janela principal
        self.master = master
        self.master.title('Conversor Decimal -> Romano')
        self.master.geometry('500x700')
        self.master.configure(bg='#ffffff')

        # Cria um frame para organizar os widgets
        self.frame = Frame(master, padx=20, pady=20, bg='#ffffff')
        self.frame.pack(expand=True)

        # Adiciona a logo da faculdade
        self.logo = PhotoImage(file='C://Users/dti/Desktop/Trabalho-Marcos/src/Imagens/logo-nassau.png')
        self.logo_label = Label(self.frame, image=self.logo, bg='#ffffff')
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Labels para entrada e saída de dados
        self.texto1 = Label(self.frame, text='Conversor decimal para romano', bg='#ffffff', font=('Arial', 12, 'bold'))
        self.texto1.grid(row=1, column=0, padx=110, pady=(10, 5))
      

        # Entrada de dados
        self.entry_var = StringVar()
        self.ed = Entry(self.frame, textvariable=self.entry_var, font=('Arial', 12), justify='center', width=15)
        self.ed.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.ed.bind("<Return>", self.enter_pressed)
        self.ed.config(validate="key", validatecommand=(self.ed.register(self.validate_input), "%S"))

        # Botão para realizar a conversão
        self.bt = Button(self.frame, width=10, text='Calcular', command=self.int_to_roman, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
        self.bt.grid(row=3, column=0, columnspan=2, padx=5, pady=20)
        

        # Resultado da conversão
        self.res = StringVar()
        self.lb = Label(self.frame, textvariable=self.res, bg='#ffffff', font=('Arial', 12, 'bold'))
        self.lb.grid(row=4, column=0, columnspan=2, padx=5, pady=(10, 0))

        # Botão para exibir as imagens dos professores
        self.bt_imagem = Button(self.frame, width=25, text='Exibir Professores felizes :3 !!', command=self.exibir_imagens, bg='#4CAF50', fg='white', font=('Arial', 12, 'bold'))
        self.bt_imagem.grid(row=5, column=0, columnspan=2, padx=5, pady=20)

        # Frame para conter as imagens dos professores
        self.frame_imagens = None

        # Texto de copyright
        self.copyright_text = Label(self.master, text='© 2024 Daniel Fernando dos Santos', bg='#ffffff', font=('Arial', 8))
        self. copyright_text.pack(side=BOTTOM, pady=5)

        # Lista com os caminhos das imagens dos professores
        self.caminhos_imagens = [
            "C:/Users/dti/Desktop/Trabalho-Marcos/src/Imagens/marcos.png",
            "C:/Users/dti/Desktop/Trabalho-Marcos/src/Imagens/cicero.png",
            "C:/Users/dti/Desktop/Trabalho-Marcos/src/Imagens/flavio.png"
        ]

    # Função para processar a conversão quando a tecla Enter é pressionada
    def enter_pressed(self, event):
        self.int_to_roman()

    # Função para validar a entrada do usuário (apenas dígitos)
    def validate_input(self, char):
        return char.isdigit() or char == ""

    # Função para converter um número decimal para romano
    def int_to_roman(self):
        n1 = self.ed.get()
        try:
            n1 = int(n1)
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
        except ValueError:
            messagebox.showerror("Erro", "Digite um número!")
            return

    # Função para exibir as imagens dos professores
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
