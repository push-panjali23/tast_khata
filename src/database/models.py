from sqlalchemy import (
    Column,
    Integer,
    String,
    DECIMAL,
    ForeignKey,
    TIMESTAMP,
    create_engine,
    func,
)
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Define the base class for the ORM models
Base = declarative_base()

# Customers Table
class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    mob = Column(String(15), nullable=False, unique=True)
    remaining_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)  # Tracks pending balance
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    orders = relationship("Order", back_populates="customer", cascade="all, delete")


# Orders Table
class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # Relationships
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete")



# Order Items Table
class OrderItem(Base):
    __tablename__ = "order_items"   

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    product_type = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    rate = Column(DECIMAL(10, 2), nullable=False)
    tax = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    amount = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    order = relationship("Order", back_populates="items")
