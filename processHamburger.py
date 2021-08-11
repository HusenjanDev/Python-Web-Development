import cgi, os

# Getting the data from the buildhamburger.html post request.
data = cgi.FieldStorage()

# Total Price of burger.
totalPrice = 0

# Total BrugerCO Points.
burgerCOPoints = 0

# Getting the different values.
getHamburgerType = data.getvalue("type")
getHamburgerBreadType = data.getvalue("bread-type")
getProgram = data.getvalue("program")

# We will store the html code in these variables.
setHamburgerType = str()
setHamburgerBreadType = str()
setHamburgerToppings = str()
setProgram = str()

if getHamburgerType == "beef":
    totalPrice += 10
    burgerCOPoints += 1
    setHamburgerType = "<li class=\"list-item\"><a>Beef Price: 10 nok</a></li>"

elif getHamburgerType == "chicken":
    totalPrice += 7
    burgerCOPoints += 1
    setHamburgerType = "<li class=\"list-item\"><a>Chicken Price: 7 nok</a></li>"

elif getHamburgerType == "rib":
    totalPrice += 12
    burgerCOPoints += 1
    setHamburgerType = "<li class=\"list-item\"><a>Rib Price: 12 nok</a></li>"

elif getHamburgerType == "vegetarian":
    totalPrice += 20
    burgerCOPoints += 1
    setHamburgerType = "<li class=\"list-item\"><a>Rib Price: 12 nok</a></li>"

if getHamburgerBreadType == "normalbun":
    totalPrice += 6
    burgerCOPoints += 1
    setHamburgerBreadType = "<li class=\"list-item\"><a>Normal bun: 6 nok</a></li>"

elif getHamburgerBreadType == "ciabatta":
    totalPrice += 10
    burgerCOPoints += 1
    setHamburgerBreadType = "<li class=\"list-item\"><a>Ciabatta: 10 nok</a></li>"

elif getHamburgerBreadType == "agnusbun":
    totalPrice += 15
    burgerCOPoints += 1
    setHamburgerBreadType = "<li class=\"list-item\"><a>Agnus bun: 15 nok</a></li>"

if data.getvalue("cheese") :
    totalPrice += 10
    burgerCOPoints += 1
    setHamburgerToppings += "<li class=\"list-item\"><a>Cheese: 10 nok</a></li>"

if data.getvalue("tomato"):
    totalPrice += 5
    burgerCOPoints += 1
    setHamburgerToppings += "<li class=\"list-item\"><a>Tomato: 5 nok</a></li>"

if data.getvalue("egg"):
    totalPrice += 7
    burgerCOPoints += 1
    setHamburgerToppings += "<li class=\"list-item\"><a>Egg: 7 nok</a></li>"

if getProgram == "yes-program":
    setProgram = "Added {} Points to BurgerCO!".format(burgerCOPoints)

if data:
    print("Content-Type: text/html")
    print("")
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<title>Hamburger</title>")
    print("<link href=\"https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600&display=swap\" rel=\"stylesheet\">")
    print("</head>")
    print("")
    print("<body>")
    print("<div class=\"box\">")
    print("<h1>Recipe</h1>")
    print("<ul class=\"list\">")
    print(setHamburgerType)
    print(setHamburgerBreadType)
    print(setHamburgerToppings)
    print(setProgram)
    print("<li><a>Total Price: {} nok</a></li>".format(totalPrice))
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
            color: #efefef;
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