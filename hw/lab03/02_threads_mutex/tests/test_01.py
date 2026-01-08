import unittest
import subprocess
import os

class TestThreadsMutex(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution03_02'))

    def test_expected_values_with_mutex(self):
        result = subprocess.run(
            [self.bin],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")

        lines = [x.strip() for x in result.stdout.strip().splitlines()]
        self.assertEqual(len(lines), 3)

        vals = [float(x) for x in lines]

        # Expected deterministic result with mutex:
        # a0 = -201 * 1e6 = -201000000
        # a1 =  99 * 1e6 =   99000000
        # a2 =  99 * 1e6 =   99000000
        exp = [-201000000.0, 99000000.0, 99000000.0]

        for v, e in zip(vals, exp):
            self.assertAlmostEqual(v, e, places=6)

if __name__ == '__main__':
    unittest.main()