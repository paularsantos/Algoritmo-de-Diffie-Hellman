# ALGORITMO DE DIFFIE-HELLMAN
# Discente - Paula Santos 

NumPrimo = 11
NumBase = 4

NumSecrAlice = 8
NumSecrBob = 23

print("VARIÁVEIS COMPARTILHADA PUBLICAMENTE")
print ("Numero primo: ",NumPrimo)
print ("Base: ",NumBase)

print (" ----------------------------------------------- \n ")
print ("TROCA DE CHAVES ENTRE ALICE E BOB")
A = (NumBase**NumSecrAlice) % NumPrimo
print ('Alice envia para Bob: ', A)

B = (NumBase ** NumSecrBob) % NumPrimo
print ("Bob envia para Alice: ", B)

print ("---------------------------------------------------\n")
print (" CHAVE CALCULADA PRIVADAMENTE")
ChaveSecrAlice = (B ** NumSecrAlice) % NumPrimo
print ('Resposta do calculo de Alice: ', ChaveSecrAlice)
ChaveSecrBob = (A ** NumSecrBob) % NumPrimo
print ('Resposta do calculo de Bob: ', ChaveSecrBob)
print ("----------------------------------------------------")
