from datetime import date
from Produto import Produto
from Pedido import Pedido
import random
import time
list_produtos = []
list_pedidos = []  

class Main():
    def main():
        print("REALIZAR PEDIDOS\n" +
              "----------------------------")
        time.sleep(3)    
        p1 = Produto(1, 'alvejante', 'OMO', 'limpeza', 24.00, 30)
        p2 = Produto(2, 'miojo', 'nissin lámen', 'pastas', 2.00, 21)
        p3 = Produto(3, 'coca-cola 1L', 'coca-cola', 'refrigerantes', 7.00, 52)
        list_produtos.append(p1)
        list_produtos.append(p2)
        list_produtos.append(p3)

        sair = False
        while sair is False:
            print("OPÇÕES:\n" + "[1] REALIZAR UM PEDIDO\n" + "[2] LISTAR PEDIDOS ANTERIORES\n" + "[3] FINALIZAR")

            n = int(input("OPÇÃO: "))
            print(" ")

            if n == 1:
                produtos = []
                for p in list_produtos:
                    print(f"[{p.id}] PRODUTO: {p.nome}, PRODUTO: {p.marca}, CATEGORIA: {p.categoria}, PREÇO: R${p.preco}, QUANTIDADE DE ESTOQUE: {p.estoque}")

                print("----------------------------")
                passar = False
                while passar == False:
                    opcao = int(input("ESCOLHER PRODUTO [ID]:"))
                    for p in list_produtos:
                        if opcao == p.id:
                            qt = int(input("QUANTIDADE:"))
                            if qt <= 0 or qt > p.estoque:
                                print("DIGITE UM VALOR POSSÍVEL")

                            else:
                                p.estoque =  p.estoque - qt

                                prod = Produto(p.id, p.nome, p.marca, p.categoria, p.preco, qt)
                                prod.preco = qt * prod.preco
                                produtos.append(prod)
                    
                    finalizar = int(input("FINALIZAR PEDIDO? \n" + "[1] SIM \n" + "[2] NÃO\n" + "OPÇÃO:"))
                    if finalizar == 1:
                        passar = True

                soma = 0
                for p in produtos:
                    soma =  soma + p.preco 

                print(f"VALOR TOTAL R${soma}")
                passar = False
                while passar == False:
                    pag = int(input("MÉTODO DE PAGAMENTO \n" + "[1] CRÉDITO\n" + "[2] DÉBITO\n" + "OPÇÃO:"))
                    if pag == 1:
                        pag = "Crédito"
                        passar = True
                        break

                    elif pag == 2:
                        pag = "Dédito"
                        passar = True
                        break

                    else:
                        print("OPÇÃO INVÁLIDA")
        
                pd = Pedido(random.randint(1,1000), date.today(), soma, pag, produtos)
                list_pedidos.append(pd)
                print("COMPRA FINALIZADA\n" + "----------------------------\n")

            elif n == 2:
                print("PEDIDOS REALIZADOS")
                print("----------------------------")
                for p in list_pedidos:
                    print(f"Id do Pedido: {p.numero_pedido}\nData {p.data}\nValor total R${p.valor_total}\nTipo de pagamento {p.pag}")
                    p.getItensPedidos()
                    print("----------------------------")
            elif n == 3:
                sair = True
                break
            
            else:
                print("OPÇÃO INVÁLIDA")
        
        print("PROGRAMA FINALIZADO\n" +
              "----------------------")

    if __name__ == '__main__':
        main()