from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("category", String),
    Column("price", Integer),
    Column("remainder", String),
)
