import unittest
import subprocess
import os
import socket
import threading
import time


class TestTcpClient(unittest.TestCase):
    def setUp(self):
        self.bin = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution03_03'))

    def start_server_ok(self, K: int, expected_key: str, reply_u64: int):
        """
        Protocol:
          client -> KEY\n
          server -> K\n
          client -> 0..K each as line
          server -> reply_u64\n
        """
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)
        host, port = srv.getsockname()

        def handler():
            conn, _ = srv.accept()
            with conn:
                f = conn.makefile("rwb", buffering=0)

                key_line = f.readline()
                if not key_line:
                    return
                key = key_line.decode("utf-8").rstrip("\n")
                # Validate key
                if key != expected_key:
                    return

                f.write(f"{K}\n".encode("utf-8"))
                f.flush()

                # Read 0..K
                for i in range(K + 1):
                    line = f.readline()
                    if not line:
                        return
                    got = int(line.decode("utf-8").strip())
                    if got != i:
                        return

                f.write(f"{reply_u64}\n".encode("utf-8"))
                f.flush()

        th = threading.Thread(target=handler, daemon=True)
        th.start()
        return host, port, srv, th

    def start_server_drop(self):
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)
        host, port = srv.getsockname()

        def handler():
            conn, _ = srv.accept()
            # Drop immediately
            conn.close()

        th = threading.Thread(target=handler, daemon=True)
        th.start()
        return host, port, srv, th

    def test_protocol_ok(self):
        # Choose K and reply
        K = 7
        key = "hello"
        reply = 18446744073709551615  # max u64 fits in Python int (printed as decimal)

        host, port, srv, th = self.start_server_ok(K, key, reply)

        try:
            result = subprocess.run(
                [self.bin, host, str(port), key],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5
            )
        finally:
            srv.close()

        self.assertEqual(result.returncode, 0)
        # stderr should be empty in normal run
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, f"{reply}\n")

    def test_disconnect_exit_0(self):
        host, port, srv, th = self.start_server_drop()

        try:
            result = subprocess.run(
                [self.bin, host, str(port), "KEY"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=5
            )
        finally:
            srv.close()

        # On disconnect: must exit 0, output may be empty
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()