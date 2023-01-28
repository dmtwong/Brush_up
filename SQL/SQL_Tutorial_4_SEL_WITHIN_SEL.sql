/*
This tutorial looks at how we can use SELECT statements within SELECT statements to perform more complex queries.

name	continent	area	population	gdp
Afghanistan	Asia	652230	25500100	20343000000
Albania	Europe	28748	2831741	12960000000
Algeria	Africa	2381741	37100000	188681000000
Andorra	Europe	468	78115	3712000000
Angola	Africa	1246700	20609294	100990000000
...

*/


/*
Bigger than Russia
1.
List each country name where the population is larger than that of 'Russia'.

world(name, continent, area, population, gdp)
*/

SELECT name FROM world
  WHERE population >
     (SELECT population FROM world
      WHERE name='Russia')

/*
Richer than UK
2.
Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.

Per Capita GDP
*/
      
SELECT name FROM world
  WHERE GDP/population >
     (SELECT GDP/population FROM world
      WHERE name='United Kingdom') 
  AND continent = 'Europe'


/*
Neighbours of Argentina and Australia
3.

List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.
*/
SELECT name, continent FROM world
  WHERE continent in (SELECT continent FROM world
      WHERE name in ('Argentina', 'Australia') ) 
  ORDER BY name
  
/*
Between Canada and Poland
4.
Which country has a population that is more than United Kingom but less than Germany? Show the name and the population.
*/
SELECT name, population FROM world
  WHERE population > (SELECT population FROM world
      WHERE name = 'United Kingdom') 
    AND population < (SELECT population FROM world
      WHERE name = 'Germany' )

/*
Percentages of Germany
5.
Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.

Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.

The format should be Name, Percentage for example:

name	percentage
Albania	3%
Andorra	0%
Austria	11%
...	...
Decimal places
Percent symbol %
*/
SELECT name, Cast(Cast(population / (SELECT population FROM 
        world WHERE name = 'Germany') * 100 as decimal(3, 0)) 
        as varchar(5)) + '%' 
FROM world
WHERE continent = 'Europe'     
      
/*
 * Fixed by removing space before %
Wrong answer. Some of the data is incorrect.
name	
Albania	3 %
Andorra	0 %
Austria	11 %
Belarus	12 %
Belgium	14 %
Bosnia and Herzegovina	5 %
Bulgaria	9 %
Croatia	5 %
Czech Republic	13 %
Denmark	7 %
Estonia	2 %
Finland	7 %
France	82 %
Germany	100 %
Greece	14 %
Hungary	12 %
Iceland	0 %
Ireland	6 %
Italy	75 %
Kazakhstan	21 %
Latvia	2 %
Liechtenstein	0 %
Lithuania	4 %
Luxembourg	1 %
Macedonia	3 %
Malta	1 %
Moldova	4 %
Monaco	0 %
Montenegro	1 %
Netherlands	21 %
Norway	6 %
Poland	48 %
Portugal	13 %
Romania	25 %
San Marino	0 %
Serbia	9 %
Slovakia	7 %
Slovenia	3 %
Spain	58 %
Sweden	12 %
Switzerland	10 %
Ukraine	53 %
United Kingdom	79 %
Vatican City	0 %
Show what the answer should be...
name	
Albania	3%
Andorra	0%
Austria	11%
Belarus	12%
Belgium	14%
Bosnia and Herzegovina	5%
Bulgaria	9%
Croatia	5%
Czech Republic	13%
Denmark	7%
Estonia	2%
Finland	7%
France	82%
Germany	100%
Greece	14%
Hungary	12%
Iceland	0%
Ireland	6%
Italy	75%
Kazakhstan	21%
Latvia	2%
Liechtenstein	0%
Lithuania	4%
Luxembourg	1%
Macedonia	3%
Malta	1%
Moldova	4%
Monaco	0%
Montenegro	1%
Netherlands	21%
Norway	6%
Poland	48%
Portugal	13%
Romania	25%
San Marino	0%
Serbia	9%
Slovakia	7%
Slovenia	3%
Spain	58%
Sweden	12%
Switzerland	10%
Ukraine	53%
United Kingdom	79%
Vatican City	0%

*/

/*
To get a well rounded view of the important features of SQL you should move on to the next tutorial concerning aggregates.

To gain an absurdly detailed view of one insignificant feature of the language, read on.

We can use the word ALL to allow >= or > or < or <=to act over a list. For example, you can find the largest country in the world, by population with this query:

SELECT name
  FROM world
 WHERE population >= ALL(SELECT population
                           FROM world
                          WHERE population>0)
You need the condition population>0 in the sub-query as some countries have null for population.

Bigger than every country in Europe
*/

/*
6.
Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)

*/
SELECT name
  FROM world
 WHERE GDP > ALL(SELECT GDP
                           FROM world
                          WHERE GDP>0 AND continent = 
                           'Europe')
/*
 * 7.
Find the largest country (by area) in each continent, show the continent, the name and the area:
The example is known as a correlated or synchronized sub-query.

Using correlated subqueries
A correlated subquery works like a nested loop: the subquery only has access to rows related to a single record at a time in the outer query. The technique relies on table aliases to identify two different uses of the same table, one in the outer query and the other in the subquery.

One way to interpret the line in the WHERE clause that references the two table is “… where the correlated values are the same”.

In the example provided, you would say “select the country details from world where the population is greater than or equal to the population of all countries where the continent is the same”.
*/
WITH tab_1 AS (
	SELECT continent, name, area, 
	   RANK() OVER (PARTITION BY continent ORDER BY 
           area DESC) as rk_area 
	FROM world
    )
SELECT continent, name, area
FROM tab_1
WHERE rk_area = 1
/*
First country of each continent (alphabetically)
8.
List each continent and the name of the country that comes first alphabetically.
*/
WITH tab_1 AS (
	SELECT continent, name, area, 
	row_number() OVER (PARTITION BY continent ORDER BY 
           name) as rk_name 
	FROM world
    )
SELECT continent, name
FROM tab_1
WHERE rk_name = 1

/*
Difficult Questions That Utilize Techniques Not Covered In Prior Sections
9.
Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.
*/
SELECT name, continent, population 
FROM world x
WHERE NOT EXISTS (
   SELECT *
   FROM world y
   WHERE y.continent = x.continent 
   AND y.population > 25000000     
   )

/*
Three time bigger
10.
Some countries have populations more than three times that of all of their neighbours (in the same continent). Give the countries and continents.
*/
SELECT x.name, x.continent
  FROM world x
  WHERE x.population > ALL(SELECT population * 3
                            FROM world y
                            WHERE y.continent = x.continent
                            AND y.name != x.name )
/*

*/

/*

*/

/*

*/