import unittest
import sys
import os
import shutil

# Add the src folder to the system path so modules can be found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.shop import Shop
from src.services.shop_service import ShopService
from src.repositories.base_repository import BaseRepository

class TestShop(unittest.TestCase):
    
    def setUp(self):
        """Runs before each test. Creates a separate directory for test data."""
        # To prevent modifying the original data.json, we override the test database path
        self.test_db_path = "tests/test_data/data.json"
        
        # Temporarily override the repository path (normally done via config files in real projects)
        import src.repositories.base_repository as repo_module
        repo_module.DB_PATH = self.test_db_path
        
        self.service = ShopService()

    def tearDown(self):
        """Runs after each test. Cleans up created files."""
        if os.path.exists("tests/test_data"):
            shutil.rmtree("tests/test_data")

    def test_shop_model_creation(self):
        """Checks whether the Shop object is created correctly"""
        shop = Shop("101", "Nike", "Ali", "Sport", 500)
        self.assertEqual(shop.name, "Nike")
        self.assertEqual(shop.price, 500.0)
        self.assertFalse(shop.is_rented)  # Default must be False

    def test_create_shop_service(self):
        """Checks creation of a shop via the service layer"""
        self.service.create_shop("102", "Adidas", "Vali", "Sport", 600)
        
        shops = self.service.get_all_shops()
        self.assertEqual(len(shops), 1)
        self.assertEqual(shops[0].shop_id, "102")

    def test_delete_shop(self):
        """Checks deletion of a shop"""
        self.service.create_shop("103", "Puma", "Hasan", "Sport", 400)
        self.service.delete_shop("103")
        
        shops = self.service.get_all_shops()
        self.assertEqual(len(shops), 0)

if __name__ == '__main__':
    unittest.main()
