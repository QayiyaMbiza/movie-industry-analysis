-- =====================================================
-- BLOCKBUSTERS
-- =====================================================

-- Highest Grossing Movies

SELECT
    name,
    genre,
    company,
    gross
FROM movies
ORDER BY gross DESC
LIMIT 20;


-- Highest Profit Movies

SELECT
    name,
    profit
FROM movies
ORDER BY profit DESC
LIMIT 20;


-- Highest Budget Movies

SELECT
    name,
    budget
FROM movies
ORDER BY budget DESC
LIMIT 20;
