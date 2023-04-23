import psutil
import ipaddress
import subprocess
import platform


def ping_host(host="8.8.8.8", count=1, timeout=1000):
    try:
        if platform.system().lower() == "windows":
            # Windows ping command
            command = ["ping", "-n", str(count), "-w", str(timeout), host]
        else:
            # Linux and macOS ping command
            command = ["ping", "-c", str(count), "-W", str(timeout), host]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Return True if the returncode is 0 (success), False otherwise
        return result.returncode == 0
    except Exception as ex:
        print(ex)
        return False


def is_public_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return not (ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local)
    except ValueError:
        return False


def check_internet():
    # Get all the connections
    connections = psutil.net_connections()
    try:
        # Check if any of the connections is to a public IP.
        for conn in connections:
            if is_public_ip(conn.raddr.ip) and conn.status == 'ESTABLISHED':
                return True
        # If no public IP is found in the connections, ping Google.
        return ping_host()
    except AttributeError:
        # If the raddr is not available, ping Google.
        return ping_host()
