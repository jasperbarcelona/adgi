$(document).ready(function(){

/*$(window).resize(function(){
	var height = $(window).height()-60;
	$("#container").css("height",height);
});


$("#search").on('click', function() {
	$(".toggleClicked").switchClass( "toggleClicked", "toggleUnclicked", 500 );
	$(".navClicked").switchClass( "navClicked", "navUnclicked", 500 );
	$("#head").animate({"left":"-100%"}, 500,'jswing');
	$("#searchHead").animate({"left":"0"}, 500,'jswing');
});*/

var height = $(window).height()-60;
$("#body-container").css("height",height);

$(".rows").on('click', function() {
	$(this).switchClass( "rows", "rows-clicked", 500 );
	$(".rows-clicked").switchClass( "rows-clicked", "rows", 500 );
});

});