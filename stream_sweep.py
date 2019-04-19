import subprocess
import numpy as np
import matplotlib.pyplot as plt

# Setup build env
# subprocess.run(['./build.sh'])

array_size = 2000

build_string = """
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_SRC_FILES := ./src/stream.c #./src/mysecond.c
LOCAL_MODULE    := stream

LOCAL_CFLAGS += -O2 -DSTREAM_ARRAY_SIZE={}
LOCAL_CFLAGS += -fopenmp
LOCAL_LDFLAGS += -fopenmp

include $(BUILD_EXECUTABLE)"""

def run_test(array_size):
    with open('Android.mk', "w") as f:
        subprocess.run(['echo', build_string.format(array_size)], stdout=f)
    
    subprocess.run(['sh', 'build.sh'])

    stream_result = subprocess.run(['sh', 'run.sh'], capture_output=True)
    str_out = stream_result.stdout.decode('utf-8').split('\n')[29].split()[1]
    print(str_out)
    bandwidth = float(str_out)
    print(bandwidth)
    return bandwidth

xs = np.linspace(100, 10000000, 40, dtype=int)
ys = np.zeros(xs.shape)

for i, x in enumerate(xs):
    ys[i] = run_test(x)

plt.plot(xs, ys)
plt.xlabel("Stream Array Size")
plt.ylabel("Bandwidth for 10 trials (MB/s)")
plt.show()