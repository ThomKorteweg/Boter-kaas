import random

from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, EvaluationAgent, start


class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)


class MyRookieAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
          reward = 1
        elif is_winner(board, opponent[self.symbol]):
          reward = -1
        else:
          reward = 0
        return reward
      
    

class MyAgent(MLAgent):

    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
      

 
 


def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1.versus")
    print("2. Random agent")
    print("3. trainen ")
    print("4. Slim ")
    print("5.plotten")
    print(67 * "-")


def TrainenEnPlotten():
  random.seed(1)
  
  my_agent = MyAgent()
  random_agent = RandomAgent()
  rookie_agent = MyRookieAgent()
  
  train_and_plot(agent=my_agent,
                 validation_agent=random_agent,
                 iterations=50,
                 trainings=100,
                 validations=1000)
  
  train_and_plot(agent=rookie_agent,
                validation_agent=random_agent,
                iterations=5,
                trainings=100,
               validations=1000)

loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        print("Menu 1 has been selected")
        start()
    elif choice == 2:
        print("Menu 2 has been selected")
        my_random_agent = MyRandomAgent()
        start(player_o=my_random_agent)
    elif choice == 3:
      print("Menu 3 has been selected")
      ## You can add your code or functions here
      rookie_agent = MyRookieAgent()
      start(player_o=rookie_agent)
    elif choice == 4:
        print("Menu 4 has been selected")
      
    elif choice == 5:
        print("Menu 5 has been selected")
        TrainenEnPlotten()
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        input("Wrong option selection. Enter any key to try again..")
