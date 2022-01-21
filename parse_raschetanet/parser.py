import bs4
import requests
import time

text = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<html lang="ru">
<head>
<meta name="viewport" content="width=device-width, initial-scale=0.35"/>
<meta charset="UTF-8"/>
<meta name="description" content="Теплотехнический расчет ограждающих конструкций онлайн в соответствии с действующими нормами, с расчетом точки росы и сопротивления паропроницанию."/>
<meta name="keywords" content="теплотехнический расчет, точка росы, теплорасчет, паропроницание" />
<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
<META HTTP-EQUIV="PRAGMA" CONTENT="NO-CACHE">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Теплотехнический расчет онлайн</title>
<link rel="stylesheet" href="css/style.css"  media="screen">
<!-- Это для мобильных
<link rel="stylesheet" href="css/mobile.css" media="handheld, only screen and (max-device-width:480px)" >
-->
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript">
var mat_id="";
var HatchType1=1;
var HatchType2=2;
var HatchType3=3;
var HatchType4=4;
var HatchType5=5;
var HatchType6=6;
var HatchType7=7;
var prirash1=0;
var prirash2=0;
var prirash3=0;
var prirash4=0;
var prirash5=0;
var prirash6=0;
var prirash7=0;
var dens1=0;
var dens2=0;
var dens3=0;
var dens4=0;
var dens5=0;
var dens6=0;
var dens7=0;
function select_mat(id_mat)
{
document.getElementById('logo1').style.display= 'block';
mat_id=id_mat;
}

function hide_logo1()
{
document.getElementById('logo1').style.display= 'none';
}

function add(id_mat)
{
document.getElementById('logo2').style.display= 'block';
mat_id1=id_mat;
}

function clear_all()
{
document.getElementById('cond_a_temp').value = '';
document.getElementById('cond_b_temp').value = '';
document.getElementById('vapor_temp').value = '';
document.getElementById('materials_temp').value = '';
document.getElementById('hatch_temp').value = '';
document.getElementById('prirash_temp').value = '';
document.getElementById('dens_temp').value = '';
}

function hide_mat(id_mat)
{
document.getElementById('logo2').style.display= 'none';
}
function input()
{
document.getElementById('logo2').style.display= 'none';
id1=mat_id1.substr(13, 1);
document.getElementById('materials'+id1).value=document.getElementById('materials_temp').value;
document.getElementById('cond_a'+id1).value=document.getElementById('cond_a_temp').value;
document.getElementById('cond_b'+id1).value=document.getElementById('cond_b_temp').value;
document.getElementById('vapor'+id1).value=document.getElementById('vapor_temp').value;
document.getElementById('thickness'+id1).focus();
id1=eval(id1);
if (document.getElementById('hatch_temp').value=='Теплоизоляционные материалы'){hatch=3};
if (document.getElementById('hatch_temp').value=='Бетон'){hatch=1};
if (document.getElementById('hatch_temp').value=='Кирпичная кладка'){hatch=2};
if (document.getElementById('hatch_temp').value=='Дерево'){hatch=7};
if (document.getElementById('hatch_temp').value=='Металлы'){hatch=4};
if (document.getElementById('hatch_temp').value=='Растворы'){hatch=5};
if (document.getElementById('hatch_temp').value=='Гидроизоляционные материалы'){hatch=6};
switch(id1)
	{
	case 1:
	prirash1=document.getElementById('prirash_temp').value;
document.getElementById("prirash1").value=prirash1;
dens1=document.getElementById('dens_temp').value;
document.getElementById("dens1").value=dens1;
document.getElementById("hidd1").value=hatch;
HatchType1=hatch;

break;
	case 2:
	prirash2=document.getElementById('prirash_temp').value;
	document.getElementById("prirash2").value=prirash2;
dens2=document.getElementById('dens_temp').value;
document.getElementById("dens2").value=dens2;
document.getElementById("hidd2").value=hatch;

HatchType2=hatch;
	break;
	case 3:
	prirash3=document.getElementById('prirash_temp').value;
dens3=document.getElementById('dens_temp').value;
document.getElementById("dens3").value=dens3;
document.getElementById("prirash3").value=prirash3;
document.getElementById("hidd3").value=hatch;
HatchType3=hatch;
	break;
	case 4:
	prirash4=document.getElementById('prirash_temp').value;
dens4=document.getElementById('dens_temp').value;
document.getElementById("dens4").value=dens4;
document.getElementById("prirash4").value=prirash4;
document.getElementById("hidd4").value=hatch;
HatchType4=hatch;
	break;
	case 5:
	prirash5=document.getElementById('prirash_temp').value;
dens5=document.getElementById('dens_temp').value;
document.getElementById("dens5").value=dens5;
document.getElementById("prirash5").value=prirash5;
document.getElementById("hidd5").value=hatch;
HatchType5=hatch;
	break;
	case 6:
	prirash6=document.getElementById('prirash_temp').value;
dens6=document.getElementById('dens_temp').value;
document.getElementById("dens6").value=dens6;
document.getElementById("prirash6").value=prirash6;
document.getElementById("hidd6").value=hatch;
HatchType6=hatch;
	break;
	case 7:
	prirash7=document.getElementById('prirash_temp').value;
dens7=document.getElementById('dens_temp').value;
document.getElementById("dens7").value=dens7;
document.getElementById("prirash7").value=prirash7;
document.getElementById("hidd7").value=hatch;
HatchType7=hatch;
	break;
	default:

	}
}

