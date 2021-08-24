"""
Entrada: una matriz [v][v] y el numero de colores
Salida un arreglo de V posciones donde cada posicion tiene asignado un color
"""
def safe(A,v,color,c):
	ans = True
	for i in range( len(A)):
		if A[v][i] == 1 and color[i] == c: ans = False
	return ans
def solve(A,m,color,v,alll):
	if v == len(A[0]):
		alll.append(list(color))
	else:
		for c in range(1,m+1):
			if safe(A,v,color,c):
				color[v] = c
				solve(A,m,color,v+1,alll)
	return alll
def main():
	alll =[]
	A=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
	V = len(A[0])
	m = 4
	color = [None for _ in range(V)]
	ans = solve(A,m,color,0,alll)
	print(ans)
	print(len(ans))
	return
main()
