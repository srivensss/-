print("你是要进行加密还是解密呢？(encrypt/decrypt)")
choose = input("你的选择是:")
if choose == 'encrypt':
    print("正在进行凯撒加密")
    mingwen = input("请输入明文为:")
    k = input("请输入偏移量为:")
    for b in  mingwen:
        print(chr(ord(b)%127+int(k)),end="")
elif choose == 'decrypt':
    print("正在进行凯撒解密")
    miwen = input("请输入密文为:")
    s = input("请输入偏移量为:")
    for c in miwen:
        print(chr((ord(c)-int(s)) % 127), end="")
else:
    print("请输入encrypt or decrypt")