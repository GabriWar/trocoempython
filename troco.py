valor = float(input("insira o valor da compra: R$"))
pagamento = float(input("insira o valor do pagamento: R$"))
troco = round((pagamento)-(valor),2)
print("o troco sera de", troco, "R$") 
#
notas100 = int(troco/100)
print ("notas de 100: ", notas100)
troco -= notas100*100
#
notas50 = int(troco/50)
print("notas de 50: ", notas50)
troco -=notas50*50
#
notas20 = int(troco/20)
print ("notas de 20: ", notas20)
troco -= notas20*20
#
notas10 = int(troco/10)
print("notas de 10: ", notas10)
troco -=notas10*10
#
notas5 = int(troco/5)
print("notas de 5: ", notas5)
troco -=notas5*5
#
notas2 = int(troco/2)
print("notas de 2: ", notas2)
troco -=notas2*2
#
moedas1real = int(troco/1)
print("moedas de 1 real: ", moedas1real)
troco -=moedas1real*1

##################
troco = troco*100
#troco = round(troco)
##################


moedas50centavos = int(troco/50)
print("moedas de 50 centavos: ", moedas50centavos)
troco -=moedas50centavos*50

moedas25centavos = int(troco/25)
print("moedas de 25 centavos: ", moedas25centavos)
troco -=moedas25centavos*25

moedas10centavos = int(troco/10)
print("moedas de 10 centavos: ", moedas10centavos)
troco -=moedas10centavos*10

moedas5centavos = int(troco/5)
print("moedas de 5 centavos: ", moedas5centavos)
troco -=moedas5centavos*5
#
troco = troco/100
print("restante",(troco))
#