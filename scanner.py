#encoding: utf-8

import socket

alvo = input("Digite o endereço ipv4:")
scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

lista_portas = list(range(0,65536))

for portas in lista_portas: 
  scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  scan.settimeout(1.0)
  conn = scan.connect_ex((alvo, portas))
  if conn == 0:
   print("A seguinte porta está aberta:",str(portas))
