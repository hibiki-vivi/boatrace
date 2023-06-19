document.getElementById("day").innerHTML = showDay();
document.getElementById("month").innerHTML = showMonth();
document.getElementById("year").innerHTML = showyear();


function showDay() {
  var now = new Date();
  var day = now.getDate();
  return day;
}
function showMonth(){
  var now = new Date();
  var month = now.getMonth()+1;
  return month;
}
function showyear(){
  var now = new Date();
  var year = now.getFullYear();
  return year;
}

var predictButton = document.querySelector('input[type="submit"]');
var selectedLocation = document.getElementById('selectedLocation');
var selectedRace = document.getElementById('selectedRace');

predictButton.addEventListener('click', function() {
  var location = document.querySelector('.location select').value;
  var race = document.querySelector('.race select').value;
  selectedLocation.value = location;
  selectedRace.value = race;
});