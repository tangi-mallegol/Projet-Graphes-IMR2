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

	def add_noeud(self,noeud,poids):
		already_there = False
		for noeud_2 in self.lst_noeud:
			if noeud_2.noeud == noeud:
				already_there = True
				if poids < noeud_2.poids:
					noeud_2.poids = poids

		if(already_there == False):		
			self.lst_noeud.append(Liaison(noeud,poids))

	def has_noeud(self,noeud):
		for noeud_boucle in self.lst_noeud:
			print noeud_boucle.__class__.__name__
			print noeud.__class__.__name__
			if noeud_boucle.noeud == noeud:
				return True
		return False

	def get_noeud(self,index):
		return self.lst_noeud[index]

	#La méthode get_liaison retourne false si il n'y a pas de laison sinon elle retourne la liaison
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

	def add_noeuds(self, lst_noeuds):
		for x in lst_noeuds:
			self.add_noeud(x.noeud,x.poids)

	def sort(self):
		self.lst_noeud.sort(key=lambda noeud: noeud.noeud.name)

class Graphe:

	def __init__(self,name, lst_noeud):
		self.name = name
		self.lst_noeud = lst_noeud

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
		for j in i.lst_noeud:
			for k in j.noeud.lst_noeud:
				new_liaison = Liaison.cp_liaison(k)
				new_liaison.poids = j.poids + k.poids
				lst_noeuds.append(new_liaison)
		i.add_noeuds(lst_noeuds)
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

def Dijkstra(graphe):
	s = ""

	print s


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
	noeud_0.add_noeud(noeud_1, 3)
	noeud_0.add_noeud(noeud_2, 6)
	noeud_1.add_noeud(noeud_2,4)
	noeud_1.add_noeud(noeud_4, -1)
	noeud_2.add_noeud(noeud_3,4)
	noeud_3.add_noeud(noeud_4,7)
	noeud_4.add_noeud(noeud_5,9)
	noeud_4.add_noeud(noeud_6,10)
	noeud_4.add_noeud(noeud_9,2)
	noeud_5.add_noeud(noeud_7,6)
	noeud_6.add_noeud(noeud_8,1)
	noeud_7.add_noeud(noeud_8,5)
	noeud_7.add_noeud(noeud_9,-3)
	noeud_8.add_noeud(noeud_9,4)
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

	noeud_1.add_noeud(noeud_2,1)
	noeud_1.add_noeud(noeud_4,4)
	noeud_2.add_noeud(noeud_3,3)
	noeud_2.add_noeud(noeud_5,1)
	noeud_3.add_noeud(noeud_5,4)
	noeud_4.add_noeud(noeud_3,2)
	noeud_5.add_noeud(noeud_4,6)
	noeud_6.add_noeud(noeud_3,3)
	noeud_6.add_noeud(noeud_5,5)

	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)
	lst_noeud.append(noeud_6)

	return Graphe("Graphe 2", lst_noeud)

def init_3():
	lst_noeud = []

	noeud_1 = Noeud([],1)
	noeud_2 = Noeud([],2)
	noeud_3 = Noeud([],3)
	noeud_4 = Noeud([],4)
	noeud_5 = Noeud([],5)

	noeud_1.add_noeud(noeud_2,1)
	noeud_2.add_noeud(noeud_3,1)
	noeud_2.add_noeud(noeud_5,1)
	noeud_3.add_noeud(noeud_4,1)
	noeud_4.add_noeud(noeud_2,1)

	lst_noeud.append(noeud_1)
	lst_noeud.append(noeud_2)
	lst_noeud.append(noeud_3)
	lst_noeud.append(noeud_4)
	lst_noeud.append(noeud_5)

	return Graphe("Graphe 2", lst_noeud)

graphe = init_1()
#graphe.print_lst_noeud()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
#print "nb_noeud = " + str(graphe.nb_noeud())
#print "nb_lien = " + str(graphe.nb_lien())
print "------- WARSHALL EN COURS -------"
graphe_ = WARSHALL(graphe)
print "-------   WARSHALL FINI   -------"
graphe_.print_graphe()
graphe_.print_matrice_liaison_poids()
#print "nb_noeud = " + str(graphe_.nb_noeud())
#print "nb_lien = " + str(graphe_.nb_lien())
#print Noeud.nb_noeud
graphe = init_3()
#graphe.print_lst_noeud()
graphe.print_graphe()
graphe.print_matrice_liaison_poids()
#print "nb_noeud = " + str(graphe.nb_noeud())
#print "nb_lien = " + str(graphe.nb_lien())
print "------- WARSHALL EN COURS -------"
graphe_ = WARSHALL(graphe)
print "-------   WARSHALL FINI   -------"
graphe_.print_graphe()
graphe_.print_matrice_liaison_poids()
