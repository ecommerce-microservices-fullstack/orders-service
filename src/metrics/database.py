from prometheus_client import Histogram

db_write_latency = Histogram(
    "db_write_latency_seconds", "Latency of writing order data to PostgreSQL"
)

db_read_latency = Histogram("db_read_latency_seconds", "Latency of reading order data")
