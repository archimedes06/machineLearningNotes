from itertools import chain, imap
#itertools = https://docs.python.org/2/library/itertools.html
#chain: https://docs.python.org/2/library/itertools.html
#
#enumerate is the equivalent of zipWithIndex in scala

def flatmap(f, items):
	return chain.from_iterable(imap(f, items))