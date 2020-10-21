import os
import sys


while True:
    option = input("Install all shit = 1\nUpdate and upgrade all = 2\nInstall nvim = 3\nGoogle time = 4\nOption: ")

    if option == "0":
        print("Thanks for using.")
        sys.exit()

    elif option == "1":
        
        apt_list = ["zip","unzip","python3","python3-pip"]
        list = ["dhcpd","openssl","reaver","hostapd","iptables",'sslstrip','aircrack-ng','lighttpd','crunch','ettercap-text-only','hashcat','pixiewps','john','git','libc6-dev','libbsd-dev', 'libevent-dev', 'libpcap-dev', 'gcc', 'make', 'pkg-config', 'tixati', 'nmap', 'vlc', 'unetbootic', 'golang','htop','transmission-cli','openjdk-8-jre-headless']
        pip_list = ['discord','pynput','tqdm','getch']
        for i in range(len(list)):
            os.system('sudo apt-get install '+str(list[i])+' -y')
        for i in range(len(apt_list)):
            os.system('sudo apt install '+str(apt_list[i])+' -y')
        for i in range(len(pip_list)):
            os.system("sudo pip3 install "+str(pip_list[i]))

        os.system('sudo apt-get install snap -y')
        os.system('sudo snap install gotop')

        break

    elif option == "2":
        os.system("sudo apt update -y;sudo apt upgrade -y;")
        break

    elif option == "3":
        os.system("git clone https://github.com/ChristianChiarulli/nvim")
        break

    elif option == "4":
        os.system('sudo timedatectl set-timezone Asia/Hong_Kong')
        break