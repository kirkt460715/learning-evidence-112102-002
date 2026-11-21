import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class FixtureTests(unittest.TestCase):
    def test_synthetic_records_match_documented_envelope(self):
        path = ROOT / 'fixtures' / 'records.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        self.assertEqual(data['dataset'], 'verification')
        self.assertIsInstance(data['records'], list)
        self.assertGreaterEqual(len(data['records']), 3)
        identifiers = [row['id'] for row in data['records']]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertTrue(all(isinstance(row, dict) for row in data['records']))

    def test_claim_revisions_source_corrections_and_actions_are_available(self):
        data = json.loads((ROOT / 'fixtures' / 'records.json').read_text(encoding='utf-8'))
        self.assertEqual({row['revision'] for row in data['catalogs']['claims']}, {'r1', 'r2'})
        self.assertIn('withdrawn', {row['status'] for row in data['catalogs']['sources']})
        self.assertTrue(any(row['kind'] == 'excerpt-correction' for row in data['records']))
        actions = [row for row in data['records'] if row['kind'] == 'student-action']
        self.assertEqual({row['opened_source'] for row in actions}, {'s-1', 'not-recorded'})
        self.assertTrue(any(row['kind'] == 'course-activity' for row in data['records']))

if __name__ == '__main__':
    unittest.main()
