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
        print(f"{self.name.title()} attacks {opponent.name.title()} for {damage} damage!") #using random damage variable here
        # if opponent.health <= 0:
        # print(f"{opponent.name} has been defeated!")
        #The two above lines were built into starter code and are redundant b/c it's already in an
        #if statement in the battle function below.

    def display_stats(self): #I changed this from the starter code b/c I think the stats displayed this way is easier to read
        print(f"{self.name.title()}'s Stats:")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")

    def player_health(self): #added this to show player's health after every turn as the Wizard's does
        print(f"{self.name.title()} health is now {self.health}")

    def heal(self):
        max_heal = round(self.health * 0.25)
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
        self.was_deflected = False #this ensure it always starts the function with was_deflected as False

    def sword_strike (self, opponent):
        opponent.health -= 25
        print(f"{self.name.title()} dealt a devestation sword strike dealing {opponent.name.title()} {self.attack_power} damage!")
    
    def deflect (self, opponent):
        reduced_damage = max(1, opponent.attack_power // 2)
        print(f"{self.name.title()} deflected the strike from {opponent.name.title()}, thus minimizing damage to {reduced_damage}")
        self.health -= reduced_damage

    def unique_abilities(self, opponent):
        print("Choose which unique ability to use: ")
        print("1. Sword Strike")
        print("2. Deflect")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            self.was_deflected = False
            self.sword_strike(opponent)
        elif choice == "2":
            self.was_deflected = True
            self.deflect(opponent)
            
        else:
            print("You selected an invalid choice. Defaulting to basic attack.")
            self.attack(opponent)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
    
    def ice_storm (self, opponent):
        opponent.health -= 30
        print(f"{self.name} cast a powerful ice storm on {opponent.name}'s head dealing 30 points in damage1")
    
    def fireball (self, opponent):
        opponent.health -= 35
        print(f"{self.name} cast a fireball at {opponent.name} dealing 35 points in damage!")
    
    def unique_abilities(self, opponent):
        print("Choose which unique ability to use: ")
        print("1. Ice Storm")
        print("2. Fireball")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            self.ice_storm(opponent)
        elif choice == "2":
            self.fireball(opponent)
        else:
            print("You selected an invalid choice. Defaulting to basic attack.")
            self.attack(opponent)
    
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
        self.was_evaded = False
        super().__init__(name, health=125, attack_power=20)
    
    def double_shot(self, opponent):
        opponent.health -= round(self.attack_power * 1.25) #this does 1.25 times the attack power
        print(f"{self.name.title()} attacks {opponent.name} with a double-shot for {round(self.attack_power * 1.25)} damage.")
        if opponent.health < 0:
            print(f"{opponent.name} has been defeated!")
        
    def evade(self, opponent):
        #50% chance to evade
        success = random.random() < 0.5 #this is a 50% chance of success
        if success:
            self.was_evaded = True
            print(f"{self.name.title()} evaded attack from {opponent.name} and was dealt 0 damage!")
            return True #this will be used in the wizard's attack function to determine if the player evaded the attack or not
        else:
            print(f"{self.name.title()} failed to evade the attack from {opponent.name}")
            return False #sets the player to False so the wizard can attack the player

    def unique_abilities(self, opponent):
        print("Choose which unique ability to use: ")
        print("1. Double Shot")
        print("2. Evade")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            self.double_shot(opponent)
        elif choice == "2":
            evader = self.evade(opponent)
            if not evader:  #if evader is False, then the opponent will attack
                opponent.attack(self) #this is the opponent attacking the player
        else:
            print("You selected an invalid choice. Defaulting to attack.")
            self.attack(opponent)
        
        return False

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=185, attack_power=30)
    
    def divine_smite(self, opponent):
        attack_damage = round(self.attack_power * 1.25)
        opponent.health -= attack_damage
        print(f"{self.name} dealt {opponent.name} {attack_damage} points in damage!")

    def healing_potion (self):
        self_heal = self.health * 0.10 #up to 10% health rejuvenation
        max_heal = min(self_heal, self.max_health - self.health)
        self.health += max_heal
        print(f"{self.name} healed himself by {max_heal} points.")

    def unique_abilities(self, opponent):
        print("Choose which unique ability to use: ")
        print("1. Divne Smite")
        print("2. Healing Potion")

        choice = input("Enter the number of your choice: ")
        if choice == "1":
            self.divine_smite(opponent)
        elif choice == "2":
            self.healing_potion()
        else:
            print("You selected an invalid choice. Defaulting to basic attack.")
            self.attack(opponent)

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
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):

    while wizard.health > 0 and player.health > 0:

        # if wizard.health > 0:
        #     wizard.attack(player)
        #     wizard.regenerate()

        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.unique_abilities(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Defaulting to attack.")
            player.attack(wizard)

        if wizard.health > 0:
            if isinstance(player, Warrior) and player.was_deflected: #this is checking if the player is a warrior and if the player was deflected
                pass #if the player was deflected, then the wizard doesn't attack and it passes to wizard.regenerate()
            elif isinstance (player, Archer) and player.was_evaded: #this is checking if the player is an archer and if the player evaded the attack
                pass #if the player evaded the attack, then the wizard doesn't attack and it passes to wizard.regenerate()
            else:
                wizard.attack(player) #if the player wasn't deflected or evaded, then the wizard attacks the player
            wizard.regenerate()
        
        if player.health > 0:
            print(f"{player.name}'s health is now {player.health}")

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