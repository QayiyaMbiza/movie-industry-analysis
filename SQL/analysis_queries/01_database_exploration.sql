-- =====================================================
-- DATABASE EXPLORATION
-- =====================================================

-- Total number of movies

SELECT COUNT(*) AS Total_Movies
FROM movies;


-- Total number of columns

PRAGMA table_info(movies);


-- Year Range

SELECT
    MIN(year) AS Earliest_Year,
    MAX(year) AS Latest_Year
FROM movies;


-- Average Budget

SELECT
    ROUND(AVG(budget),2) AS Average_Budget
FROM movies;


-- Average Gross Revenue

SELECT
    ROUND(AVG(gross),2) AS Average_Gross
FROM movies;


-- Average Runtime

SELECT
    ROUND(AVG(runtime),2) AS Average_Runtime
FROM movies;


-- Average Votes

SELECT
    ROUND(AVG(votes),2) AS Average_Votes
FROM movies;


-- Number of Production Companies

SELECT
    COUNT(DISTINCT company) AS Companies
FROM movies;


-- Number of Genres

SELECT
    COUNT(DISTINCT genre) AS Genres
FROM movies;