how to make this run on github and still work from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if not message:
            return "Error: message cannot be empty."
        os.system("start "+message)
    return """
    if you see this type in cmd and hit enter
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <p>INPUT:</p>
        <form action="/" method="post">
    <input type="text" name="message" style="width: 750; height: 45px;">
    <input type="submit" value="Send" style="width: 100; height: 45px;">
  </form>
<style>
  form{
    text-align: center;
  }
   p{
    text-align: center;
    font-size: 20;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }
    body {
    background-color: rgb(153, 255, 204);
  }
</style>
    """

if __name__ == "__main__":
    app.run()
