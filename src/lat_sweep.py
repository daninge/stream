import subprocess
import matplotlib.pyplot as plt

stuff = subprocess.run(['sh', '../run.sh'], capture_output=True)
#stuff = subprocess.run(['./stream'], capture_output=True)
lines = stuff.stdout.decode("utf-8").split("\n")

xs = []
ys = []

lines = lines[:-1]
for line in lines:
    split = line.split(',')
    xs.append(float(split[0].strip()))
    ys.append(float(split[1].strip()))
plt.yscale('log', basey=2)
plt.xscale('log', basex=2)
plt.ylabel('Time')
plt.xlabel('Array Size (KB)')
plt.plot(xs, ys, '-ob')
plt.show()
