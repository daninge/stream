adb root > /dev/null 2>&1
adb shell "mkdir -p /data/local/tmp/stream && chmod 777 /data/local/tmp/stream"
adb push ./libs/armeabi-v7a/stream /data/local/tmp/stream > /dev/null 2>&1
adb shell "cd /data/local/tmp/stream && chmod 777 ./stream && ./stream"
