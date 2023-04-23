from utils import check_internet

if check_internet():
    print("Internet access is available.")
else:
    print("No internet access.")
