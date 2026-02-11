This program is a small implementation of the almighty rock, paper, scissors game.
It is a one player version where you play against a bot that learns from its mistake throughout the game.

Bot algorithm:
It is actually rather simple, the bot chooses an handshape represented by and integer between 0 and 2 in a list of 9elements in which every handshape is evenly represented by 33 instances and make the choice of the index using radint.
Whenever the bot looses, he will take your choice in the shape of the associated integer and replace the instance he chose in his list by the value that would have beated your choice thus making it more likely to beat you if you make the same choice.
It works rather well and the bot will start to win or draw more often quite fast, but you could easily mislead him by playing the same handshape multiples times in a row and knowing how its decision algorithm works basically allows you to predict his choices basically making it almost impossible for him to win,but if you play randomly it should work just fine.

Update:
After thourough (arguable) testing of the bot, it turns out that the number of played games does have an effect on
the bot performances. Under 100 games with a human (me) it wins around 75% of the time. However when tested with a
set of shapes thats was randomly generated (randint once again) its winning rate drops to approximately 50% but 
its progression is more stable, what I mean by that is that if it takes the lead at some point it will tend
to keep it until the end, but as it progresses in the number of games it becomes very senstive to biases and 
misleading. I tested it on 100, 500, 1000, 5000 consecutives games, I tried with 10000 but my IDE (spyder) crashed. 
But the scores are usually quite close regardless of the winner, that is if the bot didnt experienced a big bias 
beforehand.
