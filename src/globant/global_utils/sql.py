group_q_numbers_employess='''
select c.department,
       c.job,
       sum(q1) q1 ,
       sum(q2) q2,
       sum(q3) q3,
       sum(q4) q4
from vw_group_hired 
where vw_group_hired.year = :x
group by 1,2
limit 10'''


total_numbers_employess_hired ='''
select 
    id,
    department, 
    year,
    hired
from vw_total_hired
where vw_total_hired.year = :x
'''