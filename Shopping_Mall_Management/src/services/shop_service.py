from src.repositories.shop_repository import ShopRepository
from src.models.shop import Shop
from src.logging_config import get_logger
from src.exceptions.custom_exceptions import ValidationException, NotFoundException

logger = get_logger("ShopService")

class ShopService:
    def __init__(self):
        self.repo = ShopRepository()

    def create_shop(self, shop_id, name, owner, category, price):
        if self.repo.get_by_id(shop_id):
            logger.warning(f"Attempt to create existing shop ID {shop_id}")
            raise ValidationException("shop_id", f"ID '{shop_id}' already exists")
        
        new_shop = Shop(shop_id, name, owner, category, price)
        self.repo.add(new_shop)
        logger.info(f"Created Shop: {name} (ID: {shop_id})")

    def get_all_shops(self):
        return self.repo.get_all()

    def update_shop(self, shop_id, **kwargs):
        shop = self.repo.get_by_id(shop_id)
        if not shop:
            raise NotFoundException("Shop", shop_id)
        
        for key, value in kwargs.items():
            if hasattr(shop, key) and value:
                setattr(shop, key, value)
        
        self.repo.update(shop_id, shop)
        logger.info(f"Updated Shop ID: {shop_id}")

    def delete_shop(self, shop_id):
        # If repository itself raises NotFoundException, no need to change it.
        # But ideally, we check first and raise our own "smart" exception.
        if not self.repo.get_by_id(shop_id):
            raise NotFoundException("Shop", shop_id)

        self.repo.delete(shop_id)
        logger.info(f"Deleted Shop ID: {shop_id}")
