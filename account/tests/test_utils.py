from collections import OrderedDict
from django.test import TestCase
from ..utils import chart_config, map_data_to_dict


class ChartConfigTest(TestCase):

    def test_chart_config_returns_ordered_dict_instance(self):
        config = chart_config("Awesome chart I've got here", "Oil", "Years")

        self.assertTrue(isinstance(config, OrderedDict))

    def test_returned_value_contains_correct_keys(self):
        config = chart_config("Awesome chart I've got here", "Oil", "Years")
        self.assertIn('yAxisName', config.keys())
        self.assertIn('xAxisName', config.keys())
        self.assertIn('caption', config.keys())
        self.assertIn('theme', config.keys())

    def test_returned_value_contains_correct_values(self):
        config = chart_config("Awesome chart I've got here", "Oil", "Years")
        
        self.assertEqual(config['caption'], "Awesome chart I've got here")
        self.assertEqual(config['xAxisName'], "Oil")
        self.assertEqual(config['yAxisName'], "Years")


class MapDataToDictTest(TestCase):

    def test_func_returns_ordered_dict_instance(self):
        config = chart_config("Awesome chart I've got here", "Oil", "Years")
        chart_data = {'A': 15, 'B': 37}

        data_to_dict = map_data_to_dict(chart_data, config)
        
        self.assertTrue(isinstance(data_to_dict, OrderedDict))
