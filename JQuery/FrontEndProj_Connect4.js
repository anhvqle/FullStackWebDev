var player1 = prompt("Player One: Enter Your Name, you will be Blue");
var player1Color = 'rgb(86, 151, 255)';   //blue
var player2 = prompt("Player Two: Enter Your Name, you will be Blue");
var player2Color = 'rgb(237, 45, 73)';    //red

var table = $('table tr');

//Start the game with Player 1
$('h3').text(player1 + ": it is your turn, please pick a column to drop your blue chip.");

var currPlayer = 1;       //1 is blue(1st player), 2 is red (2nd player)
var currColor = player1Color;
var currName = player1;

$('.board button').on('click', function() {
  var col = $(this).closest("td").index();
  var row = getBottomRow(col);
  changeColor(row, col, currColor);

  if(lineCheck() || diagonalWin()){
    endGame(currName);
  }

  currPlayer = currPlayer * -1;

  if(currPlayer === 1){
    currName = player1;
    $('h3').text(player1 + ": it is your turn, please pick a column to drop your blue chip.");
    currColor = player1Color;
  }
  else{
    currName = player2;
    $('h3').text(player2 + ": it is your turn, please pick a column to drop your red chip.");
    currColor = player2Color;
  }
})

//Change color of a button
function changeColor(row, col, color){
  return table.eq(row).find('td').eq(col).find('button').css('background-color', color);
}

//Return the current color of a specific button
function getCurrentColor(row, col) {
  return table.eq(row).find('td').eq(col).find('button').css('background-color');
}

//Return the lowest row available in a column
function getBottomRow(col){
  var color = getCurrentColor(table.length, col);
  for (var row = table.length - 1; row >= 0; row--) {
    color = getCurrentColor(row,col);
    if (color === 'rgb(128, 128, 128)') {
      return row;
    }
  }
}

//Check whether the four colors are the same
function sameColor(one, two, three, four){
  return (one === two && two === three && three === four && one !== 'rgb(128, 128, 128)' && one !== undefined)
}

//Check for horizontal or vertical win
function lineCheck(){
  for(var row = 0; row < table.length; row++){
    for(var col = 0; col < table.length; col++){
      if(sameColor(getCurrentColor(row, col), getCurrentColor(row+1, col), getCurrentColor(row+2, col), getCurrentColor(row+3, col)) ||         //vertical win
        sameColor(getCurrentColor(row, col), getCurrentColor(row, col+1),getCurrentColor(row, col+2), getCurrentColor(row, col+3))){            //horizontal win
          console.log("Detect a win");
          return true;
      }
    }
  }
}

//Check for diagonal win
function diagonalWin(){
  return false;
}

//return effects and changes when detect a winner
function endGame(playerName) {
  $('h3').fadeOut('fast');
  $('h2').fadeOut('fast');
  $('h1').text(playerName + " has won! Refresh your page to play again!").css(newCSS);
}

//Change the text after a winner is detected
var newCSS = {
  'color' : 'DarkGoldenRod',
  'fontSize' : '50px'
}
