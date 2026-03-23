import time
import sys

def boot_sequence():
    print("🚀 HomeCore Initializing...")
    time.sleep(0.5)
    print("🔌 Loading Drivers...")
    time.sleep(0.5)
    print("🛡️  Security Check... OK")
    time.sleep(0.5)
    print("✅ HomeCore Online. Waiting for commands.")

if __name__ == "__main__":
    try:
        boot_sequence()
    except KeyboardInterrupt:
        print("\n🛑 HomeCore Shutting Down.")
        sys.exit()