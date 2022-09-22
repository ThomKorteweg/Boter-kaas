import random
from bke import EvaluationAgent, start, can_win

class Mijnspeler(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    if can_win(board, opponent-symbol):
      getal = getal - 1000
    return getal
 
mijn_speler = MijnSpeler()
start(player_o=mijn_speler)

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)
 
my_random_agent = MyRandomAgent()
start(player_x=my_random_agent)