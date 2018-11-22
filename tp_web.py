import site
from tp import term_project
import cgi

print("""
Content-Type: text/html

<!DOCTYPE html>
<html>
<head>
<style>
body {
    background-color: linen;
    color: Black;
    font-size: 22px;
    font-family:‘Gill Sans’, ‘Lucida Grande’, ‘Lucida Sans Unicode’, Verdana, Helvetica, Arial, sans-serif;
}
img {
    padding: 0;
    display: block;
    margin: 0 auto;
    max-height: 100%;
    max-width: 100%;
}
h1 {
    color: maroon;
    margin-left: 40px;
} 
htext{
  position: absolute;
  top: 20px;
  left: 100px;
  font-size: 60px;
  font-family: 'Raleway',sans-serif;
  font-weight: 800;
  color: #ffffff;
}
htext1{
  position: absolute;
  top: 90px;
  left: 400px;
  font-size: 30px;
  font-family: 'Raleway',sans-serif;
  font-weight: 800;
  color: #ffffff;
}
htext2{
  position: absolute;
  top: 120px;
  left: 300px;
  font-size: 30px;
  font-family: 'Raleway',sans-serif;
  font-weight: 800;
  color: #ffffff;
}
.container {
  width: 700px;
  height: 500px;
  margin-top: 0px;
  float: left;
}
.container1 {
  width: 900px;
  height: 640px;
  float: left;
  font-size: 15px;
}
.a1{
  position: absolute;
  top: 440px;
  left: 40px;
  color: green;
}
.b1{
  position: absolute;
  top: 340px;
  left: 110px;
  color: green;
}
.c1{
  position: absolute;
  top: 440px;
  left: 115px;
  color: green;
}
.sa1{
  position: absolute;
  top: 390px;
  left: 138px;
  color:blue;
}
.sb1{
  position: absolute;
  top: 452px;
  left: 80px;
  color:blue;
}
.sc1{
  position: absolute;
  top: 380px;
  left: 70px;
  color:blue;
}
.a2{
  position: absolute;
  top: 110px;
  left: 117px;
  color: green;
}
.b2{
  position: absolute;
  top: 163px;
  left: 193px;
  color: green;
}
.c2{
  position: absolute;
  top: 250px;
  left: 133px;
  color: green;
}
.sa2{
  position: absolute;
  top: 230px;
  left: 180px;
  color:blue;
}
.sb2{
  position: absolute;
  top: 175px;
  left: 110px;
  color:blue;
}
.sc2{
  position: absolute;
  top: 125px;
  left: 175px;
  color:blue;
}
.a3{
  position: absolute;
  top: 157px;
  left: 247px;
  color: green;
}
.b3{
  position: absolute;
  top: 110px;
  left: 280px;
  color: green;
}
.c3{
  position: absolute;
  top: 250px;
  left: 390px;
  color: green;
}
.sa3{
  position: absolute;
  top: 170px;
  left: 360px;
  color:blue;
}
.sb3{
  position: absolute;
  top: 220px;
  left: 320px;
  color:blue;
}
.sc3{
  position: absolute;
  top: 120px;
  left: 250px;
  color:blue;
}
.a4{
  position: absolute;
  top: 440px;
  left: 358px;
  color: green;
}
.b4{
  position: absolute;
  top: 340px;
  left: 452px;
  color: green;
}
.c4{
  position: absolute;
  top: 440px;
  left: 520px;
  color: green;
}
.sa4{
  position: absolute;
  top: 380px;
  left: 515px;
  color:blue;
}
.sb4{
  position: absolute;
  top: 452px;
  left: 452px;
  color:blue;
}
.sc4{
  position: absolute;
  top: 380px;
  left: 397px;
  color:blue;
}
.a5{
  position: absolute;
  top: 463px;
  left: 163px;
  color: green;
}
.b5{
  position: absolute;
  top: 463px;
  left: 280px;
  color: green;
}
.c5{
  position: absolute;
  top: 570px;
  left: 173px;
  color: green;
}
.sa5{
  position: absolute;
  top: 520px;
  left: 250px;
  color:blue;
}
.sb5{
  position: absolute;
  top: 520px;
  left: 150px;
  color:blue;
}
.sc5{
  position: absolute;
  top: 453px;
  left: 220px;
  color:blue;
}
.b6{
  position: absolute;
  top: 315px;
  left: 420px;
  color: green;
}
.sa6{
  position: absolute;
  top: 195px;
  left: 600px;
  color:blue;
}
.sb6{
  position: absolute;
  top: 150px;
  left: 520px;
  color:blue;
}
.sc6{
  position: absolute;
  top: 85px;
  left: 590px;
  color:blue;
}
.sa7{
  position: absolute;
  top: 270px;
  left: 790px;
  color:blue;
}
.sb7{
  position: absolute;
  top: 365px;
  left: 715px;
  color:blue;
}
.sc7{
  position: absolute;
  top: 270px;
  left: 640px;
  color:blue;
}
.v1{
  position: absolute;
  top: 465px;
  left: 10px;
  color:orange;
}
.v2{
  position: absolute;
  top: 290px;
  left: 90px;
  color:orange;
}
.v3{
  position: absolute;
  top: 70px;
  left: 65px;
  color:orange;
}
.v4{
  position: absolute;
  top: 135px;
  left: 210px;
  color:orange;
}
.v5{
  position: absolute;
  top: 65px;
  left: 277px;
  color:orange;
}
.v6{
  position: absolute;
  top: 310px;
  left: 485px;
  color:orange;
}
.v7{
  position: absolute;
  top: 455px;
  left: 585px;
  color:orange;
}
.v8{
  position: absolute;
  top: 465px;
  left: 330px;
  color:orange;
}
.v9{
  position: absolute;
  top: 600px;
  left: 120px;
  color:orange;
}
.v10{
  position: absolute;
  top: 465px;
  left: 110px;
  color:orange;
}
.d1{
  position: absolute;
  top: 190px;
  left: 230px;
  color:green;
}
.d3{
  position: absolute;
  top: 440px;
  left: 300px;
  color:green;
}
.d4{
  position: absolute;
  top: 440px;
  left: 165px;
  color:green;
}
.d5{
  position: absolute;
  top: 300px;
  left: 145px;
  color:green;
}
 * {
    box-sizing: border-box;
  }
  .myForm {
    display: grid;
    grid-template-areas: 
      "customer taxi"
      "customer extras"
      "pickup dropoff"
      "instructions instructions"
      "submit submit";
    grid-template-columns: auto auto auto auto auto auto;  
    grid-template-rows: auto auto auto auto auto auto auto auto;
    grid-gap: 0px 0px;
    background: #eee;
    padding: 0.5em;
  }
  .myForm textarea {
    height: calc(50% - 1.2em);
    }
  .myForm button {
    background: gray;
    color: white;
    padding: 1em;
    }
  .myForm input:not([type=radio]):not([type=checkbox]), 
  .myForm textarea, 
  .myForm select {
    height: 30px;
      width: 70px;
    border: 0;
    padding: 0.5em;
    margin: 0 0;
  }
  .myForm label {
   display: block; 
  }
  fieldset {
    border: 0;
    font-size: 16px;
    font-family:‘Gill Sans’, ‘Lucida Grande’, ‘Lucida Sans Unicode’, Verdana, Helvetica, Arial, sans-serif;
  }
  .fieldset_angle {
    border: 0;
    color: green;
  }
  .fieldset_side {
    border: 0;
    color: blue;
  }
  .fieldset_vert {
    border: 0;
    color: orange;
  }

input[type="text"]{

  background-color : #FFFFCC; 
  border:4px solid #FF0000;

}

  #a1 {
    grid-area: a1;
  }
  #b1 {
    grid-area: b1;
  }
  #c1 {
    grid-area: c1;
  }
  #pickup {
    grid-area: pickup;
  }
  #dropoff {
    grid-area: dropoff;
  }
  #instructions {
    grid-area: instructions;
  }
  #submit {
    grid-area: submit;
  }
 .container1 {
    position: relative;
    font-family:‘Gill Sans’, ‘Lucida Grande’, ‘Lucida Sans Unicode’, Verdana, Helvetica, Arial, sans-serif;
}

.grid-container {
  display: grid;
  grid-template-columns: 170px 170px;
  grid-gap: 10px;
  background-color: #F8C471;
  padding: 10px;
  margin-top: 10px;
  float: left;
}
.grid-container > div {
  background-color: #F9E79F;
  text-align: center;
  font-size: 20px;
  color:rgb(140,98,56);
}
</style>
</head>
<body>
<header>
  <img class="w3-image" src="http://localhost:8080/images/header4.png" alt="Architecture" style="width:1500px">
  <htext>
  <h>Term Project</h>
  </htext>
  <htext1><h>EECS 118</h></htext1>
  <htext2><h>Haosong(Kyle) Li</h></htext2>
</header>
<br><br><br>
<p>Note: Tick P1, P2, P3 to set parallel lines. Vertices are in the form of [x,y]. Angles are in degrees.</p>
    <div class="container" align="left">
      <div id="image">
        <img src="http://localhost:8080/images/tp6.jpg" style="width:690px;">
      </div>
    </div>

    <form class="myForm">
        <fieldset class=fieldset_angle id="customer">a1: &nbsp <input type="text" name="a1" ></fieldset>
        <fieldset class=fieldset_angle id="customer">b1: &nbsp <input type="text" name="b1" ></fieldset>
        <fieldset class=fieldset_angle id="customer">c1: &nbsp <input type="text" name="c1" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa1: &nbsp <input type="text" name="sa1"></fieldset>
        <fieldset class=fieldset_side id="customer">sb1: &nbsp <input type="text" name="sb1"></fieldset>
        <fieldset class=fieldset_side id="customer">sc1: &nbsp <input type="text" name="sc1"></fieldset>
        <fieldset class=fieldset_angle id="customer">a2: &nbsp <input type="text" name="a2" ></fieldset>
        <fieldset class=fieldset_angle id="customer">b2: &nbsp <input type="text" name="b2" ></fieldset>
        <fieldset class=fieldset_angle id="customer">c2: &nbsp <input type="text" name="c2" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa2: &nbsp <input type="text" name="sa2"></fieldset>
        <fieldset class=fieldset_side id="customer">sb2: &nbsp <input type="text" name="sb2"></fieldset>
        <fieldset class=fieldset_side id="customer">sc2: &nbsp <input type="text" name="sc2"></fieldset>
        <fieldset class=fieldset_angle id="customer">a3: &nbsp <input type="text" name="a3" ></fieldset>
        <fieldset class=fieldset_angle id="customer">b3: &nbsp <input type="text" name="b3" ></fieldset>
        <fieldset class=fieldset_angle id="customer">c3: &nbsp <input type="text" name="c3" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa3: &nbsp <input type="text" name="sa3"></fieldset>
        <fieldset class=fieldset_side id="customer">sb3: &nbsp <input type="text" name="sb3"></fieldset>
        <fieldset class=fieldset_side id="customer">sc3: &nbsp <input type="text" name="sc3"></fieldset>
        <fieldset class=fieldset_angle id="customer">a4: &nbsp <input type="text" name="a4" ></fieldset>
        <fieldset class=fieldset_angle id="customer">b4: &nbsp <input type="text" name="b4" ></fieldset>
        <fieldset class=fieldset_angle id="customer">c4: &nbsp <input type="text" name="c4" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa4: &nbsp <input type="text" name="sa4"></fieldset>
        <fieldset class=fieldset_side id="customer">sb4: &nbsp <input type="text" name="sb4"></fieldset>
        <fieldset class=fieldset_side id="customer">sc4: &nbsp <input type="text" name="sc4"></fieldset>
        <fieldset class=fieldset_angle id="customer">a5: &nbsp <input type="text" name="a5" ></fieldset>
        <fieldset class=fieldset_angle id="customer">b5: &nbsp <input type="text" name="b5" ></fieldset>
        <fieldset class=fieldset_angle id="customer">c5: &nbsp <input type="text" name="c5" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa5: &nbsp <input type="text" name="sa5"></fieldset>
        <fieldset class=fieldset_side id="customer">sb5: &nbsp <input type="text" name="sb5"></fieldset>
        <fieldset class=fieldset_side id="customer">sc5: &nbsp <input type="text" name="sc5"></fieldset>
        <fieldset class=fieldset_angle id="customer">b6: &nbsp <input type="text" name="b6" ></fieldset>
        <fieldset class=fieldset_side id="customer">sa6: &nbsp <input type="text" name="sa6"></fieldset>
        <fieldset class=fieldset_side id="customer">sb6: &nbsp <input type="text" name="sb6"></fieldset>
        <fieldset class=fieldset_side id="customer">sc6: &nbsp <input type="text" name="sc6"></fieldset>
        <fieldset class=fieldset_side id="customer">sa7: &nbsp <input type="text" name="sa7"></fieldset>
        <fieldset class=fieldset_side id="customer">sb7: &nbsp <input type="text" name="sb7"></fieldset>
        <fieldset class=fieldset_side id="customer">sc7: &nbsp <input type="text" name="sc7"></fieldset>
        <fieldset class=fieldset_angle id="customer">d1: &nbsp <input type="text" name="d1" ></fieldset>
        <fieldset class=fieldset_angle id="customer">d3: &nbsp <input type="text" name="d3" ></fieldset>
        <fieldset class=fieldset_angle id="customer">d4: &nbsp <input type="text" name="d4" ></fieldset>
        <fieldset class=fieldset_angle id="customer">d5: &nbsp <input type="text" name="d5" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v1: &nbsp <input type="text" name="v1" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v2: &nbsp <input type="text" name="v2" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v3: &nbsp <input type="text" name="v3" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v4: &nbsp <input type="text" name="v4" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v5: &nbsp <input type="text" name="v5" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v6: &nbsp <input type="text" name="v6" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v7: &nbsp <input type="text" name="v7" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v8: &nbsp <input type="text" name="v8" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v9: &nbsp <input type="text" name="v9" ></fieldset>
        <fieldset class=fieldset_vert id="customer">v10: &nbsp <input type="text" name="v10" ></fieldset>
        <fieldset id="customer"><input type="checkbox" name="p1" value="True">P1</fieldset>
        <fieldset id="customer"><input type="checkbox" name="p2" value="True">P2</fieldset>
        <fieldset id="customer"><input type="checkbox" name="p3" value="True">P3</fieldset>
        <fieldset id="customer"><input value="Submit" type="submit"></div></fieldset>
    </form>
<br><br>
<p>Solvable parameters are labeled on the figure: &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
&nbsp&nbsp&nbsp&nbsp&nbsp&nbspHeight, area, and total steps:</p>
""")
form = cgi.FieldStorage()
a1=form.getfirst("a1")
b1=form.getfirst("b1")
c1=form.getfirst("c1")
sa1=form.getfirst("sa1")
sb1=form.getfirst("sb1")
sc1=form.getfirst("sc1")
a2=form.getfirst("a2")
b2=form.getfirst("b2")
c2=form.getfirst("c2")
sa2=form.getfirst("sa2")
sb2=form.getfirst("sb2")
sc2=form.getfirst("sc2")
a3=form.getfirst("a3")
b3=form.getfirst("b3")
c3=form.getfirst("c3")
sa3=form.getfirst("sa3")
sb3=form.getfirst("sb3")
sc3=form.getfirst("sc3")
a4=form.getfirst("a4")
b4=form.getfirst("b4")
c4=form.getfirst("c4")
sa4=form.getfirst("sa4")
sb4=form.getfirst("sb4")
sc4=form.getfirst("sc4")
a5=form.getfirst("a5")
b5=form.getfirst("b5")
c5=form.getfirst("c5")
b6=form.getfirst("b6")
sa5=form.getfirst("sa5")
sb5=form.getfirst("sb5")
sc5=form.getfirst("sc5")
sa6=form.getfirst("sa6")
sb6=form.getfirst("sb6")
sc6=form.getfirst("sc6")
sa7=form.getfirst("sa7")
sb7=form.getfirst("sb7")
sc7=form.getfirst("sc7")
d1=form.getfirst("d1")
d3=form.getfirst("d3")
d4=form.getfirst("d4")
d5=form.getfirst("d5")
v1=form.getfirst("v1")
v2=form.getfirst("v2")
v3=form.getfirst("v3")
v4=form.getfirst("v4")
v5=form.getfirst("v5")
v6=form.getfirst("v6")
v7=form.getfirst("v7")
v8=form.getfirst("v8")
v9=form.getfirst("v9")
v10=form.getfirst("v10")
Psb6sa7=form.getfirst("p1")
Psa6sc7=form.getfirst("p2")
Psc6sb7=form.getfirst("p3")

