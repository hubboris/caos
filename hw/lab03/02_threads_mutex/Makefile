CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -O2 -pthread

all: solution03_02

solution03_02: solution03_02.c
	$(CC) $(CFLAGS) -o solution03_02 solution03_02.c

test: all
	python3 -m unittest discover -s tests -p "test_*.py" -v

clean:
	rm -f solution03_02