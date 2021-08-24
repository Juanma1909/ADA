"""
entrada del algoritmo: 4 puntos que entran como tuplas(x,y), donde los primeros 2 puntos conforman el primer segmento y
los siguientes 2 conforman el segundo segmento
Salida: retorna True si los segmentos se intersectan o false en el caso contrario
Funcionamiento: se parte de que 2 segementos a y b se intersectan sii (a straddles b y b straddles a) o si un punto de borde reside
en el otro segmento.
para saber si straddles se calculan las orientaciones relativas mediante producto cruz y se comparan, si son opuestas se intersectan
si el producto cruz es 0, siginifica que son colineales por lo que solo se tendría que verificar que el punto en cuestion se encuentre
dentro del segmento.
"""
def crossp(p1,p2):
	return (p1[0]*p2[1])-(p2[0]*p1[1])

def direct(pi,pj,pk):
	pa = (pk[0]-pi[0],pk[1]-pi[1])
	pb = (pj[0]-pi[0],pj[1]-pi[1])
	return crossp(pa,pb)

def on_seg(pi,pj,pk):
	if  (min(pi[0],pj[0]) <= pk[0]<= max(pi[0],pj[0])) and (min(pi[1],pj[1]) <= pk[1]<= max(pi[1],pj[1])):ans = True
	else: ans = False
	return ans

def interseg(p1,p2,p3,p4):
	ans = None
	d1=direct(p3,p4,p1)
	d2=direct(p3,p4,p2)
	d3=direct(p1,p2,p3)
	d4=direct(p1,p2,p4)
	if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)): ans = True
	elif d1 == 0 and on_seg(p3,p4,p1):ans = True
	elif d2 == 0 and on_seg(p3,p4,p2):ans = True
	elif d3 == 0 and on_seg(p1,p2,p3):ans = True
	elif d4 == 0 and on_seg(p1,p2,p4):ans = True
	else: ans = False
	return ans

