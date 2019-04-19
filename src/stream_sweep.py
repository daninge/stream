import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Setup build env
# subprocess.run(['./build.sh'])

def run_test(array_size):
    subprocess.run(['make', 'clean'])
    subprocess.run(['make', "ARRAY_SIZE={}".format(array_size),'stream_c.exe'])

    stream_result = subprocess.run(['./stream_c.exe'], capture_output=True)
    str_out = stream_result.stdout.decode('utf-8').split('\n')[29].split()[1]
    print(str_out)
    bandwidth = float(str_out)
    print(bandwidth)
    return bandwidth

xs = np.linspace(100, 1000000, 100, dtype=int)
ys = np.zeros(xs.shape)

for i, x in enumerate(xs):
    ys[i] = run_test(x)

plt.plot(xs, ys)
plt.xlabel("Stream Array Size")
plt.ylabel("Bandwidth for 10 trials (MB/s)")
plt.show()