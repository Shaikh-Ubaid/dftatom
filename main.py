#!/usr/bin/env python

import subprocess as sp
import os


print("Activating the environment lf_25")
res = sp.run(["conda", "deactivate"], capture_output=True, text=True)
res = sp.run(["conda", "activate", "lf_25"], capture_output=True, text=True)
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


print("Activating the environment lf_26")
res = sp.run(["conda", "deactivate"], capture_output=True, text=True)
res = sp.run(["conda", "activate", "lf_26"], capture_output=True, text=True)
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
output_filename = f"output_lf_26.txt"
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
