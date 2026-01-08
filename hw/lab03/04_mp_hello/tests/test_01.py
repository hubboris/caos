import unittest
import subprocess
import os
import re

class TestMpHello(unittest.TestCase):
    def setUp(self):
        self.script = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution03_04.py'))

    def test_n1(self):
        result = subprocess.run(
            ["python3", self.script, "1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=8
        )
        self.assertEqual(result.returncode, 0)
        out = result.stdout.strip().splitlines()
        self.assertTrue(len(out) >= 2)

        # expect lines for process 0:
        # "0 <wait>" and "hello 0 <wait>"
        pat1 = re.compile(r"^0\s+[1-4]\s*$")
        pat2 = re.compile(r"^hello\s+0\s+[1-4]\s*$")

        self.assertTrue(any(pat1.match(line) for line in out))
        self.assertTrue(any(pat2.match(line) for line in out))

    def test_n2(self):
        result = subprocess.run(
            ["python3", self.script, "2"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=8
        )
        self.assertEqual(result.returncode, 0)
        out = result.stdout.strip().splitlines()

        for i in [0, 1]:
            pat1 = re.compile(rf"^{i}\s+[1-4]\s*$")
            pat2 = re.compile(rf"^hello\s+{i}\s+[1-4]\s*$")
            self.assertTrue(any(pat1.match(line) for line in out))
            self.assertTrue(any(pat2.match(line) for line in out))

if __name__ == '__main__':
    unittest.main()