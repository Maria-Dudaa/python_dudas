import random
# Função que gera a introdução da história
def gerar_instrucao():
    instrucoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(instrucoes)

# função que gera o desenvolvimento da história
def gerar_desenvolvimento ():
    densenvolvimentos = ["um valente cavaleiro","uma destemida guerreira", "um bravo guerreiro",
                         "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(densenvolvimentos)

#função que gera o final da historia 
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.",
              "descobrindo um tesouro escondido." , "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)
    
def gerar_historia():
    introducao = gerar_instrucao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao}  {desenvolvimento}  {final}"
    return historia

#exibe a história gerada

if __name__== "__main__":
    print(gerar_historia())