import flask
import os
import time

count = 0
myhost = os.uname()[1]
dockerized = False
if os.path.isfile('/.dockerenv'):
    dockerized = True

app = flask.Flask(__name__)

@app.route("/", methods=["GET"])
def hello():

    global count

    curr_time = time.localtime()
    curr_clock = time.strftime("%H:%M:%S", curr_time)
    print(curr_clock)
    count = count + 1

    html = f"<html><head></head><body><h1>Hello World!</h1></body>" \
           f"<h2>Server Time: {curr_clock}</h2>" \
           f"<h2>Visitor Count: {count}</h2>" \
           f"<h2>App_is_dockerized: {str(dockerized)}</h2>" \
           f"</html>"
    return html


if __name__ == "__main__":
     app.run(host="localhost", port=8080, debug=True)
