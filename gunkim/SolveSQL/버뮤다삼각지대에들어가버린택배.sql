select
  date(order_delivered_carrier_date) as delivered_carrier_date,
  count (*) as orders
from olist_orders_dataset
where
  order_delivered_customer_date is null
  AND order_delivered_carrier_date LIKE '2017-2024-01%'
  AND order_delivered_carrier_date IS NOT NULL
group by date(order_delivered_carrier_date)
order by date(order_delivered_carrier_date)
