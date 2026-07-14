import platform
import psutil
import time
import os
host_name=platform.node()
operating_system=platform.system()
def main():
    try:
        while True:
            cpu=psutil.cpu_percent(interval=1)
            RAM=psutil.virtual_memory().percent
            disk=psutil.disk_usage("/").percent
            battery=psutil.sensors_battery().percent
            if operating_system=="Linux":
                os.system("clear")
            elif operating_system=="Windows":
                os.system("cls")
            print("===============================")
            print("                         AtlasMonitor                            ")
            print("===============================")
            print("welcome")
            print("OS:",operating_system)
            print("Hostname:",host_name)
            print("----------------------------------------")
            print("Cpu usage:",cpu,"%")
            print("Ram usage:",RAM,"%")
            print("Disk usage:",disk,"%")
            print("Battery:",battery,"%")
            print()
            print("Press Ctrl+C to exit.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝")
        print("thank you for using atlasmonitor")
        print("goodbye !")
        print("⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝⸝")
if __name__ == "__main__":
    main()
