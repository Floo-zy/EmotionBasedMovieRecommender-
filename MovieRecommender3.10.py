import requests
from tabulate import tabulate
from pathlib import Path

# * declaring emotion variable
emotion: str


def giveURL(x):
    # * x refers to the number corresponding to the genre
    base_url = "https://api.themoviedb.org/3/discover/movie?api_key=87a9f28a9fa52eae1eebdb5012de2c95&with_genres="
    main_url = base_url + x
    giveTitles(main_url)


def giveTitles(url):
    response = requests.get(url)
    data = response.json()
    movies = []

    for movie in data["results"]:
        temp_dict = {
            "Title": movie["title"],
            "Release_date": movie["release_date"],
            "Rating": movie["vote_average"],
        }
        movies.append(temp_dict)

    printResults(movies)


def printResults(finale):
    global emotion
    file_name = input("Enter file name:") + ".txt"
    file_path = str(Path.cwd()) + "/" + file_name

    # * using tabulate to print it to a table
    table = tabulate(finale, headers="keys", showindex=False, tablefmt="pretty")
    # * Printing the output to a file
    with open(file_path, "w") as f:
        f.write(f'Displaying results for Emotion : "{emotion}" \n')
        f.write(table)
    print("File Saved as " + file_name)


def get_input():
    global emotion
    emotion = input(
        """
            Enter an emotion:
            1. Sad
            2. Anger
            3. Fear/Horror/Scary
            4. Joy/Happy
            5. Thrill/Excitement
            6. Suspense/Tension  
            7. Love/Romance
            --->
        """
    ).lower()
    # Drama
    if emotion == "sad":
        giveURL("18")
    # Action
    elif emotion == "anger":
        giveURL("28")
    # Horror
    elif emotion == "fear":
        giveURL("27")
    # Comedy
    elif emotion in ["joy", "happy", "happiness"]:
        giveURL("35")
    # Thriller
    elif emotion in ["excitement", "thrill"]:
        giveURL("53")
    # Mystery
    elif emotion in ["suspense", "tension"]:
        giveURL("9648")
    # Romance
    elif emotion in ["love", "romance"]:
        giveURL("10749")


def main():
    get_input()


# * Driver Code
if __name__ == "__main__":
    main()

#!DUMP
#!DEPRECATED user_votes = [data["results"][i]["vote_count"] for i in range(length_dict)]
#!DEPRECATED short_desc = [data["results"][i]["overview"] for i in range(length_dict)]
