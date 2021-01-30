import requests


def fetchPage(params):
    response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/", params=params)
    json_obj = response.json()
    num_pages = json_obj["total_pages"]

    result = []
    data = json_obj["data"]
    for movie in data:
        result.append(movie["Title"])

    print(result)
    return result, num_pages


def getMovieTitles(substr):
    result = []
    page = 1
    num_pages = float("inf")

    while page <= num_pages:
        params = {
            "Title": substr,
            "page": page
        }

        ret, pages = fetchPage(params)
        if page == 1:
            num_pages = pages

        result.extend(ret)
        page += 1

    return sorted(result)