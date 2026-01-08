import subprocess
import unittest
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parent.parent


class TestPipesPingPong(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["make"], cwd=TASK_DIR, check=True)

    def run_case(self, maxval: int) -> str:
        p = subprocess.run(
            ["./solution03_01", str(maxval)],
            cwd=TASK_DIR,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        self.assertEqual(p.stderr, "")
        return p.stdout

    def test_sample_5(self):
        out = self.run_case(5)
        self.assertEqual(out, "1 1\n2 2\n1 3\n2 4\nDone\n")

    def test_min_1(self):
        out = self.run_case(1)
        self.assertEqual(out, "Done\n")

    def test_2(self):
        out = self.run_case(2)
        self.assertEqual(out, "1 1\nDone\n")