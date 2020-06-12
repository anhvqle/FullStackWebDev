var player1 = prompt("Player One: Enter Your Name, you will be Blue");
var player1Color = 'rgb(86, 151, 255)';
var player2 = prompt("Player Two: Enter Your Name, you will be Blue");
var player2Color = 'rgb(237, 45, 73)';

var table = $('table tr');

//Start the game with Player 1
$('h3').text(player1 + ": it is your turn, please pick a column to drop your blue chip.");

var currPlayer = 1;       //1 is blue(1st player), 2 is red (2nd player)
var currColor = player1Color;

$('.board button').on('click', function() {
  var col = $(this).closest("td").index();
  var row = getBottomRow(col);
  changeColor(row, col, currColor);
  currPlayer = currPlayer * -1;

  if(currPlayer === 1){
    $('h3').text(player1 + ": it is your turn, please pick a column to drop your blue chip.");
    currColor = player1Color;
  }
  else{
    $('h3').text(player2 + ": it is your turn, please pick a column to drop your red chip.");
    currColor = player2Color;
  }
})

function changeColor(row, col, color){
  return table.eq(row).find('td').eq(col).find('button').css('background-color', color);
}

function getCurrentColor(row, col) {
  return table.eq(row).find('td').eq(col).find('button').css('background-color');
}

function getBottomRow(col){
  var color = getCurrentColor(table.length, col);
  for (var row = table.length; row >= 0; row--) {
    color = getCurrentColor(row,col);
    if (color === 'rgb(128, 128, 128)') {
      return row;
    }
  }
}
