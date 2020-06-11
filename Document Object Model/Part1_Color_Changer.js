//--------------------DOM INTERACTION--------------------
var header = document.querySelector("h1")
header.style.color = 'red'

function getRandomColor(){
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)];
  }
  return color
}

function changeHeaderColor(){
  header.style.color = getRandomColor();
}

setInterval("changeHeaderColor()",500); //change color every 0.5 sec

//------------------CONTENT INTERACTION------------------
var x = document.querySelector("p")
x.innerHTML = "This is <strong>BOLD</strong>"

var special = document.querySelector("#special")
var specialA = special.querySelector("a")
specialA.setAttribute("href","https://www.amazon.com")

var link = document.querySelector("h4")

//--------------------EVENT LISTENER---------------------
var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

// Hover (mouseover and mouseout)
headOne.addEventListener('mouseover',function(){
  headOne.textContent = "Mouse currently Over";
  headOne.style.color = 'red';
})

headOne.addEventListener('mouseout',function(){
  headOne.textContent = "Mouse Not On me."
  headOne.style.color = 'blue';
})


// On Click
headTwo.addEventListener("click",function(){
  headTwo.textContent = "Clicked On";
  headTwo.style.color = 'blue';
})

// Double Click
headThree.addEventListener("dblclick",function(){
  headThree.textContent = "Double Clicked!";
  headThree.style.color = 'red';
})
