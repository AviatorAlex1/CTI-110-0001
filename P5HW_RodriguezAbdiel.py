# Abdiel Rodriguez
# 13 APR 2025
# P5HW_RodriguezAbdiel
# Creates a Simple RPG adventure/combat style Star Wars game with the ability to go past the campaign and go into "Epic" mode. If the Player dies and has over 1000 Credits, then the player can resume playing as a revive feature.

import random

# Campaign of planets and their enemy pools and final level bosses
PLANETS = {
    "Tatooine": {
        "enemies": [("Tusken Raider", 60, 12), ("Jawa Thief", 50, 10)],
        "boss": ("Krayt Dragon", 120, 20)
    },
    "Hoth": {
        "enemies": [("Wampa", 80, 15), ("Imperial Scout", 70, 13)],
        "boss": ("AT-AT Commander", 140, 22)
    },
    "Mustafar": {
        "enemies": [("Dark Acolyte", 90, 18), ("Lava Droid", 85, 17)],
        "boss": ("Sith Lord", 160, 25)
    },
    "Coruscant": {
        "enemies": [("Sith Assassin", 100, 20), ("Bounty Enforcer", 95, 18)],
        "boss": ("Darth Tyrannus", 180, 30)
    }
}

# Elite Enemies that arrive once the main campaign is completed, and player enters EPIC mode. 
ELITE_ENEMIES = [
    ("Rogue Jedi", 130, 28),
    ("Mandalorian Veteran", 140, 30),
    ("Dark Force Wraith", 150, 32),
    ("Ancient Droid", 160, 35)
]

planet_order = list(PLANETS.keys())

# Creating the character data and attributes
class Character:
    def __init__(self, name, side, hp, attack_power):
        self.name = name
        self.side = side
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.level = 1
        self.xp = 0
        self.credits = 50
        self.inventory = {
            "health_packs": 2,
            "weapon": "Basic Lightsaber"
        }
        self.planet_index = 0
        self.current_planet = planet_order[self.planet_index]
        self.wins_on_planet = 0
        self.boss_defeated = False
        self.post_game = False

# Attack Function
    def attack(self, enemy):
        base_damage = random.randint(5, self.attack_power)
        print(f"{self.name} attacks {enemy.name} with {self.inventory['weapon']} for {base_damage} damage!")
        enemy.hp -= base_damage

# Checks if play is alive or not
    def is_alive(self):
        return self.hp > 0

# Player Heal functions
    def heal(self):
        if self.inventory["health_packs"] > 0:
            heal_amount = random.randint(20, 40)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.inventory["health_packs"] -= 1
            print(f"{self.name} uses a health pack and heals {heal_amount} HP!")
        else:
            print("No health packs left!")

# Gain XP function after completing the battle
    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP!")
        if self.xp >= self.level * 50:
            self.level_up()

# Player Leveling up function
    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.attack_power += 5
        self.hp = self.max_hp
        print(f"\n*** {self.name} leveled up to {self.level}! ***")
        print(f"Max HP: {self.max_hp}, Attack Power: {self.attack_power}")

# Earning credits post battle
    def earn_credits(self, amount):
        self.credits += amount
        print(f"{self.name} earns {amount} credits! (Total: {self.credits})")

# Different levels of planets to explore as player progresses and defeats bosses
    def explore_new_planet(self):
        if self.planet_index + 1 < len(planet_order):
            self.planet_index += 1
            self.current_planet = planet_order[self.planet_index]
            self.wins_on_planet = 0
            self.boss_defeated = False
            print(f"\n🚀 {self.name} travels to a new planet: {self.current_planet}!\n")
        else:
            print("\n🌌 You have explored all known planets! You're a galactic legend!\n")
            end_choice = input("Do you want to end the game or keep battling enemies? (end/continue): ")
            if end_choice.lower() == "end":
                print("\n🛑 Game Over. Thanks for playing!")
                exit()
            else:
                self.post_game = True
                print("\n⚔️ You chose to continue battling across the galaxy! Prepare for elite challenges!\n")

