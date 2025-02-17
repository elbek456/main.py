def max_movies_to_watch(movies: list) -> tuple:
    movies.sort(key=lambda x: x[1])

    tanlangan_kinolar = []
    oxrgi_tugash_vaqti = -1

    for boshlanish, tugash in movies:
        if boshlanish >= oxrgi_tugash_vaqti:
            tanlangan_kinolar.append((boshlanish, tugash))
            oxrgi_tugash_vaqti = tugash

    return tanlangan_kinolar, len(tanlangan_kinolar)


movies = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print(max_movies_to_watch(movies))
