
import socket

HOST = '0.0.0.0'
PORT = 5000

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)

    print("Server je pokrenut i ceka klijenta...")

    conn, addr = s.accept()
    print(f"Povezao se klijent sa adrese {addr}")

    try:
        while True:
            try:
                data = conn.recv(1024, socket.MSG_OOB)
                if data:
                    print(f"Stigla urgentna poruka: {data.decode()}")
            except Exception:
                pass
    finally:
        conn.close()
        s.close()

if __name__ == "__main__":
    main()
