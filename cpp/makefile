CXX=g++
CXXFLAGS=-std=c++11 -g -O3 -pedantic-errors -Wall -Wextra -Werror
TARGET=simple-bpe

all: ${TARGET}.cpp
	${CXX} ${CXXFLAGS} ${TARGET}.cpp -o ${TARGET}

clean:
	del ${TARGET}.exe ${TARGET}.o