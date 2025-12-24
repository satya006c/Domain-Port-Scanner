# Domain-Port-Scanner
A sleek and beginner-friendly Domain IP and Port Scanner with a modern cyber-themed interface. This project allows users to enter a domain name and retrieve its IP address and open ports, helping understand how websites are discovered and analyzed at the network level.

# 🌐 Web-Based Port Scanning Application

A fast, multithreaded web-based port scanner built using Python and Flask that scans any domain or IP address to identify open TCP ports, featuring a modern cybersecurity-themed (glassmorphism) UI.

### ⚠️ Educational & Authorized Use Only

# 📌 Features

- ✅ Scan any domain or IP address

- ⚡ Fast multithreaded scanning

- 🌐 Automatic domain → IP resolution

- 🎨 Modern cybersecurity UI (glassmorphism)

- 📊 Scrollable scan results

- 🧠 Simple & clean backend logic

- 🧪 Ideal for students & cybersecurity learners

# 🖥️ Tech Stack
### Backend

- Python 3

- Flask

- Socket Programming

- ThreadPoolExecutor (Multithreading)

### Frontend

- HTML5

- CSS3 (Custom Cyber UI)

## 📂 Project Structure
port-scanner-web/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md

# ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
git clone https://github.com/your-username/port-scanner-web.git

cd port-scanner-web

# 2️⃣ Install Dependencies
pip install flask

# 3️⃣ Run the Application
python app.py

# 4️⃣ Open in Browser
http://127.0.0.1:5000

# 🚀 Usage

Enter a domain name or IP address

Specify start and end port range

Click Start Scan

View open ports instantly

Example
Target: google.com
Ports: 80 - 443

# 🧠 How It Works

User submits target and port range

Application resolves domain to IP using DNS

Multithreaded TCP connect scan is performed

Open ports are identified

Results are displayed on the web interface

# 🏗️ Architecture
User Interface
     ↓
Flask Web Server
     ↓
DNS Resolution
     ↓
Multithreaded Port Scanner
     ↓
Scan Results

# 🔐 Ethical Notice

This tool is intended only for:

Educational purposes

Authorized security testing

Personal or lab environments

❌ Do NOT scan systems without explicit permission.

# ⚠️ Limitations

TCP connect scan only

No service/version detection

Firewall-protected ports may not respond

Not suitable for public deployment without controls

# 🔮 Future Enhancements

- Service name detection (HTTP, HTTPS, SSH)

- Scan progress bar

- PDF / CSV report export

- Authentication system

- Scan history database

- Rate limiting & logging




### 📌 Add screenshots for better GitHub presentation

# 🎓 Ideal For

- Cybersecurity students

- Networking labs

- Ethical hacking practice

- College mini & major projects

- Resume & portfolio projects

# 📜 License

This project is licensed for educational use only.
Please ensure compliance with local cybersecurity laws.

# 🤝 Contributing

- Contributions are welcome!

- Fork the repository

- Create a feature branch

- Submit a pull request

# 📚 References

- Python Documentation

- Flask Documentation

- RFC 793 – TCP Protocol

- OWASP Network Security Guide

# ⭐ Support

If you like this project, give it a star ⭐ on GitHub — it really helps!
