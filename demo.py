import random

# Define a list of spells
spells = {
    "fireball": {"damage": 50, "success_rate": 0.7},
    "ice shard": {"damage": 40, "success_rate": 0.8},
    "lightning bolt": {"damage": 60, "success_rate": 0.6},
    "heal": {"healing": 30, "success_rate": 0.9},
}

# Define the player's initial stats
player = {
    "health": 100,
    "mana": 100,
}

# Define the enemy's initial stats
enemy = {
    "health": 100,
}

def cast_spell(spell_name):
    spell = spells.get(spell_name)
    if not spell:
        print(f"The spell '{spell_name}' does not exist!")
        return
    
    success = random.random() < spell["success_rate"]
    if success:
        if "damage" in spell:
            enemy["health"] -= spell["damage"]
            print(f"You cast {spell_name} and dealt {spell['damage']} damage!")
        elif "healing" in spell:
            player["health"] += spell["healing"]
            player["health"] = min(player["health"], 100)  # Cap health at 100
            print(f"You cast {spell_name} and healed for {spell['healing']} health!")
    else:
        print(f"Your {spell_name} spell failed!")

def enemy_attack():
    damage = random.randint(10, 30)
    player["health"] -= damage
    print(f"The enemy attacks and deals {damage} damage!")

def game_status():
    print(f"\nPlayer Health: {player['health']}, Mana: {player['mana']}")
    print(f"Enemy Health: {enemy['health']}\n")

def main():
    print("Welcome to the Spell Caster Game!")
    while player["health"] > 0 and enemy["health"] > 0:
        game_status()
        spell_name = input("Enter the spell you want to cast: ").lower()
        if spell_name in spells:
            cast_spell(spell_name)
            if enemy["health"] <= 0:
                print("Congratulations! You have defeated the enemy!")
                break
            enemy_attack()
            if player["health"] <= 0:
                print("You have been defeated by the enemy.")
        else:
            print("Invalid spell name. Please try again.")
    
    print("Game Over")

if __name__ == "__main__":
    main()
