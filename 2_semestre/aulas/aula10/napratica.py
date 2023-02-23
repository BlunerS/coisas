def gradiente_descendente(x0, função, gradiente):
    precisao=1
    taxa_aprendizagem=0.0001
    max_interacoes = 1000
    x_novo = x0
    f_x_novo = funcao(x_novo)
    f_x_velho = funcao(x_novo)+100
    i=0

    while(abs(f_x_novo - f_x_velho) > precisao) and (i <= max_interacoes):
        x_velho = x_novo
        x_novo = x_velho - taxa_aprendizagem * gradiente(x_velho)
        f_x_novo = função(x_novo)
        f_x_velho = função(x_velho)
        i=i+1

    print("Precisão Alcançada:",(f_x_novo - f_x_velho))
    print("X =", x_novo)
    print("f(x)=", f_x_novo)
    return[x_novo, f_x_novo]