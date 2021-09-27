-- https://leetcode.com/problems/customers-who-never-order/

select Name as Customers
FROM
Customers a 
LEFT JOIN Orders b
ON a.Id = b.CustomerId
where b.CustomerId is null;
