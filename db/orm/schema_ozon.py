from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import MetaData
from db.orm.annotations import (
    IntegerPrimaryKey,
    IntegerColumnNN,
    TextColumnNN,
    ListIntegerColumn,
    BoolColumnNN,
    IntegerColumn,
    TextColumn,
    BoolColumn,
    TimestampWTColumn,
    NumericColumn,
    SmallintColumn,
    DoubleColumn,
    ListTextColumn,
    MoneyColumn,
    BigintColumn,
    ListJsonbColumn
)
from sqlalchemy import INTEGER


metadata_obj = MetaData(schema="ozon")


class Base(DeclarativeBase):
    metadata = metadata_obj


class CategoriesDimensions(Base):
    __tablename__ = "categories_dimensions"
    description_category_id = mapped_column(INTEGER, primary_key=True)
    description_category_name: Mapped[TextColumnNN]
    parent_id: Mapped[IntegerColumn]
    weight_min: Mapped[IntegerColumn]
    weight_max: Mapped[IntegerColumn]
    width_min: Mapped[IntegerColumn]
    width_max: Mapped[IntegerColumn]
    height_min: Mapped[IntegerColumn]
    height_max: Mapped[IntegerColumn]
    depth_min: Mapped[IntegerColumn]
    depth_max: Mapped[IntegerColumn]


class CategoriesAttributes(Base):
    __tablename__ = "categories_attributes"
    category_id: Mapped[IntegerPrimaryKey]
    required_attributes: Mapped[ListIntegerColumn]
    optional_attributes: Mapped[ListIntegerColumn]


class CategoriesAttributesM2M(Base):
    __tablename__ = "categories_attributes_m_2_m"
    category_id: Mapped[IntegerPrimaryKey]
    attribute_id: Mapped[IntegerColumn]
    is_required: Mapped[BoolColumn]


class Attributes(Base):
    __tablename__ = "attributes"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumnNN]
    description: Mapped[TextColumnNN]
    type: Mapped[TextColumnNN]
    is_collection: Mapped[BoolColumnNN]
    is_required: Mapped[BoolColumnNN]
    group_id: Mapped[IntegerColumn]
    group_name: Mapped[TextColumn]
    dictionary_id: Mapped[IntegerColumnNN]
    is_aspect: Mapped[BoolColumnNN]
    category_dependent: Mapped[BoolColumnNN]


class CategoriesOzonSimaland(Base):
    __tablename__ = "categories_ozon_simaland"
    simaland_category_id: Mapped[IntegerPrimaryKey]
    simaland_category_name: Mapped[TextColumn]
    ozon_category_id: Mapped[IntegerColumn]
    ozon_category_name: Mapped[TextColumn]
    is_have_items: Mapped[BoolColumn]
    is_confirmed: Mapped[BoolColumn]
    slug: Mapped[TextColumn]


class OldProducts(Base):
    __tablename__ = "old_products"
    marketplace_id: Mapped[IntegerPrimaryKey]
    offer_id: Mapped[TextColumn]
    product_id: Mapped[IntegerColumn]
    created_at: Mapped[TimestampWTColumn]
    ozon_created_at: Mapped[TimestampWTColumn]
    group_name: Mapped[TextColumn]
    state: Mapped[TextColumn]
    state_name: Mapped[TextColumn]
    validation_state: Mapped[TextColumn]
    state_description: Mapped[TextColumn]
    item_errors: Mapped[BoolColumn]
    box_height: Mapped[IntegerColumn]
    box_length: Mapped[IntegerColumn]
    box_width: Mapped[IntegerColumn]
    measures_unit: Mapped[TextColumn]
    box_weight: Mapped[IntegerColumn]
    weight_unit: Mapped[TextColumn]
    category_id: Mapped[IntegerColumn]
    updated_at: Mapped[TimestampWTColumn]
    decimal_measures: Mapped[BoolColumn]
    price: Mapped[NumericColumn]
    is_archived: Mapped[BoolColumn]
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


class ProductAttributes(Base):
    __tablename__ = "product_attributes"
    id: Mapped[IntegerPrimaryKey]
    product_id: Mapped[IntegerColumn]
    attribute_id: Mapped[IntegerColumn]
    dictionary_value_id: Mapped[IntegerColumn]
    value: Mapped[TextColumn]
    is_required: Mapped[BoolColumn]
    name: Mapped[TextColumn]
    tooltip: Mapped[TextColumn]
    dictionary_values: Mapped[ListJsonbColumn]


class Products(Base):
    __tablename__ = "products"
    simaland_product_id: Mapped[IntegerPrimaryKey]
    marketplace_id: Mapped[IntegerColumn]
    offer_id: Mapped[TextColumn]
    barcode: Mapped[TextColumn]
    vat: Mapped[DoubleColumn]
    category_id: Mapped[IntegerColumn]
    product_name: Mapped[TextColumn]
    product_description: Mapped[TextColumn]
    box_depth: Mapped[DoubleColumn]
    box_height: Mapped[DoubleColumn]
    box_weight: Mapped[DoubleColumn]
    box_width: Mapped[DoubleColumn]
    images: Mapped[ListTextColumn]
    primary_image: Mapped[TextColumn]
    images360: Mapped[ListTextColumn]
    color_image: Mapped[TextColumn]
    pdf_list: Mapped[ListTextColumn]
    old_price: Mapped[MoneyColumn]
    premium_price: Mapped[MoneyColumn]
    price: Mapped[MoneyColumn]
    task_id: Mapped[IntegerColumn]
    is_sent: Mapped[BoolColumn]
    is_published: Mapped[BoolColumn]
    is_stop: Mapped[BoolColumn]
    is_review: Mapped[BoolColumn]
    comment: Mapped[TextColumn]
    created_at: Mapped[TimestampWTColumn]
    updated_at: Mapped[TimestampWTColumn]


class TnvedCodes(Base):
    __tablename__ = "tnved_codes"
    id: Mapped[IntegerPrimaryKey]
    ozon_id: Mapped[IntegerColumn]
    value: Mapped[TextColumn]
    tnved_code: Mapped[BigintColumn]
    category_id: Mapped[IntegerColumn]