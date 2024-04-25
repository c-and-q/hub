from phew import server, connect_to_wifi
from phew.template import render_template
from secrets import ssid, password

print(connect_to_wifi(ssid, password))
HTML = "/html/"


@server.route("/")
async def index(request):
    return await render_template(HTML + "index.html", title="Sensors Monitor")


# @server.route("/about")
# def about(request):
#     return render_template(HTML + "about.html", title="About C&amp;Q", name="Kevin")


# @server.route("/login", ["POST", 'GET'])
# def login_form(request):
#     print(request.method)
#     if request.method == 'GET':
#         return render_template(HTML + "login.html")
#     if request.method == 'POST':
#         username = request.form.get("username", None)
#         password = request.form.get("password", None)
#         logging.debug(username)
#         logging.debug(password)
#
#         if username == "kevin" and password == "password":
#             return render_template(HTML + 'default.html', content="<h1>Welcome back, " + username + "</h1>")
#         else:
#             return render_template(HTML + 'default.html', content="Invalid username or password")


@server.catchall()
def catchall_404(request):
    return "Not found", 404


server.run()
