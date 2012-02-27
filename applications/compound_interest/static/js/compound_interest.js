function onSubmit(){
	pv=document.getElementById("pv");
	np=document.getElementById("np");
	fi=document.getElementById("fi");
	fv=document.getElementById("fv");
	invest_per_year=document.getElementById("invest_per_year_t").value;
	var req=new XMLHttpRequest();
	req.open("get","/compound_interest/default/calc?pv="+pv.value+"&fi="+fi.value+"&np="+np.value+"&fv="+fv.value+"&invest_per_year="+invest_per_year.value,false)
	req.send();
	alert("dummy"+req.responseText);
	fv.value=req.responseText;
	return false;
}