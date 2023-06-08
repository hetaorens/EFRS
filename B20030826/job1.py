import SHA1
import SM4


filepath = "流图.png"


'''
采用SHA-1算法对文件进行哈希运算，
哈希值作为加密的密钥，
用户文件采用国密SM4对称密码加密上传至服务器；
同时利用SHA-1算法对文档关键字生成搜索符，一并上传。
'''
def GenerateFileHash(filepath):
    with open(filepath,"rb") as f:
        a=f.read()
        hash_msg=SHA1.SHA1().hash(a)
    return hash_msg

def GenerateHash(string):
    hash_msg=SHA1.SHA1().hash(string)
    return hash_msg    

def Savekey(key):
    with open("key.txt","wb") as f:
        f.write(key.encode())


def Encryption(filepath):
    key = GenerateHash(filepath)
    Savekey(key)

    with open(filepath,"rb") as f:
        a=f.read()
        with open(key+".txt","w") as m:
            m.write(SM4.SM4().encrypt_cbc(a, key).decode())



class InvertedIndex:
        
    def __init__(self):
        self.index = {}

    def add_words(self, doc, words):
        for word in words:
            word = GenerateHash(hash)
            if word not in self.index:
                self.index[word] = set()
            
            self.index[word].add(doc)

    
    def search(self, query):
        
        result = set()
        if query:
            query = GenerateHash(query)
            result = self.index.get(query, set())
        return result


if __name__ == '__main__':
    Encryption("流图.png")


