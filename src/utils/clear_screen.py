# import only system from os
from os import name, system


def clear_screen():
	system('cls' if name == 'nt' else 'clear')
  
