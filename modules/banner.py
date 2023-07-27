
def banner():
    f = open('/assets/banner.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()

def menu_print():
    print("===== ClimaCast Options =====")