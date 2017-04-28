function shapes()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	canvas.strokeStyle = "yellow";
	canvas.fillStyle = "purple";
	canvas.beginPath();
	canvas.moveTo(150, 0);
	canvas.lineTo(130, 100);
	canvas.lineTo(170, 100);
	canvas.closePath();
	canvas.stroke();
	canvas.fill();
	
	var x = document.getElementById("tri1");
	tri1.beginPath();
	tri1.moveTo(170, 100);
	tri1.lineTo(130, 100);
	tri1.lineTo(170, 100);
	tri1.closePath();
	tri1.stroke();
	tri1.fill();
}

window.addEventListener("load", shapes, false);