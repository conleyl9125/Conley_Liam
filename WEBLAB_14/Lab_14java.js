
function validate() 
{
	var u = document.forms.input.username.value;
	var p = document.forms.input.password.value;
	var atPos = u.indexOf("@");
	var dotPos = u.lastIndexOf(".");	
	
	//we need... username@webAddress.extension
	//if, the following...
		//@ is not in the string
		//@ is in the wrondg place
		//there is no .com, .gov, or any other extension
		//final dot is in the wrong place	

	if((atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > u.length) && p.length < 6)
	{
		alert("Your username and password are invalid");
	}
	else
	{
		if(atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > u.length)
			alert("this is not valid email address!");
		else if(p.length < 6)
			alert("password is not long enough");
		else
			alert("Success!");
	}
}