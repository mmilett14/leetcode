--https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

SELECT customer_number 
FROM(
    SELECT customer_number, COUNT(*) cnt
    FROM Orders
    GROUP BY customer_number
    ORDER BY cnt desc
    )
WHERE rownum = 1;
