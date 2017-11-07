ent1 = input()
ent2 = input()
ent3 = input()

if(ent1 == "vertebrado"):
	if(ent2 == "ave"):
		if(ent3 == "carnivoro"):
			print("aguia")
		else:
			print("pomba")
	else:
		if(ent3 == "onivoro"):
			print("homem")
		else:
			print("vaca")
else:
	if(ent2 == "inseto"):
		if(ent3 == "hematofago"):
			print("pulga")
		else:
			print("lagarta")
	else:
		if(ent3 == "hematofago"):
			print("sanguessuga")
		else:            print("minhoca")