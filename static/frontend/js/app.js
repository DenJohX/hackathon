// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

$( "#Poverty" ).click(function(e) {
    e.preventDefault();
  $("#title").text("World poverty gap $1.25/day");
  GetData("Poverty");
});
$( "#Education" ).click(function(e) {
    e.preventDefault();
  $("#title").text("Lower secondary completion rate");
  GetData("Education");
});
$( "#Health" ).click(function(e) {
    e.preventDefault();
  $("#title").text("Number of neonatal deaths");
  GetData("Health");
});