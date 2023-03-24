SELECT date(order_purchase_timestamp) as dt
     , round(sum(payment_value),2) as revenue_daily
FROM olist_orders_dataset as o1
LEFT JOIN olist_order_payments_dataset AS o2
ON o1.order_id = o2.order_id
WHERE order_purchase_timestamp >= '2018-01-01'
GROUP BY date(order_purchase_timestamp)
;