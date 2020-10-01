
# un opérateur = un triplet (nom,précondition,action)

# constructeur
def nouvel_operateur (n,p,a):
	return (n,p,a)

# accesseurs
def nom_operateur(o) :
	return o[0]

def precondition_operateur(o) :
	return o[1]
	
def action_operateur(o) :
	return o[2]


# test opérateur applicable à un état
def est_applicable(o,e) :
	precond = precondition_operateur(o)
	return precond(e)


# liste des opérateurs applicables à un état
def operateurs_applicables(os,e):
	res = []
	for o in os:
		if est_applicable(o,e):
			res.append(o)
	return res


# applique un opérateur à un état
def applique_operateur(o,e) :
	action = action_operateur(o)
	return action(e)


def affiche_solution (e,ops,etat_en_texte):
        print(etat_en_texte(e))
        for o in ops:
                e = applique_operateur(o,e)
                print(nom_operateur(o))
                print(etat_en_texte(e))

                
def recherche_en_profondeur_rec (e,est_final,os,etat_en_texte,deja):
        print(deja)
        if (est_final(e)) :
                return []
        else:
                applicables = operateurs_applicables(os,e)
                print(applicables)
                for o in applicables:
                        succ = applique_operateur(o,e)
                        stxt = etat_en_texte(succ)
                        if not(stxt in deja):
                                deja[stxt] = 1
                                chemin = recherche_en_profondeur_rec(succ,est_final,os,etat_en_texte,deja)
                                if chemin!=None:
                                        return [ o ] + chemin
                return None


        
def recherche_en_profondeur(etat_initial,est_final,operateurs_disponibles,etat_en_texte) :
        print( recherche_en_profondeur_rec(etat_initial,est_final,operateurs_disponibles,etat_en_texte,{}))
        #affiche_solution(etat_initial,ch,etat_en_texte)

        
