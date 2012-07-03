.. _glossario:

=========
Glossário
=========

.. if you add new entries, keep the alphabetical sorting!

.. glossary::

   casar
      Combinar. Diz-se que uma expressão regular *casa* com um texto quando os
      caracteres e :term:`metacaractere`\s especificados na regex correspondem
      aos caracteres do texto, na ordem correta. Por exemplo, ``\d,\d`` casa
      com ``9,1`` mas não com ``9,`` (falta o dígito após a vírgula), e nem
      com ``91,`` (a vírgula não está entre os dígitos).

   conjunto
      Um conjunto de caracteres, como ``[AEIOUaeiou]`` para representar as
      vogais sem acentos, ou ``[0-9A-F]`` para os dígitos hexadecimais. Em uma
      expressão regular, um conjunto casa com uma ocorrência de um de seus
      caracteres, a não ser que o conjunto seja seguido de um quantificador.
      Existem :term:`metacaractere`\s que representam conjuntos pré-definidos,
      como por exemplo ``\d`` que é o mesmo que ``[0-9]``. O conjunto pode ser
      negado pelo uso do sinal ``^`` na primeira posição. Assim,
      ``[^AEIOUaeiou]`` representa qualquer caractere que não seja uma vogal.

   expressão regular
      Da Wikipédia: "Em ciência da computação, uma expressão regular [...]
      provê uma forma concisa e flexível de identificar cadeias de caracteres
      de interesse, como caracteres particulares, palavras ou padrões de
      caracteres." Na teoria das linguagens formais, as expressões regulares
      são exemplos de linguagens regulares, que podem ser processadas por um
      autômato finito. Na prática, as bibliotecas de regex mais populares são
      mais expressivas que as linguagens regulares, por exemplo ao permitir a
      definição de grupos e sua aplicação posterior na mesma expressão.
      (**en**: regular expression)

   grupo
      Uma parte de uma expressão regular delimitada por ``()``. Os grupos
      servem para facilitar a aplicação de quantificadores, para indicar
      trechos repetidos de uma regex (através de metacarateres numéricos, como
      ``\1``) ou para extração de partes específicas do texto através dos
      métodos

   metacaractere
      Um caractere que tem um significado especial dentro de uma expressão
      regular, como ``.`` ou ``?`` ou ``(`` e ``)``. Alguns metacaracteres são
      representados por mais de um caractere literal, por exemplo, ``\w`` é um
      metacaractere que representa qualquer caractere alfanumérico. Alguns
      metacaracteres têm significado diferente conforme o local onde ocorrem
      na expressão regular. O sinal ``?`` pode ser o quantificador de zero ou
      uma ocorrência, mas quando aparece após outro quantificador o ``?``
      modifica o quantificador anterior para deixá-lo não-guloso; e dentro de
      um conjunto como ``[abc?]`` o ``?`` significa apenas um ponto de
      interrogação literal.

   quantificador
      Indicador que determina quantas vezes a sequência imediatamente
      precedente deve ocorrer no padrão. A sintaxe mais geral é ``{a,b}`` onde
      ``a`` é a quantidade mínima de ocorrências e ``b`` é a máxima. Os
      quantificadores abreviados ``?``, ``+``, ``*`` significam
      respectivamente o mesmo que ``{0,1}``, ``{1,}`` (1 ou mais) e ``{,}`` (0
      ou mais).

   raw string
      (**pt**: string crua) 
      Em Python, o prefixo ``r`` pode ser usado em strings literais como
      ``r'a\nb'`` ou ``ur'a\nb'` para indicar que as contra-barras ``\`` devem
      ser interpretadas como caracteres comuns, e não como prefixos de
      sequência de escape. Nos exemplos acima, ``r'a\nb'`` é uma sequência de
      4 caracteres: ``a``, ``\``, ``n`` e ``b``. Em contraste, a string
      ``'a\nb'`` tem 3 caracteres: ``a``, ``\n`` (ASCII LF, decimal 10), e
      ``b``. Note que o ``r`` é apenas um artifício sintático, ele não altera
      o tipo da string sendo criada mas apenas seu conteúdo, pela
      interpretação diferente dos caracteres literais.

   word boundary
      (**pt**: limite de palavra) 
      A posição logo antes ou logo após uma palavra em uma expressão regular,
      denotada pelo metacaractere ``\b``.

