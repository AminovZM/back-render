from sqlalchemy import Table, Column, Integer, MetaData

metadata = MetaData()

basket = Table(
    "basket",
    metadata,
    Column("id", Integer),
    Column("quantity", Integer),
    Column("id_user", Integer)
)
