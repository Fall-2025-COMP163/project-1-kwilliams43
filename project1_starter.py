"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: AI helped debug syntax, indentation, and file I/O errors.
"""

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    if character_class == 'Warrior':
        strength = 10 + level * 5
        magic = 3 + level * 2
        health = 100 + level * 10
    elif character_class == 'Mage':
        strength = 3 + level * 2
        magic = 12 + level * 5
        health = 75 + level * 6
    elif character_class == 'Rogue':   # fixed spelling from 'Rouge'
        strength = 7 + level * 4
        magic = 8 + level * 4
        health = 85 + level * 8
    elif character_class == 'Cleric':
        strength = 8 + level * 3
        magic = 9 + level * 3
        health = 80 + level * 8
    else:
        # Default stats if invalid class entered
        strength = 5 + level * 2
        magic = 5 + level * 2
        health = 75 + level * 5
    return strength, magic, health


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100
    return {
        'name': name,
        'class': character_class,
        'level': level,
        'strength': strength,
        'magic': magic,
        'health': health,
        'gold': gold
    }


def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    """
    try:
        with open(filename, 'w') as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
        return True
    except Exception:
        return False


def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        data = {}
        for line in lines:
            key, value = line.strip().split(': ', 1)
            data[key] = value

        character = {
            'name': data['Character Name'],
            'class': data['Class'],
            'level': int(data['Level']),
            'strength': int(data['Strength']),
            'magic': int(data['Magic']),
            'health': int(data['Health']),
            'gold': int(data['Gold'])
        }
        return character
    except FileNotFoundError:
        return None


def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("========================")


def level_up(character):
    """
    Levels up character and updates stats
    """
    character['level'] += 1
    strength, magic, health = calculate_stats(character['class'], character['level'])
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    msg = f"{character['name']} leveled up to level {character['level']}!"
    print(msg)
    return msg


# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your character's name: ")
    character_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ")
    char = create_character(name, character_class)
    display_character(char)

    filename = f"{char['name']}_save.txt"
    if save_character(char, filename):
        print(f"Character saved to {filename}")

    print("Loading character...")
    loaded_char = load_character(filename)
    if loaded_char:
        display_character(loaded_char)

    print("Leveling up your character...")
    level_up(loaded_char)
    display_character(loaded_char)
