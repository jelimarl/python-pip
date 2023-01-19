import random

def choose_options():
  options = ("piedra", "papel", "tijera")
  user_option = input("¿piedra, papel o tijera? ").lower()
  
  if not user_option in options:
    print("Esa opción no es válida")
    #continue
    return None, None

# También se puede hacer con una lista
  computer_option = random.choice(options)

  print("user_option: ", user_option)
  print("computer_option: ", computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print("Empate!")

  elif user_option == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("usuario ganó!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("computadora ganó!")
      computer_wins += 1

  elif user_option == "papel":
    if computer_option == "tijera":
      print("tijera gana a papel")
      print("computador ganó!")
      computer_wins += 1
    else:
      print("papel gana a piedra")
      print("usuario ganó!")
      user_wins += 1

  elif user_option == "tijera":
    if computer_option == "piedra":
      print("piedra gana a tijera")
      print("computador ganó!")
      computer_wins += 1
    else:
      print("tijera gana a papel")
      print("usuario ganó!")
      user_wins += 1

  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
   
  if computer_wins == 2:
    print("El ganador es la computadora!")
    #break

  elif user_wins == 2:
    print("El ganador es el usuario!")
    #break

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1

  while user_wins < 2 and computer_wins < 2:
    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    check_winner(user_wins, computer_wins)

    rounds += 1
        
run_game()