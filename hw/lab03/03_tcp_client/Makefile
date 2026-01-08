CC = gcc
CFLAGS = -Wall -Wextra -std=c2x -O2

all: solution03_03

solution03_03: solution03_03.c
	$(CC) $(CFLAGS) -o solution03_03 solution03_03.c

test: all
	python3 -m unittest discover -s tests -p "test_*.py" -v

clean:
	rm -f solution03_03