let FN = prompt("What is Your First Name: ");
let LN = prompt("What is Your Last Name: ")
let age = prompt("What Is Your Age: ")
let height = prompt("What Is Your Height in centimeters: ")
let pet = prompt("What Is Your Pet Name: ")
if(FN[0] === LN[0] && age > 20 && age < 30 && height >= 170 && pet[pet.length - 1] === 'y'){
  console.log("Welcome Comrade! You've passed the Spy Test")
}
else{
  console.log("Sorry, nothing to see here.");
}
