# coding: utf-8

from unicodedata import name

squares = u'■ □ ◼ ◻ ⧉ ❒ ￭'

for c in squares.split():
	print c, hex(ord(c)), name(c)
