// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

$( "#Poverty" ).click(function(e) {
    e.preventDefault();
  GetData("Poverty");
});
$( "#Education" ).click(function(e) {
    e.preventDefault();
  GetData("Education");
});
$( "#Health" ).click(function(e) {
    e.preventDefault();
  GetData("Health");
});