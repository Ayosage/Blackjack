#need to do:
#Add wager tracking
#recylce rounds
#Ace 1 or 11
#fix bug - if user bust, game continues
#Add Ascii Art

import random



play = True
#cash = 2500

player_hands = {}
player_hands_list = []

#Start New Game, create hands as lists in dictionary player_hands
def play_new_hand():
  new_hand = input("Do you want to play a new hand of Blackjack? y/n \n").lower()
  num_players = int(input("How many other players are at the table? \n"))
  player_hands["dealer_hand"] = []
  player_hands["user_hand"] = []
  for num in range(0, num_players):
    player_hands["cp_hand_" + str(num + 1)] = []
  if new_hand == "y":
    return True
  elif new_hand == "n":
    return False

#deal 2 cards to each hand
def deal_hand():
  for hand in player_hands:
    player_hands[str(hand)] = [random.choice(cards), random.choice(cards)]
  
#check if dealer busts
def dealer_check():
  while hand_check("dealer_hand") <= 16:
    player_hands["dealer_hand"].append(random.choice(cards))
  return hand_check("dealer_hand")

# the algorithm to check the value of a hand 
def hand_check(hand):
  hand_total = 0
  for card in player_hands[str(hand)]:
    hand_total += card_value[str(card)]
  return hand_total

#user draw
def user_new_card():
  hit = input("Do you want another card? y/n \n")
  while hit == "y":
    if hit == "y":
      player_hands["user_hand"].append(random.choice(cards))
      print(f'Your Hand total is: {hand_check("user_hand")}')
      print(f' Your Hand is: {player_hands["user_hand"]}')
      if hand_check("user_hand") > 21:
        print("Bust, You Lose")
    hit = input("Do you want another card? y/n \n")

#checks computer hands for bust
def computer_check():
  num_of_players = len(player_hands) - 2
  for num in range(0, num_of_players):
    hand_check("cp_hand_" + str(num + 1))
    while hand_check("cp_hand_" + str(num + 1)) <= 16:
      player_hands["cp_hand_" + str(num + 1)].append(random.choice(cards))

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
    
        
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
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


play = play_new_hand()
while play == True:
  deal_hand()
  print(f'Your Hand: {player_hands["user_hand"]}')
  dealer_check()
  if dealer_check() > 21:
    print("Dealer Bust, Table Wins")
    print(player_hands["dealer_hand"])
  else:
    print(f'The dealers hand is: [{player_hands["dealer_hand"][0]}, _]')
    user_new_card()
    computer_check()
    final_check()
    break