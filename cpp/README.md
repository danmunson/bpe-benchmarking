# Build
A basic makefile is included which uses `g++` as the default compiler. Alternatively, the build command ran is
```
g++ -std=c++11 -g -O3 -pedantic-errors -Wall -Wextra -Werror simple-bpe.cpp -o simple-bpe
```
# Run
```
-i input file
-k number of iterations (optional, default 10)
-o output file (optional, will output to stdout if omitted)
```
### Linux
`./simple-bpe -i alice29.txt -k 100 -o tokens.txt`
### Windows
`simple-bpe.exe -i alice29.txt -k 100 -o tokens.txt`
