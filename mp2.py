import pymysql
import cgi

db=pymysql.connect(host='localhost',
                   user='root',
                   passwd='1207kyle',
                   db='gallery')
cur=db.cursor()

print("Content-Type: text/html")
print("""
	<html>
	<head><title>Welcome to my gallery</title></head>

	<body style="background-image:url('http://localhost:8080/images/background1.jpg')">

	<h3>Welcome to my gallery</h3><center>
	""")
# gal = ', '.join(map(str, [("Old Iron Collection","Clollection of Old Iron"), ("147599961849","Watermelon"),("1475999494771","A baby sitting on a chair"), ("1475999541444", "An Indian"), ("1475999549881", "Woman with glasses"), ("1475999558661", "Girl in white")]))
# cur.execute("INSERT IGNORE INTO gallery(name, description) VALUES {}".format(gal))
# db.commit()
# img = ', '.join(map(str, [("Untitiled","http://www.nobullart.com/accounts/28/2B/C3QNTT2B28/CXBUME2FPQ/lg_CXBUME2FPQ.jpg",1,1,1),("XYZ","xxx",1,1,1)]))
# cur.execute("INSERT IGNORE INTO image(title,link,gallery_id,artist_id,detail_id) VALUES {}".format(img))
# db.commit()
# art = ', '.join(map(str, [("Jeremy Holmes",1965,"USA","cute"), ("haosong",1995,"cn","handsome"), ("lgy",19992,"us","ugly"),("XiongBoCheng",2003,"India","43966666")]))
# cur.execute("INSERT IGNORE INTO artist(name,birth_year,country,description) VALUES {}".format(art))
# db.commit()
# det = ', '.join(map(str, [(1001,2006,"Photography",600,400,"US","Black and white")]))
# cur.execute("INSERT IGNORE INTO detail(image_id,year,type,width,height,location,description) VALUES {}".format(det))
# db.commit()

# List galleries
print("<h3>Galleries:</h3>")
print("<b>Name &nbsp &nbsp &nbsp Description</b><br>")
cur.execute("SELECT name,description FROM gallery")
for row in cur.fetchall():
	for item in row:
		print ("%s&nbsp&nbsp"%item)
	print("<br>")

# List images
print("<h3>Images:</h3>")
print("<b>Title&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspLink</b><br>")
cur.execute("SELECT title,link FROM image")
for row in cur.fetchall():
	count=0
	for item in row:
		if (count==0):
			print('<a href="http://localhost:8080/test/cgi-bin/image_detail1.py">%s</a>'%item)
		else:
			print ("%s"%item)
		count=count+1
	print("<br>")
# Count number of images
count = cur.rowcount
print("<b>Total number of images: </b>",count)

print("""
<br>
<br>
<b>Create a gallery:</b>
<form method="get" enctype="multipart/form-data">
Name: <input maxlength="60" size="60" name="textinput2"> 
<br>
Description: <input maxlength="60" size="60" name="textinput3"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Create an artist:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Name: <input maxlength="60" size="60" name="art_input2"> 
<br>
Birth year: <input maxlength="60" size="60" name="art_input3"> 
<br>
Country: <input maxlength="60" size="60" name="art_input4"> 
<br>
Description: <input maxlength="60" size="60" name="art_input5"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Add an image:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Title: <input maxlength="60" size="60" name="img_input2"> 
<br>
Link: <input maxlength="120" size="120" name="img_input3"> 
<br>
Gallery ID: <input maxlength="60" size="60" name="img_input4"> 
<br>
Artist ID: <input maxlength="60" size="60" name="img_input5"> 
<br>
Detail ID: <input maxlength="60" size="60" name="img_input6"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Delete an image and its detail:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Please provide the image ID you want to delete: <input maxlength="60" size="60" name="del_img_id"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Modify the details of an image:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Please provide the image ID you want to modify: <input maxlength="60" size="60" name="mod_img_id"> 
<br>
New title: <input maxlength="60" size="60" name="new_title"> 
<br>
New link: <input maxlength="60" size="60" name="new_link"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Modify the details of an artist:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Please provide the artist ID you want to modify: <input maxlength="60" size="60" name="mod_art_id"> 
<br>
New Name: <input maxlength="60" size="60" name="new_artist_name"> 
<br>
New Birth year: <input maxlength="60" size="60" name="new_birth"> 
<br>
New Country: <input maxlength="60" size="60" name="new_country"> 
<br>
New Description: <input maxlength="60" size="60" name="new_description"> 
<br>
<input value="Submit" type="submit">
</form>""")
print("""
<br>
<b>Modify a gallery:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
Please provide the gallery ID you want to modify: <input maxlength="60" size="60" name="mod_gal_id"> 
<br>
New name: <input maxlength="60" size="60" name="new_gal_name"> 
<br>
New description: <input maxlength="60" size="60" name="new_gal_description"> 
<br>
<input value="Submit" type="submit">
</form>""")

