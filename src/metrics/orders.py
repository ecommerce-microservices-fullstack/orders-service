from prometheus_client import Counter

orders_total = Counter("orders_total", "Total orders created")
orders_success_total = Counter("orders_success_total", "Total successful orders")
orders_failed_total = Counter("orders_failed_total", "Total failed orders")
