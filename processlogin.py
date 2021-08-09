import cgi

data = cgi.FieldStorage()
username = data.getvalue("name")
password = data.getvalue("password")

print("Content-Type: text/html")
print()

if username == "Emma" and password == "123":
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<title>Logged in as {}</title>".format(username))
    print("<link rel=\"stylesheet\" href=\"style.css\">")
    print("</head>")
    print("<body>")
    print("<div class=\"info-box\">")
    print("<h1>Welcome back {}</h1>".format(username))
    print("<p>Your informations</p>")
    print("<p>Email : {}</p>".format("Emma@Gmail.com"))
    print("<p>Phone number: {}</p>".format("+47 9319931"))
    print("</div>")
    print("</body>")
    print("</html>")
else:
    print("<!DOCTYPE HTML>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv=\"refresh\" content=\"0 url=http://10.0.0.25:8000/login.html\"/>")
    print(" <link rel=\"stylesheet\" href=\"style.css\">")
    print("</head>")
    print("</html>")
