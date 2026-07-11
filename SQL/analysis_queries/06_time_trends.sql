-- =====================================================
-- TIME TRENDS
-- =====================================================

-- Revenue by Year

SELECT
    year,
    SUM(gross) AS Revenue
FROM movies
GROUP BY year
ORDER BY year;


-- Revenue by Decade

SELECT
    decade,
    SUM(gross) AS Revenue
FROM movies
GROUP BY decade
ORDER BY decade;


-- Movies Released Per Year

SELECT
    year,
    COUNT(*) AS Movies
FROM movies
GROUP BY year
ORDER BY year;