td={'a1':a1,'b1':b1,'c1':c1,'sa1':sa1,'sb1':sb1,'sc1':sc1,
        'a2':a2,'b2':b2,'c2':c2,'sa2':sa2,'sb2':sb2,'sc2':sc2,
        'a3':a3,'b3':b3,'c3':c3,'sa3':sa3,'sb3':sb3,'sc3':sc3,
        'a4':a4,'b4':b4,'c4':c4,'sa4':sa4,'sb4':sb4,'sc4':sc4,
        'a5':a5,'b5':b5,'c5':c5,'sa5':sa5,'sb5':sb5,'sc5':sc5,
        'sa6':sa6,'sb6':sb6,'sc6':sc6,
        'sa7':sa7,'sb7':sb7,'sc7':sc7,
        'd1':d1,'b6':b6,'d3':d3,'d4':d4,'d5':d5,
        'v1':v1,'v2':v2,'v3':v3,'v4':v4,'v5':v5,'v6':v6,'v7':v7,'v8':v8,'v9':v9,'v10':v10,
        'Psb6sa7':Psb6sa7,'Psc6sb7':Psc6sb7,'Psa6sc7':Psa6sc7}
td1={'a1':'empt','b1':'empt','c1':'empt','sa1':'empt','sb1':'empt','sc1':'empt','ha1':'empt','hb1':'empt','hc1':'empt','area1':'empt',
        'a2':'empt','b2':'empt','c2':'empt','sa2':'empt','sb2':'empt','sc2':'empt','ha2':'empt','hb2':'empt','hc2':'empt','area2':'empt',
        'a3':'empt','b3':'empt','c3':'empt','sa3':'empt','sb3':'empt','sc3':'empt','ha3':'empt','hb3':'empt','hc3':'empt','area3':'empt',
        'a4':'empt','b4':'empt','c4':'empt','sa4':'empt','sb4':'empt','sc4':'empt','ha4':'empt','hb4':'empt','hc4':'empt','area4':'empt',
        'a5':'empt','b5':'empt','c5':'empt','sa5':'empt','sb5':'empt','sc5':'empt','ha5':'empt','hb5':'empt','hc5':'empt','area5':'empt',
        'sa6':'empt','sb6':'empt','sc6':'empt','ha6':'empt','hb6':'empt','hc6':'empt','area6':'empt',
        'sa7':'empt','sb7':'empt','sc7':'empt','ha7':'empt','hb7':'empt','hc7':'empt','area7':'empt',
        'd1':'empt','b6':'empt','d3':'empt','d4':'empt','d5':'empt','areaP':'empt',
        'Psb6sa7':False,'Psc6sb7':False,'Psa6sc7':False,
        'v1':['empt','empt'],'v2':['empt','empt'],'v3':['empt','empt'],'v4':['empt','empt'],'v5':['empt','empt'],
        'v6':['empt','empt'],'v7':['empt','empt'],'v8':['empt','empt'],'v9':['empt','empt'],'v10':['empt','empt']}

