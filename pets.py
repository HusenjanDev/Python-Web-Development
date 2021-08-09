import cgi

data = cgi.FieldStorage()

petnumber = data.getvalue("number")

print("Content-Type: text/html")
print()

if petnumber == "1":
    print("<html>")
    print("<head>")
    print("<title>{}</title>".format("Jacob"))
    print("</head>")
    print("<body>")
    print("<h1>Pet Name {}</h1>".format("Jacob"))
    print("<h1>Pet Age {}</h1>".format("12"))
    print("<h1>Pet Sex {}</h1>".format("Male"))
    print("</body>")
    print("</html>")

elif petnumber == "2":
    print("<html>")
    print("<head>")
    print("<title>{}</title>".format("Erik"))
    print("</head>")
    print("<body>")
    print("<h1>Pet Name {}</h1>".format("Erik"))
    print("<h1>Pet Age {}</h1>".format("8"))
    print("<h1>Pet Sex {}</h1>".format("Male"))
    print("</body>")
    print("</html>")

elif petnumber == "3":
    print("<html>")
    print("<head>")
    print("<title>{}</title>".format("Alpha"))
    print("</head>")
    print("<body>")
    print("<h1>Pet Name {}</h1>".format("Alpha"))
    print("<h1>Pet Age {}</h1>".format("2"))
    print("<h1>Pet Sex {}</h1>".format("Female"))
    print("</body>")
    print("</html>")

else:
    print("<html>")
    print("<head>")
    print("<title>{}</title>".format("Alpha"))
    print("</head>")
    print("<body>")
    print("<h1>Pet not found</h1>".format("Alpha"))
    print("</body>")
    print("</html>")