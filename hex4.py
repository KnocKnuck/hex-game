from jeux import *
from resolution import *

game_size=4

lenght=game_size-1

# SPÉCIFIQUE AU MORPION

# état du morpion
# une matrice 4x4
# on pourrait ajouter le nombre de cases vides
# on pourrait ajouter la liste des cases vides

# joueurs = X et O

# un coup = coordonnées (ligne,colonne) d'une case vide

def copie_matrice (matrice) :
	return [
		[matrice[0][0],matrice[0][1],matrice[0][2],matrice[0][3]],
		[matrice[1][0],matrice[1][1],matrice[1][2],matrice[1][3]],
		[matrice[2][0],matrice[2][1],matrice[2][2],matrice[2][3]],
		[matrice[3][0],matrice[3][1],matrice[3][2],matrice[3][3]]
		]


def liste_cases_vides (matrice):
	vides = []
	for nl in range(game_size):
		for nc in range(game_size):
			if matrice[nl][nc]==' ':
				vides.append((nl,nc))
	return vides

def find_path(matrice,symbole,begin,end,path,occ): #DEBUGER CA A COUP DE PRINT DANS LA GUEULE
	y=begin[0]
	x=begin[1]
	# print(x)
	# print(y)
	# print(end)
	path+=(x,y)
	possible=[(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1)]
	occ+=1
	if (occ>100):
		return False

	
	
	if x==0 and y==0:
		possible.remove((x-1,y+1))
		possible.remove((x-1,y))
		possible.remove((x,y-1))
		possible.remove((x+1,y-1))
	else:
		if x==lenght and y==lenght:
			possible.remove((x+1,y))
			possible.remove((x+1,y-1))
			possible.remove((x-1,y+1))
			possible.remove((x,y+1))
		else:
			if x==0 and y==lenght:
				possible.remove((x-1,y+1))
				possible.remove((x-1,y))
				possible.remove((x,y+1))
			else:
				if x==lenght and y==0:
					possible.remove((x+1,y))
					possible.remove((x,y-1))
					possible.remove((x+1,y-1))
				else:
					if x==0:
						possible.remove((x-1,y+1))
						possible.remove((x-1,y))
					if x==lenght:
						possible.remove((x+1,y))
						possible.remove((x+1,y-1))
					if y==0:
						possible.remove((x,y-1))
						possible.remove((x+1,y-1))
					if y==lenght:
						possible.remove((x-1,y+1))
						possible.remove((x,y+1))
	# print(possible)
	for i,j in possible:
		a=0
		# print((i,j))
		while(a<int(len(path)/2)):
			if(i==path[2*a] and j==path[2*a+1]):
				possible.remove((i,j))
				a=int(len(path)/2)
			a+=1
							
	a=0
	possiblei=[]
	possiblej=[]
	while(a<len(possible)):
		i=possible[a][0]
		j=possible[a][1]
		if matrice[i][j]==symbole:
			if i==end[0] and j==end[1]:
				return True
			else:
				possiblei.append(i)
				possiblej.append(j)
				
		
		a+=1
	a=0
	while(a<len(possiblei)):
		if(find_path(matrice,symbole,[possiblej[a],possiblei[a]],end,path,occ)):
			return True
		a+=1
	
	

	
	
def présence_ligne (matrice,symbole):
	Trouve=0

	if symbole=="X":
		debutpossible=[]
		end=[]
		for x in range(game_size):
			if matrice[x][0]==symbole:
				debutpossible.append(x)
			if matrice[x][lenght]==symbole:
				end.append(x)
		a=0;
		while(a<len(debutpossible)):
			b=0
			while(b<len(end)):
				debut=(0,debutpossible[a])
				# print(debut)
				fin=(end[b],lenght)
				if(find_path(matrice,symbole,debut,fin,(debutpossible[a],0),0)):
					Trouve=1
				b+=1
			a+=1
				
		if(Trouve==1):
			return(True)
		else:
			return(False)

	if symbole=="O":
		debutpossible=[]
		end=[]
		for x in range(game_size):
			if matrice[0][x]==symbole:
				debutpossible.append(x)
			if matrice[lenght][x]==symbole:
				end.append(x)
		a=0;
		while(a<len(debutpossible)):
			b=0
			while(b<len(end)):
				debut=(debutpossible[a],0)
				fin=(lenght,end[b])
				if(find_path(matrice,symbole,debut,fin,(0,debutpossible[a]),0)):
					Trouve=1
				b+=1
			a+=1
				
		if(Trouve==1):
			return(True)
		else:
			return(False)



