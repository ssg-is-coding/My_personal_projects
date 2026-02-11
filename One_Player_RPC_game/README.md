This program is a small implementation of the almighty rock, paper, scissors game.
It is a one player version where you play against a bot that learns from its mistake throughout the game.

Bot algorithm:
It is actually rather simple, the bot chooses an handshape represented by and integer between 0 and 2 in a list of 9elements in which every handshape is evenly represented by 33 instances and make the choice of the index using radint.
Whenever the bot looses, he will take your choice in the shape of the associated integer and replace the instance he chose in his list by the value that would have beated your choice thus making it more likely to beat you if you make the same choice.
It works rather well and the bot will start to win or draw more often quite fast, but you could easily mislead him by playing the same handshape multiples times in a row and knowing how its decision algorithm works basically allows you to predict his choices basically making it almost impossible for him to win,but if you play randomly it should work just fine.

