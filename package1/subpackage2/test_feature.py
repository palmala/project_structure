from package1.subpackage2.feature2 import feature2
import unittest
from unittest.mock import MagicMock, patch


class TestFeature2(unittest.TestCase):

    @patch('package1.common.helpers.func1')
    def test_feature2(self, mock_func1_1: MagicMock):
        mock_func1_1.return_value = "Mocked"
        self.assertEqual("MockedMocked", feature2())
