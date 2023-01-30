/*
 *This tutorial introduces the notion of a join. The database consists of three tables movie , actor and casting .

movie: id	title	yr	director	budget	gross 
actor: id	name 
casting:    movieid	actorid	ord

Movie Database
This database features two entities (movies and actors) in a many-to-many relation. Each entity has its own table. A third table, casting , is used to link them. The relationship is many-to-many because each film features many actors and each actor has appeared in many films.
movie
Field name	         Type	Notes
id	               INTEGER	An arbitrary unique identifier
title	           CHAR(70)	The name of the film - usually in the language of the first release.
yr	               DECIMAL(4)	Year of first release.
director	       INT	A reference to the actor table.
budget				INTEGER	How much the movie cost to make (in a variety of currencies unfortunately).
gross				INTEGER	How much the movie made at the box office.
Example
id	 	  title					yr	  director	budget	gross
10003	"Crocodile" Dundee II	1988	38	15800000	239606210
10004	'Til There Was You	   1997	    49	10000000	

actor
Field name			Type	Notes
id					INTEGER	An arbitrary unique identifier
name				CHAR(36)	The name of the actor (the term actor is used to refer to both male and female thesps.)
Example
id	name
20	Paul Hogan
50	Jeanne Tripplehorn

casting
Field name				Type	Notes
movieid					INTEGER	A reference to the movie table.
actorid					INTEGER	A reference to the actor table.
ord						INTEGER	The ordinal position of the actor in the cast list. The
star of the movie will have ord value 1 the co-star will have value 2, ...
Example
movieid	actorid	ord
10003	20	4
10004	50	1

*/
/*
1962 movies
1.
List the films where the yr is 1962 [Show id, title]
*/
SELECT id, title
 FROM movie
 WHERE yr=1962
/*
When was Citizen Kane released?
2.
Give year of 'Citizen Kane'.
*/
SELECT yr
 FROM movie
 WHERE title =  'Citizen Kane'
/*
Star Trek movies
3.
List all of the Star Trek movies, include the id, title and yr (all of these movies include the words Star Trek in the title). Order results by year.
*/
SELECT id, title, yr
 FROM movie
 WHERE title like 'Star Trek%'
/*
id for actor Glenn Close
4.
What id number does the actor 'Glenn Close' have?
*/
SELECT id
 FROM actor
 WHERE name = 'Glenn Close'
/*
id for Casablanca
5.
What is the id of the film 'Casablanca'
*/
SELECT id
 FROM movie
 WHERE title = 'Casablanca' 

/*
Cast list for Casablanca
6.
Obtain the cast list for 'Casablanca'.

what is a cast list?
Use movieid=11768, (or whatever value you got from the previous question)
*/
SELECT actor.name
FROM actor
JOIN casting
ON casting.actorid = actor.id
WHERE casting.movieid = 27;

/*
Alien cast list
7.
Obtain the cast list for the film 'Alien'
*/
SELECT actor.name
FROM actor
JOIN casting
ON casting.actorid = actor.id
WHERE casting.movieid = (
    SELECT id
    FROM movie
    where title = 'Alien')
/*
Harrison Ford movies
8.
List the films in which 'Harrison Ford' has appeared
*/
SELECT title
FROM movie
where id in (SELECT movieid
  FROM casting 
  WHERE actorid = (SELECT id
   FROM actor
   WHERE name = 'Harrison Ford') 
)
/*
Harrison Ford as a supporting actor
9.
List the films where 'Harrison Ford' has appeared - but not in the starring role. 
[Note: the ord field of casting gives the position of the actor. If ord=1 then this actor is in the starring role]
*/
SELECT title
FROM movie
where id in (SELECT movieid
  FROM casting 
  WHERE (actorid = (SELECT id FROM actor WHERE name = 'Harrison Ford' ) ) 
        and (ord <> 1)
)
/*
Lead actors in 1962 movies
10.
List the films together with the leading star for all 1962 films.
*/
SELECT movie.title, actor.name
FROM movie
JOIN casting
ON movie.id = casting.movieid
JOIN actor
ON casting.actorid = actor.id
WHERE movie.yr = 1962
AND casting.ord = 1;
/*
Busy years for Rock Hudson
11.
Which were the busiest years for 'Rock Hudson', show the year and the number of movies he made each year for any year in which he made more than 2 movies.
*/
SELECT yr, COUNT(title) FROM
  movie JOIN casting ON movie.id = casting.movieid
        JOIN actor   ON casting.actorid = actor.id
WHERE name = 'Rock Hudson'
GROUP BY yr
HAVING COUNT(title) > 1
/*
Lead actor in Julie Andrews movies
12.
List the film title and the leading actor for all of the films 'Julie Andrews' played in.

Did you get "Little Miss Marker twice"?
*/
SELECT A.title, B.name
FROM (SELECT movie.*
      FROM movie
      JOIN casting
      ON casting.movieid = movie.id
      JOIN actor
      ON actor.id = casting.actorid
      WHERE actor.name = 'Julie Andrews') AS A
JOIN (SELECT actor.*, casting.movieid AS movieid
      FROM actor
      JOIN casting
      ON casting.actorid = actor.id
      WHERE casting.ord = 1) as B
ON A.id = B.movieid
ORDER BY A.title;
/*
Actors with 15 leading roles
13.
Obtain a list, in alphabetical order, of actors who've had at least 15 starring roles.
*/
SELECT actor.name
FROM actor
JOIN casting
ON actor.id = casting.actorid
WHERE casting.ord = 1
GROUP BY actor.name
HAVING COUNT(*) >= 15

/*
released in the year 1978
14.
List the films released in the year 1978 ordered by the number of actors in the cast, then by title.


*/
SELECT B.title, COUNT(B.title) 
FROM casting 
JOIN (SELECT id, title
FROM movie
where yr = 1978) B
on casting.movieid = B.id
GROUP BY title
ORDER BY COUNT(B.title) DESC, title
/*

*/