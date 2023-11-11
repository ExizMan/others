import unittest
from name_func import get_form_nm
class NamesTestCase(unittest.TestCase):
    """Тесты для имени"""
    def test_first_last_name(self):
        formatted_name=get_form_nm('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
if __name__ =='__main__':
    unittest.main()