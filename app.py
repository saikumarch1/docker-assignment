from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

from game import Minesweeper


app = Flask(__name__)

game = Minesweeper(8, 10)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/board")
def board():

    return jsonify(
        game.get_visible_board()
    )


@app.route("/reveal", methods=["POST"])
def reveal():

    data = request.json

    row = int(data["row"])
    col = int(data["col"])

    result = game.reveal(row, col)

    return jsonify({
        "board": game.get_visible_board(),
        "status": result
    })


@app.route("/flag", methods=["POST"])
def flag():

    data = request.json

    row = int(data["row"])
    col = int(data["col"])

    game.toggle_flag(row, col)

    return jsonify({
        "board": game.get_visible_board()
    })


@app.route("/restart", methods=["POST"])
def restart():

    global game

    game = Minesweeper(8, 10)

    return jsonify({
        "board": game.get_visible_board()
    })


@app.route("/hint")
def hint():

    hint_cell = game.find_safe_hint()

    return jsonify({
        "hint": hint_cell
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )