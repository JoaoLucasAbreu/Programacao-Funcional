 
class Agenda():
    def __init__(self, nome, contatos = []):
        self.nome = nome
        self.contatos = contatos
    
    def addContato(self, contato):
        self.contatos.append(contato)

    def delContato(self, sequencia):
        for c in self.contatos:
            s = c.pais + c.ddd + c.numero
            if sequencia == s:
                self.contatos.remove(c)

    def listarContatos(self):
        print("CONTATOS DA AGÊNDA " + self.nome)
        print("---------------")
        for c in self.contatos:
            print("CONTATO: " + c.nome + " " + c.sobrenome + " +" + c.pais + c.ddd + c.numero)
            print("---------------")