-- =====================================================
-- GENRE ANALYSIS
-- =====================================================

-- Highest Average Revenue

SELECT
    genre,
    ROUND(AVG(gross),2) AS Average_Revenue
FROM movies
GROUP BY genre
ORDER BY Average_Revenue DESC;


-- Highest Total Revenue

SELECT
    genre,
    SUM(gross) AS Total_Revenue
FROM movies
GROUP BY genre
ORDER BY Total_Revenue DESC;


-- Number of Movies per Genre

SELECT
    genre,
    COUNT(*) AS Movies
FROM movies
GROUP BY genre
ORDER BY Movies DESC;