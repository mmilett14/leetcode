-- https://leetcode.com/problems/rising-temperature/

SELECT 
    Id 
    
FROM
    Weather a
    
WHERE
    a.Temperature > (SELECT Temperature FROM Weather b WHERE b.RecordDate = a.RecordDate - 1);
