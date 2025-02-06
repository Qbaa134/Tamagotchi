import time
import random
import threading

# Wzory jajek
EGGS = [
    """
     _______
    /       \\
   /  O O   \\
  |         |
   \\_______/
    """,
    """
     _______
    /       \\
   /  * *   \\
  |    ~    |
   \\_______/
    """,
    """
     _______
    /       \\
   /  @ @   \\
  |    ^    |
   \\_______/
    """,
    """
     _______
    /       \\
   /  # #   \\
  |   _-_   |
   \\_______/
    """
]

# Funkcja wyboru jajka
def choose_egg():
    print("Choose your egg!")
    for i, egg in enumerate(EGGS, start=1):
        print(f"\nEgg {i}:")
        print(egg)
    
    while True:
        choice = input("\nEnter the number of your chosen egg (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= len(EGGS):
            print(f"\nYou chose Egg {choice}:")
            print(EGGS[int(choice) - 1])
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

# Wzory Tamagotchi w różnych fazach wzrostu
TAMAGOTCHI_ASCII_STAGES = [
    """
     _______
    /       \\
   /         \\
  |           |
   \\_________/
    """,
    """
     (^_^)
    /     \\
   |       |
    \\_____/
    """,
    """
     ^_^
    / O O \\
    |  ~  |
     \\___/
    """,
    """
    (O_O)
   /       \\
  /  @ @    \\
 (    ~      )
  \\_______/
    """,
    """
     (*_*)
   /   ^   \\
  /   @ @   \\
 (    -.-    )
  \\________/
    """,
    """
     (^_^)
  / \\___/ \\
 (   o o   )
  \\__ ~ __/
    """,
    """
     [>_<]
   /       \\
  /   o o   \\
 (    ~_~    )
  \\_______/
    """
]

# Klasa Tamagotchi
class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.hunger = 100
        self.energy = 100
        self.happiness = 100
        self.health = 100
        self.age = 0
        self.stage = 0
        self.alive = True
        self.points = 0  # Punkty za aktywności
        self.lock = threading.Lock()

    def grow(self):
        while self.alive:
            time.sleep(240)  # Co 4 minuty (240 sekund)
            self.age += 1
            self.stage = min(self.age // 4, len(TAMAGOTCHI_ASCII_STAGES) - 1)
            with self.lock:
                print("\nYour Tamagotchi has grown!")
                print(TAMAGOTCHI_ASCII_STAGES[self.stage])

    def feed(self):
        food_type = input("Choose food: 1. Fruits  2. Vegetables  3. Sweets: ")
        if food_type == "1":
            self.hunger += 20
            self.points += 5  # Zbieranie punktów za aktywność
            print("You fed your Tamagotchi fruits. Hunger level increased!")
        elif food_type == "2":
            self.hunger += 25
            self.points += 7  # Zbieranie punktów za aktywność
            print("You fed your Tamagotchi vegetables. Hunger level increased more!")
        elif food_type == "3":
            self.hunger += 10
            self.points += 3  # Zbieranie punktów za aktywność
            print("You fed your Tamagotchi sweets. But be careful with too many!")
        else:
            print("Invalid choice!")
        self.hunger = min(100, self.hunger)

    def play(self):
        game_type = input("Choose game: 1. Ball  2. Hide and Seek  3. Puzzle: ")
        if game_type == "1":
            self.happiness += 10
            self.energy -= 5
            self.points += 5  # Zbieranie punktów za aktywność
            print("You played with a ball!")
        elif game_type == "2":
            self.happiness += 15
            self.energy -= 10
            self.points += 8  # Zbieranie punktów za aktywność
            print("You played hide and seek!")
        elif game_type == "3":
            self.happiness += 5
            self.points += 4  # Zbieranie punktów za aktywność
            print("You solved a puzzle!")
        else:
            print("Invalid choice!")
        self.happiness = min(100, self.happiness)
        self.energy = max(0, self.energy)

    def sleep(self):
        duration = int(input("How many hours should your Tamagotchi sleep? (1-5): "))
        if 1 <= duration <= 5:
            self.energy += duration * 10
            self.points += 2  # Zbieranie punktów za aktywność
            print(f"{self.name} slept for {duration} hours. Energy level increased!")
        else:
            print("Invalid input!")
        self.energy = min(100, self.energy)

    def heal(self):
        method = input("Choose a method: 1. Medicine  2. Rest  3. Herbal Tea: ")
        if method == "1":
            self.health += 20
            self.points += 10  # Zbieranie punktów za aktywność
            print("You gave your Tamagotchi medicine!")
        elif method == "2":
            self.health += 10
            self.points += 5  # Zbieranie punktów za aktywność
            print("You let your Tamagotchi rest!")
        elif method == "3":
            self.health += 15
            self.points += 8  # Zbieranie punktów za aktywność
            print("You gave your Tamagotchi herbal tea!")
        else:
            print("Invalid choice!")
        self.health = min(100, self.health)

    def physiology(self):
        print("\nPhysiology time!")
        action_type = input("Choose an action: 1. Poop  2. Pee: ")
        if action_type == "1":
            print("Your Tamagotchi pooped!")
            self.points += 3  # Zbieranie punktów za aktywność
        elif action_type == "2":
            print("Your Tamagotchi peed!")
            self.points += 2  # Zbieranie punktów za aktywność
        else:
            print("Invalid choice!")

    def shop(self):
        print("\nWelcome to the Shop!")
        print(f"You have {self.points} points.")
        print("What would you like to buy?")
        print("1. Toy (10 points)")
        print("2. New Food (15 points)")
        print("3. Health Potion (20 points)")
        print("4. Exit shop")
        
        choice = input("Enter your choice: ")
        if choice == "1" and self.points >= 10:
            self.points -= 10
            print("You bought a Toy!")
        elif choice == "2" and self.points >= 15:
            self.points -= 15
            print("You bought New Food!")
        elif choice == "3" and self.points >= 20:
            self.points -= 20
            print("You bought a Health Potion!")
        elif choice == "4":
            print("Leaving shop...")
        else:
            print("You don't have enough points or invalid choice!")

    def status(self):
        print("\n--- Status ---")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Age: {self.age}")
        print(f"Points: {self.points}")
        print("-----------------")

    def time_passes(self):
        self.hunger -= 5
        self.energy -= 5
        self.happiness -= 5
        self.health -= random.randint(0, 3)

        if self.hunger <= 0 or self.energy <= 0 or self.health <= 0:
            self.alive = False

    def is_alive(self):
        return self.alive

def main():
    choose_egg()  # Wywołanie funkcji wyboru jajka
    name = input("\nWhat do you want to name your Tamagotchi? ")
    pet = Tamagotchi(name)

    # Uruchamiamy osobny wątek dla wzrostu Tamagotchi
    growth_thread = threading.Thread(target=pet.grow)
    growth_thread.start()

    while pet.is_alive():
        pet.status()
        print("\nChoose an action:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Heal")
        print("5. Physiology")
        print("6. Shop")
        print("7. Do nothing")

        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.heal()
        elif choice == "5":
            pet.physiology()
        elif choice == "6":
            pet.shop()
        elif choice == "7":
            print(f"{pet.name} is waiting...")
        else:
            print("Invalid choice!")

        pet.time_passes()
        time.sleep(1)

    print(f"\nOh no! {pet.name} has passed away. Game over.")

if __name__ == "__main__":
    main()
