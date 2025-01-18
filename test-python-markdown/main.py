# Print inicial
print("Data is a New Oil")

# Variáveis
idade = 34
nome = "Marco"
altura = 1.75  # Nova variável para demonstrar números decimais
ativo = True  # Variável booleana

# Print de variáveis
print(f"Idade: {idade}")
print(f"Nome: {nome}")
print(f"Altura: {altura} m")
print(f"Ativo: {ativo}")

# Soma e manipulação de variáveis
nova_idade = idade + 1
print(f"Sua nova idade será: {nova_idade}")

# Lista
lista = [1, 2, 3, 4, 5]

# Métodos de lista
lista_invertida = lista[::-1]  # Alternativa ao reverse(), para não modificar a lista original
print("Lista invertida:", lista_invertida)

# Adicionando e removendo itens da lista
lista.append(6)  # Adiciona um item no final da lista
lista.remove(3)  # Remove o item 3 da lista
print("Lista modificada:", lista)

# Verificar se um item existe na lista
if 4 in lista:
    print("O número 4 está na lista.")
else:
    print("O número 4 não está na lista.")

# Dicionário
pessoa = {
    "nome": "Marco",
    "idade": 34,
    "altura": 1.75
}

# Acessando dicionário
print(f"Nome do dicionário: {pessoa['nome']}")
print(f"Idade do dicionário: {pessoa['idade']}")
print(f"Altura do dicionário: {pessoa['altura']}")

# Laços de repetição (for)
for i in range(1, 6):
    print(f"Contagem: {i}")

# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando a função
print(saudacao(nome))

# Exceções (try/except)
try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Por favor, digite um número válido.")

# Condicional (if/else)
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
