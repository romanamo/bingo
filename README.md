# Bingo

Generate a bingo fields with custom words, optional bonus field, NxN grid size 
and variable width and height via command line.

## Examples
Minimalistic example using`greek.txt`:
```commandline
python bingo.py -words greek.txt 
```

Detailed example using `greek.txt`:
```commandline
python bingo.py -width 2000 -height 2000 -steps 7 -words greek.txt -bonus True -seed 42
```

## Requirements

- Python 3
- Python Packages: [Pillow](https://pypi.org/project/pillow/) > 10.1

## Parameter

| Parameter | Datentyp | Beschreibung                           | Default                                 |
|-----------|----------|----------------------------------------|-----------------------------------------|
| -words    | str      | words text file                        | -                                       |
| -width    | int      | width of image in pixels               | 1000                                    |
| -height   | int      | height of image in pixels              | 1000                                    |
| -steps    | int      | grid size length                       | 5                                       |
| -seed     | int      | seed for the bingo                     | current time in nanoseconds since epoch |
| -bonus    | bool     | adds bonus field if side length is odd | False                                   |
