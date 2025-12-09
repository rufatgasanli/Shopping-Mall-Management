from src.repositories.rental_repository import RentalRepository
from src.repositories.shop_repository import ShopRepository
from src.models.rental import Rental
from src.exceptions.custom_exceptions import BusinessRuleException, NotFoundException
from src.logging_config import get_logger

logger = get_logger("RentalService")

class RentalService:
    def __init__(self):
        self.rental_repo = RentalRepository()
        self.shop_repo = ShopRepository()

    def create_rental(self, rental_id, shop_id, tenant, start, end):
        shop = self.shop_repo.get_by_id(shop_id)
        if not shop:
            raise NotFoundException("Shop", shop_id)
        
        if shop.is_rented:
            raise BusinessRuleException(f"Shop '{shop_id}' is already rented!")

        rental = Rental(rental_id, shop_id, tenant, start, end, shop.price)
        self.rental_repo.add(rental)

        shop.is_rented = True
        self.shop_repo.update(shop_id, shop)
        logger.info(f"Created Rental {rental_id} for Shop {shop_id}")

    def update_rental(self, rental_id, **kwargs):
        rental = self.rental_repo.get_by_id(rental_id)
        if not rental:
            raise NotFoundException("Rental", rental_id)
        
        for key, value in kwargs.items():
            if value and hasattr(rental, key):
                setattr(rental, key, value)
        
        self.rental_repo.update(rental_id, rental)
        logger.info(f"Updated Rental ID: {rental_id}")

    def delete_rental(self, rental_id):
        rental = self.rental_repo.get_by_id(rental_id)
        if not rental:
            raise NotFoundException("Rental", rental_id)

        shop = self.shop_repo.get_by_id(rental.shop_id)
        if shop:
            shop.is_rented = False
            self.shop_repo.update(shop.shop_id, shop)

        self.rental_repo.delete(rental_id)
        logger.info(f"Deleted Rental {rental_id}")

    def get_all_rentals(self):
        return self.rental_repo.get_all()