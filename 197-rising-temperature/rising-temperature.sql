# Write your MySQL query statement below
select w2.id from Weather as w1 inner join Weather as w2
where subdate(w2.recordDate,1) = w1.recordDate and 
w2.temperature > w1.temperature