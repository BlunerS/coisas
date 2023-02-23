def calcula (a, b):
    soma=a+b
    divide=a/b
    multiplica=a*b
    return soma, divide, multiplica

def calcula_preco (preco_compra, markup) :
    preco_venda = markup * preco_compra
    return preco_venda