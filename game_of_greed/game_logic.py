import random

def handle_type_error(func):
  def wrapper(args):
    try:
      return func(args)
    except Exception as e:
      return 0
  return wrapper


class GameLogic:
  def __init__(self):
    pass

  @staticmethod
  @handle_type_error
  def calculate_score(args):
    score = 0
    frequency = {}

    # single input
    if type(args) == int:
      if args == 1:
        score += 100
      elif args == 5:
        score += 50
      return score

    # Straight
    if len(args) == 6:
      arr = list(args)
      arr.sort()
      if arr == [ 1,2,3,4,5,6 ]:
        score += 1500
        return score
      

    # input Frequency
    for i in args:
      if i in frequency:
        frequency[i] += 1
      else:
        frequency[i] = 1

    # 3 pairs
    pair_arr = []
    for i in frequency:
      if frequency[i] == 2:
        pair_arr.append(i)
      if len(pair_arr) == 3:
        score = 1500
        return score
      
    # Scoring tuple input
    for key in frequency:
      if key == 1:
        if frequency[key] >= 3:
          score += 1000
          remain_ones = frequency[key] - 3
          for i in range(remain_ones):
            score += 1000
        else:
          score += frequency[key] * 100
      
      elif key == 5:
        if frequency[key] >= 3:
          score += 500
          remain_fives = frequency[key] - 3
          for i in range(remain_fives):
            score += 500
        else:
          score += frequency[key] * 50
     
      elif frequency[key] >= 3:
        score += 100 * key
        remaining = frequency[key] - 3
        for num in range(remaining):
          score += key * 100
    return score
      
  @staticmethod
  def roll_dice(num):
    results = []
    for i in range(num):
      results.append(random.randint(1,6))

    return tuple(results)