function clear1()
{
document.getElementById('thickness1').value = '';
document.getElementById('cond_a1').value = '';
document.getElementById('cond_b1').value = '';
document.getElementById('vapor1').value = '';
document.getElementById('materials1').value = 'Выбрать';
document.getElementById('hidd1').value = 0;
sendValue1();
}
function clear2()
{
document.getElementById('thickness2').value = '';
document.getElementById('cond_a2').value = '';
document.getElementById('cond_b2').value = '';
document.getElementById('vapor2').value = '';
document.getElementById('materials2').value = 'Выбрать';
document.getElementById('hidd2').value = 0;
sendValue1();
}
function clear3()
{
document.getElementById('thickness3').value = '';
document.getElementById('cond_a3').value = '';
document.getElementById('cond_b3').value = '';
document.getElementById('vapor3').value = '';
document.getElementById('materials3').value = 'Выбрать';
document.getElementById('hidd3').value = 0;
sendValue1();
}
function clear4()
{
document.getElementById('thickness4').value = '';
document.getElementById('cond_a4').value = '';
document.getElementById('cond_b4').value = '';
document.getElementById('vapor4').value = '';
document.getElementById('materials4').value = 'Выбрать';
document.getElementById('hidd4').value = 0;
sendValue1();
}
function clear5()
{
document.getElementById('thickness5').value = '';
document.getElementById('cond_a5').value = '';
document.getElementById('cond_b5').value = '';
document.getElementById('vapor5').value = '';
document.getElementById('materials5').value = 'Выбрать';
document.getElementById('hidd5').value = 0;
sendValue1();
}
function clear6()
{
document.getElementById('thickness6').value = '';
document.getElementById('cond_a6').value = '';
document.getElementById('cond_b6').value = '';
document.getElementById('vapor6').value = '';
document.getElementById('materials6').value = 'Выбрать';
document.getElementById('hidd6').value = 0;
sendValue1();
}function clear7()
{
document.getElementById('thickness7').value = '';
document.getElementById('cond_a7').value = '';
document.getElementById('cond_b7').value = '';
document.getElementById('vapor7').value = '';
document.getElementById('materials7').value = 'Выбрать';
document.getElementById('hidd7').value = 0;
sendValue1();
}

function move_up(id)
{
id=id.substr(7, 1);
id=parseInt(id);
var temp_first_thickness=document.getElementById('thickness'+(id-1)).value;
var temp_first_cond_a=document.getElementById('cond_a'+(id-1)).value;
var temp_first_cond_b=document.getElementById('cond_b'+(id-1)).value;
var temp_first_cond_vapor=document.getElementById('vapor'+(id-1)).value;
var temp_first_cond_materials=document.getElementById('materials'+(id-1)).value;
var temp_first_cond_hidd=document.getElementById('hidd'+(id-1)).value;
if(id==1){var temp_HatchType=HatchType1;}
if(id==2){var temp_HatchType=HatchType1;}
if(id==3){var temp_HatchType=HatchType2;}
if(id==4){var temp_HatchType=HatchType3;}
if(id==5){var temp_HatchType=HatchType4;}
if(id==6){var temp_HatchType=HatchType5;}
if(id==7){var temp_HatchType=HatchType6;}
document.getElementById('thickness'+(id-1)).value =document.getElementById('thickness'+(id)).value;
document.getElementById('cond_a'+(id-1)).value = document.getElementById('cond_a'+(id)).value;
document.getElementById('cond_b'+(id-1)).value = document.getElementById('cond_b'+(id)).value;
document.getElementById('vapor'+(id-1)).value = document.getElementById('vapor'+(id)).value;
document.getElementById('materials'+(id-1)).value = document.getElementById('materials'+(id)).value;
document.getElementById('hidd'+(id-1)).value = document.getElementById('hidd'+(id)).value;
if(id==2){HatchType1=HatchType2;}
if(id==3){HatchType2=HatchType3;}
if(id==4){HatchType3=HatchType4;}
if(id==5){HatchType4=HatchType5;}
if(id==6){HatchType5=HatchType6;}
if(id==7){HatchType6=HatchType7;}
document.getElementById('thickness'+(id)).value = temp_first_thickness;
document.getElementById('cond_a'+(id)).value = temp_first_cond_a;
document.getElementById('cond_b'+(id)).value = temp_first_cond_b;
document.getElementById('vapor'+(id)).value = temp_first_cond_vapor;
document.getElementById('materials'+(id)).value = temp_first_cond_materials;
document.getElementById('hidd'+(id)).value = temp_first_cond_hidd;
if(id==2){HatchType2=temp_HatchType;}
if(id==3){HatchType3=temp_HatchType;}
if(id==4){HatchType4=temp_HatchType;;}
if(id==5){HatchType5=temp_HatchType;}
if(id==6){HatchType6=temp_HatchType;}
if(id==7){HatchType7=temp_HatchType;}
sendValue1();
}
function move_down(id)
{

id=id.substr(9, 1);
id=parseInt(id);
var temp_first_thickness=document.getElementById('thickness'+(id)).value;
var temp_first_cond_a=document.getElementById('cond_a'+(id)).value;
var temp_first_cond_b=document.getElementById('cond_b'+(id)).value;
var temp_first_cond_vapor=document.getElementById('vapor'+(id)).value;
var temp_first_cond_materials=document.getElementById('materials'+(id)).value;
var temp_first_cond_hidd=document.getElementById('hidd'+(id)).value;

if(id==1){var temp_HatchType=HatchType1;}
if(id==2){var temp_HatchType=HatchType2;}
if(id==3){var temp_HatchType=HatchType3;}
if(id==4){var temp_HatchType=HatchType4;}
if(id==5){var temp_HatchType=HatchType5;}
if(id==6){var temp_HatchType=HatchType6;}
if(id==7){var temp_HatchType=HatchType7;}
document.getElementById('thickness'+(id)).value =document.getElementById('thickness'+(id+1)).value;
document.getElementById('cond_a'+(id)).value = document.getElementById('cond_a'+(id+1)).value;
document.getElementById('cond_b'+(id)).value = document.getElementById('cond_b'+(id+1)).value;
document.getElementById('vapor'+(id)).value = document.getElementById('vapor'+(id+1)).value;
document.getElementById('materials'+(id)).value = document.getElementById('materials'+(id+1)).value;
document.getElementById('hidd'+(id)).value = document.getElementById('hidd'+(id+1)).value;

if(id==1){HatchType1=HatchType2;}
if(id==2){HatchType2=HatchType3;}
if(id==3){HatchType3=HatchType4;}
if(id==4){HatchType4=HatchType5;}
if(id==5){HatchType5=HatchType5;}
if(id==6){HatchType6=HatchType7;}
document.getElementById('thickness'+(id+1)).value = temp_first_thickness;
document.getElementById('cond_a'+(id+1)).value = temp_first_cond_a;
document.getElementById('cond_b'+(id+1)).value = temp_first_cond_b;
document.getElementById('vapor'+(id+1)).value = temp_first_cond_vapor;
document.getElementById('materials'+(id+1)).value = temp_first_cond_materials;
document.getElementById('hidd'+(id+1)).value = temp_first_cond_hidd;
if(id==1){HatchType2=temp_HatchType;}
if(id==2){HatchType3=temp_HatchType;}
if(id==3){HatchType4=temp_HatchType;}
if(id==4){HatchType5=temp_HatchType;}
if(id==5){HatchType6=temp_HatchType;}
if(id==6){HatchType7=temp_HatchType;}

sendValue1();
}






