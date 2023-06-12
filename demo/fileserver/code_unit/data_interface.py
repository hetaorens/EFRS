"""_summary_
        do something:
        存取文件通过hash加密,
        以HASH值存取文件名称,
        并用HASH为密钥使用SM4加密算法加密文件。
        
        Returns:
            _type_: _description_
            byte : sha1_code 文件的hash结果
        """

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
        a = SM4()
        encode_msg = a.encrypt_cbc(file_content, sha1_code)
        f.write(encode_msg)
        state = 0


def sm4_decrypt(file_content, sha1_code):
    a = SM4()
    msg = a.decrypt_cbc(file_content, sha1_code)
    return msg

def decrypt(filename):
    try:
        os.chdir('media')
    except:
        pass
      
    with open(filename,"rb") as f:
        msg = f.read()
        decode_msg = sm4_decrypt(msg, filename)

    try:
        with open("temp", "wb") as f:
            f.write(decode_msg)
    except IOError:
        print("tmp文件写入失败")
    


# if __name__ == "__main__":
#     with open(r"D:\360MoveData\Users\mia san mia\Desktop\2\1.md", 'r') as f:
#         filecontent = f.read()
#         encrypt(filecontent)        
#     filename = "EFBB33E729E1F73E687B3F3E3520115E078A5696"
#     decrypt(filename)

 