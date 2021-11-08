################################################
def barra():
    print("------------------------------------------------")
################################################
barra()
valor = float(input("insira o valor da compra: R$"))
barra()
pagamento = float(input("insira o valor do pagamento: R$"))
barra()
troco = round((pagamento)-(valor),2)
print("o troco sera de", troco, "R$") 
barra()
###############################################
trocog = troco
def globaltrocog():
    global trocog
################################################
def calctroco(x,t):
    global trocog
    if t >= (x):
        tx =(t / (x))
        if tx !=1.0:
            tx = round(tx - 0.5)
        print(int(tx),"notas de", x, "R$")
        t -= (tx*(x))
        trocog = t
################################################
def calctroco1real(x,t):
    global trocog
    if t >= (x):
        tx =(t / (x))
        if tx !=1.0:
            tx = round(tx - 0.5)
        print(int(tx),"moedas de", x, "real")
        t -= (tx*(x))
        trocog = t
################################################
def calctrococents(x,t):
    global trocog
    if t >= (x):
        tx =(t / (x))
        if tx !=1:
            tx = round(tx - 0.5)
        print(int(tx),"moedas de", x, "centavos")
        t -= (tx*(x))
        trocog = t
################################################
print("e pode ser dado em: ")
barra()
################################################
calctroco(x=100, t=trocog)
calctroco(x=50, t=trocog)
calctroco(x=20, t=trocog)
calctroco(x=10, t=trocog)
calctroco(x=5, t=trocog)
calctroco(x=2, t=trocog)
calctroco1real(x=1, t=trocog)
################################################
trocog = trocog*100
################################################
calctrococents(x=50, t=trocog)
calctrococents(x=25, t=trocog)
calctrococents(x=10, t=trocog)
if trocog > 4.9:
    trocog += 0.1
calctrococents(x=5, t=trocog)
print(trocog)
################################################
barra()