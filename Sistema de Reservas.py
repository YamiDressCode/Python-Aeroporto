Estados = ["Acre", "Alagoas", "Amazonas", "Bahia", "Ceará", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul", 
               "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte", 
               "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"]
Assentos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

Extras = []

print("Bem vindo a Vorteix, para reservar seu voo precisaremos de alguns dados,por favor, Digite seu CPF:")
CPF = input()
print("Porfavor digite seu nome completo:")
Nome = input()
print("Porfavor selecione a data de partida")
print("Dia:")
dia = input()
print("Mês:")
mes = input()
print("Ano:")
ano = input()
print(f"Escolha seu serviço, 1 - Reservar voo , 2 - Ver voos disponiveis , 3 - Ver assentos ")
a = int(input())
if a == 1:
    c = ""
    while len(Assentos) > 0 and c != 1:
        print("Bem vindo ao aeroporto para onde deseja ir?")
        destino = input()
        print("Qual a origem do voo?")
        origem = input()
        if origem == destino:                                                #MENSAGEM CASO O USÁRIO QUEIRA IR PARA O MESMO ESTADO DE ORIGEM
            print("Você já está no local de Destino")
            break
        else: print("Você deseja passagem de 1 - Ida ou 2 - Ida e Volta?")
        Tipo = int(input())
       
        if Tipo == 2:                                               #ESCOLHA DE TIPO DE PASSAGEM
            print(f"Ok passagem de Ida e volta, de:{origem} para:{destino}")
        if Tipo == 1:
            print(f"Ok passagem de Ida, de:{origem} para:{destino}")
        print("Escolha seu assento")
        for y in Estados:
            if y == destino:                                       #COMPRA DE PASSAGEM POR ASSENTO
             print(f"Assentos Disponíveis : {Assentos}")
             lugar = int(input())
             Extras.append(lugar)
        for x in Assentos:
            if x == lugar:
                Assentos.remove(lugar)
                print("Deseja finalizar sua compra? (1-S/2-N)")
                c = int(input())
                if c == 2:
                        while c%2 == 0:
                         print("Escolha seus assentos extras")
                         print(f"Assentos Disponíveis:{Assentos}")
                         extra = int(input())
                         print("Deseja finalizar sua compra? (1-S/2-N)") 
                         c = int(input())
                         for w in Assentos:
                             if w == extra:
                                 Extras.append(extra)                                  
                                 Assentos.remove(extra)
                if c == 1:
                        custo = 80.00
                        total = len(Extras)*custo
                        print(f"<< Obrigado pela sua compra,\n {Nome},CPF:{CPF},seus assentos são {Extras} e seu destino é {destino},\n para a data de {dia}/{mes}/{ano},\n Total de:{total}.\n Valor unitário R$:80,00 >>")
                        breakpoint
                if c != 1 and c != 2:
                        print("Opção Inválida, porfavor reinicie")                                     
if len(Assentos) <= 0:                                            #CASO ONDE OS ASSENTOS ACABARAM E INFORMA O USUARIO
    print("Voos encerrados")
    breakpoint 
    #FUNÇÃO DE VER OS VOOS 
if a == 2:
    print(f"{Estados}")
    #FUNÇÃO DE VER OS ASSENTOS LIVRES
if a == 3:
    print(f"{Assentos}")