#!/bin/bash
mkdir "$1/"
touch "$1"/a.py
touch "$1"/b.py
touch "$1"/c.py
touch "$1"/d.py

echo "# N = int(input())" >> "$1"/a.py
echo "# N = int(input())" >> "$1"/b.py
echo "# N = int(input())" >> "$1"/c.py
echo "# N = int(input())" >> "$1"/d.py

echo "# S = input()" >> "$1"/a.py
echo "# S = input()" >> "$1"/b.py
echo "# S = input()" >> "$1"/c.py
echo "# S = input()" >> "$1"/d.py

echo "# a_li = list(map(int, input().split()))" >> "$1"/a.py
echo "# a_li = list(map(int, input().split()))" >> "$1"/b.py
echo "# a_li = list(map(int, input().split()))" >> "$1"/c.py
echo "# a_li = list(map(int, input().split()))" >> "$1"/d.py

echo "# N, M = map(int, input().split())" >> "$1"/a.py
echo "# N, M = map(int, input().split())" >> "$1"/b.py
echo "# N, M = map(int, input().split())" >> "$1"/c.py
echo "# N, M = map(int, input().split())" >> "$1"/d.py
