# Advanced Minesweeper Docker Project

This project is a playable Minesweeper web game developed using:

- Flask
- DFS Algorithm
- BFS Hint System
- Docker

## Features

- Interactive browser gameplay
- DFS automatic reveal
- BFS safe hint system
- Flagging mines
- Restart button
- Timer
- Docker containerization

## Run Locally

python app.py

## Docker Build

docker build -t minesweeper-game .

## Docker Run

docker run -d -p 5000:5000 minesweeper-game