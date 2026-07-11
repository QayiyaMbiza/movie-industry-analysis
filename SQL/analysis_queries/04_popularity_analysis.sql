-- =====================================================
-- POPULARITY ANALYSIS
-- =====================================================

-- Highest Rated Movies

SELECT
    name,
    score,
    gross
FROM movies
ORDER BY score DESC
LIMIT 20;


-- Most Voted Movies

SELECT
    name,
    votes,
    gross
FROM movies
ORDER BY votes DESC
LIMIT 20;


-- Revenue vs Score

SELECT
    name,
    score,
    gross
FROM movies
ORDER BY score DESC;


-- Revenue vs Votes

SELECT
    name,
    votes,
    gross
FROM movies
ORDER BY votes DESC;