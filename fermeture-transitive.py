# coding: utf8
class Liaison:

	def __init__(self,noeud,poids):
		self.noeud = noeud
		self.poids = poids

	@staticmethod
	def cp_liaison(liaison):
		return Liaison(liaison.noeud, liaison.poids)

class Noeud:

	def __init__(self, lst_noeud, number):
		#Alimentation des variables de l'instance
		self.name = number
		self.lst_noeud = lst_noeud

	def add_noeud_oriente(self,noeud,poids):
		already_there = False
		for noeud_2 in self.lst_noeud:
			if noeud_2.noeud == noeud:
				already_there = True
				if poids < noeud_2.poids:
					noeud_2.poids = poids

		if(already_there == False):		
			self.lst_noeud.append(Liaison(noeud,poids))

	def add_noeud_non_oriente(self,noeud,poids):
		already_there = False
		for noeud_2 in self.lst_noeud:
			if noeud_2.noeud == noeud:
				already_there = True
				if poids < noeud_2.poids:
					noeud_2.poids = poids

		if(already_there == False):		
			self.lst_noeud.append(Liaison(noeud,poids))
			noeud.lst_noeud.append(Liaison(self,poids))

	def add_noeuds_orientes(self, lst_noeuds):
		for x in lst_noeuds:
			self.add_noeud_oriente(x.noeud,x.poids)

	def add_noeuds_non_orientes(self, lst_noeuds):
		for x in lst_noeuds:
			self.add_noeud_non_oriente(x.noeud,x.poids)

	def has_noeud(self,noeud):
		for noeud_boucle in self.lst_noeud:
			#print noeud_boucle.__class__.__name__
			#print noeud.__class__.__name__
			if noeud_boucle.noeud == noeud:
				return True
		return False

	def get_noeud(self,index):
		return self.lst_noeud[index]

	#La méthode get_liaison retourne false si il n'y a pas de liaison sinon elle retourne la liaison
	def get_liaison(self, noeud):
		for noeud_boucle in self.lst_noeud:
			if noeud_boucle.noeud == noeud:
				return noeud_boucle
		return False

	def print_noeud(self):
		self.sort()
		s = str(self.name) + " => { "
		for _noeud in self.lst_noeud:
			s = s + str(_noeud.noeud.name) + " (" + str(_noeud.poids) + ") ,"
		s = s[:-1] + "}"
		print s

	def sort(self):
		self.lst_noeud.sort(key=lambda noeud: noeud.noeud.name)

class Graphe:

	def __init__(self,name, lst_noeud):
		self.name = name
		self.lst_noeud = lst_noeud

	def get_noeuds_precedent(self,noeud):
		lst_noeud_precedent = []
		for noeud_precedent_potentiel in self.lst_noeud:
			if arc(noeud_precedent_potentiel,noeud):
				lst_noeud_precedent.append(noeud_precedent_potentiel)
		return lst_noeud_precedent

	def arc(self,i,j):
		return i.has_noeud(j)

	def get_noeud(self,i):
		return self.lst_noeud[i]

	def print_graphe(self):
		for noeud in self.lst_noeud:
			noeud.print_noeud()

	def print_matrice_liaison_poids(self):
		print "\nReprésentation sous forme matricielle du graphe " + str(self.name) + "\n"
		x = "  "
		for noeud in self.lst_noeud:
			x = x + "   " + str(noeud.name)
		print x
		print "  " + "-" * (len(self.lst_noeud) * 4 + 4)
		for noeud in self.lst_noeud:
			s =  str(noeud.name) + " | "
			for noeud_fils_possible in self.lst_noeud:
				#On récupère faux si pas de liaison sinon la liaison
				liaison_possible = noeud.get_liaison(noeud_fils_possible)
				if(liaison_possible != False) :
					s = s + " " + str(liaison_possible.poids)
					if(len(str(liaison_possible.poids)) > 1):
						s = s + " "
					else:
						s = s + "  "
				else:
					s = s + " 0  "
			print s + " |"
		print "  " + "-" * (len(self.lst_noeud) * 4 + 4)

	def nb_noeud(self):
		return len(self.lst_noeud)

	def nb_lien(self):
		nb_liaison = 0
		for i in xrange(0,len(self.lst_noeud)):
			nb_liaison = nb_liaison + len(self.get_noeud(i).lst_noeud)
		return nb_liaison

	def print_lst_noeud(self):
		print self.lst_noeud

	def get_lst_noeud(self):
		return self.lst_noeud

	def min_chemin(i):
		noeud_plus_pres = None
		poids_min = float('inf')
		for noeud in i.lst_noeud:
			if noeud.poids < poids_min:
				noeud_plus_pres = noeud.noeud
				poids_min = noeud.poids
		return [noeud_plus_pres,poids_min]
			
#WARSHALL
#G+← G
#pour i de 1 à n faire
#	pour x de 1 à n faire
#		si arc(G+, x, i) alors
#			pour y de 1 à n faire
#				si arc(G+, i, y) alors
#					ajouterArc(G+, x, y)
#				fsi
#			fait
#		fsi
#	fait
#fait

