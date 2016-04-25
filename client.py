import os
from socket import *

def clientUDP(ip, porta):
	HOST = ip
	PORT = int(porta)
	addr = (HOST, PORT)
	UDPSock = socket(AF_INET, SOCK_DGRAM)
	while True:
		data = input("Escolha uma opção:\n '+' para Soma\n '-' para Subtração\n '*' para Multiplicação\n '/' para Divisão\n 'pot' para Potenciação\n 'fat' para Fatorial\n 'raiz' para Raiz Quadrada\n '%' para Porcentagem\n\n 'exit' para sair\n ")
		UDPSock.sendto(data.encode('utf-8'), addr)
		if data == "+":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "-":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "*":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "/":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "pot":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "fat":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "raiz":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "%":
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			UDPSock.sendto(data.encode('utf-8'), addr)
		elif data == "exit":
			print('\n')
			break
	UDPSock.close()
	os._exit(0)

def clientTCP(ip, porta):
	HOST = ip
	PORT = int(porta)
	addr = (HOST, PORT)
	TCPSock = socket(AF_INET, SOCK_STREAM)
	TCPSock.connect(addr)
	while True:
		data = input("Escolha uma opção:\n '+' para Soma\n '-' para Subtração\n '*' para Multiplicação\n '/' para Divisão\n 'pot' para Potenciação\n 'fat' para Fatorial\n 'raiz' para Raiz Quadrada\n '%' para Porcentagem\n\n 'exit' para sair\n ")
		print('\n')
		if data == "+":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 1: ")
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 2: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "-":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 1: ")
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 2: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "*":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 1: ")
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 2: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "/":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 1: ")
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 2: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "pot":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 1: ")
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor 2: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "fat":
			TCPSock.send(data.encode('utf-8'))
			data = input("Digite o valor: ")
			TCPSock.send(data.encode('utf-8'))
		elif data == "raiz":
			TCPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor: ")
			TCPSock.sendto(data.encode('utf-8'), addr)
		elif data == "%":
			TCPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 1: ")
			TCPSock.sendto(data.encode('utf-8'), addr)
			data = input("Digite o valor 2: ")
			TCPSock.sendto(data.encode('utf-8'), addr)
		elif data == "exit":
			TCPSock.send(data.encode('utf-8'))
			break
		else:
			print("Entrada Inválida, tente novamente\n")
	TCPSock.close()
	os._exit(0)

# ipClient = "127.0.0.1"
# portaClient = 13000
ipClient = input("Entre com o endereço ip do cliente: ")
portaClient = input("Insira a porta que deverá ser utilizada: ")
print("Selecione a opção\n")
print("0 - Cliente UDP")
print("1 - Cliente TCP\n")
entrada = input("Opção: ")

while True:
	if (entrada == "0"):
		clientUDP(ipClient, portaClient)
	elif(entrada == "1"):
		clientTCP(ipClient, portaClient)
	else:
		entrada = input("Entrada Inválida, tente 0 para UDP ou 1 para TCP: ")