from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import JSONB
from db.orm.annotations import (
    IntegerPrimaryKey,
    TextColumn,
    IntegerColumn,
    BoolColumn,
    NumericColumn,
    TimestampWTColumn, 
    SmallintColumn
)


metadata_obj = MetaData(schema="public")


class Base(DeclarativeBase):
    metadata = metadata_obj


class MxProductsOzon(Base):
    __tablename__ = "mx_products_ozon"
    marketplace_id: Mapped[IntegerPrimaryKey]
    offer_id: Mapped[TextColumn] = mapped_column(
        nullable=False,
        index=True,
    )
    product_id: Mapped[IntegerColumn] = mapped_column(index=True)
    created_at: Mapped[TimestampWTColumn] = mapped_column(
        nullable=False,
        server_default="timezone('Europe/Moscow'::text, CURRENT_TIMESTAMP)",
    )
    ozon_created_at: Mapped[TimestampWTColumn]
    group_name: Mapped[TextColumn]
    state: Mapped[TextColumn]
    state_name: Mapped[TextColumn] = mapped_column(index=True)
    validation_state: Mapped[TextColumn]
    state_description: Mapped[TextColumn]
    item_errors: Mapped[BoolColumn]
    box_height: Mapped[IntegerColumn]
    box_length: Mapped[IntegerColumn]
    box_width: Mapped[IntegerColumn]
    measures_unit: Mapped[TextColumn]
    box_weight: Mapped[IntegerColumn]
    weight_unit: Mapped[TextColumn]
    category_id: Mapped[IntegerColumn] = mapped_column(index=True)
    updated_at: Mapped[TimestampWTColumn] = mapped_column(
        nullable=False,
        server_default="timezone('Europe/Moscow'::text, CURRENT_TIMESTAMP)",
        index=True,
    )
    decimal_measures: Mapped[BoolColumn] = mapped_column(server_default="false")
    price: Mapped[NumericColumn]
    is_archived: Mapped[BoolColumn] = mapped_column(
        nullable=False,
        server_default="false",
        index=True,
    )
    product_name: Mapped[TextColumn]
    product_description: Mapped[TextColumn]
    task_id: Mapped[IntegerColumn]
    fbo_stock: Mapped[SmallintColumn]
    fbs_stock: Mapped[SmallintColumn]
    barcode: Mapped[TextColumn]
    price_index: Mapped[TextColumn]
    external_min_price: Mapped[NumericColumn]
    external_price_index: Mapped[NumericColumn]
    ozon_min_price: Mapped[NumericColumn]
    ozon_price_index: Mapped[NumericColumn]
    self_min_price: Mapped[NumericColumn]
    self_price_index: Mapped[NumericColumn]
