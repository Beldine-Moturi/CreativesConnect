#!/usr/bin/python3
"""Contains test cases for the BaseModel class"""
from datetime import datetime
from models.base_model import BaseModel
import time
import unittest


t_format = "%Y-%m-%dT%H:%M:%S.%f"


class TestBaseModelClassInstantiation(unittest.TestCase):
    """Tests the Instantiation of Base Model class objects
    and attribute assignment"""

    def setUp(self):
        """sets up the resources required to run the tests"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """deletes the resources used after tests are run"""

        del self.model1
        del self.model2

    def test_instantiation(self):
        """Tests that objects of this class are correctly created"""

        self.assertIs(type(self.model1), BaseModel)
        attr_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
        }

        for attr, typ in attr_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertTrue(hasattr(self.model1, attr))
                self.assertIs(type(self.model1.__dict__[attr]), typ)

    def test_id_attribute(self):
        """Tests that the id attribute is a valid
        universally unique identifier(uuid)"""

        for obj in [self.model1, self.model2]:
            uuid = obj.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""

        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_intantiation_with_kwargs(self):
        """Tests that objects can properly be created with the
        kwargs argument"""

        attributes = ['id', 'created_at', 'updated_at']

        my_model = BaseModel(**{})
        self.assertNotIn('__class__', my_model.__dict__)
        for att in attributes:
            with self.subTest(att=att):
                self.assertTrue(hasattr(my_model, att))

        model1_json = self.model1.to_dict()
        new_model1 = BaseModel(**model1_json)
        self.assertNotIn('__class__', new_model1.__dict__)
        self.assertEqual(len(new_model1.__dict__), len(self.model1.__dict__))
        for att in attributes:
            with self.subTest(att=att):
                self.assertTrue(hasattr(new_model1, att))
                self.assertEqual(
                    new_model1.__dict__[att],
                    self.model1.__dict__[att]
                    )

        self.model2.name = "My_Second_model"
        self.model2.number = 100
        model2_json = self.model2.to_dict()
        new_model2 = BaseModel(**model2_json)
        self.assertNotIn('__class__', new_model1.__dict__)
        self.assertEqual(len(self.model2.__dict__), len(new_model2.__dict__))
        attributes.extend(['name', 'number'])
        for att in attributes:
            with self.subTest(att=att):
                self.assertTrue(hasattr(new_model2, att))
                if att not in ["created_at", "updated_at"]:
                    self.assertEqual(
                        new_model2.__dict__[att],
                        self.model2.__dict__[att]
                        )


class TestBaseModelClassMethods(unittest.TestCase):
    """defines functions that test the methods defined in the Base class"""

    def setUp(self):
        """Sets up the resources needed to run the tests"""

        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        """Deletes the resources created when running the tests"""

        del self.model1
        del self.model2

    def test_save_method(self):
        """Tests that this methods correctly updates the public instance
        attribute updated_at with the current datetime when called"""

        old = self.model1.updated_at
        self.model1.save()
        new = self.model1.updated_at
        self.assertNotEqual(old, new)

    def test_str_method(self):
        """Tests that the __str__ method correctly returns
        a string representation of objects of this class"""

        string = "[BaseModel] ({}) {}".format(
            self.model1.id,
            self.model1.__dict__
            )
        self.assertEqual(string, str(self.model1))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""

        my_dict = self.model1.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "__class__"]
        self.assertCountEqual(my_dict.keys(), expected_attrs)
        self.assertEqual(my_dict['__class__'], 'BaseModel')

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""

        new_dict = self.model2.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(
            new_dict["created_at"],
            self.model2.created_at.strftime(t_format)
            )
        self.assertEqual(
            new_dict["updated_at"],
            self.model2.updated_at.strftime(t_format)
            )


if __name__ == '__main__':
    unittest.main()
