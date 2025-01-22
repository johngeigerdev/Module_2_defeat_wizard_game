# Base Character class
import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = random.randint(5, self.attack_power) #this randomizes the attack power of the attacker from 5 to their max attack power
        opponent.health -= damage #this subtracts the damage from the opponent's health
        print(f"{self.name} attacks {opponent.name} for {damage} damage!") #using random damage variable here
        # if opponent.health <= 0:
        #     print(f"{opponent.name} has been defeated!")
        #The two above lines were built into starter code and are redundant b/c it's already in an
        #if statement in the battle function below.

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        max_heal = self.health * 0.25
        # above is creating a variable of healing amount being 25% of the character's health. 
        #the below uses the 'min' method to choose the smallest value between the heal amount and
        #the difference between max health and current health. It chooses the lesser of these 2 values to ensure
        #it doesn't go over the max health.
        heal_amount = min(max_heal, self.max_health - self.health)
        self.health += heal_amount
        print(f"{self.name} has been regained {round(heal_amount)} of his health.")

# Implement the Warrior, Mage, and EvilWizard classes below
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
    def Sword_Strike (self, opponent):
        opponent.health -= 25
        print(f"{self.name} dealt a devestation sword strike dealing {opponent.name} {self.attack_power} damage!")
    def deflect (self, opponent):
        opponent.attack_power = opponent.attack_power//2 #this cuts opponent's attack power in half rounded down to nearest integer
        print(f"{self.name} deflected a the strike from {opponent.name}, thus minimizing damage to {opponent.attack_power//2}")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    def Ice_storm (self, opponent):
        opponent.health -= 30
        print(f"{self.name} cast a powerful ice storm on {opponent.name}'s head dealing 30 points in damage1")
    def Fireball (self, opponent):
        opponent.health -= 35
        print(f"{self.name} cast a fireball at {opponent.name} dealing 35 {self.max_health} in damage!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=125, attack_power=20)
    
    def DoubleShot(self, opponent):
        opponent.health -= self.attack_power * 2
        print(f"{self.name} attacks {opponent.name} for {self.attack_power * 2} damage.")
        if opponent.health < 0:
            print(f"{opponent.name} has been defeated!")
        
    def Evade(self, opponent):
        opponent.attack_power = 0
        print(f"{self.name} evaded attack from {opponent.name} and was dealt 0 damage!")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=185, attack_power=30)
    

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        pass  # Implement Archer class
    elif class_choice == '4':
        pass  # Implement Paladin class
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()