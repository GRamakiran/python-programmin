while True:
 player1=input("which one do you want to chose either rock or paper or scissor  ")
 player2=input("which one do you want to chose either rock or paper or scissor  ")
 if player1==player2:
 	 print("chosen same game tie")
 elif player1=="rock":
	 if player2=="scissor":
		 print("rock beats scissor so, player1 won")
	 else:
		 print("player2 won")
 elif player1=="scissor":
	 if player2=="paper":
		 print("scissor beats paper so, player1 won")
	 else:
		 print("player2 won")
 elif player1=="paper":
	 if player2=="rock":
		 print("paper beats rock so, player1 won")
	 else:
		 print("player2 won")
 else:
	 print("invalid inputs")
 play_again=input("play again yes or no:  ")
 if play_again =="no":
	 break
