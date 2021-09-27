# Curso-Python-Alura

Codigos baseados no curso de python na alura.

## Curso jogos (pasta jogos)

O programa se inicia com o arquivo jogos.py. Lá é possivel selecionar o jogo que quer jogar. Você poderá optar pelo jogo da forca ou de adivinhação:

### Forca

O jogo da forca é um jogo em que o programa lê um arquivo txt q contém diversas palavras. O jogo sorteia uma aleatóriamente, e na sequencia  seleciona para ser a palavra escolhida. O jogador poderá chutar letras e a cada letra chutada certa, a letra será mostrada na posição correta na palavra. Caso erre, uma "parte do corpo" sera colocada na forca, sendo no total 7 tentativas. 

### Adivinhação 

O jogo da adivinhação é um jogo em que tem como objetivo acertar um número entre 1 e 100 escolhido pelo computador aleatóriamente. No início do jogo é possivel escolher o nível de dificudade sendo elas: Fácil (com 20 tentativas), Médio (com 10 tentativas) e Difícil (com 5 tentativas).

## Curso brasilidades

O curso de brasilidades foi ensinado a fazer um tratamento de dados nos padrões brasileiros. Utilizando recursos de Orientação a Objeto, bibliotecas e uma API.

### Validação de CPF e CNPJ

Utilizou inicialmente uma verificação para uma contagem de digitos para saber se é um Cpf ou Cnpj chamando uma classe estatica chamada Documento. Ao verificar o número de digitos é chamada a inicialização da classe do documento selecionado. Utilizando a biblioteca validate_doccbr foi possivel validar os números dos documentos, independente se for um CPF ou um CNPJ. Foi implementado também um método str para exibir o CPF no padrão "xxxxxxxxx-xx" e o CNPJ no padrão "xx.xxx.xxx/xxxx-xx" utilizando métodos da biblioteca. 

### Validação de Telefones

Para a validação de telefones foi utilizado uma expressão regular para que seja possivel validar telefones com 8 números (residenciais) e com 9 números (celulares), além de não validar telefones sem o código de área e ainda sendo opcional o codigo de país. Tambem foi implementado uma classe str para que ao printar o numero de telefone ele tenha o padrão "+xx(xx)xxxxx-xxxx" 

### Manipulação e Formatação de Datas

Para isso foi utilizado uma biblioteca chamada datetime na qual era possivel a utilização de diversas funções de manipulações de datas, além de ter diversas funcionalidades para manipulação das mesmas. No projeto foi criado funçoes para mostrar o dia da semana do cadastro, o tempo que o usuário esta cadastrado alem de formatar a data no padrão "dia/mês/ano hora:minutos".

### Verificação de CEP

Para isso foi utilizado uma API chamada viacep (https://viacep.com.br) no qual é possível, através de um CEP, ter retornos de logradouro, cidade, uf e muito mais. Com isso, foi implementado no projeto uma função que, ao registrar o cep, ela retorna o bairro, cidade e estado daquele cep extraindo os dados de um arquivo .json. 


