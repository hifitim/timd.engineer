function landing_time() 
{
	var d = new Date()
	var timezone = d.toString().match(/\(([A-Za-z\s].*)\)/)[1]
	var monthNames = ["January", "February", "March", "April", "May", "June", 
					  "July", "August", "September", "October", "November", "December"];
	var weekday = [ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	var n = weekday[d.getDay()];
	var m = monthNames[d.getMonth()];
	var y = d.getFullYear();
	var mm = d.getMinutes().toString();
	if(mm.length == 1)
		mm = "0"+mm;
	var hh = d.getHours().toString();
	if(hh.length == 1)
		hh = "0"+hh;
	var ss = d.getSeconds().toString();
	if(ss.length == 1)
		ss = "0"+ss;
	document.getElementById("landing-time").dateTime = n + " " + m + " " + y + " " + hh+":"+mm+":"+ss + " " + timezone
	document.getElementById("landing-time").innerHTML = n + " " + m + " " + y + " " + hh+":"+mm+":"+ss + " " + timezone
	document.getElementById("landing-time").style.textAlign = "center";
}