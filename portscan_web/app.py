from flask import Flask, render_template, request
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

# Resolve domain or IP
def resolve_domain(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None

# Scan a single port
def scan_single_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)   # LOWER timeout = faster
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

# Multithreaded port scanner
def scan_ports_fast(ip, start_port, end_port):
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {
            executor.submit(scan_single_port, ip, port): port
            for port in range(start_port, end_port + 1)
        }

        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    return sorted(open_ports)

@app.route("/", methods=["GET", "POST"])
def index():
    open_ports = []
    resolved_ip = ""
    error = ""

    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])

        resolved_ip = resolve_domain(target)

        if resolved_ip:
            open_ports = scan_ports_fast(resolved_ip, start_port, end_port)
        else:
            error = "Invalid domain or IP address"

    return render_template(
        "index.html",
        open_ports=open_ports,
        resolved_ip=resolved_ip,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
