
        else:
            self.print_invalid_choice()

        if self.decision_counter == 0:
            self.energy = min(self.energy + 30, 100)
            self.fun = min(self.fun + 30, 100)
            self.health = min(self.health + 30, 100)
            self.decision_counter = 5
            print(f"It's now the end of Week {self.week_counter}.")
            print("You receive +30 to your Energy, Fun, and Health.\n")
            self.week_counter += 1

        if self.week_counter == 5: