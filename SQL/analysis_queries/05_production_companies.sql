-- =====================================================
-- PRODUCTION COMPANIES
-- =====================================================

-- Highest Revenue Companies

SELECT
    company,
    SUM(gross) AS Total_Revenue
FROM movies
GROUP BY company
ORDER BY Total_Revenue DESC
LIMIT 20;


-- Movie Count

SELECT
    company,
    COUNT(*) AS Movie_Count
FROM movies
GROUP BY company
ORDER BY Movie_Count DESC
LIMIT 20;


-- Average Revenue

SELECT
    company,
    ROUND(AVG(gross),2) AS Average_Revenue
FROM movies
GROUP BY company
ORDER BY Average_Revenue DESC
LIMIT 20;