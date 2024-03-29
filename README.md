# [Advent of Code](https://adventofcode.com/)

## $year=[2022](https://adventofcode.com/2022)
[Day 1: Calorie Counting](https://adventofcode.com/2022/day/1) 
[Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2)
[Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3)
[Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4)
[Day 5: Supply Stacks](https://adventofcode.com/2022/day/5)
[Day 6: Tuning Trouble ](https://adventofcode.com/2022/day/6)
[Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7)
[Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8)

## Use `init`

The `init` script is a Bash script that automates the creation of a Python project structure for a particular coding challenge. It uses a file called `.init_mem` to store information about solved challenges
```bash
├── main.py
├── resources
│   ├── input.txt
│   └── input_test.txt
├── src
│   ├── __init__.py
│   ├── task1.py
│   └── task2.py
├── tests
│   ├── __init__.py
│   ├── test_task1.py
│   └── test_task2.py
└── utils
    ├── __init__.py
    └── utils.py
```
### Usage
```bash
chmod +x init
./init <day> "<challenge>"
```
### Undo
```bash
sed -i '$d' ".init_mem" # removes last entry
rm -r <folder>
```
