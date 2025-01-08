import time

class Game:
    def __init__(self):
        self.locations = self.create_world()
        self.current_location = "Forest"
        self.inventory = []

    def create_world(self):
        # Define locations and their descriptions
        return {
            "Forest": {
                "description": "You are in a dense forest. Paths lead east and south.",
                "connections": {"east": "Clearing", "south": "Cave Entrance"},
                "items": ["stick"],
            },
            "Clearing": {
                "description": "You are in a bright clearing. There's a small hut here. Paths lead west.",
                "connections": {"west": "Forest"},
                "items": ["key"],
            },
            "Cave Entrance": {
                "description": "You stand before the entrance of a dark cave. The forest is to the north.",
                "connections": {"north": "Forest"},
                "items": [],
            },
        }

    def display_location(self):
        # Show the current location's description
        location = self.locations[self.current_location]
        print(location["description"])
        if location["items"]:
            print("You see the following items:", ", ".join(location["items"]))

    def process_command(self, command):
        # Process player commands
        words = command.lower().split()
        if len(words) == 0:
            print("I don't understand that command.")
            return

        action = words[0]

        if action == "go":
            self.move(words[1] if len(words) > 1 else None)
        elif action == "look":
            self.display_location()
        elif action == "take":
            self.take_item(words[1] if len(words) > 1 else None)
        elif action == "inventory":
            self.show_inventory()
        elif action in ["quit", "exit"]:
            print("Thanks for playing!")
            return False
        else:
            print("I don't understand that command.")
        return True

    def move(self, direction):
        # Handle movement between locations
        if direction in self.locations[self.current_location]["connections"]:
            self.current_location = self.locations[self.current_location]["connections"][direction]
            self.display_location()
        else:
            print("You can't go that way.")

    def take_item(self, item):
        # Handle picking up items
        location = self.locations[self.current_location]
        if item in location["items"]:
            location["items"].remove(item)
            self.inventory.append(item)
            print(f"You take the {item}.")
        else:
            print("That item is not here.")

    def show_inventory(self):
        # Show the player's inventory
        if self.inventory:
            print("You are carrying:", ", ".join(self.inventory))
        else:
            print("You are not carrying anything.")

    def start(self):
        # Main game loop
        print("\033[96mhot, breath sickens the noxious air in the metal van")
        time.sleep(3)
        print("chattering tones that radiate my ears.")
        time.sleep(3)
        print("fresh is the screen, lay my head as I watch the snow pass")
        time.sleep(3)
        print("sky and earth swalloweed into a blankent that covers the world")
        time.sleep(3)
        print("time stretches, snaps, and recoils")
        time.sleep(3)
        print("a jolt,")
        time.sleep(1)
        print("a skid,")
        time.sleep(1)
        print("a splintered tree.")
        time.sleep(3)
        print("then lost myself in the frigid sea")
        time.sleep(3)
        print("last I saw... rather... last I felt")
        time.sleep(3)
        print("was its heated breath")
        time.sleep(3)
        print("and their piercing...")
        time.sleep(3)
        print("""
 ▄████▄   ▒█████   ██▓    ▓█████▄    ▓█████▓██   ██▓▓█████   ██████ 
▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▀ ██▌   ▓█   ▀ ▒██  ██▒▓█   ▀ ▒██    ▒ 
▒▓█    ▄ ▒██░  ██▒▒██░    ░██   █▌   ▒███    ▒██ ██░▒███   ░ ▓██▄   
▒▓▓▄ ▄██▒▒██   ██░▒██░    ░▓█▄   ▌   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄   ▒   ██▒
▒ ▓███▀ ░░ ████▓▒░░██████▒░▒████▓    ░▒████▒ ░ ██▒▓░░▒████▒▒██████▒▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒    ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
  ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒     ░ ░  ░▓██ ░▒░  ░ ░  ░░ ░▒  ░ ░
░        ░ ░ ░ ▒    ░ ░    ░ ░  ░       ░   ▒ ▒ ░░     ░   ░  ░  ░  
░ ░          ░ ░      ░  ░   ░          ░  ░░ ░        ░  ░      ░  
░                          ░                ░ ░                     
""")
        self.display_location()
        while True:
            command = input("> ")
            if not self.process_command(command):
                break

# Uncomment the line below to play the game
Game().start()
