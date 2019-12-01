from netmiko import ConnectHandler
import getpass
def koneksi():
    pilih = int(input("Masukan Pilihan : "))
    if pilih == 1:
        while True:
            co = input('Command : ')
            output = connection.send_command(co)
            print(output)
            co = ''
    elif pilih == 2:
        se = input("Masukan nama file dan directorynya : ")
        output = connection.send_config_from_file(se)
        print(output)
        se = ''
    else:
        print("Eror")


ip = input("Ip : ")
username = input("Username : ")
psswd = input("Password : ")#getpass.getpass()
linux = {
    'device_type':'linux',
    'ip':ip,#'192.168.43.197'
    'username':username,#'root',
    'password':psswd,#'flaskdisk010',
    'port':22,
    'verbose':True
}

connection = ConnectHandler(**linux)
connection.enable()
print("""-----Menu-----
1. Use CLI
2. Upload Config""")
koneksi()
connection.disconnect()