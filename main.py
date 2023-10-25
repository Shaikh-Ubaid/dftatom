#!/usr/bin/env python

import subprocess as sp
import os


print("Using tools as follows:")
res = sp.run(["which", "lfortran"], capture_output=True, text=True)
print(res.stdout + "\n" + res.stderr)
res = sp.run(["lfortran", "--version"], capture_output=True, text=True)
print(res.stdout + "\n" + res.stderr)
res = sp.run(["which", "gfortran"], capture_output=True, text=True)
print(res.stdout + "\n" + res.stderr)
res = sp.run(["gfortran", "--version"], capture_output=True, text=True)
print(res.stdout + "\n" + res.stderr)


print(f"Running Benchmarks ...")
res = sp.run(["time", "./bench.sh"], capture_output=True, text=True)
output_filename = f"output_lf_25.txt"
print(f"Saving output to {output_filename} ...")
# os.makedirs(os.path.dirname(output_filename), exist_ok=True)
with open(output_filename, "w") as output_file:
    output_file.write("STDOUT:\n\n")
    output_file.write(res.stdout)
    output_file.write("\n\n\n")
    output_file.write("STDERR:\n\n")
    output_file.write(res.stderr)
    print(f"Output saved succesfully!")
print()
