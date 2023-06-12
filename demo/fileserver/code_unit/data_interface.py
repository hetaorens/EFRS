"""_summary_
        do something:
        存取文件通过hash加密,
        以HASH值存取文件名称,
        并用HASH为密钥使用SM4加密算法加密文件。
        
        Returns:
            _type_: _description_
            byte : sha1_code 文件的hash结果
        """


# sha1_code =hashlib.sha1(file_content).hexdigest()

# from gmssl import sm4
# b = sm4.CryptSM4()
# print(sha1_code)

# import binascii
# b.set_key(binascii.a2b_hex(sha1_code),mode=sm4.SM4_ENCRYPT)
# encode_msg= b.crypt_cbc(bytes.fromhex("F"*32),file_content)

# import os
# os.chdir('media')
# try: 
#     f=open(sha1_code,"r") 
#     print("文件存在")
# except FileNotFoundError:

#     f=open(sha1_code,"wb")
#     f.write(encode_msg)
# #example end
# pass



import os
from SHA1 import SHA1
from SM4 import SM4



def encrypt(file_content):
    s = SHA1()
    sha1_code = s.hash(file_content)
    print(sha1_code)
    

    try:
        os.chdir('media')
    except:
        pass
    
    try: 
        f = open(sha1_code,"r") 
        print("文件存在")
        state = 1
    except FileNotFoundError:

        f=open(sha1_code,"wb")
        encode_msg = sm4_encrypt(file_content, sha1_code)
        f.write(encode_msg)
        state = 0


def sm4_encrypt(file_content, sha1_code):

    a = SM4()
    encode_msg = a.encrypt_cbc(file_content, sha1_code)
    
    return encode_msg


# if __name__ == '__main__':
#     with open(r"D:\360MoveData\Users\mia san mia\Desktop\2\1.md",'r') as f:
#         data = f.read()
#         encrypt(data)