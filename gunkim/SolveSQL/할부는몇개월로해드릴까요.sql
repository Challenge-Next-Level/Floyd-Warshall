select oopd.payment_installments as payment_installments,
count(distinct oopd.order_id) as order_count,
min(oopd.payment_value) as min_value,
max(oopd.payment_value) as max_value,
avg(oopd.payment_value) as avg_value
from olist_order_payments_dataset oopd
where oopd.payment_type = 'credit_card'
group by oopd.payment_installments