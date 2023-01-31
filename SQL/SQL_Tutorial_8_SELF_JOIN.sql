/*
stops(id,                  name)
route(num, company, pos,   stop)
Edinburgh Buses
This database consists of two tables: stops and routes

stops
This is a list of areas served by buses. The detail does not really include each actual bus stop - just areas within Edinburgh and whole towns near Edinburgh.

Field	Type	Notes
id	INTEGER	Arbitrary value
name	CHAR(30)	The name of an area served by at least one bus
route
A route is the path through town taken by a bus.

Field	Type	Notes
num	CHAR(5)	The number of the bus - as it appears on the front of the vehicle. Oddly these numbers often include letters
company	CHAR(3)	Several bus companies operate in Edinburgh. The main one is Lothian Region Transport - LRT
pos	INTEGER	This indicates the order of the stop within the route. Some routes may revisit a stop. Most buses go in both directions.
stop	INTEGER	This references the stops table
As different companies use numbers arbitrarily the num and the company are both required to identify a route.

Footnotes
This data has been scanned in from the Edinburgh Travelmap published by TRAVELINE, City of Edinburgh Council.
TRAVELINE is your one-stop information point for details of all local public transport services in Lothian, and complementary facilities provided by The City of Edinburgh Council. To contact TRAVELINE you can phone:
0800 23 23 23 local calls
0131 225 38 58 national calls.

Many infrequent services have been omitted
Many route variations have been ignored. These include peak time limited stop services and truncated services.

1.
How many stops are in the database.
*/
SELECT count(id)
FROM stops
/*
2.
Find the id value for the stop 'Craiglockhart'
*/
SELECT id
FROM stops
where name = 'Craiglockhart'
/*
3.
Give the id and the name for the stops on the '4' 'LRT' service.
SELECT route.stop, stops.name
FROM route
JOIN stops
ON route.num = stops.id
WHERE num = '4' AND company = 'LRT'

*/
SELECT A.stop, stops.name
FROM ( SELECT *
       FROM route
       WHERE num = '4' AND company = 'LRT') A
JOIN stops
ON A.stop = stops.id
/*
Routes and stops
4.
The query shown gives the number of routes that visit either London Road (149) or Craiglockhart (53).
Run the query and notice the two services that link these stops have a count of 2. Add a HAVING clause to restrict the output to these two routes.
*/
SELECT company, num, COUNT(*)
FROM route WHERE stop=149 OR stop=53
GROUP BY company, num
HAVING COUNT(*) = 2
/*
5.
Execute the self join shown and observe that b.stop gives all the places you can get to from Craiglockhart, 
without changing routes. Change the query so that it shows the services from Craiglockhart to London Road.
*/
SELECT a.company, a.num, a.stop, b.stop
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
WHERE a.stop=53 and b.stop = 149
/*
6.
The query shown is similar to the previous one, however by joining two copies of the stops table we can refer to stops by name rather than by number. 
Change the query so that the services between 'Craiglockhart' and 'London Road' are shown. If you are tired of these places try 'Fairmilehead' against 'Tollcross'
*/
SELECT a.company, a.num, stopa.name, stopb.name
FROM route a JOIN route b ON
  (a.company=b.company AND a.num=b.num)
  JOIN stops stopa ON (a.stop=stopa.id)
  JOIN stops stopb ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'and stopb.name = 'London Road' 
/*
Using a self join
7.
Give a list of all the services which connect stops 115 and 137 ('Haymarket' and 'Leith')
*/
SELECT DISTINCT A.company, B.num
FROM route AS A
JOIN route AS B
ON (A.company = B.company) AND (A.num = B.num)
WHERE A.stop = 115 AND B.stop = 137

/*
8.
Give a list of the services which connect the stops 'Craiglockhart' and 'Tollcross'
*/
SELECT a.company, a.num
FROM route a 
JOIN route b 
ON (a.company=b.company
    AND a.num=b.num)