$(document).ready(function(){
				$('#List_of_matirials').change(function(){
					sendValue($(this).val(),$(this).attr("id"));
				});
			});

			function sendValue(str,str4){
				$.post("ajax.php", { sendToValue: str,sendToValue4: str4 },
				function(data){
				    $('#display').html(data.returnFromValue);
				}, "json");
			}
function insert(mat1)
{

document.getElementById('logo1').style.display= 'none';

document.getElementById(mat_id).value=document.getElementById('option_select').options[mat1].text;
id=mat_id.substr(9, 1);
if (id==1){
document.getElementById('thickness1').focus();
}
else if (id==2){
document.getElementById('thickness2').focus();
}
else if (id==3){
document.getElementById('thickness3').focus();
}
else if (id==4){
document.getElementById('thickness4').focus();
}
else if (id==5){
document.getElementById('thickness5').focus();
}
else if (id==6){
document.getElementById('thickness6').focus();
}
else if (id==7){
document.getElementById('thickness7').focus();
}
get_properties(document.getElementById('option_select').options[mat1].text,mat_id);
}

	function lookup(inputString,norma1) {
		if(norma1.checked){norma='snip'}else {norma='sp'};

		if(inputString.length == 0) {
			// Hide the suggestion box.
			$('#suggestions').hide();

		} else {
			$.post("rpc.php", {queryString: ""+inputString+"", queryString2: norma}, function(data){
				if(data.length >0) {
					$('#suggestions').show();
					$('#autoSuggestionsList').html(data);

				}
			});
		}
	} // lookup

	function fill(thisValue) {
		$('#inputString').val(thisValue);
		setTimeout("$('#suggestions').hide();", 200);
		sendValue1();
	}

			function sendValue1()
			{


				var sendToValue1=document.getElementById('thickness1').value/1000;
				var sendToValue2=document.getElementById('thickness2').value/1000;
				var sendToValue3=document.getElementById('thickness3').value/1000;
				var sendToValue4=document.getElementById('thickness4').value/1000;
				var sendToValue5=document.getElementById('thickness5').value/1000;
				var sendToValue6=document.getElementById('thickness6').value/1000;
				var sendToValue7=document.getElementById('thickness7').value/1000;
				var city_o=document.getElementById('inputString').value;
				var tint_o=document.getElementById('tint').value;
				var moisture_o=document.getElementById('moisture').value;
				var odnorodnost_o=document.getElementById('odnorodnost').value;
				var building1=document.getElementById('building');
				var building_o=building1.options[building1.selectedIndex].text;
				var wall1=document.getElementById('wall');
				var wall_o=wall1.options[wall1.selectedIndex].text;
				var option1_o=document.getElementById('option1').checked;
				var option2_o=document.getElementById('option_rosa').checked;
				var option3_o=document.getElementById('option_prirash').checked;
				if(document.getElementById('norma1').checked==true){option4_o='snip'} else {option4_o='sp'};

				var materials1_o=document.getElementById('materials1').value;
				var thickness1_o=document.getElementById('thickness1').value/1000;
				var cond_a1_o=document.getElementById('cond_a1').value;
				var cond_b1_o=document.getElementById('cond_b1').value;
				var vapor1_o=document.getElementById('vapor1').value;
				var dens1_o=document.getElementById('dens1').value;
				var prirash1_o=document.getElementById('prirash1').value;
				var hidden1_o=document.getElementById('hidd1').value;

				var materials2_o=document.getElementById('materials2').value;
				var thickness2_o=document.getElementById('thickness2').value/1000;
				var cond_a2_o=document.getElementById('cond_a2').value;
				var cond_b2_o=document.getElementById('cond_b2').value;
				var vapor2_o=document.getElementById('vapor2').value;
				var dens2_o=document.getElementById('dens2').value;
				var prirash2_o=document.getElementById('prirash2').value;
				var hidden2_o=document.getElementById('hidd2').value;


				var materials3_o=document.getElementById('materials3').value;
				var thickness3_o=document.getElementById('thickness3').value/1000;
				var cond_a3_o=document.getElementById('cond_a3').value;
				var cond_b3_o=document.getElementById('cond_b3').value;
				var vapor3_o=document.getElementById('vapor3').value;
				var dens3_o=document.getElementById('dens3').value;
				var prirash3_o=document.getElementById('prirash3').value;
				var hidden3_o=document.getElementById('hidd3').value;

				var materials4_o=document.getElementById('materials4').value;
				var thickness4_o=document.getElementById('thickness4').value/1000;
				var cond_a4_o=document.getElementById('cond_a4').value;
				var cond_b4_o=document.getElementById('cond_b4').value;
				var vapor4_o=document.getElementById('vapor4').value;
				var dens4_o=document.getElementById('dens4').value;
				var prirash4_o=document.getElementById('prirash4').value;
				var hidden4_o=document.getElementById('hidd4').value;

				var materials5_o=document.getElementById('materials5').value;
				var thickness5_o=document.getElementById('thickness5').value/1000;
				var cond_a5_o=document.getElementById('cond_a5').value;
				var cond_b5_o=document.getElementById('cond_b5').value;
				var vapor5_o=document.getElementById('vapor5').value;
				var dens5_o=document.getElementById('dens5').value;
				var prirash5_o=document.getElementById('prirash5').value;
				var hidden5_o=document.getElementById('hidd5').value;


				var materials6_o=document.getElementById('materials6').value;
				var thickness6_o=document.getElementById('thickness6').value/1000;
				var cond_a6_o=document.getElementById('cond_a6').value;
				var cond_b6_o=document.getElementById('cond_b6').value;
				var vapor6_o=document.getElementById('vapor6').value;
				var dens6_o=document.getElementById('dens6').value;
				var prirash6_o=document.getElementById('prirash6').value;
				var hidden6_o=document.getElementById('hidd6').value;


				var materials7_o=document.getElementById('materials7').value;
				var thickness7_o=document.getElementById('thickness7').value/1000;
				var cond_a7_o=document.getElementById('cond_a7').value;
				var cond_b7_o=document.getElementById('cond_b7').value;
				var vapor7_o=document.getElementById('vapor7').value;
				var dens7_o=document.getElementById('dens7').value;
				var prirash7_o=document.getElementById('prirash7').value;
				var hidden7_o=document.getElementById('hidd7').value;

				if(document.getElementById('option_rosa').checked == true){
										document.getElementById('display1').src = "ajax6.php?sendToValue1="+sendToValue1+"&sendToValue11="+HatchType1
					+"&sendToValue2="+sendToValue2+"&sendToValue22="+HatchType2
					+"&sendToValue3="+sendToValue3+"&sendToValue33="+HatchType3
					+"&sendToValue4="+sendToValue4+"&sendToValue44="+HatchType4
					+"&sendToValue5="+sendToValue5+"&sendToValue55="+HatchType5
				+"&sendToValue6="+sendToValue6+"&sendToValue66="+HatchType6
				+"&sendToValue7="+sendToValue7+"&sendToValue77="+HatchType7
											+"&vapor1="+vapor1_o
											+"&vapor2="+vapor2_o
											+"&vapor3="+vapor3_o
											+"&vapor4="+vapor4_o
											+"&vapor5="+vapor5_o
											+"&vapor6="+vapor6_o
											+"&vapor7="+vapor7_o
											+"&cond_a1="+cond_a1_o
											+"&cond_b1="+cond_b1_o
											+"&cond_a2="+cond_a2_o+"&cond_b2="+cond_b2_o
											+"&cond_a3="+cond_a3_o+"&cond_b3="+cond_b3_o
											+"&cond_a4="+cond_a4_o+"&cond_b4="+cond_b4_o
											+"&cond_a5="+cond_a5_o+"&cond_b5="+cond_b5_o
											+"&cond_a6="+cond_a6_o+"&cond_b6="+cond_b6_o
											+"&cond_a7="+cond_a7_o+"&cond_b7="+cond_b7_o
											+"&moisture="+moisture_o
											+"&tint="+tint_o
											+"&city="+city_o
											+"&odnorodnost="+odnorodnost_o
											+"&wall="+wall_o
											+"&norma="+option4_o;

					}else {
					document.getElementById('display1').src = "ajax2.php?sendToValue1="+sendToValue1+"&sendToValue11="+HatchType1
					+"&sendToValue2="+sendToValue2+"&sendToValue22="+HatchType2
					+"&sendToValue3="+sendToValue3+"&sendToValue33="+HatchType3
					+"&sendToValue4="+sendToValue4+"&sendToValue44="+HatchType4
					+"&sendToValue5="+sendToValue5+"&sendToValue55="+HatchType5
				+"&sendToValue6="+sendToValue6+"&sendToValue66="+HatchType6
				+"&sendToValue7="+sendToValue7+"&sendToValue77="+HatchType7+"&tint="+tint_o+"&city="+city_o+"&norma="+option4_o+"&building="+building_o;
					};

$.post("ajax4.php", {
	city: city_o,
	tint: tint_o,
	moisture: moisture_o,
	wall: wall_o,
	building: building_o,
	option1: option1_o,
	option2: option2_o,
	option3: option3_o,
	option4: option4_o,
	odnorodnost:odnorodnost_o,
materials1: materials1_o,thickness1:thickness1_o,cond_a1:cond_a1_o,cond_b1:cond_b1_o,vapor1:vapor1_o,dens1:dens1_o,prirash1:prirash1_o,h_hatch1:hidden1_o,
materials2: materials2_o,thickness2:thickness2_o,cond_a2:cond_a2_o,cond_b2:cond_b2_o,vapor2:vapor2_o,dens2:dens2_o,prirash2:prirash2_o,h_hatch2:hidden2_o,
materials3: materials3_o,thickness3:thickness3_o,cond_a3:cond_a3_o,cond_b3:cond_b3_o,vapor3:vapor3_o,dens3:dens3_o,prirash3:prirash3_o,h_hatch3:hidden3_o,
materials4: materials4_o,thickness4:thickness4_o,cond_a4:cond_a4_o,cond_b4:cond_b4_o,vapor4:vapor4_o,dens4:dens4_o,prirash4:prirash4_o,h_hatch4:hidden4_o,
materials5: materials5_o,thickness5:thickness5_o,cond_a5:cond_a5_o,cond_b5:cond_b5_o,vapor5:vapor5_o,dens5:dens5_o,prirash5:prirash5_o,h_hatch5:hidden5_o,
materials6: materials6_o,thickness6:thickness6_o,cond_a6:cond_a6_o,cond_b6:cond_b6_o,vapor6:vapor6_o,dens6:dens6_o,prirash6:prirash6_o,h_hatch6:hidden6_o,
materials7: materials7_o,thickness7:thickness7_o,cond_a7:cond_a7_o,cond_b7:cond_b7_o,vapor7:vapor7_o,dens7:dens7_o,prirash7:prirash7_o,h_hatch7:hidden7_o

},function(data){
	$('#info_res').html(data.returnFromValue);
	$('#output').html(data.output);
	}, "json"); }


