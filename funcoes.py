from math import sqrt

def leVetorUDP(socket, buff):
	vetor = []
	i = 0
	while i < 3:
		(data, addr) = socket.recvfrom(buff)
		vetor.append(data.decode('utf-8'))
		i += 1
	val1 = int(vetor[1])
	val2 = int(vetor[2])
	return val1, val2

def leVetorTCP(dt, conn, buff):
	vetor = []
	i = 1
	vetor.append(dt.decode('utf-8'))
	while i < 3:
		dt = conn.recv(buff)
		vetor.append(dt.decode('utf-8'))
		i += 1
	val1 = int(vetor[1])
	val2 = int(vetor[2])
	return val1, val2

def leUnicoUDP(socket, buff):
	vetor = []
	i = 0
	while i < 2:
		(data, addr) = socket.recvfrom(buff)
		vetor.append(data.decode('utf-8'))
		i += 1
	val1 = int(vetor[1])
	return val1

def leUnicoTCP(dt, conn, buff):
	vetor = []
	i = 1
	vetor.append(dt.decode('utf-8'))
	while i < 2:
		dt = conn.recv(buff)
		vetor.append(dt.decode('utf-8'))
		i += 1
	val1 = int(vetor[1])
	return val1

def soma(a, b):
	print (a + b)

def subtracao(a, b):
	print (a - b)

def multiplicacao(a, b):
	print (a * b)

def divisao(a, b):
	if b != 0: 
		print (a / b);
	else:
		print('Não é possível efetuar divisão por 0') 
		return
		
def potenciacao(a, b):
	print (a ** b)

def fatorial(a):
	resultado = 1;
	for a in range(1, a + 1):
		resultado = a * resultado
	print (resultado);

def raizquadrada(a):
	raiz = sqrt(a)
	print(raiz)

def porcentagem(a, b):
	porcento = a * (b / 100)
	print (porcento)