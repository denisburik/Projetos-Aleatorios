version = "1.0.1"

introMsg = "Iniciando, Assistente LBtec - Versão {}".format(version)

def intro():
	msg = "Assistente BKtec - Versão {}, Criada por Leo Burik".format(version)
	print("-" * len(msg) + "\n{}\n".format(msg) + "-" * len(msg) )

lista_erro = [
	"Não Entendi nada",
	"Fale denovo",
	"Repita novamente"
]

conversa = {
	"Olá": "oi leo tudo bem?",
	"sim e você": "Estou bem obrigada por perguntar",
  	"sim": "Que bom, em que posso ajudar ?",
	"Bom dia": "Bom dia leo",
}
comandos = {
	"Desligar": "Desligando",
	"Reiniciar": "Reiniciando"
}

def verify_name(user_name):
	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é", "")

	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo", "")

	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o", "")

	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Meu nome é", "")
	
	return user_name

def verify_name_exist(name):
	dados = open("dados/nomes.txt", "r")
	name_list = dados.readlines()

	if not name_list:
		null_list = open("dados/nomes.txt", "r")
		content = null_list.readlines()
		content.append("{}".format(name))

		null_list = open("dados/nomes.txt", "w")
		null_list.writelines(content)

		null_list.close()

		return "Olá {}".format(name)

	if line == "leo":
		return "Olá criador"
	else:
		for line in name_list:
			return "Olá {}, acho que já nos conhecemos".format(name)

	null_list = open("dados/nomes.txt", "r")
	content = null_list.readlines()
	content.append("\n{}".format(name))

	null_list = open("dados/nomes.txt", "w")
	null_list.writelines(content)

	null_list.close()


def name_list_open():
	try:
		name =  open("dados/nomes.txt", "r")
		name.close()
	except FileNotFoundError:
		name =  open("dados/nomes.txt", "r")
		name.close()