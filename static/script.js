let timer = 0;


setInterval(() => {

    timer++;

    document.getElementById(
        "timer"
    ).innerText = `Time: ${timer}s`;

}, 1000);


async function loadBoard() {

    const response = await fetch("/board");

    const board = await response.json();

    renderBoard(board);
}


function renderBoard(board) {

    const boardDiv =
        document.getElementById("board");

    boardDiv.innerHTML = "";

    for (let row = 0; row < board.length; row++) {

        for (let col = 0; col < board[row].length; col++) {

            const button =
                document.createElement("button");

            button.className = "cell";

            const value = board[row][col];

            if (value !== "X") {

                button.classList.add("revealed");

                button.innerText = value;
            }

            if (value === "F") {

                button.classList.add("flag");

                button.innerText = "🚩";
            }

            button.onclick = () => {

                revealCell(row, col);
            };

            button.oncontextmenu = (e) => {

                e.preventDefault();

                flagCell(row, col);
            };

            boardDiv.appendChild(button);
        }
    }
}


async function revealCell(row, col) {

    const response = await fetch("/reveal", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            row: row,
            col: col
        })
    });

    const data = await response.json();

    renderBoard(data.board);

    if (data.status === "lost") {

        document.getElementById(
            "status"
        ).innerText = "Game Over!";
    }
}


async function flagCell(row, col) {

    const response = await fetch("/flag", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            row: row,
            col: col
        })
    });

    const data = await response.json();

    renderBoard(data.board);
}


async function restartGame() {

    timer = 0;

    const response = await fetch("/restart", {

        method: "POST"
    });

    const data = await response.json();

    renderBoard(data.board);

    document.getElementById(
        "status"
    ).innerText = "";
}


async function getHint() {

    const response = await fetch("/hint");

    const data = await response.json();

    if (data.hint) {

        alert(
            `Safe Cell Hint: (${data.hint[0]}, ${data.hint[1]})`
        );
    }
}


loadBoard();