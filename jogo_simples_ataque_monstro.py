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

# Criando personagens
player_name = input("Digite o nome do seu personagem: ")
player = Character(player_name, 100, 15)
monster = Character("Monstro", 80, 10)

print("Jogo Iniciado!")

# === TAREFA GRUPO 1 ===
# Adicionar mais monstros aleatórios com diferentes características.
# Sugestão: Criar uma função create_monster() que gera monstros com atributos variados.

# === TAREFA GRUPO 2 ===
# Melhorar o sistema de itens, permitindo que o jogador colete mais itens ao derrotar monstros.
# Sugestão: Criar uma função collect_item() que adiciona itens ao inventário.

# === TAREFA GRUPO 3 ===
# Adicionar um sistema de experiência e níveis para o jogador.
# Sugestão: Criar uma função gain_experience() e aumentar atributos com base no nível.

# === TAREFA GRUPO 4 ===
# Implementar habilidades especiais que o jogador pode usar durante a batalha.
# Sugestão: Criar uma função use_skill() e permitir que o jogador escolha uma habilidade.

# === TAREFA GRUPO 5 ===
# Melhorar o sistema de combate com chance de crítico (dano extra).
# Sugestão: Usar random para calcular chance de crítico.

# === TAREFA GRUPO 6 ===
# Implementar um sistema de fuga, onde o jogador pode tentar escapar da batalha.
# Sugestão: Criar uma função run_away() com chance de sucesso.

# Jogo simples: jogador ataca o monstro até que um deles morra
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
    print("Você venceu!")
else:
    print("Você perdeu.")

# Mostrando uso de bitwise
print("\nPontos de nível inicial:", bin(level_points))
level_points = level_points << 1  # Ganha o dobro de pontos
print("Pontos de nível após bônus:", bin(level_points))