function get_properties(name_of_material,mat_id){
						id=mat_id.substr(9, 1);
						$.post("ajax3.php", { sendToValue5: name_of_material,sendToValue6: id },
				function(data){

			if (id==1) {
			    $('#display3').html(data.returnFromValue1);
				$('#display4').html(data.returnFromValue2);
				$('#display21').html(data.returnFromValue4);
				HatchType1=data.returnFromValue3;
				dens1=data.returnFromValue5;
				prirash1=data.returnFromValue6;
						document.getElementById("hidd1").value=HatchType1;
						document.getElementById("dens1").value=dens1;
						document.getElementById("prirash1").value=prirash1;
				}
			else if (id==2) {
				    $('#display5').html(data.returnFromValue1);
					 $('#display6').html(data.returnFromValue2);
					 $('#display22').html(data.returnFromValue4);
					 HatchType2=data.returnFromValue3;
					dens2=data.returnFromValue5;
					prirash2=data.returnFromValue6;
						document.getElementById("hidd2").value=HatchType2;
						document.getElementById("dens2").value=dens2;
						document.getElementById("prirash2").value=prirash2;
				}
							else if (id==3) {

				    $('#display7').html(data.returnFromValue1);
					 $('#display8').html(data.returnFromValue2);
					 $('#display23').html(data.returnFromValue4);
					 HatchType3=data.returnFromValue3;
					 dens3=data.returnFromValue5;
				prirash3=data.returnFromValue6;
						document.getElementById("hidd3").value=HatchType3;
						document.getElementById("dens3").value=dens3;
						document.getElementById("prirash3").value=prirash3;
				}
							else if (id==4) {

				    $('#display9').html(data.returnFromValue1);
					 $('#display10').html(data.returnFromValue2);
					 $('#display24').html(data.returnFromValue4);
					 HatchType4=data.returnFromValue3;
									dens4=data.returnFromValue5;
				prirash4=data.returnFromValue6;
						document.getElementById("hidd4").value=HatchType4;
						document.getElementById("dens4").value=dens4;
						document.getElementById("prirash4").value=prirash4;
				}
							else if (id==5) {

				    $('#display11').html(data.returnFromValue1);
					 $('#display12').html(data.returnFromValue2);
					 $('#display25').html(data.returnFromValue4);
					 HatchType5=data.returnFromValue3;
					 				dens5=data.returnFromValue5;
				prirash5=data.returnFromValue6;
						document.getElementById("hidd5").value=HatchType5;
						document.getElementById("dens5").value=dens5;
						document.getElementById("prirash5").value=prirash5;
				}
							else if (id==6) {

				    $('#display13').html(data.returnFromValue1);
					 $('#display14').html(data.returnFromValue2);
					 $('#display26').html(data.returnFromValue4);
					 HatchType6=data.returnFromValue3;
									dens6=data.returnFromValue5;
				prirash6=data.returnFromValue6;
							document.getElementById("hidd6").value=HatchType6;
						document.getElementById("dens6").value=dens6;
						document.getElementById("prirash6").value=prirash6;
				}
											else if (id==7) {

				    $('#display15').html(data.returnFromValue1);
					 $('#display16').html(data.returnFromValue2);
					 $('#display27').html(data.returnFromValue4);
					 HatchType7=data.returnFromValue3;
					 dens7=data.returnFromValue5;
				prirash7=data.returnFromValue6;
						document.getElementById("hidd7").value=HatchType7;
						document.getElementById("dens7").value=dens7;
						document.getElementById("prirash7").value=prirash7;
				}
				}, "json");
			}
