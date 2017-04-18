def sum_of_num(name,cmpy,*colls, **keyw):
	print (name,cmpy, sep="@", end= "\t")
	print (colls)
	print (keyw)

sum_of_num('Steve', 'Apple',11,12,13,14,15, lang="Python", author="Guido Van Rossum", version = 3.5)
#name="Steve", cmpy = "Apple", age= 67