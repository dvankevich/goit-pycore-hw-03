import random

def get_numbers_ticket(min, max, quantity):
    '''
    generating a set of unique random numbers.
    Args:
        min (int): the minimum possible number in the set. >= 1
        max (int): maximum possible number in a set. <= 1000
        quantity(int): number of numbers to choose. Value between min and max
    Returns:
        []: a list of randomly selected, sorted numbers. If the parameters do not meet
            the specified constraints, the function returns an empty list.
    '''
    result_list = []
    if min >= 1 and max <=1000 and quantity >= min and quantity <=max :
       result_set = set()
       while len(result_set) < quantity:
          result_set.add(random.randint(min,max))
          # можна без циклу і множин:
          # result_list = random.sample(range(min, max + 1), quantity)

       result_list = list(result_set)
       result_list.sort()

    return result_list



if __name__ == "__main__":
  print(get_numbers_ticket.__doc__)

  assert get_numbers_ticket(0,0,0) == []
  assert get_numbers_ticket(1,1001,6) == []
  assert get_numbers_ticket(1,45,50) == []
  assert len(get_numbers_ticket(1,36,5)) == 5
  #print(get_numbers_ticket(1,36,5))
  #print(get_numbers_ticket(1,49,6))