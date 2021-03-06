/* in this part of the project you will analyze data from Twitch using SQL */

/* inspect the stream and chat table */
SELECT * FROM stream
LIMIT 20;

SELECT * FROM chat
LIMIT 20;

SELECT DISTINCT game
FROM stream;

SELECT DISTINCT channel
FROM stream;

/* most popular games in the stream table */
SELECT COUNT(*) AS 'number of users per game', game
FROM stream
GROUP BY game
ORDER BY 1 DESC;

/* the most popular game appears to  be 'League of Legends'. Find out where those viewers are located */
SELECT COUNT(*) AS 'number of users per country', country
FROM stream 
WHERE game = 'League of Legends'
GROUP BY country
ORDER BY 1 DESC;

/* a list of different sources users use to view the stream */
SELECT COUNT(*) AS 'number of users per player', player
FROM stream
GROUP BY 2
ORDER BY 1 DESC;

/* create a new column with genre and group each of the games into their genres */
SELECT game,
  CASE
    WHEN game = 'League of Legends' THEN 'MOBA'
    WHEN game = 'Dota 2' THEN 'MOBA'
    WHEN game = 'Heroes of the Storm' THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive' THEN 'FPS'
    WHEN game = 'DayZ' THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved' THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*) AS 'number of users per genre'
FROM stream
GROUP BY 2
ORDER BY 3 DESC;
 
/* how does view count change in the course of a day in the US */
SELECT time 
FROM stream
LIMIT 10;

SELECT time, 
    strftime('%S', time) AS 'seconds of streamtime'
FROM stream
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', time) AS 'hour of streamtime',
  COUNT(*) AS 'number of viewers per hour'
FROM stream
WHERE country = 'US'
GROUP BY 1;

/* join the stream and chat table on their shared column */
SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;  
