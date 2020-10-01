import random
def ValeurFinPartie (id_minmax,id_adversaire,id_gagnant,couche):
	if id_gagnant==id_minmax:
		return 1
	elif id_gagnant==id_adversaire:
		return -1
	else:
		return 0



# Évalue une situation de jeu pour le joueur IA (niveau Max)

def ValeurMax (état,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup,couche) :
	couche+=1
	(terminée,gagnant) = fin_partie(état,id_minmax,id_adversaire,True)
	if terminée:
		return ValeurFinPartie(id_minmax,id_adversaire,gagnant,couche)
	else :
		coups	 = coups_possibles(état,id_minmax)
		bestScore = -1e99
		for coup in coups:
			nétat = applique_coup(état,id_minmax,coup)
			nscore = ValeurMin(nétat,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup,couche)
			if nscore > bestScore:
				bestScore = nscore
		return bestScore


# Évalue une situation de jeu pour le joueur humain (niveau Min)

def ValeurMin (état,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup,couche) :
	couche+=1

	if(couche>5):
		# bestScore=-1e99
		bestScore = -1*random.randint(0,100)-10
		return bestScore
	
	(terminée,gagnant) = fin_partie(état,id_minmax,id_adversaire,False)
	if terminée:
		# print(état)
		# print(couche)
		return ValeurFinPartie(id_minmax,id_adversaire,gagnant,couche)
	else:
		coups	 = coups_possibles(état,id_adversaire)
		bestScore = +1e99
		# print(bestScore)
		for coup in coups:
			nétat = applique_coup(état,id_adversaire,coup)
			nscore = ValeurMax(nétat,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup,couche)
			if nscore < bestScore:
				bestScore = nscore
		# print(bestScore)
		return bestScore


# Décider du coup à jouer (pour l'IA) en appliquant l'algorithme MinMax

def DecisionMinMax(état,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup) :
	coups	 = coups_possibles(état,id_minmax)
	bestScore = -1e99
	for coup in coups:
		nétat = applique_coup(état,id_minmax,coup)
		print('coup')
		print(coup)
		nscore = ValeurMin(nétat,id_minmax,id_adversaire,fin_partie,coups_possibles,applique_coup,0)
		print('nscore')
		print(nscore)
		if nscore > bestScore:
			bestScore = nscore
			bestCoup  = coup
	# bestCoup = (random.randint(0,10),random.randint(0,10))
	print(bestCoup)
	print(bestScore)
	if bestScore<-9:
		print('random play')
	return bestCoup
