import random

class Character:
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack


    def attack_enemy(self, enemy):
        critical_chance = random.randint(1,10)
        damage = self.attack
    # Definindo o dano críticoa
        if self.name == player_name and critical_chance <= 2: # 20% de chance
            damage +=10
            print(f"{player_name} atingiu o monstro com dano crítico {self.name} causou + 10 de dano")
        enemy.health -= damage
        print(f" {self.name} atacou {enemy.name} causando {damage} de dano.")
    #definindo a esquiva
        miss_chance = random.randint(1, 10)
        if self.name == player_name and miss_chance <= 2: # 20% de chance
            damage += 0
            print(f"{player_name} esquivou do ataque {self.name} causou 0 de dano")
        self.health -= damage
        

    def is_alive(self):
        return self.health > 0

    def run_away(self):
        return random.random() < 0.5  # 50% de chance de fugir


cura = 20  # Valor de cura



# Usando set para habilidades únicas
skills = {"Golpe Rápido", "Defesa Rápida"}

# Usando bitwise para criar um sistema de pontos
level_points = 0b0011  # 3 pontos iniciais

# Nomes aleatórios para o monstro
monstern=['esqueleto','zumbi','demonio','lobo selvagem','slime','bicho papão']

# Dados do monstro
monstername=random.choice(monstern)
monsterpv=random.randint(80,150)
monsteratk=random.randint(10,20)

# Criando personagens
player_name = input("Digite o nome do seu personagem: ")
player = Character(player_name, 100, 15)
monster = Character(monstername, monsterpv, monsteratk)


print("Jogo Iniciado!")

# Jogo simples: jogador ataca o monstro até que um deles morra
# Definindo a função de fuga 
while player.is_alive() and monster.is_alive():
    print("\n--- Sua vez ---")
    action = input("Digite 'a' para atacar, 'i' para usar a cura ou 'r' para fugir: ").lower()

    if action == 'a':
        player.attack_enemy(monster)
# Cura
    elif action == 'i':
            player.health += cura
            print(str(player_name)+" usou a cura e recuperou 20 pontos de vida.")


    elif action == 'r':
        if player.run_away():
            print(str(player_name)+" fugiu da batalha!")
            break
        else:
            print(str(player_name)+" não conseguiu fugir.")

    # Removido bloco de inventário pois não está definido

    else:
        print("Ação inválida. Tente novamente.")

    if monster.is_alive():
        print("\n--- Turno do "+str(monstername)+" ---")
        monster.attack_enemy(player)

# Verifica o resultado
if monster.is_alive():
    print("O "+str(monstername)+" venceu!")
elif player.is_alive():
    print("você venceu!")
else:
    print("Você perdeu.")

# Mostrando uso de bitwise
print("\nPontos de nível inicial:", bin(level_points))
level_points = level_points << 1  # Ganha o dobro de pontos
print("Pontos de nível após bônus:", bin(level_points))
