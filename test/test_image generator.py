import os
import sys

from unittest import TestCase, main
from unittest.mock import patch

module_path = os.path.abspath('../main')
sys.path.append(module_path)

from main.image_generator import randomly_select_gender, generate_random_id


class Test(TestCase):

    @patch('random.choice', side_effect=lambda x: 'Male')
    def test_randomly_select_gender_male(self, mock_choice):
        self.assertEqual(randomly_select_gender(), 'Male')

    @patch('random.choice', side_effect=lambda x: 'Female')
    def test_randomly_select_gender_female(self, mock_choice):
        self.assertEqual(randomly_select_gender(), 'Female')

    @patch('random.choices', side_effect=lambda x, k: '12345678')
    def test_generate_random_id(self, mock_choices):
        self.assertEqual(generate_random_id(), '12345678')


if __name__ == '__main__':
    main()
