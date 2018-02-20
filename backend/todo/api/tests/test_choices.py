from django.test import TestCase
from ..misc.choices import to_external, to_internal, TaskStatus


class ChoicesTest(TestCase):

    def test_to_internal_valid(self):
        """Convert to db value"""
        extVal = 'Open'
        inVal = to_internal(TaskStatus, extVal)
        self.assertEqual(inVal, TaskStatus.OPEN)

    def test_to_external_valid(self):
        """Convert to external"""
        inVal = TaskStatus.OPEN
        extVal= to_external(TaskStatus, inVal)
        self.assertEqual(extVal, 'Open')

    def test_to_internal_invalid(self):
        """Convert to db value"""
        extVal = 'Ope'
        try:
            inVal = to_internal(TaskStatus, extVal)
            self.fail('Exception expected')
        except Exception:
            pass

    def test_to_external_invalid(self):
        """Convert to external"""
        inVal = 'os'
        try:
            extVal= to_external(TaskStatus, inVal)
            self.fail('Exception expected')
        except Exception:
            pass
