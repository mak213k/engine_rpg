import random

class Character:
    def __init__(self, tipo: str, name: str, health: int, attack: int):
        self.tipo = tipo
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        damage = self.attack
        enemy.health -= damage
        print(f"{self.tipo} {self.name} atacou {enemy.name} causando {damage} de dano.")

    def is_alive(self):
        return self.health > 0


# Usando dicionário para itens
items = {
    "potion": ("cura", 20),
    "shield": ("defesa", 5)
}

# Usando lista e tupla para o inventário
inventory = ["potion", "shield", "potion"]

# Usando set para habilidades únicas
skills = {"Golpe Rápido", "Defesa Rápida"}

# Usando bitwise para criar um sistema de pontos
level_points = 0b0011  # 3 pontos iniciais


# ===== CRIAÇÃO DO PERSONAGEM =====
player_name = input("Digite o nome do seu personagem: ")

classes_validas = {"mago", "guerreiro", "paladino", "bardo"}

while True:
    player_class = input(
        "Escolha a classe (mago, guerreiro, paladino, bardo): "
    ).lower()

    if player_class in classes_validas:
        break
    else:
        desistir = input(
            "Essa classe não existe, agora voce tem dois caminhos, desistir dessa jornada ou continuar e enfrentar os maiores desafios de sua existencia.\nVocê vai desistir dessa aventura? (Sim/Não): "
        ).lower()

        if desistir == "sim":
            print("Sabia que essa aventura não era para você, volte para sua vida comum, Fim de jornada...")
            exit()
        elif desistir == "não":
            continue
        else:
            print("Resposta inválida. Voltando à escolha da classe.")


player = Character(player_class.capitalize(), player_name, 100, 15)
monster = Character("Monstro", "Grande Árvore Apodrecida", 80, 10)

print("\nJogo Iniciado!")


# ===== LOOP PRINCIPAL DO JOGO =====
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


# ===== RESULTADO FINAL =====
if player.is_alive():
    print("Você venceu!")
else:
    print("Você perdeu.")


# ===== SISTEMA DE PONTOS (BITWISE) =====
print("\nPontos de nível inicial:", bin(level_points))
level_points = level_points << 1  # Ganha o dobro de pontos
print("Pontos de nível após bônus:", bin(level_points))
