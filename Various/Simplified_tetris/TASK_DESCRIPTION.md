# Tetris

<p>Implement a simple ‘text-mode’ version of the ‘Tetris’ game, following the specification below.<p>

<p>There are 5 pieces In this version of Tetris:<p>
  
<pre>
 ****

 *
 *
 **

  *
  *
 **

  *
 **
 *

 **
 **
</pre>

<p>and they fall down a 20x20 tetris board:</p>

<pre>
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 *                    *
 **********************
</pre>

<p>The game starts with a random piece appearing at the top of the board. The user is then prompted to make a move:</p>

- a (return): move piece left
- d (return): move piece right
- w (return): rotate piece counter clockwise
- s (return): rotate piece clockwise

<p>If the move the user selects is valid, then it is executed and the screen redrawn. If it is not valid then they are again prompted to enter a valid move. Note that the game only updates after the user has entered a valid action.</p>

<p>A valid move is defined thus: The piece is altered as per the user’s input, and then displaced by 1 row downwards. If the piece, drawn at it’s new location, is not outside the bounds of the board, and does not overlap any pieces that previously fell, then it is a valid move. If the piece’s new position is such that it allows no valid move, then a new piece appears along the top of the board, randomly positioned along the x-axis. If this new piece happens offer no valid move, then the game is over and the program exits.</p>
