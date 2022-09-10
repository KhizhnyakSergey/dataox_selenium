from sqlalchemy.orm.session import Session
from typing import List
from database import Product


def save_products(db: Session, products=List[Product]):
    db.bulk_save_objects(products)
    db.commit()
