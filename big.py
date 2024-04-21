import bluetooth

def check_nearby_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    if nearby_devices:
        print("Found {} nearby devices:".format(len(nearby_devices)))
        for addr, name in nearby_devices:
            print("  {} - {}".format(addr, name))
    else:
        print("No nearby devices found.")

if __name__ == "__main__":
    check_nearby_devices()