</script>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-5710279348857296",
          enable_page_level_ads: true
     });
</script>
</head>
 <body>
 <form method="POST" action='ras4et.php' target="_blank">
<div id="carrier">
<h1 id="header">Теплотехнический расчет онлайн</h1>
<div id="menucarrier" align='center'>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Небоскреб слева -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-5710279348857296"
     data-ad-slot="8127626960"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script><br><br><p style="font-family:arial;color:black;font-size:16px;">Ещё онлайн расчеты:</p><br>
<br><p style="font-family:arial;color:black;font-size:16px;"><a href='beam1/index.php' alt="Расчет балки." title="Расчет балки." >Расчет балки.</a></p>
<br><p style="font-family:arial;color:black;font-size:16px;"><a href='woodbeam/index.php' alt="Расчет балки." title="Расчет балки." >Расчет деревянной балки(экспертиза).</a></p>
<div id="menu">
</div></div>
<div id="adscarrier" align='center'>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- небоскреб справа -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-5710279348857296"
     data-ad-slot="9604360160"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script><br><br><p style="font-family:arial;color:black;font-size:16px;">Ещё онлайн расчеты:</p><br>
<p style="font-family:arial;color:black;font-size:16px;"><a href='heat2/index.php' alt="Расчет теплопотерь и затрат на отопление." title="Расчет теплопотерь и затрат на отопление." >Расчет теплопотерь.</a></p><br>
<p style="font-family:arial;color:black;font-size:16px;"><a href='heat1/index.php' alt="Расчет стеклопакета" title="Расчет стеклопакета" >Расчет стеклопакета.</a></p>
<br>
<p style="font-family:arial;color:black;font-size:16px;"><a href='ground1/index.php' alt="Глубина промерзания грунта." title="Глубина промерзания грунта." >Глубина промерзания грунта.</a></p>

</div>
<div id="menu1">       <p align='center'><a href='index.php'><font color='#FFFFFF' face='Verdana' size='2'>Главная</font></a><font color='#FFFFFF' face='Verdana' size='2'> | </font><a href='rasch.php'><font color='#FFFFFF' face='Verdana' size='2'>Все расчеты</font></a><font color='#FFFFFF' face='Verdana' size='2'>   | </font><a href='sortament/index.php'><font color='#FFFFFF' face='Verdana' size='2'>Сортамент</font></a><font color='#FFFFFF' face='Verdana' size='2'>   | </font><a href='mats.php'><font color='#FFFFFF' face='Verdana' size='2'>Материалы</font></a><font color='#FFFFFF' face='Verdana' size='2'>   | </font><a href='text.php'><font color='#FFFFFF' face='Verdana' size='2'> Статьи</font></a><font color='#FFFFFF' face='Verdana' size='2'>       | </font><a href='email.php'><font color='#FFFFFF' face='Verdana' size='2'> Контакты</font></a></p></div>
<input type="hidden" id="hidd1" value=0 name='hidden1' />
<input type="hidden" id="hidd2" value=0 name='hidden2' />
<input type="hidden" id="hidd3" value=0 name='hidden3' />
<input type="hidden" id="hidd4" value=0 name='hidden4' />
<input type="hidden" id="hidd5" value=0 name='hidden5' />
<input type="hidden" id="hidd6" value=0 name='hidden6' />
<input type="hidden" id="hidd7" value=0 name='hidden7' />
<input type="hidden" id="dens1" value=0 name='dens1' />
<input type="hidden" id="dens2" value=0 name='dens2' />
<input type="hidden" id="dens3" value=0 name='dens3' />
<input type="hidden" id="dens4" value=0 name='dens4' />
<input type="hidden" id="dens5" value=0 name='dens5' />
<input type="hidden" id="dens6" value=0 name='dens6' />
<input type="hidden" id="dens7" value=0 name='dens7' />
<input type="hidden" id="prirash1" value=0 name='prirash1' />
<input type="hidden" id="prirash2" value=0 name='prirash2' />
<input type="hidden" id="prirash3" value=0 name='prirash3' />
<input type="hidden" id="prirash4" value=0 name='prirash4' />
<input type="hidden" id="prirash5" value=0 name='prirash5' />
<input type="hidden" id="prirash6" value=0 name='prirash6' />
<input type="hidden" id="prirash7" value=0 name='prirash7' />
<div id="text">
<div id='logo1' style='display:none'>
<table width="180px">
<tr >
<td>
<select id='List_of_matirials' size='22' style="width:280px";>

