import unittest
import subprocess
import os

class TestPipePingPong(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'solution03_01')
        )

    def test_5(self):
        result = subprocess.run(
            [self.bin, '5'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            result.stdout,
            "1 1\n2 2\n1 3\n2 4\nDone\n"
        )

if __name__ == '__main__':
    unittest.main()