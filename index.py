# coding: utf-8

import cgi 
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")



html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
<h1>Moteur de recherche</h1>
	<div style="text-align:center;">
    <form action="/index.py" method="post">
    
        <input type="text" name="search" value="Rechercher..." /></br>
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
     </div>
  	<h2>Résultat</h2>"""
j=2
i=1
s="\n	<ul> "
while i<j:
	s=s+"""
  		<li>Valeur Test</li>
	"""
	if form.getvalue("search") is None:
		i=i
	else:
		s=s+"<li>"+form.getvalue("search")+"</li>"
	i=i+1

html = html+s+"""
	</ul> 
</body>
</html>
"""

print(html)
