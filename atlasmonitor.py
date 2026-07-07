import platform
import psutil
host_name=platform.node()
operating_system=platform.system()
cpu=psutil.cpu_percent(interval=1)
RAM=psutil.virtual_memory().percent
disk=psutil.disk_usage("/").percent
print("=========================")
print("Atlas Monitor v0.1")
print("=========================")
print("welcome")
print("OS :",operating_system)
print("user:",host_name)
print("cpu usage:",cpu)
print("ram usage:",RAM)
print("disk usage :",disk)
