-- =====================================================
-- ROI ANALYSIS
-- =====================================================

-- Highest ROI Movies

SELECT
    name,
    budget,
    gross,
    ROI
FROM movies
ORDER BY ROI DESC
LIMIT 20;


-- Lowest ROI Movies

SELECT
    name,
    budget,
    gross,
    ROI
FROM movies
ORDER BY ROI ASC
LIMIT 20;


-- Average ROI

SELECT
    ROUND(AVG(ROI),2) AS Average_ROI
FROM movies;