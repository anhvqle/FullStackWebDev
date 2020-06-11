// var x = $('h1');
// // You can easily edit the css properties:
// x.css("color",'red');
// x.css("background","blue");
// // Multiple CSS properties at once:
// var newCSS = {
//   "color":"white",
//   "background":"blue",
//   "border":"5px solid red"
// }
// x.css(newCSS);
//
// // Grabbing multiple returns an array-like object:
// var listItems = $('li');
// listItems.css("color",'red');
// listItems.eq(0).css('color','blue');
// listItems.eq(1).css('color','purple');
//
// // Changing Text:
// $('h1').text("Brand New Text!")
// // Changing HTML
// $('h1').html("<em>Now in Italics</em>")
// // Changing an attribute
// $("input").eq(1).attr('type','checkbox');
// // Changing values
// $("input").eq(0).val("Enter Something Else");
// // Add a Class
// $('h2').addClass("turnRed")
// // Remove a Class
// $("h2").removeClass("turnRed");
// // Toggle the Class on and Off
// $("h3").toggleClass("turnBlue");
//
// jQuery makes it easy to interact with the DOM!

// List of all possible events!
// https://api.jquery.com/category/events/

//////////////
// CLICKS ///
////////////

// On Click
$('h1').click(function(){
  console.log("There was a click!");
})

// Click on multiple elements
$('li').click(function() {
  console.log("Click on any li !");
})

// Using This with jQuery
$('h3').click(function() {
  $(this).text("I was changed!");
})

/////////////////
// KEYPRESS ////
///////////////
// Using This with jQuery
$('input').eq(0).keypress(function() {
  $('h3').toggleClass("turnRed");
})

// We can use this event object, that has a ton of information!
$('input').eq(0).keypress(function(event) {
  console.log(event);
})

// Each Keyboard Key has a Keycode, for example Enter is 13
$('input').eq(0).keypress(function(event) {
  if(event.which === 13){
    $('h3').toggleClass("turnRed");
  }
})

////////////
// ON() ///
//////////

// on() basically works like addEventListener()
$('h1').on("dblclick",function() {
  $('h1').addClass('turnBlue');
})

$('li').on('mouseenter',function() {
  $(this).toggleClass('turnRed');
})

/////////////////////////////
// EFFECTS and ANIMATIONS //
///////////////////////////

// http://api.jquery.com/category/effects/

$('input').eq(1).val("FADE OUT EVERYTHING");

$('input').eq(1).on("click",function(){
  $(".container").fadeOut(3000) ;
})


$('input').eq(1).on("click",function(){
  $(".container").slideUp(1000) ;
})
