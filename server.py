import os
from socket import *
from Funcoes import *

def serverUDP(porta):
	HOST = ""
	PORT = int(porta)
	buf = 1024
	addr = (HOST, PORT)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	UDPSock.bind(addr)
	print ("Aguardando para receber mensagens...")
	while True:
		(data, addr) = UDPSock.recvfrom(buf)
		print ("Mensagem recebida: " + data.decode('utf-8'))
		if data.decode('utf-8') == "+":
			a, b = leVetorUDP(UDPSock, buf)
			soma(a, b)
		elif data.decode('utf-8') == "-":
			a, b = leVetorUDP(UDPSock, buf)
			subtracao(a, b)
		elif data.decode('utf-8') == "*":
			a, b = leVetorUDP(UDPSock, buf)
			multiplicacao(a, b)
		elif data.decode('utf-8') == "/":
			a, b = leVetorUDP(UDPSock, buf)
			divisao(a, b)
		elif data.decode('utf-8') == "pot":
			a, b = leVetorUDP(UDPSock, buf)
			potenciacao(a, b)
		elif data.decode('utf-8') == "fat":
			a = leUnicoUDP(UDPSock, buf)
			fatorial(a)
		elif data.decode('utf-8') == "raiz":
			a = leUnicoUDP(UDPSock, buf)
			raizquadrada(a)
		elif data.decode('utf-8') == "%":
			a, b = leVetorUDP(UDPSock, buf)
			porcentagem(a, b)
		elif data.decode('utf-8') == "exit":
			print ("Client Disconnected")
			break
		else:
			input("Entrada Inválida, tente novamente")
	UDPSock.close()
	os._exit(0)

def serverTCP(porta):
	HOST = ""
	PORT = int(porta)
	buf = 1024
	addr = (HOST, PORT)
	TCPSock = socket(AF_INET, SOCK_STREAM)
	TCPSock.bind(addr)
	TCPSock.listen(1)
	print ("Aguardando para receber mensagens...")
	while True:
		connection, client = TCPSock.accept()
		print ("Cliente conectado"), client
		while True:
			data = connection.recv(buf)
			print ("Mensagem recebida: " + data.decode('utf-8'))
			if data.decode('utf-8') == "+":
				a, b = leVetorTCP(data, connection, buf)
				soma(a, b)
			elif data.decode('utf-8') == "-":
				a, b = leVetorTCP(data, connection, buf)
				subtracao(a, b)
			elif data.decode('utf-8') == "*":
				a, b = leVetorTCP(data, connection, buf)
				multiplicacao(a, b)
			elif data.decode('utf-8') == "/":
				a, b = leVetorTCP(data, connection, buf)
				divisao(a, b)
			elif data.decode('utf-8') == "pot":
				a, b = leVetorTCP(data, connection, buf)
				potenciacao(a, b)
			elif data.decode('utf-8') == "fat":
				a = leUnicoTCP(data, connection, buf)
				fatorial(a)
			elif data.decode('utf-8') == "raiz":
				a = leUnicoTCP(data, connection, buf)
				raizquadrada(a)
			elif data.decode('utf-8') == "%":
				a, b = leVetorTCP(data, connection, buf)
				porcentagem(a, b)
			elif data.decode('utf-8') == "exit":
				print ("Client Disconnected")
				break
	TCPSock.close()
	os._exit(0)

# portaClient = 13000
portaClient = input("Insira a porta que deverá ser utilizada: ")
print("Selecione a opção\n")
print("0 - Servidor UDP")
print("1 - Servidor TCP\n")
entrada = input()

while True:
	if (entrada == "0"):
		serverUDP(portaClient)
	elif(entrada == "1"):
		serverTCP(portaClient)
	else:
		entrada = input("Entrada Inválida, tente 0 para UDP ou 1 para TCP: ")