# Enemy Spawning function
def generate_enemy(player):
    if player.post_game:
        name, hp, atk = random.choice(ELITE_ENEMIES)
        print(f"\n🚨 An elite enemy appears: {name}!")
        return Character(name, "Elite", hp, atk)
    else:
        planet_data = PLANETS[player.current_planet]
        if player.wins_on_planet >= 3 and not player.boss_defeated:
            name, hp, atk = planet_data["boss"]
            print(f"\n👑 Boss Battle Initiated: {name} has appeared!")
            return Character(name, "Boss", hp, atk)
        else:
            name, hp, atk = random.choice(planet_data["enemies"])
            return Character(name, "Enemy", hp, atk)

# Shop system
def visit_shop(player):
    while True:
        print(f"\n🛒 Welcome to the shop, {player.name}!")
        print(f"Credits: {player.credits}")
        print("Items for sale:")
        print("1. Health Pack (20 credits)")
        print("2. Weapon Upgrade (50 credits)")
        print("3. Exit Shop")

        choice = input("Choose an item to buy (1/2/3): ")

        if choice == "1":
            if player.credits >= 20:
                player.credits -= 20
                player.inventory["health_packs"] += 1
                print("Purchased a health pack!")
            else:
                print("Not enough credits.")
        elif choice == "2":
            if player.credits >= 50:
                player.credits -= 50
                player.attack_power += 5
                player.inventory["weapon"] = "Enhanced Lightsaber"
                print("Weapon upgraded to Enhanced Lightsaber!")
            else:
                print("Not enough credits.")
        elif choice == "3":
            break
        else:
            print("Invalid option.")

#  Inital Player creation
def create_character():
    print("Welcome to Star Wars RPG!")
    name = input("Enter your character's name: ")
    print("Choose your side:\n1. Jedi\n2. Sith")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        return Character(name, "Jedi", 100, 20)
    else:
        return Character(name, "Sith", 100, 25)

# Battle logic
def battle(player, enemy):
    print(f"\n⚔️ A wild {enemy.name} appears on {player.current_planet}!")
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.name}'s HP: {player.hp} | {enemy.name}'s HP: {enemy.hp}")
        print("Choose an action:\n1. Attack\n2. Heal\n3. View Inventory")
        action = input("Action (1/2/3): ")

        if action == "1":
            player.attack(enemy)
        elif action == "2":
            player.heal()
            continue
        elif action == "3":
            print(f"\nInventory: {player.inventory}")
            continue
        else:
            print("Invalid choice. Turn skipped.")
            continue

        if enemy.is_alive():
            enemy.attack(player)
        else:
            print(f"\n✅ {enemy.name} has been defeated!")
            player.gain_xp(30)
            player.earn_credits(25)

            if enemy.side == "Boss":
                print(f"\n🎉 You defeated the boss of {player.current_planet}!")
                player.boss_defeated = True
                player.explore_new_planet()
            else:
                player.wins_on_planet += 1

# Game over screen with retry option
def game_over_screen(player):
    print("\n💀 GAME OVER 💀")
    print(f"Credits: {player.credits}")
    if player.credits >= 1000:
        retry = input("You have over 1000 credits. Do you want to revive and retry? (y/n): ")
        if retry.lower() == 'y':
            player.hp = player.max_hp
            player.inventory["health_packs"] = 2
            print("\n🛡️ You are revived with full HP and 2 health packs! Fight on!")
            return True
    print("\nReturning to main menu...")
    return False

# Main game loop
def main():
    while True:
        player = create_character()
        while player.is_alive():
            enemy = generate_enemy(player)
            battle(player, enemy)
            if not player.is_alive():
                if not game_over_screen(player):
                    break
            elif not player.boss_defeated:
                visit_shop(player)
                cont = input("Do you want to fight another enemy? (y/n): ")
                if cont.lower() != 'y':
                    break
        again = input("Do you want to start a new game? (y/n): ")
        if again.lower() != 'y':
            print("\nThanks for playing Star Wars RPG!")
            break

if __name__ == "__main__":
    main()