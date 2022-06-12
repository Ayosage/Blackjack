#need to do:
#Add wager tracking
#Add Ascii Art

import random



play = True
#cash = 2500

player_hands = {}
player_hands_list = []

#Start New Game, create hands as lists in dictionary player_hands
def play_new_hand():
  num_players = int(input("How many other players are at the table? \n"))
  player_hands["dealer_hand"] = []
  player_hands["user_hand"] = []
  for num in range(0, num_players):
    player_hands["cp_hand_" + str(num + 1)] = []

#deal 2 cards to each hand
def deal_hand():
  for hand in player_hands:
    player_hands[str(hand)] = [random.choice(card_values), random.choice(card_values)]
  
#check if dealer busts
def dealer_check():
  while hand_check("dealer_hand") <= 16:
    player_hands["dealer_hand"].append(random.choice(card_values))
  return hand_check("dealer_hand")

# the algorithm to check the value of a hand 
def hand_check(hand):
  hand_total = 0
  for card in player_hands[str(hand)]:
    hand_total += card_value[str(card)]
  if 'A' in player_hands[str(hand)] and hand_total > 21.6:
    hand_total -= 10
  return hand_total

#user draw
def user_new_card():
  hit = input("Do you want another card? y/n \n")
  while hit == "y":
    if hit == "y": 
      player_hands["user_hand"].append(random.choice(card_values))
      print(f'Your Hand total is: {round(hand_check("user_hand"))}')
      print(f' Your Hand is: {player_hands["user_hand"]}')
      if hand_check("user_hand") > 21.6:
        print("Bust, You Lose")
        break
    hit = input("Do you want another card? y/n \n")

#checks computer hands for bust
def computer_check():
  num_of_players = len(player_hands) - 2
  for num in range(0, num_of_players):
    hand_check("cp_hand_" + str(num + 1))
    while hand_check("cp_hand_" + str(num + 1)) <= 16:
      player_hands["cp_hand_" + str(num + 1)].append(random.choice(card_values))

#final score check
def final_check():
  high_score = 0
  win_hand = ""
  for hand in player_hands:
    hand_total = 0
    for card in player_hands[str(hand)]:
      hand_total += card_value[str(card)]
    if hand_total >= high_score and hand_total < 22:
      high_score = hand_total
      win_hand = hand
  print(win_hand)
  print(high_score)
  print(player_hands)

def end_play():
  end = input("Do you want to play another round of Blackjack? Y/N \n").lower()
  if end == "y":
    return True
  else:
    return False
  
card_value = {
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10.1,
  "Q": 10.2,
  "K": 10.3,
  "A": 11,
}
card_values = list(card_value.keys())

play = True
while play:
  play_new_hand()
  deal_hand()
  print(f'Your Hand: {player_hands["user_hand"]}')
  dealer_check()
  if dealer_check() > 21:
    print("Dealer Bust, Table Wins")
    print(player_hands["dealer_hand"])
    continue
  
  print(f'The dealers hand is: [{player_hands["dealer_hand"][0]}, _]')
  user_new_card()
  computer_check()
  final_check()
  play = end_play()
