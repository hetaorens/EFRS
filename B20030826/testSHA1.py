import unittest
import hashlib
import SHA1

testcase = ["sadwad","sdaw","2134","dsfaaeff"]


class Test(unittest.TestCase):
    
    def setUp(self) -> None:
        super().setUp()
        print("测试前的操作")
    
    
    def tearDown(self) -> None:
        super().tearDown()
        print("测试后的操作")

    def test_01(self):
        print("001")
        filepath = "流图.png"

        testfunc = ""
        with open(filepath, 'rb') as file:
            # while True:
            #     # 以每次读取的块大小更新哈希对象
            #     data = file.read(4096)  # 每次读取4096字节
            #     if not data:
            #         break
            #     hashlib.sha1().update(data)
            #     testfunc =testfunc + SHA1.SHA1().hash(data).lower()
            data = file.read()
            hashlib.sha1().update(data)
            testfunc = SHA1.SHA1().hash(data).lower()
        
        standard = hashlib.sha1().hexdigest()

        print(type(standard))
        print(type(testfunc))
        
        self.assertEqual(standard, testfunc)




    def test_02(self):
        for i in testcase:
            print("当前参数：%s" % i)
            a = SHA1.SHA1().hash(i.encode()).lower()
            b = hashlib.sha1(i.encode()).hexdigest()
            self.assertEqual(a,b)





if __name__ == '__main__':
    suite = unittest.TestSuite()
    test = [Test("test_01"),Test("test_02")]

    suite.addTests(test)
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream = f,verbosity=2)  
        runner.run(suite)  
