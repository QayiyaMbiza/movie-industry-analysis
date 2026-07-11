-- =====================================================
-- BUDGET VS REVENUE
-- =====================================================

-- Top 20 Highest Budget Movies

SELECT
    name,
    budget,
    gross
FROM movies
ORDER BY budget DESC
LIMIT 20;


-- Top 20 Highest Grossing Movies

SELECT
    name,
    budget,
    gross
FROM movies
ORDER BY gross DESC
LIMIT 20;


-- Top 20 Most Profitable Movies

SELECT
    name,
    budget,
    gross,
    profit
FROM movies
ORDER BY profit DESC
LIMIT 20;


-- Budget vs Gross

SELECT
    name,
    budget,
    gross
FROM movies
ORDER BY budget DESC;