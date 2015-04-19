$(document).ready(function(){
    $("#email").change(function(){
	console.log("email input");
        $("#contactInfo").val($("#email").val());
    });
    $("#phone").change(function(){
	console.log("phone input");
	$("#contactInfo").val($("#phone").val());
    });

    $("#saveItemButton").click(function(){
        console.log("saveItemButton clicked");
	var formData=$("#saveItemForm").serialize();
	console.log("formData: " + formData);
	$.get('saveItem.cgi',
    	    formData,
	    function(result){
		//window.location.replace("iFoundIndex.html");	
		window.location.replace("item.cgi");
		console.log(result);	
    });
     console.log("submitted");

    });
});
