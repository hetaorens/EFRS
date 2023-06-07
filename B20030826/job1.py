import SHA1
import SM4


filepath = "流图.png"

def generatehash(filepath):
    with open(filepath,"rb") as f:
        a=f.read()
        hash_msg=SHA1.SHA1().hash(a)
    return hash_msg
    