print("""
<br>
<b>Find the images by:</b>
<form action="mp2.py" method="get" enctype="multipart/form-data">
<input type="radio" name="findby" value="type">type, please enter the type below:<br>
<input type="radio" name="findby" value="c_year"> range of creation year, please enter below(format:1957-1988):<br>
<input type="radio" name="findby" value="a_name"> artist name, please enter below:<br>
<input type="radio" name="findby" value="location"> location, please enter below:<br>
<input type="radio" name="findby" value="country"> country, please enter below:<br>
<input type="radio" name="findby" value="b_year"> birth year, please enter below:<br>
<input maxlength="60" size="60" name="findimage"> 
<br>
<input value="Submit" type="submit">
</form>""")


form = cgi.FieldStorage()
input_text2 = form.getfirst("textinput2")
input_text3 = form.getfirst("textinput3")

art2=form.getfirst("art_input2")
art3=form.getfirst("art_input3")
art4=form.getfirst("art_input4")
art5=form.getfirst("art_input5")

img2=form.getfirst("img_input2")
img3=form.getfirst("img_input3")
img4=form.getfirst("img_input4")
img5=form.getfirst("img_input5")
img6=form.getfirst("img_input6")

delimgid=form.getfirst("del_img_id")

mod_img_id=form.getfirst("mod_img_id")
new_title=form.getfirst("new_title")
new_link=form.getfirst("new_link")

mod_art_id=form.getfirst("mod_art_id")
new_artist_name=form.getfirst("new_artist_name")
new_birth=form.getfirst("new_birth")
new_country=form.getfirst("new_country")
new_description=form.getfirst("new_description")

mod_gal_id=form.getfirst("mod_gal_id")
new_gal_name=form.getfirst("new_gal_name")
new_gal_description=form.getfirst("new_gal_description")

findby=form.getfirst("findby")
findimage=form.getfirst("findimage")

if None not in [input_text2,input_text3]:
	gal = ', '.join(map(str, [(input_text2,input_text3)]))
	cur.execute("INSERT IGNORE INTO gallery(name, description) VALUES {}".format(gal))
db.commit()
if None not in [art2,art3,art4,art5]:
	art = ', '.join(map(str, [(art2,art3,art4,art5)]))
	cur.execute("INSERT IGNORE INTO artist(name, birth_year, country, description) VALUES {}".format(art))
db.commit()
if None not in [img2,img3,img4,img5,img6]:
	img = ', '.join(map(str, [(img2,img3,img4,img5,img6)]))
	cur.execute("INSERT IGNORE INTO image(title, link, gallery_id, artist_id, detail_id) VALUES {}".format(img))
db.commit()
if None not in [delimgid]:
	cur.execute("DELETE from image WHERE image.image_id=%s",delimgid)
	cur.execute("DELETE from detail WHERE detail.image_id=%s",delimgid)