<option>Бетоны и растворы</option><option>Бетоны на пористых заполнителях</option><option>Бетоны ячеистые</option><option>Вспенененный синтетический каучук</option><option>Дерево и изделия из него</option><option>Засыпки</option><option>Кладка из пустотного кирпича</option><option>Кладка из сплошного кирпича</option><option>Материалы гидроизоляционные</option><option>Материалы облицовочные </option><option>Материалы рулонные</option><option>Металлы и стекло</option><option>Минераловатные</option><option>Невентилируемая воздушная прослойка</option><option>Облицовка природным камнем </option><option>Пенопласт</option><option>Пенополистирол</option><option>Пенополиуретан</option><option>Пеностекло,газостекло</option><option>Перлитопластбетон</option><option>Перлитофосфогелевые изделия</option><option>Плиты из природных материалов</option><option>Строительные растворы</option><option>Экструдированный пенополистирол </option></select>
</td>
<td><div id="display">
<select id='option_select' style="width:480px;" name='List of matirials2' size='22' ></select>
</div>
</td>
</tr>
<tr><td align ='center' height='60' colspan="2"><button type='button'  onclick="hide_logo1()" >Отмена</button></td></tr>
</table>

</div>
<div id='logo2' style="display:none" >
<table>
<tr>
<td colspan=2 align='center' >Укажите характеристики материала</td>
</tr>
<tr>
<td >Название материала</td>
<td ><input type="text" name="materials_temp" size="75" value="" id="materials_temp" ></td>
</tr>
<tr><td >Предельно допустимое приращение расчетного массового отношения <br>влаги в материале(для теплоизоляционных материалов) &#916 <i>w<sub>av</sub></i>,%</td>
<td ><input type="text" name="prirash_temp" size="2" id="prirash_temp" value="" ></td>
</tr>
<tr><td>Сопротивление &lambda;<sub>А</sub>Вт/(м°С)</td>
<td><input type="text" name="cond_a_temp" size="2" id="cond_a_temp" value="" ></td></tr>
<tr><td>Сопротивление &lambda;<sub>Б</sub>Вт/(м°С)</td>
<td><input type="text" name="cond_b_temp" size="2" id="cond_b_temp" value="" ></td>
</tr>
<tr><td>Паропроницаемость &mu;мг/(м&middot;ч&middot;Па)</td>

<td><input type="text" name="vapor_temp" size="2" id="vapor_temp" value="" ></td></tr>
<tr><td>Плотность кг/м.куб(для теплоизоляционных материалов) </td>

<td ><input type="text" name="dens_temp" size="2" id="dens_temp" value="" ></td>
</tr>
<tr><td>Тип штриховки</td><td>
<select id="hatch_temp" name="hatch_temp" ">
<option selected="selected">Теплоизоляционные материалы</option>
<option>Бетон</option>
<option>Дерево</option>
<option>Кирпичная кладка</option>
<option>Металлы</option>
<option>Растворы</option>
<option>Гидроизоляционные материалы</option>
</select></td></tr>
<tr>
<td colspan=2 align=center><BR><input type="button" value="&#160&#160&#160Ок&#160&#160&#160" onclick="input()" />&#160&#160&#160&#160&#160&#160&#160<input type="button" value="Отмена" onclick="hide_mat()" />&#160&#160&#160&#160&#160&#160&#160<input type="button" value="Очистить" onclick="clear_all()" /><BR>&#160</td></tr>

</table>
</div>


<div>
<P>Расчет выполнить согласно:
<P><input type="radio" id="norma1" name="norma" value = "snip" onchange="sendValue1()"><label for="norma1">СНиП 23-02-2003 и СНиП 23-01-99*</label></>
<P><input type="radio" id="norma2" name="norma" value = "sp" checked onchange="sendValue1()"><label for="norma2">СП 50.13330.2012 и СП 131.13330.2018 (действует с 1 августа 2020г.)</label></>

			<div>
				<P>Населенный пункт: (автозаполнение)
				<br>
				<input type="text"  size="40" autocomplete="off" name="city" value="Москва" id="inputString" onkeyup="lookup(this.value, document.getElementById('norma1'));" onfocus="if(this.value == 'Москва') { this.value = ''; }"  onblur="fill();" />
			</div>

			<div class="suggestionsBox" id="suggestions" style="display: none;" >
				<img src="upArrow.png" style="position: relative; top: -12px; left: 30px;" alt="upArrow" />
				<div class="suggestionList" id="autoSuggestionsList">
					&nbsp;
				</div>
			</div>

	</div>




<p>Тип зданий и помещений</p>
<select id="building" name="building" onchange="sendValue1();">
<option selected="selected">Жилые.</option>
<option>Лечебно-профилактические и детские учреждения, школы, интернаты.</option>
<option>Общественные, кроме жилых, лечебно-профилактических и детских учреждений, школ, интернатов.</option>
<option>Административные и бытовые.</option>
<option>Производственные.</option>
<option>Производственные здания со значительными избытками явной теплоты.</option>
</select>

<p> Вид ограждающей конструкции</p>
<select id="wall" name="wall" onchange="sendValue1();">
<option selected="selected">Наружные стены.</option>
<option>Наружные стены с вентилируемым фасадом.</option>
<option>Перекрытия над проездами.</option>
<option>Покрытия.</option>
<option>Перекрытия чердачные (с кровлей из штучных материалов).</option>
<option>Перекрытия чердачные (с кровлей из рулонных материалов).</option>
<option>Перекрытия над неотапливаемыми подвалами со световыми проемами в стенах.</option>
<option>Перекрытия над неотапливаемыми подвалами без световых проемов в стенах, расположенные выше уровня земли.</option>
<option>Перекрытия над холодными подвалами, сообщающимися с наружным воздухом.</option>
<option>Перекрытия над неотапливаемыми подпольями,расположенных ниже уровня земли.</option>
<option>Перекрытия над холодными (с ограждающими стенками) подпольями.</option>
<option>Перекрытия над холодными (без ограждающих стенок) подпольями.</option>


