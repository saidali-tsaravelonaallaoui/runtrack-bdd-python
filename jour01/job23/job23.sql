SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant);
-- -- Autre méthode
SELECT * FROM etudiant ORDER BY age DESC LIMIT 1;