db.commit()
if None not in [mod_img_id,new_title,new_link]:
	cur.execute("UPDATE image SET title=%s, link=%s WHERE image.image_id=%s",(new_title,new_link,mod_img_id))
db.commit()
if None not in [mod_art_id,new_artist_name,new_birth,new_country,new_description]:
	cur.execute("UPDATE artist SET name=%s, birth_year=%s, country=%s, description=%s WHERE artist.artist_id=%s",(new_artist_name,new_birth,new_country,new_description,mod_art_id))
db.commit()
if None not in [mod_gal_id,new_gal_name,new_gal_description]:
	cur.execute("UPDATE gallery SET name=%s, description=%s WHERE gallery.gallery_id=%s",(new_gal_name,new_gal_description,mod_gal_id))
db.commit()
if findby!=None:
	if findby=="type":
		cur.execute("SELECT image_id FROM detail WHERE detail.type=%s",findimage)
		data=cur.fetchall()
	if findby=="c_year":
		newfind=findimage.split('-')
		cur.execute("SELECT image_id FROM detail WHERE detail.year>=%s AND detail.year<=%s",(newfind[0],newfind[1]))
		data=cur.fetchall()		
	if findby=="a_name":
		cur.execute("SELECT image_id FROM image,artist WHERE image.artist_id=artist.artist_id AND artist.name=%s",findimage)
		data=cur.fetchall()
	if findby=="location":
		cur.execute("SELECT image_id FROM detail WHERE detail.location=%s",findimage)
		data=cur.fetchall()
	if findby=="country":
		cur.execute("SELECT image_id FROM image,artist WHERE image.artist_id=artist.artist_id AND artist.country=%s",findimage)
		data=cur.fetchall()
	if findby=="b_year":
		cur.execute("SELECT image_id FROM image,artist WHERE image.artist_id=artist.artist_id AND artist.birth_year=%s",findimage)
		data=cur.fetchall()
	for item in data:
		cur.execute("SELECT link,width,height,name,year,type,location,detail.description,title FROM detail,artist,image WHERE image.image_id=detail.image_id AND image.artist_id=artist.artist_id AND detail.image_id=%s",item[0])
		wh=cur.fetchall()
		whlist=[]
		for item in wh[0]:
			whlist.append(item)
		print("<figure>")
		print("""<img src=%s width=%s length=%s/>"""%(whlist[0],whlist[1]*0.3,whlist[2]*0.3))
		print("""<figcaption><a href="http://localhost:8080/test/cgi-bin/detail_art.py">%s</a>&nbsp%s&nbsp%s&nbsp%s&nbsp%s&nbsp%s
		</figcaption>"""%(whlist[3],whlist[8],whlist[4],whlist[5],whlist[6],whlist[7]))
		print("</figure>")


# cur.execute("SELECT name,description FROM gallery")
# for row in cur.fetchall():
# 	for item in row:
# 		print ("%s"%item)
# 	print("<p> </p>")

# cur.execute("SELECT * FROM artist")
# for row in cur.fetchall():
# 	for item in row:
# 		print ("%s"%item)
# 	print("<p> </p>")

# cur.execute("SELECT * FROM image")
# for row in cur.fetchall():
# 	for item in row:
# 		print ("%s"%item)
# 	print("<br>")

# cur.execute("SELECT * FROM detail")
# for row in cur.fetchall():
# 	for item in row:
# 		print ("%s"%item)
# 	print("<br>")

# print(img1)
# cur.execute("SELECT link FROM image WHERE image.image_id=%s",img1)
# url=cur.fetchone()[0]
# print("<br>",url)
# print("<img src=%s>"%url)

print("</center></body></html>\n")


db.close



"""
gallery (gallery_id, name, description)
primary key(gallery_id)
image (image_id, title, link, gallery_id, artist_id, detail_id)
primary key(image_id)
artist (artist_id, name, birth_year, country, description)
primary key(artist_id)
detail (detail_id, image_id, year, type, width, height, location, description)
primary key(detail_id)
"""