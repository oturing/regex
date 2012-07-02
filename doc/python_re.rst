=============================================
Expressões regulares em Python: módulo ``re``
=============================================

Conceitos
=========

Python não tem uma sintaxe literal para expressões regulares, como existe em Perl, JavaScript e Ruby (como ``/\d+/``). As funções do módulo ``re`` aceitam uma string representando a expressão regular. Recomenda-se prefixar a string com ``r''`` para indicar uma :term:`raw string`, evitand conflitos entre as sequências de escape de Python (como ``\b`` que é o caractere ASCII *backspace*) e os metacaracteres de regex (onde ``\b`` significa :term:`word boundary`). Veja um exemplo de uso da função ``match``:

>>> import re
>>> re.match(r'\d{4}$', '1234')
<_sre.SRE_Match object at 0x101161d30>

funções × métodos
=================

Se as expressões regulares são constantes e vão ser usadas muitas vezes, vale a pena construir um objeto expressão regular invocando a função ``re.compile``. O objeto devolvido tem métodos que correspondem às funções de mesmo nome. Exemplo com o método ``match``::

  >>> milhar = re.compile(r'\d{4}$')
  >>> milhar.match('1234')
  <_sre.SRE_Match object at 0x101161d30>

Em um laço com muitas aplicações de expressões regulares, esta segunda forma tem a vantagem de evitar repetir a compilação da expressão regular. A função ``timeit`` mostra redução do tempo de 1,56s para 0,41s::

  >>> from timeit import timeit
  >>> setup = """import re"""
  >>> timeit("""re.match(r'\d{4}', '1234')""", setup)
  1.5645811557769775
  >>> setup = """import re
  ... milhar = re.compile(r'\d{4}')"""
  >>> timeit("""milhar.match('1234')""", setup)
  0.4098658561706543

Vale notar que ``timeit`` executa o código do primeiro argumento 1.000.000 de vezes por default; em um sistema real, essa diferença pode ser irrelevante. O segundo argumento, ``setup`` nos exemplos acima, é executado apenas uma vez pelo ``timeit``.

``match`` × ``search`` 
----------------------

Os métodos de ``RegexObject.match`` e ``RegexObject.search`` tomam uma string como argumento e devolvem um objeto ``Match`` com informações sobre o padrão encontrado ou ``None`` caso o padrão não seja encontrado.

  >>> import re
  >>> milhar = re.compile('\d{4}')
  >>> milhar.match('9999')
  <_sre.SRE_Match object at 0x10317fd30>
  >>> milhar.match('999')                   # <- devolve None
  >>> milhar.match('999') is None
  True

O método ``match`` verifica se a expressão regular casa com o texto desde o início, enquanto ``search`` percorre o texto para tentar encontrar um casamento. Por exemplo::

  >>> milhar = re.compile('\d{4}')
  >>> milhar.match('1234xyz')
  <_sre.SRE_Match object at 0x10317fd30>
  >>> milhar.match('1234xyz')
  <_sre.SRE_Match object at 0x10317f850>
  >>> milhar.search('1234xyz')
  <_sre.SRE_Match object at 0x10317fd30>
  >>> milhar.match('abc1234xyz')            # <- devolve None
  >>> milhar.search('abc1234xyz')
  <_sre.SRE_Match object at 0x10317f850>

Na prática, o método ``match`` é conveniente para validar textos em formatos estruturados (por exemplo, validar um e-mail ou um telefone). O método ``search`` é mais útil para extrair informações de um texto do que para validar seu formato.


