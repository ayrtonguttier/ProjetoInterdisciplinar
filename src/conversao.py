
# https://en.wikipedia.org/wiki/Octal

def paraOctal(valorInteiro):
    divisor = maiorPotencia(valorInteiro)

    quociente = int(valorInteiro / divisor)
    resto = valorInteiro % divisor

    if(divisor == 8):
        return str(quociente) + str(resto)

    return str(quociente) + paraOctal(resto)

def maiorPotencia(valorInteiro):
    potencia = 8
    while True:
        aux = potencia * 8
        if aux > valorInteiro:            
            return potencia
        else:
            potencia = aux

# https://en.wikipedia.org/wiki/Octal



#https://en.wikipedia.org/wiki/Binary_number
def paraBinario(valorInteiro):    
    quociente = int(valorInteiro / 2)    
    if(quociente == 0):
        return '1'
    
    resto = valorInteiro % 2    
    atual = '0'
    if(resto > 0):
        atual = '1'

    return paraBinario(quociente) + atual
#https://en.wikipedia.org/wiki/Binary_number



# https://en.wikipedia.org/wiki/Hexadecimal
def paraHexadecimal(valorInteiro):
    resto = valorInteiro % 16
    if(valorInteiro - resto == 0):
        return buscaCaracter(resto)
    
    proximoValor = int((valorInteiro - resto) / 16)
    proximoChar = paraHexadecimal(proximoValor)
    charAtual = buscaCaracter(resto)    
    return proximoChar + charAtual

def buscaCaracter(number):
    alpha = "0123456789ABCDEF"
    return alpha[number]
# https://en.wikipedia.org/wiki/Hexadecimal


menu = {}
menu['1'] = paraBinario
menu['2'] = paraHexadecimal
menu['3'] = paraOctal

def mostrarMenu():        
    print('1 - Inteiro para binário')
    print('2 - Inteiro para hexadecimal')
    print('3 - Inteiro para octal')
    print('9 - Encerrar aplicação')

escolha = '-1'

while(escolha not in menu.keys()):
    mostrarMenu()
    escolha = input('Escolha entre as opções acima para conversão: ')
    if(escolha == '9'):
        exit()

    if(escolha in menu.keys()):
        valor = int(input('Forneça o valor para conversão: '))
        print('O resultado da conversão é: ' + menu[escolha](valor))
        print('')
        escolha = '-1'





# para conferencia dos valores foi utilizada a ferramenta: https://www.rapidtables.com/convert/number/binary-to-decimal.html