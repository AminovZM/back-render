from sqlalchemy import Table, Column, Integer, MetaData, TIMESTAMP
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()


order = Table(
    "order",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),  # Здесь autoincrement=True указывает, что столбец будет автоматически увеличиваться
    Column("data_orders", JSONB),  # Колонка для хранения JSONB данных
    Column("id_user", Integer),
    Column("timestamp", TIMESTAMP),

)
