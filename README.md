# syn-flood-example

Example SYN flood and TCP server script for learning TCP attacks.

---

🔒 **SYN Flood Script – For Educational & Testing Purposes Only**

This Python script demonstrates a **SYN Flood attack**, one of the most common types of **Denial-of-Service (DoS)** attacks. It works by rapidly sending a large number of TCP SYN packets to a target IP and port, overwhelming the target's ability to respond to connection requests.

---

## 🚧 How It Works

- The script forges TCP packets with the SYN flag set (simulating the first part of a TCP handshake).
- It continuously sends these packets using Scapy to a specified IP and port.
- The target receives an excessive number of half-open connections (SYN-RECEIVED state), which can exhaust system resources over time.

---

## ⚙️ Key Parameters

- `target_ip`: The IP address of the victim server.
- `target_port`: The open port to flood with SYN packets (commonly 80, 443, or others).
- `iface`: (Optional) The network interface to send packets through (e.g., `eth0`, `lo0`).
- `end_time`: A timeout condition, defining how long the attack should run.

---

## 🧪 Use Case

- **Educational environments** to learn about TCP handshakes and DoS attacks.
- **Testing labs or sandboxed VMs** to evaluate firewalls, intrusion detection systems (IDS), or rate-limiting.
- **Red team/pentesting exercises** (with explicit permission).

---

## 📦 Requirements

- Python 3.x
- [Scapy](https://scapy.net/)

Install Scapy:

```bash
pip install scapy
````

---

## ▶️ How to Run It

You’ll need **three Terminal windows**. Here’s the exact sequence:

---

### 🟢 Terminal 1: Start the Server

Run:

```bash
python3 tcp_server.py
```

You’ll see:

```
Server listening on 127.0.0.1:5000...
```

---

### 🟡 Terminal 2: Start tcpdump

Run:

```bash
sudo tcpdump -i lo0 -n -c 1000 tcp port 5000
```

This captures **1000 packets** and shows SYN traffic, e.g.:

```
[timestamp] IP 127.0.0.1.[port] > 127.0.0.1.5000: Flags [S], seq ..., length 0
```

---

### 🔴 Terminal 3: Launch the SYN Flood

Run:

```bash
sudo python3 syn_flood.py
```

You’ll see:

```
Starting SYN Flood on 127.0.0.1:5000...
Sent 1 packets.
[repeated for each packet]
Flood completed in [time] seconds.
```

---

## 🔍 What You’ll See

* **Server Terminal:** Prints `Connection from ('127.0.0.1', [port])` for each SYN packet that gets through.
* **tcpdump Terminal:** Logs every SYN packet hitting port 5000.
* **Flood Terminal:** Confirms packets are being sent.

---

⚠️ **Disclaimer**

> This tool is for **educational** and **ethical research** purposes **only**.
>
> Do **not** use this script against any system you do not own or do not have **explicit authorization** to test.
>
> Misuse of this tool can result in legal consequences.

---
