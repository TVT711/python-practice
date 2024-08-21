import json
import unittest
from parkingsystem import load_pricing_rules  # Assuming ParkingSystem is correctly defined in this module
from unittest.mock import mock_open, patch


class TestParkingSystem(unittest.TestCase):
    def test_load_pricing_rules_success(self):
        # Mock data to be returned by open
        mock_data = '{"day": {"08:00-16:59": {"max_stay_hours": 8, "price_per_hour": 2}}}'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            with patch('json.load') as mock_json_load:
                mock_json_load.return_value = json.loads(mock_data)
                result = load_pricing_rules()
                self.assertEqual(result, json.loads(mock_data))


if __name__ == '__main__':
    unittest.main()