new_td={}
for item in td:
  if td[item]!=None:
    if item not in {'Psb6sa7','Psc6sb7','Psa6sc7'}:
      if item in {'v1','v2','v3','v4','v5','v6','v7','v8','v9','v10'}:
        new_td[item]=eval(td[item])
      else:
        new_td[item]=float(td[item])
    elif item in {'Psb6sa7','Psc6sb7','Psa6sc7'}:
      new_td[item]=bool(td[item])
tp1=term_project(**new_td)
sol1=tp1.show_result()

sol2={}
for item in sol1:
  sol2[item]=sol1[item]
for item in td1:
  if item not in sol1:
    sol1[item]='N/A'
  if item in sol2 and item in {'a1','b1','c1','a2','b2','c2','a3','b3','c3','a4','b4','c4','a5','b5','c5','b6','d1','d3','d4','d5'}:
    sol2[item]=str(sol2[item])+'&deg'
  if item not in sol2:
    sol2[item]=' '
  
print("""
  <div class="container1">
  <img src="http://localhost:8080/images/tp7.jpg" style="width:897px;">
  <div class="a1">%s</div>
  <div class="b1">%s</div>
  <div class="c1">%s</div>
  <div class="a2">%s</div>
  <div class="b2">%s</div>
  <div class="c2">%s</div>
  <div class="a3">%s</div>
  <div class="b3">%s</div>
  <div class="c3">%s</div>
  <div class="a4">%s</div>
  <div class="b4">%s</div>
  <div class="c4">%s</div>
  <div class="a5">%s</div>
  <div class="b5">%s</div>
  <div class="c5">%s</div>
  <div class="b6">%s</div>
  <div class="sa1">%s</div>
  <div class="sb1">%s</div>
  <div class="sc1">%s</div>
  <div class="sa2">%s</div>
  <div class="sb2">%s</div>
  <div class="sc2">%s</div>
  <div class="sa3">%s</div>
  <div class="sb3">%s</div>
  <div class="sc3">%s</div>
  <div class="sa4">%s</div>
  <div class="sb4">%s</div>
  <div class="sc4">%s</div>
  <div class="sa5">%s</div>
  <div class="sb5">%s</div>
  <div class="sc5">%s</div>
  <div class="sa6">%s</div>
  <div class="sb6">%s</div>
  <div class="sc6">%s</div>
  <div class="sa7">%s</div>
  <div class="sb7">%s</div>
  <div class="sc7">%s</div>
  <div class="v1">%s</div>
  <div class="v2">%s</div>
  <div class="v3">%s</div>
  <div class="v4">%s</div>
  <div class="v5">%s</div>
  <div class="v6">%s</div>
  <div class="v7">%s</div>
  <div class="v8">%s</div>
  <div class="v9">%s</div>
  <div class="v10">%s</div>
  <div class="d1">%s</div>
  <div class="d3">%s</div>
  <div class="d4">%s</div>
  <div class="d5">%s</div>
  </div>
<div class="grid-container">
  <div>h(sa1): %s</div>
  <div>h(sb1): %s</div>
  <div>h(sc1): %s</div>  
  <div>h(sa2): %s</div>
  <div>h(sb2): %s</div>
  <div>h(sc2): %s</div>
  <div>h(sa3): %s</div>
  <div>h(sb3): %s</div>
  <div>h(sc3): %s</div>
  <div>h(sa4): %s</div>
  <div>h(sb4): %s</div>
  <div>h(sc4): %s</div>
  <div>h(sa5): %s</div>
  <div>h(sb5): %s</div>
  <div>h(sc5): %s</div>
  <div>h(sa6): %s</div>
  <div>h(sb6): %s</div>
  <div>h(sc6): %s</div>
  <div>h(sa7): %s</div>
  <div>h(sb7): %s</div>
  <div>h(sc7): %s</div>
  <div>area1: %s</div>
  <div>area2: %s</div>
  <div>area3: %s</div>
  <div>area4: %s</div>
  <div>area5: %s</div>
  <div>area6: %s</div>
  <div>area7: %s</div>
  <div>areaP: %s</div>
  <div>Total steps:%s</div>
</div>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br>

<p>areaP is the area of the pentagon</p>
</body>
"""%(sol2['a1'],sol2['b1'],sol2['c1'],sol2['a2'],sol2['b2'],sol2['c2'],sol2['a3'],sol2['b3'],sol2['c3'],
  sol2['a4'],sol2['b4'],sol2['c4'],sol2['a5'],sol2['b5'],sol2['c5'],sol2['b6'],
  sol2['sa1'],sol2['sb1'],sol2['sc1'],sol2['sa2'],sol2['sb2'],sol2['sc2'],sol2['sa3'],sol2['sb3'],sol2['sc3'],
  sol2['sa4'],sol2['sb4'],sol2['sc4'],sol2['sa5'],sol2['sb5'],sol2['sc5'],sol2['sa6'],sol2['sb6'],sol2['sc6'],
  sol2['sa7'],sol2['sb7'],sol2['sc7'],sol2['v1'],sol2['v2'],sol2['v3'],sol2['v4'],sol2['v5'],sol2['v6'],
  sol2['v7'],sol2['v8'],sol2['v9'],sol2['v10'],
  sol2['d1'],sol2['d3'],sol2['d4'],sol2['d5'],
  sol1['ha1'],sol1['hb1'],sol1['hc1'],
  sol1['ha2'],sol1['hb2'],sol1['hc2'],
  sol1['ha3'],sol1['hb3'],sol1['hc3'],
  sol1['ha4'],sol1['hb4'],sol1['hc4'],
  sol1['ha5'],sol1['hb5'],sol1['hc5'],
  sol1['ha6'],sol1['hb6'],sol1['hc6'],
  sol1['ha7'],sol1['hb7'],sol1['hc7'],
  sol1['area1'],sol1['area2'],sol1['area3'],
  sol1['area4'],sol1['area5'],sol1['area6'],
  sol1['area7'],sol1['areaP'],sol1['total_steps']))


