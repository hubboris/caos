SHELL := /bin/bash

CC := gcc
CFLAGS := -O2 -Wall -Wextra -Wpedantic -std=c11

TARGET := solution03_01
SRC := solution03_01.c

.PHONY: all clean test

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(TARGET)

test: all
	python3 -m unittest -v

clean:
	rm -f $(TARGET)