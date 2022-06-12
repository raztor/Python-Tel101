Kevin and Stuart want to play the '**The Minion Game**'.  

**Game Rules**  

Both players are given the same string, .  
Both players have to make substrings using the letters of the string .  
Stuart has to make words starting with _consonants_.  
Kevin has to make words starting with _vowels_.  
The game ends when both players have made all possible substrings.  

**Scoring**  
A player gets `+1` point for each occurrence of the substring in the string .  

**For Example**:  
String \= _BANANA_  
Kevin's vowel beginning word = _ANA_  
Here, _ANA_ occurs twice in _BANANA_. Hence, Kevin will get `2` Points.

For better understanding, see the image below:

![](https://s3.amazonaws.com/hr-challenge-images/9693/1450330231-04db904008-banana.png "banana.png")

Your task is to determine the winner of the game and their score.

**Function Description**

Complete the _minion\_game_ in the editor below.

_minion\_game_ has the following parameters:

-   _string string:_ the string to analyze

**Prints**

-   _string:_ the winner's name and score, separated by a space on one line, or `Draw` if there is no winner