select phone
from {{ ref('dim_broker') }} 
where phone RLIKE '[A-Za-z]'