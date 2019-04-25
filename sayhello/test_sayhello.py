import unittest
from sayhello import db,app

class SayhelloTestCase(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED = False,
            SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        )
        db.create_all()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_page(self):
        response = self.client.get("/")
        data = response.get_data(as_text=True)
        self.assertIn("Say Hello",data)


if __name__ =="__main__":
    unittest.main()