
class Paciente:
    def __init__(self, numero_processo, nome, idade):
        self.numero_processo = numero_processo
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"Processo: {self.numero_processo} | Nome: {self.nome} | Idade: {self.idade}"



class NoAVL:
    def __init__(self, paciente):
        self.paciente = paciente
        self.esquerda = None
        self.direita = None
        self.altura = 1



class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        return no.altura if no else 0

    def fator_balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita)

    # Rotação à direita (LL)
    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    # Rotação à esquerda (RR)
    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    # Inserção AVL
    def inserir(self, no, paciente):
        if not no:
            return NoAVL(paciente)

        if paciente.numero_processo < no.paciente.numero_processo:
            no.esquerda = self.inserir(no.esquerda, paciente)
        elif paciente.numero_processo > no.paciente.numero_processo:
            no.direita = self.inserir(no.direita, paciente)
        else:
            print(" Número de processo já existente.")
            return no

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        fb = self.fator_balanceamento(no)

        # Casos de balanceamento
        if fb > 1 and paciente.numero_processo < no.esquerda.paciente.numero_processo:
            return self.rotacao_direita(no)

        if fb < -1 and paciente.numero_processo > no.direita.paciente.numero_processo:
            return self.rotacao_esquerda(no)

        if fb > 1 and paciente.numero_processo > no.esquerda.paciente.numero_processo:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        if fb < -1 and paciente.numero_processo < no.direita.paciente.numero_processo:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir_paciente(self, paciente):
        self.raiz = self.inserir(self.raiz, paciente)

    # percurso em ordem
    def em_ordem(self, no):
        if no:
            self.em_ordem(no.esquerda)
            print(no.paciente)
            self.em_ordem(no.direita)


# Menu

def menu():
    print("\n SISTEMA DE GESTÃO DE PACIENTES")
    print("1 - Inserir paciente")
    print("2 - Listar pacientes (ordenados)")
    print("0 - Sair")


if __name__ == "__main__":
    arvore = ArvoreAVL()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                numero = int(input("Número do processo: "))
                nome = input("Nome do paciente: ")
                idade = int(input("Idade: "))

                paciente = Paciente(numero, nome, idade)
                arvore.inserir_paciente(paciente)

                print(" Paciente inserido com sucesso!")

            except ValueError:
                print(" Dados inválidos. Tente novamente.")

        elif opcao == "2":
            print("\n Lista de pacientes (ordenados por número de processo):")
            if arvore.raiz is None:
                print("Nenhum paciente registado.")
            else:
                arvore.em_ordem(arvore.raiz)

        elif opcao == "0":
            print(" A sair do sistema...")
            break

        else:
            print(" Opção inválida.")

