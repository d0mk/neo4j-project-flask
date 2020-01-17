def get_genres(s):
    return s.run('MATCH (n:Genre) RETURN properties(n) AS properties')


def get_actors(s):
    return s.run('MATCH (n:Person) WHERE n.type = "actor" RETURN properties(n) AS properties')


def get_directors(s):
    return s.run('MATCH (n:Person) WHERE n.type = "director" RETURN properties(n) AS properties')


def get_movies(s):
    return s.run('MATCH (n:Movie) RETURN properties(n) AS properties')


def get_production_companies(s):
    return s.run('MATCH (n:Company) RETURN properties(n) AS properties')


def get_actors_from_movie(s, movie_title):
    return s.run('MATCH (n:Person)-[r:ACTED_IN]-(m:Movie) '
                 'WHERE n.type = "actor" AND (m.title = $m OR m.original_title = $m) '
                 'RETURN properties(n) AS properties', m=movie_title)


def get_movies_by_director(s, director_name):
    return s.run('MATCH (n:Person)-[r:HAS_DIRECTED]-(m:Movie) '
                 'WHERE n.type = "director" AND n.name = $d '
                 'RETURN properties(m) AS properties', d=director_name)


def get_movies_with_actor(s, actor_name):
    return s.run('MATCH (n:Person)-[r:ACTED_IN]-(m:Movie) '
                 'WHERE n.type = "actor" AND n.name = $a '
                 'RETURN properties(m) AS properties', a=actor_name)


def get_movies_with_actor_in_genre(s, actor_name, genre_name):
    return s.run('MATCH (n:Person)-[r:ACTED_IN]-(m:Movie)-[w:BELONGS_TO]-(g:Genre) '
                 'WHERE n.type = "actor" AND n.name = $a AND g.name = $g '
                 'RETURN properties(m) AS properties', a=actor_name, g=genre_name)


def get_movies_by_min_rating(s, rating):
    return s.run('MATCH (n:Movie) '
                 'WHERE n.rating >= $r '
                 'RETURN properties(n) AS properties', r=rating)


def get_movies_by_min_runtime(s, runtime):
    return s.run('MATCH (n:Movie) '
                 'WHERE n.runtime >= $r '
                 'RETURN properties(n) AS properties', r=runtime)


def get_movies_by_min_year(s, year):
    return s.run('MATCH (n:Movie) '
                 'WHERE n.year >= $y '
                 'RETURN properties(n) AS properties', y=year)


def get_movies_by_genre(s, genre):
    return s.run('MATCH (n:Movie)-[r:BELONGS_TO]-(g:Genre) '
                 'WHERE g.name = $g '
                 'RETURN properties(n) AS properties', g=genre)