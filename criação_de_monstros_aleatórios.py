import random

class Character:
    def __init__(self, name: str, health: int, attack: int):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = self.attack
        enemy.health -= damage
        print(f"{self.name} atacou {enemy.name} causando {damage} de dano.")

    def is_alive(self):
        return self.health > 0

# Função para criar monstros aleatórios
def create_monster():
    nomes = ["Goblin", "Orc", "Esqueleto", "Slime", "Lobo Selvagem", "zumbi", "urso"]
    nome = random.choice(nomes)
    health = random.randint(50, 120)
    attack = random.randint(5, 20)
    return Character(nome, health, attack)

# Usando dicionário para itens
items = {
    "potion": ("cura", 20),
    "shield": ("defesa", 5),}

# Usando lista e tupla para o inventário
inventory = ["potion", "shield", "potion","shield"]

# Usando set para habilidades únicas
skills = {"Golpe Rápido", "Defesa Rápida"}

# Usando bitwise para criar um sistema de pontos
level_points = 0b0011  # 3 pontos iniciais

# Criando personagens
player_name = input("Digite o nome do seu personagem: ")
player = Character(player_name, 100, 15)
monster = create_monster()
print(f"\nUm {monster.name} apareceu! Vida: {monster.health}, Ataque: {monster.attack}")

print("\nJogo Iniciado!")

# Loop do jogo
while player.is_alive() and monster.is_alive():
    print("\n--- Sua vez ---")
    action = input("Digite 'a' para atacar ou 'i' para usar item: ").lower()

    if action == 'a':
        player.attack_enemy(monster)
    elif action == 'i' and inventory:
        item = inventory.pop(0)
        effect, value = items.get(item, (None, 0))
        if effect == "cura":
            player.health += value
            print(f"Você usou uma {item} e recuperou {value} pontos de vida.")
        elif effect == "defesa":
            player.attack += value
            print(f"Você usou um {item} e ganhou {value} pontos de ataque.")
        else:
            print("Item desconhecido.")
    else:
        print("Ação inválida ou sem itens.")

    if monster.is_alive():
        print("\n--- Turno do Monstro ---")
        monster.attack_enemy(player)

# Verifica o resultado
if player.is_alive():
    print("\nVocê venceu!")
else:
    print("\nVocê perdeu.")

# Mostrando uso de bitwise
print("\nPontos de nível inicial:", bin(0b0011))
level_points = level_points << 1  # Ganha o dobro de pontos
print("Pontos de nível após bônus:", bin(level_points))
