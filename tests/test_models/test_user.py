#!/usr/bin/python3
"""
Module for User class
"""
import os
import models
import unittest
from datetime import datetime
from models.user import User

class TestUser_save(unittest.TestCase):
    """Unittests for testing class."""

    
    def setUp(self):
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save() 

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attributes(self):
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test.user.last_name, "")
    def test_user_inherits_from_base_model(self):
        test_user = User()
        self.assertTrue(issubclass(User,BaseModel))

    def test_user_str_representation(self):
        test_user = User()
        test_user.email = "eldadfikre456@gmail.com"
        test_user.first_name = "Eldad"
        test_user.last_name = "Mamo"
        test_user.password = "password123"
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("eldadfikre456@gmail.com", user_str)
        self.assertIn("Eldad", user_str)
        self.assertIn("Mamo", user_str)

    def test_user_to_dict(self):
        test_user = User()
        test_user.email = "eldadfikre456@gmail.com"
        test_user.first_name = "Eldad"
        test_user.last_name = "Mamo"
        test_user.save()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "eldadfikre456@gmail.com")
        self.assertEqual(user_dict['first_name', "Eldad"])
        self.assertEqual(user_dict['last_name', "Mamo"])

    def test_user_instance_creation(self):
        test_user = User(email="eldadfikre456@gmail.com", password="password123"
        first_name="Eldad", last_name="Mamo")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "eldadfikre456@gmail.com")
        self.assertEqual(user_dict['password', "password123"])
        self.assertEqual(user_dict['first_name', "Eldad"])
        self.assertEqual(user_dict['last_name', "Mamo"])
    
    deftest_user_id_generation(self):
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)

if __name__ == "__main__":
    unittest.main()
