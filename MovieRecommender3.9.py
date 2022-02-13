import requests
from tabulate import tabulate
from pathlib import Path


def giveURL(x):
    base_url = "https://api.themoviedb.org/3/discover/movie?api_key=87a9f28a9fa52eae1eebdb5012de2c95&with_genres="
    main_url = base_url + x
    giveTitles(main_url)


def giveTitles(url):
    r = requests.get(url)
    data = r.json()
    length_dict = len(data["results"])

    # grabbing the movie data
    movies = [data["results"][i]["title"] for i in range(length_dict)]
    ratings = [data["results"][i]["vote_average"] for i in range(length_dict)]
    user_votes = [data["results"][i]["vote_count"] for i in range(length_dict)]

    # creating dictionary containing movie data
    finale = {"Movie Name": movies, "Ratings": ratings, "Votes": user_votes}

    printResults(finale)


def printResults(finale):
    file_name = input("Enter file name:") + ".txt"
    file_path = str(Path.cwd()) + "/" + file_name

    # using tabulate to print it to a table
    table = tabulate(finale, headers="keys", showindex=False, tablefmt="pretty")
    with open(file_path, "w") as f:
        f.write(f"Displaying results for emotion {emotion}\n")
        f.write(table)
    print("File Saved as " + file_name)


# main function
def main():
    global emotion
    emotion = str(
        input(
            """Enter an emotion:
                        List of emotions----->sad,anger,fear/horror,joy,thrill,suspense and love<-----\n"""
        )
    ).lower()
    # Drama
    if emotion == "sad":
        giveURL("18")
    # Action
    elif emotion in "anger":
        giveURL("28")
    # Horror
    elif emotion == ["fear", "horror"]:
        giveURL("27")
    # Comedy
    elif emotion == "joy":
        giveURL("35")
    # Thriller
    elif emotion == "thrill":
        giveURL("53")
    # Mystery
    elif emotion in "suspense":
        giveURL("9648")
    # Romance
    elif emotion == "love":
        giveURL("10749")


if __name__ == "__main__":
    main()