def WARSHALL(graphe):
	graphe_ = graphe
	nb_noeud_add = 0
	for i in graphe_.lst_noeud:
		lst_noeuds = []
		for j in graphe_.lst_noeud:
			for k in graphe_.lst_noeud:
				if(graphe_.arc(j,i) and graphe_.arc(i,k)):	
					j.add_noeud_oriente(k,1)
	return graphe_

#DIJKSTRA
#X={1,…,n}
#s=1
#P[i,j]=poids de l'arc (i,j)
#D[1]=+ courte distance courante de s(1) à i
#début
#	E={1}
#	pour i de 2 à n faire
#		D[i]←p[1,i]
#	fait
#	pour i de 2 à n faire
#		choisir t appartient à X-E tel que D[t] soit min
#		ajouter t à E
#		pour chaque x successeur de t faire
#			D[x]=min(D[x], D[t]+p[x,t])
#		faire
#	faire
#fin


#paramètre de type { "noeud" : noeud, "poids" : poids, "chemin" : [A,B,C] }
def printCheminLePlusCourt(chemin_le_plus_cours):
	print "Noeud : " + chemin_le_plus_cours["noeud"].name
	print "Poids du chemin : " + str(chemin_le_plus_cours["poids"])
	string_chemin = ""
	for noeud in chemin_le_plus_cours["chemin"]:
		string_chemin += " " + noeud.name
	print "Chemin : " + string_chemin

def Dijkstra(graphe, noeud_start, noeud_end):
	#Nous allons représenter les noeuds sous forme d'un tableau à 3 dimensions
	# 1 : Le noeud
	# 2 : Le poids du chemin le plus court pour arriver jusque là
	# 3 : Le chemin le plus court pour arriver jusque là

	#Initialisation de l'algorithme
	lst_noeuds_utilises = []
	lst_noeuds_restants = []
	for noeud in graphe.lst_noeud:
		if noeud != noeud_start:
			lst_noeuds_restants.append({"noeud" : noeud , "poids" : float('inf') , "chemin" : [] })
	lst_noeuds_utilises.append({ "noeud" : noeud_start, "poids" : 0 , "chemin" : [noeud_start]})

	#Début algorithme

	#tant qu'il y a reste des chemins à calculer
	while len(lst_noeuds_restants):
		#On calcule le point le plus près
		chemin_min = float('inf')
		noeud_min = None
		noeud_min_pere = None
		chemin = []
		for noeud_utilise in lst_noeuds_utilises:
			for noeud_restant in lst_noeuds_restants:
				#Si un arc existe et que (son poids + celui du chemin pour aller jusqu'au noeud_utilise)
				#est inférieur au poid minimum trouvé pour l'instant
				result1 = graphe.arc(noeud_utilise["noeud"] , noeud_restant["noeud"])
				if graphe.arc(noeud_utilise["noeud"] , noeud_restant["noeud"]) and noeud_utilise["noeud"].get_liaison(noeud_restant["noeud"]).poids + noeud_utilise["poids"] < chemin_min:
					#print noeud_restant["noeud"].name
					chemin_min = noeud_utilise["noeud"].get_liaison(noeud_restant["noeud"]).poids
					noeud_min = noeud_restant
					noeud_min_pere = noeud_utilise

		#On enlève le noeud des noeuds restants à explorer
		lst_noeuds_restants.remove(noeud_min)
		#On met le bon poids ainsi que le bon chemin
		noeud_min["poids"] = noeud_min_pere["poids"] + noeud_min_pere["noeud"].get_liaison(noeud_min["noeud"]).poids
		chemin = noeud_min_pere["chemin"]
		for noeud in noeud_min["chemin"]:
			print noeud.name
		chemin.append(noeud_min["noeud"])
		for noeud in chemin:
			print noeud.name
		print "---"
		noeud_min["chemin"] = chemin
		#On ajoute le chemin aux chemins traités
		lst_noeuds_utilises.append(noeud_min)

	#On a traité tous les chemins
	for noeud in lst_noeuds_utilises:
		if noeud["noeud"] == noeud_end:
			return noeud

'''
	lst_noeuds_restants = graphe_.lst_noeud
	lst_noeud_utilises = []
	if(len(lst_noeuds_restants) > 0):
		#On ajoute le premier noeud
		lst_noeud_utilises.append([lst_noeuds_restants[0],0])
		noeud_selectionne = [lst_noeuds_restants[0],0]
		while len(lst_noeuds_restants):
			poids_min = float('inf')
			for noeud in lst_noeud_utilises:
				for noeud_fils in noeud.lst_noeud:
					if noeud_fils 
			#Tableau qui contient le noeud + le poids [noeud,poids]
			noeud_min = graphe_.min_chemin(noeud_selectionne)
			noeud_min[1] = noeud_selectionne[1] + noeud_min[1]
			lst_noeud_utilises.append(noeud_min)
			lst_noeuds_restants.remove(noeud_selectionne[0])
	print s
'''

