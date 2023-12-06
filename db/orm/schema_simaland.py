from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import MetaData
from sqlalchemy.dialects.postgresql import JSONB
from db.orm.annotations import (
    IntegerPrimaryKey,
    TextColumn,
    IntegerColumn,
    BoolColumn,
    NumericColumn,
    ListTextColumn,
    TimestampWTColumn, 
    DoubleColumn
)


metadata_obj = MetaData(schema="simaland")


class Base(DeclarativeBase):
    metadata = metadata_obj


class Categories(Base):
    __tablename__ = "categories"
    category_id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]
    level: Mapped[IntegerColumn]
    slug: Mapped[TextColumn]
    path: Mapped[TextColumn]
    is_leaf: Mapped[BoolColumn]
    is_adult: Mapped[BoolColumn]
    icon: Mapped[TextColumn]
    page: Mapped[IntegerColumn]
    is_connect_ozon: Mapped[BoolColumn]


class Items(Base):
    __tablename__ = "items"
    id: Mapped[IntegerPrimaryKey]
    sid: Mapped[IntegerColumn]
    name: Mapped[TextColumn]
    description: Mapped[TextColumn]
    slug: Mapped[TextColumn]
    price: Mapped[NumericColumn]
    balance: Mapped[TextColumn]
    box_depth: Mapped[IntegerColumn]
    box_height: Mapped[IntegerColumn]
    box_width: Mapped[IntegerColumn]
    depth: Mapped[IntegerColumn]
    height: Mapped[IntegerColumn]
    width: Mapped[IntegerColumn]
    weight: Mapped[IntegerColumn]
    is_price_fixed: Mapped[BoolColumn]
    is_adult: Mapped[BoolColumn]
    is_markdown: Mapped[BoolColumn]
    trademark_id: Mapped[IntegerColumn]
    country_id: Mapped[IntegerColumn]
    unit_id: Mapped[IntegerColumn]
    nested_unit_id: Mapped[IntegerColumn]
    base_photo_url: Mapped[TextColumn]
    minimum_order_quantity: Mapped[IntegerColumn]
    min_qty: Mapped[IntegerColumn]
    qty_multiplier: Mapped[IntegerColumn]
    is_paid_delivery: Mapped[BoolColumn]
    supply_period: Mapped[IntegerColumn]
    is_remote_store: Mapped[BoolColumn]
    parent_item_id: Mapped[IntegerColumn]
    barcodes: Mapped[TextColumn]
    is_exclusive: Mapped[BoolColumn]
    category_id: Mapped[IntegerColumn]
    settlements_balance = mapped_column(JSONB)
    wholesale_price: Mapped[NumericColumn]
    price_max: Mapped[NumericColumn]
    is_protected: Mapped[BoolColumn]
    wholesale = mapped_column(JSONB)
    vat: Mapped[IntegerColumn]
    page: Mapped[IntegerColumn]
    generated_urls: Mapped[TextColumn]
    is_upload_ozon: Mapped[BoolColumn]
    is_sent_ozon: Mapped[BoolColumn]
    is_photo_processed: Mapped[BoolColumn]
    trademark: Mapped[TextColumn]
    country: Mapped[TextColumn]
    unit: Mapped[TextColumn]
    is_blacklist: Mapped[BoolColumn]


class DataType(Base):
    __tablename__ = "data_type"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]


class ItemAttribute(Base):
    __tablename__ = "item_attribute"
    id: Mapped[IntegerPrimaryKey]
    attribute_id: Mapped[IntegerColumn]
    item_id: Mapped[IntegerColumn]
    boolean_value: Mapped[BoolColumn]
    int_value: Mapped[IntegerColumn]
    float_value: Mapped[DoubleColumn]
    option_value: Mapped[IntegerColumn]
    numrange_value: Mapped[TextColumn]
    on_page: Mapped[IntegerColumn]


class SimaAttribute(Base):
    __tablename__ = "sima_attribute"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]
    description: Mapped[TextColumn]
    data_type_id: Mapped[IntegerColumn]
    unit_id: Mapped[IntegerColumn]


class SimaOption(Base):
    __tablename__ = "sima_option"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]


class Unit(Base):
    __tablename__ = "unit"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]



    