# bonus


def matrice_en_texte (matrice) :
	trait = "  ·———·———·———·———·\n"
	texte = "   1   2   3   4 \n"+trait
	for i in range(game_size):
		ligne =matrice[i]
		j=i
		while j>0:
			if j==9:
				texte += " "
				j=8
			# if j==10:
				# trait = "  ·———·———·———·———·———·———·———·———·———·———·———·\n"
				# texte += "   "
				# j=8
			j-=1
			texte +="  "
		texte += str(i+1)+"  \ "+ligne[0]+" \ "+ligne[1]+" \ "+ligne[2]+" \ "+ligne[3]+" \ \n"
		j=i
		texte +="  "
		while j>0:

			j-=1
			texte +="  "
		texte +=  trait
	j=i
	while j>0:
		j-=1
		texte +="  "
	texte += "	    1   2   3   4 \n"
	return texte


def affiche_matrice (matrice) :
	print()
	print(matrice_en_texte(matrice))



def adversaire (joueur) :
	if joueur=='X':
		return 'O'
	else:
		return 'X'


# INSTANCIATION DES FONCTIONS GÉNÉRIQUES POUR LE MORPION

def coups_possibles (état,joueur):
	return liste_cases_vides(état)


def applique_coup (état,joueur,coup):
	nm = copie_matrice(état)
	(ligne,colonne) = coup
	nm[ligne][colonne] = joueur
	return nm


def fin_partie (état,id_minmax,adversaire,mon_tour):
	if (présence_ligne(état,"X")):
		return (True,"X")
	elif (présence_ligne(état,"O")):
		  return (True,"O")
	elif (liste_cases_vides(état)==[]):
		return (True,"")
	else:
		return (False,"")


# pour l'interaction avec l'utilisateur

def int_input (msg):
	try:
		val = int(input(msg))
	except ValueError:
		val = -1
	return val


état_initial = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]


# APPELS DES FONCTIONS DE JEU

état_courant = état_initial
#état_courant = [['X',' ','X'],[' ','O',' '],[' ',' ','O']]

joueuria = "X"
humain   = adversaire(joueuria)

humain_joue = True # qui commence ?

partie_en_cours = True

affiche_matrice(état_courant)


while (partie_en_cours) :

	# au joueur humain de jouer...
	if humain_joue :
		saisie_ok = False
		while not saisie_ok:
			lig = int_input("  Ligne de votre coup  : ")-1
			col = int_input("Colonne de votre coup  : ")-1
			if ((lig in range(0,game_size)) and (col in range(0,game_size)) and état_courant[lig][col]==" ") :
				saisie_ok = True
			else:
				if lig==41 and col==41:
					saisie_ok = True
					lig=0
					col=0
					état_courant=[[' ',' ',' ',' '],['O',' ',' ',' '],['O',' ',' ',' '],['O',' ',' ',' ']]
				else:
					print("On recommence...")
		état_courant = applique_coup(état_courant,humain,(lig,col))
		affiche_matrice(état_courant)

		(terminée,gagnant) = fin_partie(état_courant,joueuria,humain,True)
	else:
		humain_joue = True
		terminée	= False

	# au tour de MinMax
	if not terminée :

		(lig,col) = DecisionMinMax(état_courant,joueuria,humain,fin_partie,coups_possibles,applique_coup)
		état_courant = applique_coup(état_courant,joueuria,(lig,col))

		print("  Coup choisi par MinMax :",lig+1,"x",col+1)
		affiche_matrice(état_courant)
		print()

		(terminée,gagnant) = fin_partie(état_courant,joueuria,humain,False)

	if terminée:
		partie_en_cours = False
		if gagnant == "":
			print("Match nul.")
		else:
			print("Victoire pour les",gagnant)