def init_1():
	lst_noeud = []
	noeud_0 = Noeud([],0)
	noeud_1 = Noeud([],1)
	noeud_2 = Noeud([],2)
	noeud_3 = Noeud([],3)
	noeud_4 = Noeud([],4)
	noeud_5 = Noeud([],5)
	noeud_6 = Noeud([],6)
	noeud_7 = Noeud([],7)
	noeud_8 = Noeud([],8)
	noeud_9 = Noeud([],9)
	noeud_0.add_noeud_oriente(noeud_1, 1)
	noeud_0.add_noeud_oriente(noeud_2, 1)
	noeud_1.add_noeud_oriente(noeud_2, 1)
	noeud_1.add_noeud_oriente(noeud_4, 1)
	noeud_2.add_noeud_oriente(noeud_3, 1)
	noeud_3.add_noeud_oriente(noeud_4, 1)
	noeud_4.add_noeud_oriente(noeud_5, 1)
	noeud_4.add_noeud_oriente(noeud_6, 1)
	noeud_4.add_noeud_oriente(noeud_9, 1)
	noeud_5.add_noeud_oriente(noeud_7, 1)
	noeud_6.add_noeud_oriente(noeud_8, 1)
	noeud_7.add_noeud_oriente(noeud_8, 1)
	noeud_7.add_noeud_oriente(noeud_9, 1)
	noeud_8.add_noeud_oriente(noeud_9, 1)
	lst_noeud.append(noeud_0)
	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)
	lst_noeud.append(noeud_6)
	lst_noeud.append(noeud_7)
	lst_noeud.append(noeud_8)
	lst_noeud.append(noeud_9)
	return Graphe("Graphe 1", lst_noeud)

def init_2():
	lst_noeud = []
	noeud_6 = Noeud([],6)
	noeud_1 = Noeud([],1)
	noeud_2 = Noeud([],2)
	noeud_3 = Noeud([],3)
	noeud_4 = Noeud([],4)
	noeud_5 = Noeud([],5)

	noeud_1.add_noeud_oriente(noeud_2,1)
	noeud_1.add_noeud_oriente(noeud_4,1)
	noeud_2.add_noeud_oriente(noeud_3,1)
	noeud_2.add_noeud_oriente(noeud_5,1)
	noeud_3.add_noeud_oriente(noeud_5,1)
	noeud_4.add_noeud_oriente(noeud_3,1)
	noeud_5.add_noeud_oriente(noeud_4,1)
	noeud_6.add_noeud_oriente(noeud_3,1)
	noeud_6.add_noeud_oriente(noeud_5,1)

	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)
	lst_noeud.append(noeud_6)

	return Graphe("Graphe 2", lst_noeud)

def init_3():
	lst_noeud = []

	noeud_1 = Noeud([],"A")
	noeud_2 = Noeud([],"B")
	noeud_3 = Noeud([],"C")
	noeud_4 = Noeud([],"D")
	noeud_5 = Noeud([],"E")

	noeud_1.add_noeud_oriente(noeud_2,1)
	noeud_2.add_noeud_oriente(noeud_3,1)
	noeud_2.add_noeud_oriente(noeud_5,1)
	noeud_3.add_noeud_oriente(noeud_4,1)
	noeud_4.add_noeud_oriente(noeud_2,1)

	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)

	return Graphe("Graphe 3", lst_noeud)

def init_4():
	lst_noeud = []

	noeud_1 = Noeud([],"A")
	noeud_2 = Noeud([],"B")
	noeud_3 = Noeud([],"C")
	noeud_4 = Noeud([],"D")
	noeud_5 = Noeud([],"E")

	noeud_1.add_noeud_oriente(noeud_2,3)
	noeud_2.add_noeud_oriente(noeud_3,5)
	noeud_3.add_noeud_oriente(noeud_2,4)
	noeud_4.add_noeud_oriente(noeud_5,1)
	noeud_2.add_noeud_oriente(noeud_5,6)
	noeud_3.add_noeud_oriente(noeud_4,7)
	noeud_4.add_noeud_oriente(noeud_2,4)

	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)

	return Graphe("Graphe 3", lst_noeud)



graphe = init_1()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
print "------- WARSHALL EN COURS -------"
graphe_ = WARSHALL(graphe)
print "-------   WARSHALL FINI   -------"
graphe_.print_graphe()
graphe_.print_matrice_liaison_poids()


graphe = init_2()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
print "------- WARSHALL EN COURS -------"
graphe_ = WARSHALL(graphe)
print "-------   WARSHALL FINI   -------"
graphe_.print_graphe()
graphe_.print_matrice_liaison_poids()


graphe = init_3()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
print "------- WARSHALL EN COURS -------"
graphe_ = WARSHALL(graphe)
print "-------   WARSHALL FINI   -------"
graphe_.print_graphe()
graphe_.print_matrice_liaison_poids()


graphe = init_4()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
print "------- DIJKSTRA EN COURS -------"
chemin_le_plus_cours = Dijkstra(graphe, graphe.lst_noeud[0], graphe.lst_noeud[4])
print "-------   DIJKSTRA FINI   -------"
printCheminLePlusCourt(chemin_le_plus_cours)
