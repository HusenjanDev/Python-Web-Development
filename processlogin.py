import cgi

# Getting the POST-Request.
data = cgi.FieldStorage()

# Getting the name.
name = data.getvalue("name")
# Getting the password.
password = data.getvalue("password")

# Checking if the user is allowed.
if name == "Emma" and password =="123":
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<title>Login Panel</title>")
    print("<link href=\"https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600&display=swap\" rel=\"stylesheet\">")
    print("</head>")
    print("<body>")
    print("<div class=\"box\">")
    print("<h1>{}</h1>".format(name))
    print("<ul class=\"list\">")
    print("<li class=\"list-item\"><a>Email: {}</a></li>".format("Emma@Gmail.com"))
    print("<li class=\"list-item\"><a>Phone number: {}</a></li>".format("+47 9319912"))
    print("</ul>")
    print("</div>")
    print("</body>")
    print("<style>")
    print("""
        * {
            padding: 0px;
            margin: 0px;
        }

        body {
            font-family: 'Open Sans', sans-serif;
            font-size: 14px;
            background: #101010;
        }

        li {
            list-style-type: none;
        }

        .box {
            position: fixed;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
            border-radius: 10px;
            background: #222222;
            border: 1px solid #3f3f3f;
        }

        .box h1 {
            color: #efefef;
            text-transform: uppercase;
            opacity: 80%;
            margin: 10px 20px 10px 20px;
        }

        .list {
            margin: 0px 20px 20px 20px;
        }

        .list-item a {
            color: #efefef;
            opacity: 50%;
            text-decoration: none;
        }

        .list-item {
            color: #efefef;
            margin-bottom: 10px;
        }

        /* Hover effects */
        .list-item a:hover {
            cursor: pointer;
            animation: 0.5s forwards hAnimation;
        }

        /* Animations */
        @keyframes hAnimation {
            0%{
                opacity: 50%;
            } 100% {
                opacity: 90%;
            }
        }
    """)
    print("</style>")
    print("</html>")
else: 
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE HTML>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv=\"refresh\" content=\"0 url=http://10.0.0.25:8000/login.html\"/>")
    print("</head>")
    print("</html>")