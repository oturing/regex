
.. _exercicios:

==========
Exercícios
==========

.. _exer_espec:

1. Especificadores e quantificadores
====================================

1.1. CPF com ou sem pontuação
-----------------------------

A expressão regular ``\d{3}\.\d{3}\.\d{3}\/\d{2}`` casa um CPF como
772.843.809-34. Inclua quantificadores para que a pontuação seja opcional. 

A regex resultante deve casar com 77284380934.

1.2. CPF com pontuação diferente ou espaços
-------------------------------------------

Modifique a solução do exercício 1.1 para aceitar CPFs escritos com espaços ou
pontos entre os grupos de três digitos, e com hifen ``-`` ou barra ``/`` antes
dos dois dígitos de controle.

A regex resultante deve casar com 772 843 809/34, 772.843.809/34, e continuar
casando com as strings aceitas pela solução de 1.1.

.. _exer_ancoras:

2. Âncoras
==========

2.1. Escreva uma regex capaz de encontrar no texto deste parágrafo todas as
palavras que teriminam com a letra "o".

2.2. Escreva uma regex capas de encontrar no parágrafo acima todas as palavras
que começam e terminam com vogais.


3. Agrupamento
==============

3.1. Hora e minutos
-------------------

Na seção :ref:`alguns_exem` da Introdução foi apresentada a expressão regular ``[012]\d:[0-5]\d`` para validar horas e minutos no formato HH:MM. Porém esta regex aceita o texto 25:00 que não é uma hora válida. Modifique a regex para corrigir esta falha. A solução envolve o uso 

3.2. Octeto de endereços IPv4
-----------------------------

Endereços IPv4 são formados por 4 octetos separados por ``:``, e cada octeto é
um número entre 0 e 255, por exemplo: 192.169.1.1. Note que 256 não é um octeto
válido, mas 156 é. Escreva uma regex para validar apenas um octeto de IPv4.

3.3. Endereços IPv4 completo
----------------------------

Amplie a solução do exercício 3.2 para validar endereços IP completos como
192.169.1.1 e 255.0.0.0.


