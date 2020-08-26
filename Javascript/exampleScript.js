var play = prompt("Would you like to start the roster web app? y/n");
var roster = [];
var action = "empty"
if(play === 'y'){
  while(action !== 'quit'){
    action = prompt("Please select an action: add, remove, display, or quit.")
    if(action === 'add'){
      var name = prompt("What name would you like to add?")
      roster.push(name)
    }
    else if(action === 'display'){
      console.log(roster);
    }
    else if(action === 'remove'){
      var name = prompt("What name would you like to remove?")
      var index = roster.indexOf(name);
      roster.splice(index, 1);
    }
    else if (action === 'quit') {
      alert("Thanks for using the web app")
    }
    else {
      alert("Command not recognized")
    }
  }
}
// Part 6 - Objects Exercise

////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31,
  nameLength: function(){
    console.log(this.name.length);
  }
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.
function nameLength() {
  console.log(employee["name"].length);
}


///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
function printInfo() {
  alert("Name is " + this.name + ", Job is " + this.job + ", Age is " + this.age);
}
// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.



///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
function lastName() {
  console.log(employee["name"].split(" ")[1]);
}

// Add a method called lastName that prints
// out the employee's last name to the console.

// You will need to figure out how to split a string to an array.
// Hint: http://www.w3schools.com/jsref/jsref_split.asp
