# Projeto interdisciplinar cruzeiro do sul 2022.

### Opção 1 converter números inteiros na base 10 para números binários, hexadecimais e octais.
<br>


# Como usar

Ao executar o comando `python src/conversao.py` deverá aparecer o menu abaixo:

## Menu

![Menu](./assets/Menu.png)

## Conversão de base 10 para base 2
Ao utilizar a `opção 1` será solicitado um número inteiro na base 10 para conversão em binário.
![ExemploDecimalParaBinario](./assets/InteiroParaBinario.png)
Fonte: https://en.wikipedia.org/wiki/Binary_number

## Conversão de base 10 para base 16
Ao utilizar a `opção 2` será solicitado um número inteiro na base 10 para conversão em hexadecimal
![ExemploDecimalParaHexadecimal](./assets/InteiroParaHexa.png)
Fonte: https://en.wikipedia.org/wiki/Hexadecimal

## Conversão de base 10 para base 8
Ao utilizar a `opção 3` será solicitado um número inteiro na base 10 para conversão em octal
![ExemploDecimalParaHexadecimal](./assets/InteiroParaOctal.png)
Fonte: https://en.wikipedia.org/wiki/Octal

Ao utilizar a `opção 9` o sistema deverá fechar.

Se qualquer outro número ou letra for utilizado o sistema solicitará novamente que o usuário escolha uma opção.

# Sobre o fonte

## Código do menu
Na primeira parte do código eu crio um dicionário onde:
 - A `chave` é a opção que deverá ser selecionada no menu.
 - O `valor` é a função que deverá ser executada quando a opção for escolhida.

Em seguida crio a função `mostrarMenu` que é responsável por mostrar as opções disponíveis.

Após a criação da função inicializo a variável escolha com '-1' para que ela não esteja entre as opções e entre no while.

Dentro do while chamo a função `mostrarMenu`.<br>
Solicito que o usuário escolha uma das opções.<br>
Se a escolha for `9` encerro o processo.<br>
Se a escolha estiver entre as opções possíveis executo a função associada a escolha.

``` Python
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
```

## Código de conversão em binário

O código da conversão em binário é uma função recursiva que calcula o quociente da divisão entre o valor recebido como parâmetro e o número 2.<br>
Caso o quociente seja 0 ele retorna `'1'`.<br>
Em seguida calcula o resto da mesma divisão feita anteriormente.<br>
Initializa a variavel atual com o valor `'0'` e se o resto for maior que zero substitui o valor por `'1'`.<br>

Por fim retorna recursivamente a concatenação do cálculo binário do quociente mais o cálculo binário já realizado.

``` Python
def paraBinario(valorInteiro):    
    quociente = int(valorInteiro / 2)    
    if(valorInteiro == 0):
        return 0

    if(quociente == 0):
        return '1'
    
    resto = valorInteiro % 2    
    atual = '0'
    if(resto > 0):
        atual = '1'

    return paraBinario(quociente) + atual
```

## Código de conversão em hexadecimal

O código da conversão em hexadecimal possui dois métodos.<br>
O primeiro método calcula o hexadecimal.<br>
O segundo método substitui o valor calculado pelo caracter respectivo.<br>
Similar a conversão para binário, a conversão para hexadecimal é uma série de divisões porém, dessa vez, por `16`.

``` Python
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
```

## Código de conversão em octal

A conversão em octal é talvez a mais complexa.<br>
Primeiro devemos identificar por qual número faremos a divisão do valor recebido como parâmetro.<br>
Para isso o método `maiorPotencia` calcula a maior potência de `8` que seja menor que o valor passado por parâmetro.<br>
Este valor então é utilizado como divisor do valor a ser convertido.<br>
O quociente dessa divisão é por fim concatenado com o resto caso o divisor seja 8.<br>
Ou ele será concatenado com o mesmo cálculo feito para o valor do resto.

``` Python
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
```
# Fontes

As fontes de pesquisa utilizadas foram:<br>
https://en.wikipedia.org/wiki/Octal<br>
https://en.wikipedia.org/wiki/Binary_number<br>
https://en.wikipedia.org/wiki/Hexadecimal

A ferramenta utilizada para conferencia dos valores:<br>
https://www.rapidtables.com/convert/number/binary-to-decimal.html
