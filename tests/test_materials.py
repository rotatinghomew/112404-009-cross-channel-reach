from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from museum_workbench.inputs import read_table


class MaterialTests(unittest.TestCase):
    def test_tables_have_rows_and_uniform_record_fields(self):
        paths = sorted((ROOT / 'data').glob('*.csv'))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            with self.subTest(table=path.name):
                rows = read_table(path)
                self.assertTrue(rows)
                self.assertTrue(all(all(isinstance(v, str) for v in row.values()) for row in rows))
                self.assertEqual(set(rows[0]), set(rows[-1]))
                self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows))

    def test_scenario_materials_have_resolvable_business_references(self):
        channels = read_table(ROOT / "data/channels.csv")
        events = read_table(ROOT / "data/events.csv")
        requests = read_table(ROOT / "data/aggregation_requests.csv")
        self.assertTrue({row["channel_id"] for row in events} <= {row["channel_id"] for row in channels})
        repeated = [row["visitor_token"] for row in events if row["visitor_token"]]
        self.assertLess(len(set(repeated)), len(repeated))
        self.assertIn("withdrawn", {row["consent_state"] for row in events})
        self.assertTrue(any("age-band" in row["dimension_set"] for row in requests))

    def test_dates_and_identifiers_remain_strings(self):
        for path in (ROOT / 'data').glob('*.csv'):
            rows = read_table(path)
            self.assertTrue(all(isinstance(value, str) for row in rows for value in row.values()))


if __name__ == '__main__':
    unittest.main()
