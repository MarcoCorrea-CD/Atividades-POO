import time

# Classe Base (Abstração e Herança)
class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        self._titulo = titulo # [cite: 14, 33]
        self._ano_publicacao = 0 # Valor padrão
        self.ano_publicacao = ano_publicacao # [cite: 16] Chama o setter para validação

    # Encapsulamento: Getters e Setters (@property)
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, valor):
        # Validação de dados: garante que _ano_publicacao seja positivo
        try:
            valor_int = int(valor)
            if valor_int > 0:
                self._ano_publicacao = valor_int
            else:
                print(f"Erro: O ano de publicação ({valor}) deve ser um número positivo.")
        except ValueError:
            print(f"Erro: O ano de publicação ({valor}) deve ser um número inteiro válido.")

    # Método genérico (será sobrescrito - Polimorfismo)
    def apresentar_detalhes(self):
        return f"Título: {self._titulo}, Ano: {self._ano_publicacao}"

# ---

# Classe Filha: Livro (Herança)
class Livro(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, autor, num_paginas):
        super().__init__(titulo, ano_publicacao) # [cite: 22] Chama o construtor da classe base
        self._autor = autor # [cite: 21]
        self._num_paginas = 0 # Valor padrão
        self.num_paginas = num_paginas # [cite: 32] Chama o setter para validação

    # Encapsulamento (Getters e Setters específicos)
    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def num_paginas(self):
        return self._num_paginas

    @num_paginas.setter
    def num_paginas(self, valor):
        # Validação de dados: _num_paginas > 50
        try:
            valor_int = int(valor)
            if valor_int > 50:
                self._num_paginas = valor_int
            else:
                print(f"Erro: O número de páginas ({valor}) deve ser maior que 50.")
        except ValueError:
            print(f"Erro: O número de páginas ({valor}) deve ser um número inteiro válido.")

    # Polimorfismo (Sobrescrita de método)
    def apresentar_detalhes(self):
        # [cite: 37, 39, 40]
        return (f"[LIVRO] Título: {self.titulo}, Ano: {self.ano_publicacao} | "
                f"Autor: {self.autor}, Páginas: {self.num_paginas}")

# ---

# Classe Filha: Revista (Herança)
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao, volume):
        super().__init__(titulo, ano_publicacao) # [cite: 26]
        self._edicao = 0 # [cite: 27]
        self._volume = 0 # [cite: 27]
        # Adicionando setters para consistência
        self.edicao = edicao
        self.volume = volume

    # Encapsulamento (Getters e Setters específicos)
    @property
    def edicao(self):
        return self._edicao

    @edicao.setter
    def edicao(self, valor):
        try:
            self._edicao = int(valor)
        except ValueError:
            print(f"Erro: Edição ({valor}) deve ser um número inteiro.")

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, valor):
        try:
            self._volume = int(valor)
        except ValueError:
            print(f"Erro: Volume ({valor}) deve ser um número inteiro.")


    # Polimorfismo (Sobrescrita de método)
    def apresentar_detalhes(self):
        # [cite: 37, 41, 42]
        return (f"[REVISTA] Título: {self.titulo}, Ano: {self.ano_publicacao} | "
                f"Edição: {self.edicao}, Volume: {self.volume}")

# ---

# Função principal com Menu Interativo
def main():
    # Crie uma única lista chamada acervo
    acervo = []

    # Instanciação de objetos iniciais para teste
    print("Carregando acervo inicial de exemplo...")
    l1 = Livro("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", 1200) # [cite: 46]
    r1 = Revista("National Geographic", 2023, 10, 150) # [cite: 48]
    l2 = Livro("Clean Code", 2008, "Robert C. Martin", 464) # [cite: 50]
    
    acervo.extend([l1, r1, l2]) # [cite: 53]
    time.sleep(1)

    # Use if/elif/else dentro de um loop while True
    while True:
        print("\n--- Sistema de Gerenciamento de Biblioteca ---")
        print("1. Cadastrar Livro")   # [cite: 57]
        print("2. Cadastrar Revista") # [cite: 59]
        print("3. Listar Acervo")     # [cite: 60]
        print("4. Sair")             # [cite: 63]
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # 1. Cadastrar Livro [cite: 57]
            print("\n[Cadastro de Livro]")
            titulo = input("Título: ")
            ano = input("Ano de Publicação: ")
            autor = input("Autor: ")
            paginas = input("Número de Páginas (deve ser > 50): ")
            
            novo_livro = Livro(titulo, ano, autor, paginas)
            
            # Validação: Só adiciona se os setters não tiverem retornado erro (valores > 0)
            if novo_livro.ano_publicacao > 0 and novo_livro.num_paginas > 50:
                acervo.append(novo_livro)
                print(f"Livro '{novo_livro.titulo}' cadastrado com sucesso!")
            else:
                print("Cadastro falhou. Verifique os dados (Ano > 0, Páginas > 50).")

        elif opcao == '2':
            # 2. Cadastrar Revista [cite: 59]
            print("\n[Cadastro de Revista]")
            titulo = input("Título: ")
            ano = input("Ano de Publicação: ")
            edicao = input("Edição: ")
            volume = input("Volume: ")
            
            nova_revista = Revista(titulo, ano, edicao, volume)

            # Validação: Só adiciona se o ano for válido (valor > 0)
            if nova_revista.ano_publicacao > 0:
                acervo.append(nova_revista)
                print(f"Revista '{nova_revista.titulo}' cadastrada com sucesso!")
            else:
                 print("Cadastro falhou. Verifique os dados (Ano > 0).")

        elif opcao == '3':
            # 3. Listar Acervo (Demonstração do Polimorfismo)
            print("\n--- Acervo Atual da Biblioteca ---")
            if not acervo:
                print("O acervo está vazio.")
            else:
                # Percorre a lista e chama o método polimórfico
                for i, item in enumerate(acervo, 1):
                    print(f"{i}. {item.apresentar_detalhes()}") 
            print("---------------------------------")

        elif opcao == '4':
            # 4. Sair [cite: 63]
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()
