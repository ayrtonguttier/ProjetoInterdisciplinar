# Projeto interdisciplinar cruzeiro do sul 2022.

## Índice

[ComoUsar][Como usar]


# Como usar

Ao executar o comando "python conversao.py" deverá aparecer o menu abaixo:

![Menu](./assets/Menu.png)

## Conversão de base 10 para base 2
Ao utilizar a opção 1 será solicitado um número inteiro na base 10 para conversão em binário.
![ExemploDecimalParaBinario](./assets/InteiroParaBinario.png)
Fonte: https://en.wikipedia.org/wiki/Binary_number

## Conversão de base 10 para base 16
Ao utilizar a opção 2 será solicitado um número inteiro na base 10 para conversão em hexadecimal
![ExemploDecimalParaHexadecimal](./assets/InteiroParaHexa.png)
Fonte: https://en.wikipedia.org/wiki/Hexadecimal

## Conversão de base 10 para base 8
Ao utilizar a opção 3 será solicitado um número inteiro na base 10 para conversão em octal
![ExemploDecimalParaHexadecimal](./assets/InteiroParaOctal.png)
Fonte: https://en.wikipedia.org/wiki/Octal

Ao utilizar a opção 9 o sistema deverá fechar.

Se qualquer outro número ou letra for utilizado o sistema solicitará novamente que o usuário escolha uma opção.

# Sobre o fonte

## Código do menu

Na primeira parte do código eu crio um dicionário onde:<br>
A <b>chave</b> é a opção que deverá ser selecionada no menu.<br>
O <b>valor</b> é a função que deverá ser executada quando a opção for escolhida.

Em seguida crio a função <b>mostrarMenu</b> que é responsável por mostrar as opções disponíveis.

Após a criação da função inicializo a variável escolha com '-1' para que ela não esteja entre as opções e entre no while.

Dentro do while chamo a função <b>mostrarMenu</b>.<br>
Solicito que o usuário escolha uma das opções.<br>
Se a escolha for <b>9</b> encerro o processo.<br>
Se a escolha estiver entre as opções possíveis executo a função associada a escolha.

![CódigoMenu](./assets/CodigoMenu.png)

## Código de conversão em binário

O código da conversão em binário é uma função recursiva que calcula o quociente da divisão entre o valor recebido como parâmetro e o número 2.<br>
Caso o quociente seja 0 ele retorna '1'.<br>
Em seguida calcula o resto da mesma divisão feita anteriormente.<br>
Initializa a variavel atual com o valor '0' e se o resto for maior que zero substitui o valor por '1'.<br>

Por fim retorna recursivamente a concatenação do cálculo binário do quociente mais o cálculo binário já realizado.

![CódigoBinário](./assets/CodigoBinario.png)


## Código de conversão em hexadecimal

O código da conversão em hexadecimal possui dois métodos.<br>
O primeiro método calcula o hexadecimal.<br>
O segundo método substitui o valor calculado pelo caracter respectivo.<br>
Similar a conversão para binário, a conversão para hexadecimal é uma série de divisões porém, dessa vez, por 16.

![CódigoHexadecimal](./assets/CodigoHexa.png)


## Código de conversão em octal

A conversão em octal é talvez a mais complexa.<br>
Primeiro devemos identificar por qual número faremos a divisão do valor recebido como parâmetro.<br>
Para isso o método <b>maiorPotencia</b> calcula o maior múltiplo de 8 que seja menor que o valor passado por parâmetro.<br>
Este valor então é utilizado como divisor do valor a ser convertido.<br>
O quociente dessa divisão é por fim concatenado com o resto caso o divisor seja 8.<br>
Ou ele será concatenado com o mesmo cálculo feito para o valor do resto.

![CódigoOctal](./assets/CodigoOctal.png)


# Fontes

As fontes de pesquisa utilizadas foram:<br>
https://en.wikipedia.org/wiki/Octal<br>
https://en.wikipedia.org/wiki/Binary_number<br>
https://en.wikipedia.org/wiki/Hexadecimal

A ferramenta utilizada para conferencia dos valores:<br>
https://www.rapidtables.com/convert/number/binary-to-decimal.html
