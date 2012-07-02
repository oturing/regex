================================
Expressões regulares: introdução
================================

Idéia básica
============

- Uma expressão regular é uma notação para representar padrões em strings.

- O termo em inglês é *regular expression* de onde vem as abreviações *regex* e *RE* (o módulo Python pertinente chama-se ``re``). Em ciência da computação, o termo :term:`expressão regular` tem um significado bem específico; na prática, as notações usadas na maioria das linguagens de programação atuais são mais expressivas que as expressões regulares da teoria de linguages formais.

- Alguns exemplos:

  - ``\d{5}-\d{3}`` é o padrão de um CEP: 5 dígitos, um ``-`` (hífen) e mais 3 dígitos, como ``05432-001``; o sequência ``\d`` é um :term:`metacaractere`, que representa um dígito (0 a 9); a sequência ``{n}`` é um :term:`quantificador`: ela indica que o padrão precedente deve ser repetido ``n`` vezes.

  - ``\d{1,2}:\d{2}`` representa um número em formato de horas e minutos, como ``3:59`` ou ``14:00``; o quantificador {1,2} indica que o texto deve ter 1 ou 2 dígitos antes do sinal ``:``; note que esta expressão regular também representa o texto ``99:99`` que não é uma hora válida (horas válidas serão o tema de um exercício).

  - ``[A-Z]{3}-\d{4}`` é o padrão de uma placa de automóvel no Brasil: três letras de ``A`` a ``Z`` seguidas de um ``-`` (hífen) seguido de quatro dígitos, como ``CKD-4592``; uma sequência entre colchetes como ``[A-Z]`` define um :term:`conjunto` e dentro dos ``[]`` o hífen serve para indicar uma faixa de caracteres, ou seja, ``[A-E]`` é uma forma abreviada de especificar o conjunto ``[ABCDE]``.

  
