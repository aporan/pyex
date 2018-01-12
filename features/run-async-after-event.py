import time
import queue
import threading

def server(block_queue):
    while True:

        print("[+] Received packet")
        print("... retrieving from database")
        print("... processing packet")
        time.sleep(3)
        print("... updating to database")
        print("[+] Database updated.")

        if not block_queue.empty():
            block, value = block_queue.get()
            block(value)
            block_queue.task_done()

def block_flag(queue, func_block):
    queue.put((func_block, threading.current_thread().name))

def block_device(thread_name):
    print("{} [+] Received blocking call".format(thread_name))
    print("{} ... waiting for approval ".format(thread_name))

    print("{} ... calling server function".format(thread_name))
    print("{} ... updating database".format(thread_name))
    print("{} [+] Blocked .".format(thread_name))


if __name__=="__main__":
    block_queue = queue.Queue()

    server_thread = threading.Thread(target=server, args=(block_queue,))
    server_thread.start()

    for i in range(100):
        temp_thread = threading.Thread(target=block_flag, args=(block_queue, block_device))
        temp_thread.daemon = True

        temp_thread.start()

    server_thread.join()
