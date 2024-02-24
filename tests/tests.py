import unittest
import unittest.mock
from .. import restaurant_roulette


class RouletteFunctionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_list = ['pizza', 'chinese']
        self.joinable_list = ['sushi']
        self.not_a_list = False
        return super().setUp()

    def test_join_list(self):
        result = restaurant_roulette.join_list(
            self.sample_list,
            self.joinable_list)
        self.assertEqual(result, ['pizza', 'chinese', 'sushi'])

    def test_get_random_results(self):
        result = restaurant_roulette.get_random_results(
            required_results=1,
            target_list=self.sample_list
        )
        self.assertIn(result, self.sample_list)
