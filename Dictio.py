from classDictio import *

fruits=DictionnaireOrdonne()
fruits["pomme"]=52
fruits["poire"]=34
fruits["prune"]=128
fruits["melon"]=15
fruits.sort()
fruits.reverse()
leg=DictionnaireOrdonne()
leg["haricots"]=27
leg["patates"]=43
autre=DictionnaireOrdonne()

autre=fruits+leg

