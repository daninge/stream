
LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)

LOCAL_SRC_FILES := ./src/stream.c #./src/mysecond.c
LOCAL_MODULE    := stream

LOCAL_CFLAGS += -O2 -DSTREAM_ARRAY_SIZE=10000000
LOCAL_CFLAGS += -fopenmp
LOCAL_LDFLAGS += -fopenmp

include $(BUILD_EXECUTABLE)
