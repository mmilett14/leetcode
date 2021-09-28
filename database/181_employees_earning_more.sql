-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT 
    a.Name Employee 

FROM 
    Employee a 

    INNER JOIN Employee b 
    
    ON a.ManagerId = b.Id 

WHERE 
    a.Salary > b.Salary;
