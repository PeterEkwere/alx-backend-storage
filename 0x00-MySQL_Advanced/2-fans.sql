--  script that ranks country origins of bands, ordered by the number of (non-unique) fans
CREATE TEMPORARY TABLE ranking AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin;

SELECT origin, nb_fans
FROM ranking
ORDER BY nb_fans DESC;
