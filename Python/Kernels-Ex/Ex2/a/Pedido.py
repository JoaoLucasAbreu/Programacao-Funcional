class Pedido:
    def __init__(self, numero_pedido, data, valor_total, pag, itens_pedido = []):
        self.valor_total = valor_total
        self.pag = pag
        self.itens_pedido = itens_pedido
        self.numero_pedido = numero_pedido
        self.data = data

    
    def listar_itens(self):
        return  self.itens_pedido

    def getItensPedidos(self):
        for p in self.itens_pedido:
            print(f"PRODUTO: {p.nome}, MARCA: {p.marca}\nCATEGORIA: {p.categoria}\nVALOR: R${p.preco}\nQUANTIDADE: {p.estoque}\n")

        
