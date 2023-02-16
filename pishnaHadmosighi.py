all_users = {}
all_albums = {}


def add_user(username, age, city, albums, all_users, all_albums):
    all_users[username] = {}
    all_users[username]["age"] = age
    all_users[username]["city"] = city
    all_users[username]["albums"] = albums


def add_album(name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[name] = {}
    all_albums[name]["singer"] = artist_name
    all_albums[name]["genre"] = genre
    all_albums[name]["tracks"] = tracks


def query_user_artist(username, artist_name, all_users, all_albums):
    ans = 0
    for album in all_users[username]["albums"]:
        if all_albums[album]["singer"] == artist_name:
            ans += all_albums[album]["tracks"]
    return ans


def query_user_genre(username, genre, all_users, all_albums):
    ans = 0
    for album in all_users[username]["albums"]:
        if all_albums[album]["genre"] == genre:
            ans += all_albums[album]["tracks"]
    return ans


def query_age_artist(age, artist_name, all_users, all_albums):
    ans = 0
    for user, info in all_users.items():
        if info["age"] == age:
            for album in all_users[user]["albums"]:
                if all_albums[album]["singer"] == artist_name:
                    ans += all_albums[album]["tracks"]
    return ans


def query_age_genre(age, genre, all_users, all_albums):
    ans = 0
    for user, info in all_users.items():
        if info["age"] == age:
            for album in all_users[user]["albums"]:
                if all_albums[album]["genre"] == genre:
                    ans += all_albums[album]["tracks"]
    return ans


def query_city_artist(city, artist_name, all_users, all_albums):
    ans = 0
    for user, info in all_users.items():
        if info["city"] == city:
            for album in all_users[user]["albums"]:
                if all_albums[album]["singer"] == artist_name:
                    ans += all_albums[album]["tracks"]
    return ans


def query_city_genre(city, genre, all_users, all_albums):
    ans = 0
    for user, info in all_users.items():
        if info["city"] == city:
            for album in all_users[user]["albums"]:
                if all_albums[album]["genre"] == genre:
                    ans += all_albums[album]["tracks"]
    return ans

# DO NOT USE YOUR OWN TESTS HERE, USE SAMPLE TEST INSTEAD