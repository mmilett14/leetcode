SELECT
    Email
    
FROM
    Person
    
GROUP BY Email

HAVING SUM(1) > 1;
