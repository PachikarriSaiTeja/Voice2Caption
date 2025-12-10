import sounddevice as sd

print("Default device:", sd.default.device)
print("\nAll devices:\n")
print(sd.query_devices())
