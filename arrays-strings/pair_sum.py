# Define pair_sum(lst, target) to return a tuple of unique indices whose elements sum to the target, guaranteeing exactly one such pair exists.

def pair_sum(numbers, target):
  previous_numbers = {}
  
  for index, num in enumerate(numbers):
    complement = target - num
    
    if complement in previous_numbers:
      return (index, previous_numbers[complement])
    
    previous_numbers[num] = index

print(pair_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)