JOIN stops stopa 
ON (a.stop=stopa.id)
JOIN stops stopb 
ON (b.stop=stopb.id)
WHERE stopa.name='Craiglockhart'and stopb.name = 'Tollcross' 
/*
9.
Give a distinct list of the stops which may be reached from 'Craiglockhart' by taking one bus, 
including 'Craiglockhart' itself, offered by the LRT company. Include the company and bus no. of the relevant services.

name	company	num
Balerno	LRT	47
Balerno Church	LRT	47
Bingham	LRT	4
Brunstane	LRT	45
Canonmills	LRT	27
Canonmills	LRT	47
Cockburn Crescent	LRT	47
Colinton	LRT	10
Colinton	LRT	45
Colinton	LRT	47
Craiglockhart	LRT	10
Craiglockhart	LRT	27
Craiglockhart	LRT	4
Craiglockhart	LRT	45
Craiglockhart	LRT	47
Crewe Toll	LRT	27
Currie	LRT	45
Currie	LRT	47
Duddingston	LRT	45
Fairmilehead	LRT	4
Hanover Street	LRT	27
Hanover Street	LRT	45
Hanover Street	LRT	47
Haymarket	LRT	4
Hillend	LRT	4
Hunters Tryst	LRT	27
Leith	LRT	10
Leith Walk	LRT	10
London Road	LRT	4
London Road	LRT	45
Muirhouse	LRT	10
Newhaven	LRT	10
Northfield	LRT	4
Northfield	LRT	45
Oxgangs	LRT	27
Oxgangs	LRT	4
Princes Street	LRT	10
Princes Street	LRT	4
Riccarton Campus	LRT	45
Silverknowes	LRT	10
Silverknowes	LRT	27
Tollcross	LRT	10
Tollcross	LRT	27
Tollcross	LRT	45
Tollcross	LRT	47
Torphin	LRT	10

*/
SELECT stopB.name, A.company, B.num
FROM route AS A
JOIN route AS B
ON (A.company = B.company) AND (A.num = B.num)
  JOIN stops stopa ON (A.stop=stopa.id)
  JOIN stops stopb ON (B.stop=stopb.id)
WHERE stopA.name = 'Craiglockhart' and A.company = 'LRT'
ORDER BY stopB.name
/*
10.
Find the routes involving two buses that can go from Craiglockhart to Lochend.
Show the bus no. and company for the first bus, the name of the stop for the transfer,
and the bus no. and company for the second bus.
*/
/*
Result:
company	num	name	name
Show what the answer should be...
num	company	name	num	company
10	LRT	Leith	34	LRT
10	LRT	Leith	35	LRT
10	LRT	Leith	87	LRT
10	LRT	Leith	C5	SMT
10	LRT	Princes Street	65	LRT
10	LRT	Princes Street	C5	SMT
27	LRT	Canonmills	34	LRT
27	LRT	Canonmills	35	LRT
27	LRT	Crewe Toll	20	LRT
4	LRT	Haymarket	65	LRT
4	LRT	Haymarket	C5	SMT
4	LRT	London Road	20	LRT
4	LRT	London Road	34	LRT
4	LRT	London Road	35	LRT
4	LRT	London Road	42	LRT
4	LRT	London Road	46A	LRT
4	LRT	London Road	65	LRT
4	LRT	London Road	87	LRT
4	LRT	London Road	87A	LRT
4	LRT	London Road	C5	SMT
4	LRT	Princes Street	65	LRT
4	LRT	Princes Street	C5	SMT
45	LRT	Duddingston	42	LRT
45	LRT	Duddingston	46A	LRT
45	LRT	London Road	20	LRT
45	LRT	London Road	34	LRT
45	LRT	London Road	35	LRT
45	LRT	London Road	42	LRT
45	LRT	London Road	46A	LRT
45	LRT	London Road	65	LRT
45	LRT	London Road	87	LRT
45	LRT	London Road	87A	LRT
45	LRT	London Road	C5	SMT
45	LRT	Riccarton Campus	65	LRT
47	LRT	Canonmills	34	LRT
47	LRT	Canonmills	35	LRT

*/

/*
WHERE s1.name = 'Craiglockhart'
AND s2.name = 'Lochend'
*/
SELECT t1.num, t1.company, t1.name2, t2.num, t2.company
FROM (SELECT DISTINCT a.num, a.company, stopa.id AS id1, 
             stopa.name AS name1, 
             stopb.id AS id2,     
             stopb.name AS name2
      FROM route a 
      JOIN route b 
      ON (a.company=b.company AND a.num=b.num)
         JOIN stops stopa ON (a.stop=stopa.id)
         JOIN stops stopb ON (b.stop=stopb.id)
    ) AS t1
JOIN (SELECT DISTINCT a.num, a.company, stopa.id AS id1, 
             stopa.name AS name1, 
             stopb.id AS id2,     
             stopb.name AS name2
      FROM route a 
      JOIN route b 
      ON (a.company=b.company AND a.num=b.num)
         JOIN stops stopa ON (a.stop=stopa.id)
         JOIN stops stopb ON (b.stop=stopb.id)
    ) AS t2
ON t1.name2 = t2.name1
WHERE t1.name1 = 'Craiglockhart' 
  AND t2.name2 = 'Lochend' 
/*

*/

/*

*/
/*

*/

/*

*/

/*

*/
/*

*/

/*

*/

/*

*/

/*

*/