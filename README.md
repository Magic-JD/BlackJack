# BlackJack

A simple blackjack game

- To run create a new configuration with main.py

- Basic rules of betting:
Before the deal begins, the gambler places a bet.
Bet must be within the boundaries of minimum and maximum bets, generally $2 - $500.
Blackjack is a 2 player game, the dealer vs the gambler
After gambler places a bet:
 if the gambler loses - the dealer (house) takes the bet.
 if the gambler wins - the gambler keeps the bet plus receives the same amount from the dealer (house)
 if the gambler has blackjack (a 10 / face card + ace)and the dealer does not, the gambler wins automatically, 
  keeping their bet and receiving 1.5 times the amount from the dealer
 if the dealer has blackjack and the gambler does not, the dealer wins automatically and takes the
  gamblers bet
 if the gambler and dealer draw ("push") - gambler keeps the original bet and receives nothing extra.
 
- The Dealer's Play
 The dealer's play is automatic:
  if total >= 17, the dealer must stick
  if total < 17, the dealer must take (a) card(s) until total is >= 17
  if dealer has an ace, and counting it as 11 would bring the total to >= 17 (bot not > 21), the dealer 
   must  count the ace as 11 and stick.
  
   
 
 Rules taken from:
 https://bicyclecards.com/how-to-play/blackjack/