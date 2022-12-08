from functools import reduce


def cont():
    pessoas = [
    {'nome': 'Pedro', 'idade': 11},
    {'nome': 'Mariana', 'idade': 18},
    {'nome': 'Arthur', 'idade': 26},
    {'nome': 'Rebeca', 'idade': 6},
    {'nome': 'Tiago', 'idade': 19},
    {'nome': 'Gabriela', 'idade': 17},
    ]

    mapeado = map(lambda i: i['idade'], pessoas)
    filtrado = filter(lambda f: f < 18, mapeado)
    soma_idades = reduce(lambda idade, f: idade + f, filtrado, 0)

    # soma_idades = reduce(lambda idade, f: idade + f, filter(lambda f: f < 18, map(lambda i: i['idade'], pessoas)), 0)


    print(soma_idades)
    return soma_idades