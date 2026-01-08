CC = gcc
CFLAGS = -Wall -Wextra -std=c2x

TARGET = solution03_01

all: $(TARGET)

$(TARGET): solution03_01.c
	$(CC) $(CFLAGS) -o $(TARGET) solution03_01.c

test: all
	python3 -m unittest discover -s tests -p "test_*.py" -v

clean:
	rm -f $(TARGET)