
import socket
import time

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 5000

def main():
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, SERVER_PORT))
        print("Uspesno sam se povezao sa serverom.")

        for i in range(10, -1, -1):
            poruka = f"Ima jos {i} pokusaja pre prekida veze."
            s.send(poruka.encode(), socket.MSG_OOB)
            print(f"Saljem upozorenje: {poruka}")
            time.sleep(5)

        print("Klijent zatvara konekciju.")

    except Exception as e:
        print(f"Doslo je do greske: {e}")

    finally:
        if s:
            s.close()

if __name__ == "__main__":
    main()