</select>
<p>Расчетная средняя температура внутреннего воздуха здания &#176C[<a href='moist_temp.php' target="_blank">?</a>]<input type="text" name="tint" size="2"  value="20" id="tint" onchange="sendValue1();">
<p>Относительная влажность внутреннего воздуха &#966<sub>int</sub> &#037;[<a href='moist_temp.php' target="_blank">?</a>]<input type="text" name="moisture" size="2"  value="55" id="moisture" onchange="sendValue1();">
<p>Коэффициент теплотехнической однородности <i>r </i>[<a href='text_1.php' target="_blank">?</a>] <input type="text" name="odnorodnost" size="2" value="0.92" id="odnorodnost" onchange="sendValue1();">
<P>Опции расчета:</p>
<P><input type="checkbox"  name="option1" id="option1" value="a1" onclick="sendValue1();"/><label for="option1">Выполнен расчет по нормируемому удельному показателю расхода тепловой энергии</label>[<a href='text_4.php' target="_blank">?</a>]</p>

<P><input type="checkbox"  name="option_prirash" id="option_prirash" value="a2" onclick="sendValue1();"/><label for="option_prirash">Расчет сопротивления паропроницанию</label></p>
<P><input type="checkbox"  name="option_rosa" id="option_rosa" value="a3" onclick="sendValue1();"/><label for="option_rosa">Расчет точки росы</label></p>

<table>
<tr>
<td>№</td>
<td>Название материала(от наружного слоя к внутреннему)</td>
<td >&delta;,мм</td>
<td >&lambda;<sub>А</sub> Вт/(м°С)</td>
<td >&lambda;<sub>Б</sub> Вт/(м°С)</td>

<td >&mu;мг/ (м&middot;ч&middot;Па)</td>

<td></td><td></td><td></td>



</tr>
<tr>
<td>1</td>
<td><input type="text" name="materials1" size="75" value="Выбрать" id="materials1" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness1" autocomplete="off" size="2" value="" id="thickness1"  onkeyup="sendValue1();"></td>
<td align="center"><div id="display3"><input type="text" name="cond_a1" size="2" id="cond_a1" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display4"><input type="text" name="cond_b1" size="2" value="" id="cond_b1" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display21"><input type="text" name="vapor1" size="2" value="" id="vapor1" onkeyup="sendValue1();"></div></td>
<td ><input type="button" value="DEL" onclick="clear1()" /></td>
<td width=4 valign="bottom"><input type="image" src="DOWN.png" onclick="move_down(this.id); return false;" name="button_up" id="move_down1"value="move_down1"  class="button_up"/></td>
<td><input type="button" value="&#160+&#160" id="add_materials1" onclick="add(this.id)" ></td>
</tr>

<tr>
<td>2</td>
<td><input type="text" name="materials2" size="75" value="Выбрать" id="materials2" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness2" autocomplete="off" size="2" value="" id="thickness2" onkeyup="sendValue1();"></td>
<td align="center"><div id="display5"><input type="text" name="cond_a2" size="2" id="cond_a2" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display6"><input type="text" name="cond_b2" size="2" value="" id="cond_b2" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display22"><input type="text" name="vapor2" size="2" value="" id="vapor2" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear2()" /></td>
<td width=4>
<input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up2" value="move_up2" />
<input type="image" src="DOWN.png" onclick="move_down(this.id); return false;" name="button_down" id="move_down2" value="move_down2" /></td>
<td><input type="button" value="&#160+&#160" id="add_materials2" onclick="add(this.id)" ></td>
</tr>
<tr>
<td>3</td>
<td><input type="text" name="materials3" size="75" value="Выбрать" id="materials3" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness3" autocomplete="off" size="2" value="" id="thickness3" onkeyup="sendValue1();"></td>
<td align="center"><div id="display7"><input type="text" name="cond_a3" size="2" id="cond_a3" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display8"><input type="text" name="cond_b3" size="2" value="" id="cond_b3" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display23"><input type="text" name="vapor3" size="2" value="" id="vapor3" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear3()" /></td>
<td width=4 ><input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up3" value="move_up3" /><input type="image" src="DOWN.png" onclick="move_down(this.id); return false;" name="button_up" id="move_down3" value="move_down3" /></td>
<td><input type="button" value="&#160+&#160" id="add_materials3" onclick="add(this.id)" ></td>
</tr>
<tr>
<td>4</td>
<td><input type="text" name="materials4" size="75" value="Выбрать" id="materials4" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness4"autocomplete="off" size="2" value="" id="thickness4" onkeyup="sendValue1();"></td>
<td align="center"><div id="display9"><input type="text" name="cond_a4" size="2" id="cond_a4" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display10"><input type="text"  name="cond_b4" size="2" value="" id="cond_b4" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display24"><input type="text" name="vapor4" size="2" value="" id="vapor4" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear4()" /></td>
<td width=4 ><input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up4" value="move_up4" /><input type="image" src="DOWN.png" onclick="move_down(this.id); return false;" name="button_up" id="move_down4"value="move_down4"  class="button_up"/></td>
<td><input type="button" value="&#160+&#160" id="add_materials4" onclick="add(this.id)" ></td>
</tr>
<tr>
<td>5</td>
<td><input type="text" name="materials5" size="75" value="Выбрать" id="materials5" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness5" autocomplete="off" size="2" value="" id="thickness5" onkeyup="sendValue1();"></td>
<td align="center"><div id="display11"><input type="text" name="cond_a5" size="2" id="cond_a5" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display12"><input type="text" name="cond_b5" size="2" value="" id="cond_b5" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display25"><input type="text" name="vapor5" size="2" value="" id="vapor5" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear5()" /></td>
<td width=4 ><input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up5" value="move_up5" /><input type="image" src="DOWN.png"  onclick="move_down(this.id); return false;"  name="button_up" id="move_down5"value="move_down5"  class="button_up"/></td>
<td><input type="button" value="&#160+&#160" id="add_materials5" onclick="add(this.id)" ></td>
</tr>
<tr>
<td>6</td>
<td><input type="text" name="materials6" size="75" value="Выбрать" id="materials6" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness6" autocomplete="off" size="2" value="" id="thickness6" onkeyup="sendValue1();"></td>
<td align="center"><div id="display13"><input type="text" name="cond_a6" size="2" id="cond_a6" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display14"><input type="text" name="cond_b6" size="2" value="" id="cond_b6" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display26"><input type="text" name="vapor6" size="2" value="" id="vapor6" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear6()" /></td>
<td width=4 ><input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up6" value="move_up6" /><input type="image" src="DOWN.png" onclick="move_down(this.id); return false;" name="button_up" id="move_down6"value="move_down6"  class="button_up"/></td>
<td><input type="button" value="&#160+&#160" id="add_materials6" onclick="add(this.id)" ></td>
</tr>
<tr>
<td>7</td>
<td><input type="text" name="materials7" size="75" value="Выбрать" id="materials7" onfocus="select_mat(this.id)"></td>
<td><input type="text" name="thickness7" autocomplete="off" size="2" value="" id="thickness7" onkeyup="sendValue1();"></td>
<td align="center"><div id="display15"><input type="text" name="cond_a7" size="2" id="cond_a7" value="" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display16"><input type="text" name="cond_b7" size="2" value="" id="cond_b7" onkeyup="sendValue1();"></div></td>
<td align="center"><div id="display27"><input type="text" name="vapor7" size="2" value="" id="vapor7" onkeyup="sendValue1();"></div></td>

