import random
import sys
import os
import subprocess
from Crypto.Util.number import getPrime
from itertools import product
from tqdm import tqdm

print("Compiling C++")
os.system("g++ ./BabyStep.cpp -lgmp -lgmpxx -o BabyStep")
os.system("g++ ./PollardRho.cpp -lgmp -lgmpxx -o PollardRho")

print("Generating tasks")
random.seed(0)
n_small = getPrime(40, random.randbytes)
n_big = getPrime(44, random.randbytes)
a_small = random.randint(1, n_small)
a_big = random.randint(1, n_big)
x_small = random.randint(1, n_small)
x_big = random.randint(1, n_big)
b_small = pow(a_small, x_small, n_small)
b_big = pow(a_big, x_big, n_big)

with open("input_small.txt", "w") as f:
    f.write(f"{a_small} {b_small} {n_small}")

with open("input_big.txt", "w") as f:
    f.write(f"{a_big} {b_big} {n_big}")

runs = 4
sizes = ["small", "big"]
languages = ["Python", "C++"]
algorithms = ["BabyStep", "PollardRho"]
tasks = runs * list(product(sizes, languages, algorithms))
random.shuffle(tasks)

print("Running tests")
with open("results.txt", "w") as f:
    for size, language, algorithm in tqdm(tasks):
        command = "/bin/bash -c \"time ./"
        command += algorithm
        command += ".py" if language == "Python" else ""
        command += " < input_"
        command +=  size
        command += ".txt\""
        out = subprocess.check_output(command, env={"TIMEFORMAT": '%3U %3S'}, stderr=subprocess.STDOUT, shell=True).strip().decode()
        res, time = out.split("\n")
        res = int(res)
        if size == "small":
            assert pow(a_small, res, n_small) == b_small, f"Failed for test case: (a: {a_small}, b: {b_small}, n: {n_small}, size: {size}, language: {language}, algorithm: {algorithms}. Outputed {res}, possible answer: {x_small}"
        else: 
            assert pow(a_big, res, n_big) == b_big, f"Failed for test case: (a: {a_big}, b: {b_big}, n: {n_big}, size: {size}, language: {language}, algorithm: {algorithms}. Outputed {res}, possible answer: {x_big}"
        sys, usr = map(float, time.split())
        f.write(f"{size},{language},{algorithm},{sys+usr}\n")



