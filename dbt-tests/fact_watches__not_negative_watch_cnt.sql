select 
    watch_cnt
from {{ ref('fact_watches') }} 
where watch_cnt < 0