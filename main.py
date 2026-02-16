class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        
    def cadastrar(self):
        print(f"Livro: {self.titulo}, Autor: {self.autor}, ano: {self.ano}")
        print("Cadastro realizado com sucesso")
        
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro {self.titulo} foi emprestado com sucesso!")
        else:
            print(f"O livro {self.titulo} já está emprestado.")
            
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro {self.titulo} foi devolvido com sucesso!")
        else:
            print(f"O livro {self.titulo} já estava disponível.")  
            
class Revista(Livro):
    def __init__(self, titulo, autor, ano, edicao):
        super().__init__(titulo, autor, ano)
        self.edicao = edicao
    
    def cadastrar(self):
        print(f"Revista: {self.titulo}, Autor: {self.autor}, ano: {self,ano}, edição: {self.edicao}")
        print("Cadastro realizado com sucesso!!")
        
biblioteca = []

while True:
    print("\Escolha uma opção: ")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Revista")
    print("3 - Listar Itens")
    print("4 - Emprestar Itens")
    print("5 - Devolver Itens")
    print("6 - Sair")
    
    opcao = input("Digite a opção: ")
    
    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        ano = input("Ano do livro: ")
        livro = Livro(titulo, autor, ano)
        livro.cadastrar()
        biblioteca.append(livro)
        
    elif opcao == "2":
        titulo = input("Título da revista: ")
        autor = input("Autor da revista: ")
        ano = input("Ano da revista: ")
        edicao = input("Edição da revista: ")
        revista = Revista(titulo, autor, ano, edicao)
        revista.cadastrar()
        biblioteca.append(revista)
    
    elif opcao == "3":
        print("\nItens cadastrados na biblioteca: ")
        for i, item in enumerate(biblioteca, start=1):
            status = "Disponível" if item.disponivel else "Emprestado"
            print(f"{i} - {item.titulo} ({status})")
            
    elif opcao == "4":
        indice = int(input("Digite o número do item para emprestar: ")) - 1
        if 0 <= indice < len(biblioteca):
            biblioteca[indice].emprestar()
        else:
            print("Item inválido.")
    
    elif opcao == "5":
        indice = int(input("Digite o número do item para devolver: ")) -1
        if 0 <= indice < len(biblioteca):
            biblioteca[indice].devolver()
        else:
            print("Item inválido.")
    
    elif opcao == "6":
        print("Encarrando o sistema...")
        break
    
    else:
        print("Opção inválida, tente novamente.")