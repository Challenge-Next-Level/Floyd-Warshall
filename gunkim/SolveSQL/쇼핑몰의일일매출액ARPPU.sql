SELECT date(order_purchase_timestamp) as dt
     , count(distinct customer_id) as pu
     , round(sum(payment_value),2) as revenue_daily
     , round(sum(payment_value) /count(distinct customer_id),2) as arppu
FROM olist_orders_dataset as o1
LEFT JOIN olist_order_payments_dataset AS o2
ON o1.order_id = o2.order_id
WHERE order_purchase_timestamp >= '2018-01-01'
GROUP BY date(order_purchase_timestamp)
;