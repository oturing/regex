# coding: utf-8
import re

texto = '''linha 1
linha 2
outra linha
linha final
'''

texto2 = 'linha 1\nlinha 2\noutra linha\nlinha final\n'
print texto == texto2

print 'com re.MULTILINE'
print re.findall(r'^li', texto, re.MULTILINE)
print 'sem re.MULTILINE'
print re.findall(r'^li', texto)

texto3 = u'''Escreva uma regex capaz de encontrar no texto deste parágrafo
todas as palavras que teriminam com a letra “O”'''

print u' '.join(re.findall(ur'\w*[oO]\b', texto3, re.UNICODE))
print u' '.join(re.findall(ur'\b[AEIOUaeiou]\w*[AEIOUaeiou]\b', texto3, re.UNICODE))

print re.findall(ur'(\w+)\1', 'papa papo', re.UNICODE)

