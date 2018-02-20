from django.test import TestCase
from ..misc.validators import validateJson


class ValidatorTest(TestCase):

    def setUp(self):
        self.schema = {
            'type': 'object',
            'properties': {
                'key1': {
                    'type': 'string'
                },
                'key2': {
                    'type': 'string'
                },
                'key3': {
                    'type': 'string'
                },
            },
            'required': [
                'key1',
                'key2',
            ],
        }

    def test_json_validation_true(self):
        """Json validation test"""
        toValidate = {
            'key1': 'key1str',
            'key2': 'key2str'
        }
        status = validateJson(toValidate, self.schema)
        self.assertTrue(status)

    def test_json_validation_false(self):
        """Json validation test"""
        toValidate = {
            'key1': 'key1str',
            'key2': 1234,
            'key3': 'adsf'
        }
        status = validateJson(toValidate, self.schema)
        self.assertFalse(status)
