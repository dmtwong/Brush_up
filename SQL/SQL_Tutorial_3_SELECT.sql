/*
Show the year and subject that won 'Albert Einstein' his prize.
*/
SELECT yr, subject
  FROM nobel
 WHERE winner = 'Albert Einstein'

/*
Give the name of the 'peace' winners since the year 2000, including 2000.
*/
SELECT winner
  FROM nobel
 WHERE yr >= 2000
   AND subject = 'peace'

/*
Show all details (yr, subject, winner) of the literature prize winners for 1980 to 1989 inclusive.
*/
SELECT yr, subject, winner
  FROM nobel
 WHERE yr BETWEEN 1980 AND 1989 
   AND subject = 'literature'
   
/*
Show all details of the presidential winners:
Theodore Roosevelt
Thomas Woodrow Wilson
Jimmy Carter
Barack Obama
*/
SELECT * FROM nobel
 WHERE winner IN ('Theodore Roosevelt',
                  'Thomas Woodrow Wilson',
                  'Jimmy Carter',
		  'Barack Obama')
		  
/*
Show the winners with first name John
*/
SELECT winner FROM nobel
WHERE winner like 'John %'

/*
Show the year, subject, and name of winners for 1980 excluding chemistry and medicine
*/
SELECT yr, subject, winner
 FROM nobel
 WHERE yr = 1980
 EXCEPT 
   SELECT yr, subject, winner
   FROM nobel
   WHERE yr = 1980 and 
         subject in ('medicine', 'Chemistry')
         
/*
Show year, subject, and name of people who won a 'Medicine' prize in an early year 
(before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)
*/
SELECT yr, subject, winner
 FROM nobel
 where (yr < 1910 and subject = 'medicine') or 
       (yr >= 2004 and subject = 'literature')
       
/*
Find all details of the prize won by PETER GRÜNBERG
Non-ASCII characters
The u in his name has an umlaut. You may find this link useful https://en.wikipedia.org/wiki/%C3%9C#Keyboarding
*/
SELECT *
FROM nobel
WHERE winner LIKE 'peter gr_nberg'

/*
Escaping single quotes
You can't put a single quote in a quote string directly. You can use two single quotes within a quoted string.
*/
SELECT *
FROM nobel
WHERE winner like 'eugene o_neill'

/*
List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order.
*/
SELECT winner, yr, subject
FROM nobel
WHERE winner like 'Sir %'
ORDER BY yr DESC, winner

/*
Show the 1984 winners and subject ordered by subject and winner name; but list chemistry and physics last.
*/
SELECT winner, subject
FROM nobel
WHERE yr = 1984
ORDER BY
    case
        when subject in ('Chemistry', 'Physics') then 1
        else 0
    end
    , subject
    , winner