select 
    sk_create_date, 
    sk_close_date
from {{ ref('fact_trade') }} 
where sk_close_date < sk_create_date