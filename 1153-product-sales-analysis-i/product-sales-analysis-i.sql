# Write your MySQL query statement below
select product_name , year, price from Sales a left join product b
on a.product_id = b.product_id