# Listas:
nomes = ["lira", "Gui", "Mi"]

# pegar  uma infomação de uma lista
fulano = nomes[2]
print(fulano)

# Adicionar infos na lista:
nomes.append("Miguel") # .append -> serve para adicionar alguma coisa no final de uma lista
print(nomes)

# Dicionarios:

pessoa = {"nome": "Miguel", "Idade": 19, "peso": 55, "cidade":  "Sorocaba-SP" }

peso = pessoa["peso"]
print(peso)

# COMO VAMOS USAR ESSA ESTRUTURA?

lista_mensagens = []

mensagem1 = {"role": "user", "content": "python"} # role -> quem  enviou | content -> conteudo
mensagem2 = {"role": "assistant", "content": "resposta da IA"} # role -> quem  enviou | content -> conteudo

lista_mensagens.append(mensagem1)
lista_mensagens.append(mensagem2)

print(lista_mensagens)