<td ><input type="button" value="DEL" onclick="clear7()" /></td>

<td width=4 valign="top"><input type="image" src="UP.png" onclick="move_up(this.id); return false;" name="button_up" id="move_up7" value="move_up7" /></td>

<td><input type="button" value="&#160+&#160" id="add_materials7" onclick="add(this.id)" ></td>
</tr>
</table>
<br>
<div id="info_res"><B>Укажите конструкцию ограждения</B></div>
<br>
<div id="content">
<div id="pict" ><img id="display1" align="middle" src="GetPic.png"  width='450' height='360'></div>
<div id="output"></div>
</div>
<div  align="center"><input  type=submit value="Отчет" name="B1"></div>
<br>
<div align="center"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
 <!--гор центр -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-5710279348857296"
     data-ad-slot="3281086162"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
<br>

</form></div>
</div>
<div id="footer" >
<!--LiveInternet counter--><script type="text/javascript"><!--
document.write("<a href='http://www.liveinternet.ru/click' "+
"target=_blank><img src='//counter.yadro.ru/hit?t12.10;r"+
escape(document.referrer)+((typeof(screen)=="undefined")?"":
";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
";"+Math.random()+
"' alt='' title='LiveInternet: показано число просмотров за 24"+
" часа, посетителей за 24 часа и за сегодня' "+
"border='0' width='88' height='31'><\/a>")
//--></script><!--/LiveInternet-->




<!-- Yandex.Metrika informer -->
<a href="https://metrika.yandex.ru/stat/?id=25845446&amp;from=informer"
target="_blank" rel="nofollow"><img src="//bs.yandex.ru/informer/25845446/3_1_FFFFFFFF_EFEFEFFF_0_pageviews"
style="width:88px; height:31px; border:0;" alt="Яндекс.Метрика" title="Яндекс.Метрика: данные за сегодня (просмотры, визиты и уникальные посетители)" onclick="try{Ya.Metrika.informer({i:this,id:25845446,lang:'ru'});return false}catch(e){}"/></a>
<!-- /Yandex.Metrika informer -->

<!-- Yandex.Metrika counter -->
<script type="text/javascript">
(function (d, w, c) {
    (w[c] = w[c] || []).push(function() {
        try {
            w.yaCounter25845446 = new Ya.Metrika({id:25845446,
                    webvisor:true,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true});
        } catch(e) { }
    });

    var n = d.getElementsByTagName("script")[0],
        s = d.createElement("script"),
        f = function () { n.parentNode.insertBefore(s, n); };
    s.type = "text/javascript";
    s.async = true;
    s.src = (d.location.protocol == "https:" ? "https:" : "http:") + "//mc.yandex.ru/metrika/watch.js";

    if (w.opera == "[object Opera]") {
        d.addEventListener("DOMContentLoaded", f, false);
    } else { f(); }
})(document, window, "yandex_metrika_callbacks");
</script>
<noscript><div><img src="//mc.yandex.ru/watch/25845446" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->

</div>

</div>


</body>
</html>
"""
# res = requests.get('http://rascheta.net/')
# soup = bs4.BeautifulSoup(res.text, features='html.parser')
soup = bs4.BeautifulSoup(text, features='html.parser')

scripts = soup.find_all('script')
selects = soup.find_all('select')

mat_cat_select = selects[0]
mat_cat_opts = mat_cat_select.find_all('option')

# ['Бетоны и растворы', 'Бетоны на пористых заполнителях', 'Бетоны ячеистые', 'Вспенененный синтетический каучук', 'Дерево и изделия из него', 'Засыпки', 'Кладка из пустотного кирпича', 'Кладка из сплошного кирпича', 'Материалы гидроизоляционные', 'Материалы облицовочные ', 'Материалы рулонные', 'Металлы и стекло', 'Минераловатные', 'Невентилируемая воздушная прослойка', 'Облицовка природным камнем ', 'Пенопласт', 'Пенополистирол', 'Пенополиуретан', 'Пеностекло,газостекло', 'Перлитопластбетон', 'Перлитофосфогелевые изделия', 'Плиты из природных материалов', 'Строительные растворы', 'Экструдированный пенополистирол ']
mat_cats = [o.text for o in mat_cat_opts]

materials = dict()
for mc in mat_cats:
    form_data = {
        'sendToValue': f'{mc}',
        'sendToValue4': 'List_of_matirials'   # intended, typo in ajax expected data
    }
    print('send', mc)
    res = requests.post('http://rascheta.net/ajax.php', data=form_data).json()
    mat_soup = bs4.BeautifulSoup(res['returnFromValue'], features='html.parser')
    mat_opts = mat_soup.find_all('option')

    time.sleep(1)
    mats = [o.text for o in mat_opts]
    mat_params = []
    for mat in mats:
        res = requests.post('http://rascheta.net/ajax3.php', data={
            'sendToValue5': f'{mat}',
            'sendToValue6': '1'
        }).json()
        param_soup = bs4.BeautifulSoup(
            res['returnFromValue1'] +
            res['returnFromValue2'] +
            res['returnFromValue4'],
            features='html.parser'
        ).find_all('input')
        params = [i.attrs['value'] for i in param_soup]
        mat_params += [[mat] + params]

        time.sleep(1)

    materials[mc] = mat_params
    print('receive', mat_params)
    time.sleep(1)

print(materials)
with open('../materials.txt', mode='wt', encoding='utf-8') as f:
    f.write(str(materials))
