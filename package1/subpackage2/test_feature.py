from package1.subpackage2.feature2 import feature2
import unittest
from unittest.mock import MagicMock, patch


class TestFeature2(unittest.TestCase):

    @patch('package1.subpackage2.feature2.func1')
    @patch('package1.subpackage1.feature1.func1')
    def test_feature2(self, mock_func1_1: MagicMock, mock_func1_2: MagicMock):
        mock_func1_1.return_value = "Mocked"
        mock_func1_2.return_value = "Mocked"
        self.assertEqual("MockedMocked", feature2())
