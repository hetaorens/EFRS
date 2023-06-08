import SM4
import unittest
from gmssl import sm4



class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        #print("测试前的操作")
    
    
    def tearDown(self) -> None:
        super().tearDown()
        #print("测试后的操作")


    def test_01(self):
        key = "1234"*4
        b = sm4.CryptSM4()
        b.set_key(key.encode(),mode=sm4.SM4_ENCRYPT)

        filepath = r"D:\github\EFRS\testcase\Xftp.exe"

        with open(filepath, 'rb') as file:
            data = file.read()      
            standard = b.crypt_cbc(bytes.fromhex("F"*32),data)
            testfunc = SM4.SM4().encrypt_cbc(data, key.encode())
        
        #print(testfunc,standard)


        self.assertEqual(standard, testfunc)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    test = [TestCase("test_01")]

    suite.addTests(test)
    with open('SM4Report.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream = f,verbosity=2)  
        runner.run(suite)  