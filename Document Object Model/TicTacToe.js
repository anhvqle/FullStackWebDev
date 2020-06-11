var squares = document.querySelectorAll('td')
var restart = document.querySelector('#RestartButton')

function clear(){
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}
restart.addEventListener('click', clear);

function fillSquare(){
  if(this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent === 'X') {
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
}

for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', fillSquare);
}
