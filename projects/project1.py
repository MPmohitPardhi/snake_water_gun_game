from flask import Flask, request, render_template_string, jsonify
import random

app = Flask(__name__)

# Your exact original logic kept in this function
def play_game(youchoice):
    computer = random.choice([-1, 1, 0])
    youdict = {"s": 1, "w": -1, "g": 0}
    rewersdict = {1: "snake", -1: "water", 0: "Gun"}
    you = youdict[youchoice]
    result = ""

    # Print-style response converted to strings
    output = f"You chose {rewersdict[you]}<br>Computer chose {rewersdict[computer]}<br>"

    if computer == you:
        result = "It's a draw"
    else:
        if computer == -1 and you == 1:
            result = "You win!"
        elif computer == -1 and you == 0:
            result = "You lose!"
        elif computer == 1 and you == -1:
            result = "You lose!"
        elif computer == 1 and you == 0:
            result = "You win!"
        elif computer == 0 and you == -1:
            result = "You win!"
        elif computer == 0 and you == 1:
            result = "You lose!"
        else:
            result = "Error"

    return output + f"<strong>{result}</strong>"

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Snake Water Gun Game</title>
    <style>
        body {
            background: linear-gradient(to right, #fbc2eb, #a6c1ee);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding-top: 60px;
            color: #333;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        .btn {
            padding: 15px 30px;
            font-size: 20px;
            border: none;
            margin: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            background-color: #fff;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .btn:hover {
            background-color: #333;
            color: #fff;
        }
        #result {
            margin-top: 30px;
            font-size: 22px;
            background: #ffffffcc;
            padding: 20px;
            border-radius: 10px;
            display: inline-block;
            min-width: 300px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <h1>Snake 🐍 Water 💧 Gun 🔫</h1>
    <button class="btn" onclick="play('s')">Snake</button>
    <button class="btn" onclick="play('w')">Water</button>
    <button class="btn" onclick="play('g')">Gun</button>

    <div id="result"></div>

    <script>
        function play(choice) {
            fetch("/play", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ youchoice: choice })
            })
            .then(res => res.json())
            .then(data => {
                document.getElementById("result").innerHTML = data.result;
            });
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/play", methods=["POST"])
def game():
    data = request.get_json()
    youchoice = data.get("youchoice")
    if youchoice not in ["s", "w", "g"]:
        return jsonify({"result": "<span style='color:red;'>Invalid choice</span>"})
    result = play_game(youchoice)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
