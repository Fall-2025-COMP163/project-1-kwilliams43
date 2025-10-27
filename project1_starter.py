"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    level = 1 
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100   
return {'name': name, "class": character_class, 'level': level, 'strength': strength, 'magic': magic, 'health': health, 'gold': gold}
    

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    if character_class == 'Warrior':
        strength = 10 + level * 5
        magic = 3 + level * 2
        health = 100 + level * 10
    elif character_class =='Mage':
        strength = 3 + level * 2
        magic = 12 + level * 5
        health = 75 + level * 6
    elif character_class =='Rouge':
        strength = 7 + level * 4
        magic = 8 + level * 4
        health = 85 + level * 8
    elif character_class == 'Cleric':
        strength = 6 + level * 3
        magic = 10 + level * 4
        health = 95 + level * 9
    else:
        strength = 8 + level * 2
        magic = 9 + level * 3
        health = 80 + level * 8
    return (strength, magic, health)
        

    
    
  

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    with open(fliename, 'w') as file:
        f.write(f'Charaacter Name: {character['name']}\n')
        f.write(f'Class: {character['class']}\n')
        f.write(f'Strength: {character['strength']}\n')
        f.write(f'Magic: {character['magic']}\n')
        f.write(f'Health: {character['health']}\n')
        f.write(f'Gold: {character[gold]}\n')
        return True


        

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    with open(filename,'r') as file:
        lines = f.readlines()


    
        
    
    

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
