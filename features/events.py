import time
import threading

def server(server_event, block_event, lock):
    while True:
        server_event.clear()
        print("[+] Received packet")
        print("... retrieving from database")
        print("... processing packet")
        time.sleep(3)
        print("... updating to database")
        print("[+] Database updated.")
        server_event.set()

def block(server_event, block_event, lock):
    print("{} [+] Received blocking call".format(threading.current_thread().name))
    print("{} ... waiting for approval ".format(threading.current_thread().name))
    server_event.wait() # you can also provide a time for a timeout
    block_event.set()
    print("{} ... calling server function".format(threading.current_thread().name))
    print("{} ... updating database".format(threading.current_thread().name))
    print("{} [+] Blocked .".format(threading.current_thread().name))

if __name__=="__main__":
    server_event = threading.Event()
    block_event = threading.Event()
    lock = threading.Lock()

    server_thread = threading.Thread(target=server, args=(server_event, block_event, lock))
    server_thread.start()

    for i in range(5):
        temp_thread = threading.Thread(target=block, args=(server_event, block_event, lock))
        temp_thread.daemon = True

        temp_thread.start()

    server_thread.join()

