import random

class GameLogic:
  def __init__(self):
    pass

  @staticmethod
  def calculate_score(args):
    score = 0
    frequency = {}
    for i in args:
      if i in frequency:
        frequency[i] += 1
      else:
        frequency[i] = 1
    
    # Score Logic
    for key in frequency:
      if key == 1:
        if frequency[key] == 3:
          score += 1000
        else:
          score += frequency[key] * 100
        continue
      if frequency[key] == 3:
        score += 100  * key
      if key == 5:
        score += frequency[key] * 50
    return score
      
        

  @staticmethod
  def roll_dice(*args):
    results = []
    for i in args:
      results.append(random.randint(0,6))
    return tuple(results)

  
class Banker:
  def __init__(self):
    self.unbanked = 0
    self.banked = 0

  def shelf(self, points=0):
    self.unbanked += points


  def bank(self):
    self.banked = self.unbanked
    self.unbanked = 0
    return self.banked

  def clear_shelf(self):
    self.shelf = 0



  
  '''
  # single fives == 50
  # ones == 100
  # three of a kind == 100 X number rolled except ones are worth 1000
  # four-6 of a kind == each de doubles amount of previous roll
  # straight == 1500
  # three pairs are worth 1000

  1 == 100
  5 == 50
  1,1,1 == 1000
  2,2,2 == 200
  3,3,3 == 300
  4,4,4 == 400
  5,5,5 == 500
  6,6,6 == 600
  '''
  

# print(GameLogic.calculate_score(2,3,3,4,5,5))
# b = Banker()
# b.shelf(100)
# b.shelf(50)
# b.shelf(100)
# b.bank()
# print(f'There are {b.unbanked} unbanked and {b.banked} banked points')

previous = (1,2,3,4,5,6)
score = GameLogic.roll_dice(*previous)
ss = [1,5,1]
print(GameLogic.calculate_score(ss))

