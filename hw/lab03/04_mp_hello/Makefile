PY = python3

all: solution03_04

solution03_04: solution03_04.py
	$(PY) -m py_compile solution03_04.py

test: all
	$(PY) -m unittest discover -s tests -p "test_*.py" -v

clean:
	rm -f __pycache__/solution03_04.*.pyc
	rm -rf __pycache__