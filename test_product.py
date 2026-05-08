import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def test_init(self):
        p = Product("101", "Pen", 10)
        self.assertEqual(p.model, "101")
        self.assertEqual(p.name, "Pen")
        self.assertEqual(p.quantity, 10)

    def test_add_stock(self):
        p = Product("1", "Item", 10)
        p.update_stock(5)
        self.assertEqual(p.quantity, 15)

    def test_remove_stock(self):
        p = Product("1", "Item", 10)
        p.update_stock(-5)
        self.assertEqual(p.quantity, 5)

    def test_negative_error(self):
        p = Product("1", "Item", 10)
        with self.assertRaises(ValueError):
            p.update_stock(-20)

    def test_to_dict(self):
        p = Product("101", "Pen", 10)
        self.assertEqual(p.to_dict(), {
            "model": "101",
            "name": "Pen",
            "quantity": 10
        })

if __name__ == "__main__":
    unittest.main()