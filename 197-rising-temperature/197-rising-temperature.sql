# Write your MySQL query statement below

select Weather.id from Weather join weather w on DATEDIFF(Weather.recordDate, w.recordDate) = 1 and Weather.temperature > w.temperature;