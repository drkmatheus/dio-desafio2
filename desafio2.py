while True:
    try:
        numVit = int(input("Insira o seu número de vitórias: "))
        if numVit < 0:
            print("Parâmetros digitados inválidos. O número de vitórias não pode ser negativo. Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

while True:
    try:
        numDer = int(input("Insira o seu número de derrotas: "))
        if numDer < 0:
            print("Parâmetros digitados inválidos. O número de derrotas não pode ser negativo. Tente novamente.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")    
		        
def calcVitorias(v, d):
	saldoVitorias = v - d
	return saldoVitorias

def verificaRanking(saldoVitorias):
	if (saldoVitorias < 10):
		ranking = "Ferro"
	elif (saldoVitorias <= 20):
		ranking = "Bronze"
	elif (saldoVitorias <= 50):
		ranking = "Prata"
	elif (saldoVitorias <= 80):
		ranking = "Ouro"
	elif (saldoVitorias <= 90):
		ranking = "Diamante"
	elif (saldoVitorias <= 100):
		ranking = "Lendário"
	else:
		ranking = "Imortal"
	return ranking
	
saldoVitorias = calcVitorias(numVit, numDer)
ranking = verificaRanking(saldoVitorias)

print(f"O Heroi tem **{saldoVitorias}** de saldo de vitórias e está no ranking de **{ranking}**")