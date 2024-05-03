import socket


ports = [21, 22, 80, 8080, 443, 445, 3306, 25]
# ports = range(1,65537)


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex(("linesapp.com.br",port))
    if code == 0:
        print(f"{port}\tport open")