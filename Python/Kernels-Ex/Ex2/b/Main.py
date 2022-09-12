from Contato import Contato
from Agenda import Agenda
contatos = []

class Main():
    def main():
        print("CRIAR UMA AGÊNDA DE CONTATOS\n" +
              "----------------------------")
        agenda = Agenda(input("NOME DA AGÊNDA:").upper(), contatos)

        sair = False
        while sair is False:
            print("OPÇÕES:\n" + "[1] ADICIONAR UM CONTATO\n" + "[2] DELETAR UM CONTATO\n" + "[3] MOSTRAR LISTA DE CONTATOS\n" + "[4] FINALIZAR")
            n = int(input("OPÇÃO: "))
            print(" ")

            if n == 1:
                nome = input("NOME:").upper()
                sobrenome = input("SOBRENOME:").upper()
                passar = False
                while passar == False:
                    numero = input("NÚMERO (PAIS - DDD - NUMERO)\n" + "EXEMPLO: 55011971161108\n" + "NÚMERO:")
                    if len(numero) != 14:
                        print("NÚMERO INVÁLIDO")
                    else:
                        passar = True
                        pais = numero[0:2]
                        ddd = numero[2:5]
                        n = numero[5:]
                        agenda.addContato(Contato(nome, 
                                                sobrenome, 
                                                pais, 
                                                ddd, 
                                                n))

            elif n == 2:
                agenda.delContato(input("QUAL NUMERO DELETAR (COMPLETO): "))
            
            elif n == 3:
                agenda.listarContatos()
            
            elif n == 4:
                sair = True
                break
            
            else:
                print("OPÇÃO INVÁLIDA")
        
        print("PROGRAMA FINALIZADO\n" +
              "----------------------")
              
    if __name__ == '__main__':
        main()