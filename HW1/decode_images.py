from base64 import b64decode
txt_files = ['learngit-main.txt', 'learngit-remote.txt']
for txt in txt_files:
    b = bytes()
    with open(txt, 'r', encoding='ascii') as txt_fd:
        b = b64decode(txt_fd.read())

    with open(txt[:-4] + '.jpg', 'wb') as img_fd:
        img_fd.write(b)
