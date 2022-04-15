from colorama import Fore

def InteiroParaBinario(valor, processaResultado):
    aux = valor
    resultado = ""
    continua = True
    while continua:
        resto = aux % 2
        aux = int(aux / 2)
        if(resto > 0):
            resultado = "1" + resultado
        else:
            resultado = "0" + resultado
        if aux == 0:
            continua = False
    processaResultado(resultado)

def InteiroParaHexadecimal(valor, processaResultado):
    caracteres = "0123456789ABCDEF"
    resultado = ""
    aux = valor
    continua = True
    while continua:
        resto = aux % 16
        if(aux - resto == 0):
            resultado = caracteres[resto] + resultado
            continua = False
        else:
            resultado = caracteres[resto] + resultado
            aux = int((aux - resto) / 16)
    processaResultado(resultado)

def MaiorPotencia(valorInteiro):
    potencia = 8
    while True:
        aux = potencia * 8
        if aux > valorInteiro:
            return potencia
        else:
            potencia = aux

def InteiroParaOctal(valor, processaResultado):
    resultado  = ""
    aux = valor
    continua = True
    while continua:
        maiorPotencia = MaiorPotencia(aux)
        quociente = int(aux / maiorPotencia)
        resto = aux % maiorPotencia

        resultado = resultado + str(quociente)

        aux = resto
        if(maiorPotencia == 8):
            resultado = resultado + str(resto)
            continua = False

    processaResultado(resultado)

def Todos(valor, processaResultado):
    print("Inteiro para " + ColoreTexto(Fore.BLUE, "binário") + ":")
    InteiroParaBinario(valor, processaResultado)

    print("Inteiro para " + ColoreTexto(Fore.BLUE, "hexadecimal") + ":")
    InteiroParaHexadecimal(valor, processaResultado)


    print("Inteiro para "+ ColoreTexto(Fore.BLUE, "octal") +":")
    InteiroParaOctal(valor, processaResultado)

def Sair():
    exit(0)


dicionarioDeFuncoes = {
    1: InteiroParaBinario,
    2: InteiroParaHexadecimal,
    3: InteiroParaOctal,
    4: Todos,
    9: Sair
}

def solicitarTipo():
    for key in dicionarioDeFuncoes:
        print(str(key) + " - " + dicionarioDeFuncoes[key].__name__)
    try:
        escolha = int(input("Escolha entre as opções acima: \n"))
        print("")
        return escolha
    except:
        return solicitarTipo()

def solicitarValor():
    try:
        escolha = int(input("Forneça o valor para conversão: \n"))
        print("")
        return escolha
    except:
        print("Favor digite um valor inteiro válido.")
        return solicitarValor()

def Calcular(funcao, processaResultado):
    valor = solicitarValor()
    funcao(valor, processaResultado)

def ColoreTexto(cor, texto):
    return cor + texto + Fore.RESET

def EscreveResultado(resultado):
    print("O resultado do cálculo é: " + ColoreTexto(Fore.RED, resultado))
    print("")

def Run():
    tipo = solicitarTipo()
    if tipo == 9:
        dicionarioDeFuncoes[tipo]()
    else:
         Calcular(dicionarioDeFuncoes[tipo], EscreveResultado)

    Run()


Run()
