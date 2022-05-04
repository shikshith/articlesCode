from flask import Flask,jsonify,request
import csv

allMovies = []
with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    return jsonify({
        "data": allMovies[0],
        "status": "success"
    })

@app.route("/liked-movie", methods=["POST"])
def liked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/Did-not-watch", methods=["POST"])
def notWatchedMovies():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    did_not_watch.append(movie)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
    app.run()