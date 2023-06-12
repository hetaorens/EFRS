from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        file_content = file.read()

        

        # fs.save(file.name, file)
        
        # print(file_content)
        # print(f"SHA1 is :{sha1_code}")
        print(type(file))
        import code_unit
        """_summary_
        do something:
        存取文件通过hash加密,
        以HASH值存取文件名称,
        并用HASH为密钥使用SM4加密算法加密文件。
        Returns:
            _type_: _description_
            byte : sha1_code 文件的hash结果
            state : 是否存在文件的状态
        """
        #example
        import hashlib
        sha1_code =hashlib.sha1(file_content).hexdigest()
        from gmssl import sm4
        b = sm4.CryptSM4()
        print(sha1_code)
        import binascii
        b.set_key(binascii.a2b_hex(sha1_code),mode=sm4.SM4_ENCRYPT)
        encode_msg= b.crypt_cbc(bytes.fromhex("F"*32),file_content)
        
        import os
        print(os.getcwd())
        try:
            os.chdir('media')
        except:
            pass
        try: 
            f=open(sha1_code,"r") 
            print("文件存在")
            state=1
        except FileNotFoundError:

            f=open(sha1_code,"wb")
            f.write(encode_msg)
            state=0
            import code_unit.sql_unit
            code_unit.sql_unit.save_file_index(file.name,sha1_code)

        #example end
        pass

        
        return render(request, 'fileupload/upload_success.html',{"sha1":sha1_code,"state":state})
    return render(request, 'fileupload/upload.html')  



def check_file(request):
    if request.method == 'POST' and request.POST.get('filename'):
        filename = request.POST['filename']
        fs = FileSystemStorage()
        file_exists = fs.exists(filename)
        if file_exists:
            import os
            try:
                os.chdir('media')
            except:
                pass
            from gmssl import sm4
            b = sm4.CryptSM4()
            print(filename)
            import binascii
            b.set_key(binascii.a2b_hex(filename),mode=sm4.SM4_DECRYPT)
            # encode_msg= b.crypt_cbc(bytes.fromhex("F"*32),file_content)
            print(fs.url(filename))
            decode_msg=b.crypt_cbc(bytes.fromhex("F"*32),open(filename,"rb").read())
            print(decode_msg)
            with open("temp","wb") as f:
                f.write(decode_msg)
            return render(request, 'fileupload/check.html', {'filename': filename, 'file_exists': file_exists, 'download_url': fs.url("temp")})
        else:
            return render(request, 'fileupload/check.html', {'filename': filename, 'file_exists': file_exists})
    return render(request, 'fileupload/check.html')
 

 
def home(request):
    return render(request, 'fileupload/home.html')






