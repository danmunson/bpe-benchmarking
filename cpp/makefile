CXX=g++
CXXFLAGS=-std=c++11 -g -O3 -pedantic-errors -Wall -Wextra -Werror
TARGET=simple-bpe

ifdef ComSpec
    RM=del /F /Q
else
    RM=rm -f
endif

all: ${TARGET}.cpp
	${CXX} ${CXXFLAGS} ${TARGET}.cpp -o ${TARGET}

clean:
	${RM} ${TARGET}.exe ${TARGET}.o
