# Important variables:
#     movie_db: list of 4-tuples (imported from movies.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE MOVIE CHAT BOT:
# what movies were made in _ (must be date, because we don't have location)
# what movies were made between _ and _
# what movies were made before _
# what movies were made after _
# who directed %
# who was the director of %
# what movies were directed by %
# who acted in %
# when was % made
# in what movies did % appear
# bye

#  Include the movie database, named movie_db
from movies import movie_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "movie" (a tuple)
def get_title(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[0]


def get_director(movie: Tuple[str, str, int, List[str]]) -> str:
    return movie[1]


def get_year(movie: Tuple[str, str, int, List[str]]) -> int:
    return movie[2]


def get_actors(movie: Tuple[str, str, int, List[str]]) -> List[str]:
    return movie[3]

##print("movie_db[0] is: " + str(movie_db))
##print("the director is: " +str(movie_db[0][1]))
##print(get_director(movie_db[0]))

# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def title_by_year(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made in the passed in year
    """

    return[get_title(i) for i in movie_db if get_year(i) == int(matches[0])]

##    year = int(matches[0])
    
##  def movie_made_in_year(movie: Tuple[str,str,int,List[str]])-> bool:
##        return year == get_year(movie)
##    
##    listofMovies = filter(movie_made_in_year, movie_db)
##    listofTitles = map(get_title,listofMovies)
##    return list(listofTitles)
    
    
    

##assert title_by_year(["1974"]) == ['amarcord','chinatown'],"failed title_by_year test" 
##assert title_by_year(["1972"]) == ['the godfather'],"failed title_by_year test" 
        
    



def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all movies made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get movies from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of movie titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get movies made in 1991, 1992, 1993 & 1994)
    """
    
    return [get_title(i)for i in movie_db if get_year(i) in list(range(int(matches[0]),int(matches[1])+1))]
        
    


def title_before_year(matches: List[str]) -> List[str]:
    """Finds all movies made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only before)
    """
    return [get_title(i) for i in movie_db if get_year(i) < int(matches[0])]


def title_after_year(matches: List[str]) -> List[str]:
    """Finds all movies made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of movie titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any movies made that year, only after)
    """
    return[get_title(i) for i in movie_db if get_year(i) > int(matches[0])]


def director_by_title(matches: List[str]) -> List[str]:
    """Finds director of movie based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the director of the movie
    """
    return[get_director(i) for i in movie_db if get_title(i) == matches[0]]


def title_by_director(matches: List[str]) -> List[str]:
    """Finds movies directed by the passed in director

    Args:
        matches - a list of 1 string, just the director

    Returns:
        a list of movies titles directed by the passed in director
    """
    return[get_title(i) for i in movie_db if get_director(i) == matches[0]]


def actors_by_title(matches: List[str]) -> List[str]:
    """Finds actors who acted in the passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of actors who acted in the passed in title
    
    """
    
    #list comprehension isn't going to work: bc it's putting a list in a list
    for i in movie_db:
        if get_title(i) == matches[0]:
            return get_actors(i)



def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in movie title

    Args:
        matches - a list of 1 string, just the movie title

    Returns:
        a list of one item (an int), the year that the movie was made
    """
    return[get_year(i) for i in movie_db if get_title(i) == matches[0]]


def title_by_actor(matches: List[str]) -> List[str]:
    """Finds titles of all movies that the given actor was in

    Args:
        matches - a list of 1 string, just the actor

    Returns:
        a list of movie titles that the actor acted in
    """
    
    return[get_title(i) for i in movie_db if matches[0] in get_actors(i)]

#new actors by year
    

def actors_by_year(matches:List[int])-> List[str]:
     """Finds all actors in movies from a specific year

    Args:
        matches - a list of one item[int] the year that the movie was made

    Returns:
        a list of actors who acted in movies released that year
    """
     for i in movie_db:
        if get_year(i) == int(matches[0]):
            print(get_actors(i))
            return get_actors(i)


# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what movies were made in _"), title_by_year),
    (str.split("what movies were made between _ and _"), title_by_year_range),
    (str.split("what movies were made before _"), title_before_year),
    (str.split("what movies were made after _"), title_after_year),
    # note there are two valid patterns here two different ways to ask for the director
    # of a movie
    (str.split("who directed %"), director_by_title),
    (str.split("who was the director of %"), director_by_title),
    (str.split("what movies were directed by %"), title_by_director),
    (str.split("who acted in %"), actors_by_title),
    (str.split("when was % made"), year_by_title),
    (str.split("in what movies did % appear"), title_by_actor),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    num_matches = 0
    result: List[str] = []
  
    for (pattern,function) in pa_list:
        if match(pattern,src) != None:
            num_matches += 1
            result = function(match(pattern,src))
            
  
    if num_matches == 0:
           return ["I don't understand"]
    elif result == []:
        return["No answers"]
    else:
        return result
    #for each pattern, action pair in pa_list
    #   try to match - call match with that pattern and the source(src)
    #       save the results from match, in x
    #   if we matched:
    #       increment num_matches
    #       set the result to the results of calling the associated action function
    #           function, passing it the result from match, x
    #if
    #elif
    #else
    #you have access to num matches and access to result


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the movie database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the following line once you've written all of your code and are ready to try
# it out. Before running the following line, you should make sure that your code passes
# the existing asserts.
#query_loop()

##if __name__ == "__main__":
##    assert sorted(title_by_year(["1974"])) == sorted(["amarcord", "chinatown"]), "failed title_by_year test"
##    assert sorted(title_by_year(["1960"])) == sorted(["spartacus"]), "failed title_by_year test" #I wrote this one
##    assert sorted(title_by_year(["1952"])) == sorted(["othello","an american in paris"]), "failed title_by_year test" #I wrote this one
##    
##    assert sorted(title_by_year_range(["1970", "1972"])) == sorted(["the godfather", "johnny got his gun"]), "failed title_by_year_range test"
##    assert sorted(title_by_year_range(["1972", "1973"])) == sorted(["the godfather","the day of the jackal","the exorcist"]), "failed title_by_year_range test"
##    assert sorted(title_before_year(["1950"])) == sorted(["casablanca", "citizen kane", "gone with the wind", "metropolis"]), "failed title_before_year test"
##    assert sorted(title_after_year(["1990"])) == sorted(["boyz n the hood", "dead again", "the crying game", "flirting", "malcolm x"]), "failed title_after_year test"
##    assert sorted(director_by_title(["jaws"])) == sorted(["steven spielberg"]), "failed director_by_title test"
##    assert sorted(title_by_director(["steven spielberg"])) == sorted(["jaws"]), "failed title_by_director test"
##    print(sorted(actors_by_title(["jaws"])))
##    assert sorted(actors_by_title(["jaws"])) == sorted([
##            "roy scheider",
##            "robert shaw",
##            "richard dreyfuss",
##            "lorraine gary",
##            "murray hamilton",]), "failed actors_by_title test"
##    assert sorted(year_by_title(["jaws"])) == sorted(
##        [1975]
##    ), "failed year_by_title test"
##    assert sorted(year_by_title(["iceman"])) == sorted([1984]), "failed year_by_title test" #I wrote this one
##    assert sorted(title_by_actor(["orson welles"])) == sorted(
##        ["citizen kane", "othello"]
##    ), "failed title_by_actor test"
##    
##    assert sorted(search_pa_list(["hi", "there"])) == sorted(
##        ["I don't understand"]
##    ), "failed search_pa_list test 1"
##    assert sorted(search_pa_list(["who", "directed", "jaws"])) == sorted(
##        ["steven spielberg"]
##    ), "failed search_pa_list test 2"
##    assert sorted(search_pa_list(["who", "ran", "jaws"])) == sorted(
##        ["I don't understand"]
##    ), "failed search_pa_list test 2"
##    assert sorted(search_pa_list(["who", "directed", "dead again"])) == sorted(
##        ["kenneth branagh"]
##    ), "failed search_pa_list test 2"
##    assert sorted(
##        search_pa_list(["what", "movies", "were", "made", "in", "2020"])
##    ) == sorted(["No answers"]), "failed search_pa_list test 3"
##    assert sorted(
##        search_pa_list(["what", "movies", "were", "made", "in", "1900"])
##    ) == sorted(["No answers"]), "failed search_pa_list test 3"
##    assert sorted(
##        search_pa_list(["what", "movies", "were", "made", "in", "1700"])
##    ) == sorted(["No answers"]), "failed search_pa_list test 3"
##    assert sorted(search_pa_list(["who", "directed", "a star is born"])) == sorted(
##        ["george cuckor"]
##    ), "failed search_pa_list test 2"
##    assert sorted(search_pa_list(["who", "directed", "after the rehearsal"])) == sorted(
##        ["ingmar bergman"]
##    ), "failed search_pa_list test 2"
##    assert sorted(search_pa_list(["who", "acted", "in", "a star is born"])) == sorted(['judy garland', 'james mason', 'jack carson', 'tommy noonan', 'charles bickford'])
##
##
##
###_____________________________________________actors_by_year
##    assert sorted(actors_by_year(["1926"])) == sorted(["alfred abel","gustay frohlich","brigitte helm","rudolf kleinrogge","heinrich george"]), "failed actors_by_year_range test"
##
##    assert isinstance(title_by_year(["1974"]), list), "title_by_year not returning a list"
##    assert isinstance(title_by_year_range(["1970", "1972"]), list), "title_by_year_range not returning a list"
##    assert isinstance(title_before_year(["1950"]), list), "title_before_year not returning a list"
##    assert isinstance(title_after_year(["1990"]), list), "title_after_year not returning a list"
##    assert isinstance(director_by_title(["jaws"]), list), "director_by_title not returning a list"
##    assert isinstance(title_by_director(["steven spielberg"]), list), "title_by_director not returning a list"
##    assert isinstance(actors_by_title(["jaws"]), list), "actors_by_title not returning a list"
##    assert isinstance(year_by_title(["jaws"]), list), "year_by_title not returning a list"
##    assert isinstance(title_by_actor(["orson welles"]), list), "title_by_actor not returning a list"

   # print("All tests passed!")
