
WAITING_COMMAND = "w"
START_BATTLE_COMMAND = "s"
QUIT_COMMAND = "q"

class CLRunner():
    current_command = WAITING_COMMAND
    
    def run(self):
        print("Welcome to the Kyrons Legacy Damage Calculator!\n"
              + "List of Commands:\n"
              + "\t s: Start Battle\n"
              + "\t q: Quit")
        while self.current_command != QUIT_COMMAND:
            new_command = input("Enter Command: ")
            self.process_command(new_command)
            self.current_command = new_command

    def process_command(self, command):
        if command == WAITING_COMMAND:
            pass
        elif command == START_BATTLE_COMMAND:
            print("Starting Battle!")
        elif command == QUIT_COMMAND:
            print("Thanks for playing!")
        else:
            print("{command} is not a valid command, please try again".format(command = command))

if __name__ == "__main__":
    CLRunner().run()