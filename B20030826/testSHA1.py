import unittest
import hashlib
import SHA1

testcase = ["sadwad","sdaw","2134","dsfaaeff","的饭卡还记得回复可见","3859274herfhdjkgiue39设计"]


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
            data = file.read()
            testfunc = SHA1.SHA1().hash(data).lower()
            standard = hashlib.sha1(data).hexdigest()
        self.assertEqual(standard, testfunc)
    

    def test_02(self):
        for i in testcase:
            print("当前参数：%s" % i)
            a = SHA1.SHA1().hash(i.encode()).lower()
            b = hashlib.sha1(i.encode()).hexdigest()
            self.assertEqual(a,b)

            
    def test_03(self):
            print("003")
            filepath = "job1.py"

            testfunc = ""
            with open(filepath, 'rb') as file:
                data = file.read()
                testfunc = SHA1.SHA1().hash(data).lower()
                standard = hashlib.sha1(data).hexdigest()
        
            self.assertEqual(standard, testfunc)
    
    def test_04(self):
            print("004")
            filepath = r"D:\github\EFRS\testcase\4.zip"

            testfunc = ""
            with open(filepath, 'rb') as file:
                data = file.read()
                testfunc = SHA1.SHA1().hash(data).lower()
                standard = hashlib.sha1(data).hexdigest()
        
            self.assertEqual(standard, testfunc)
    
    def test_05(self):
            print("005")
            filepath = r"D:\github\EFRS\testcase\1.jpg"

            testfunc = ""
            with open(filepath, 'rb') as file:
                data = file.read()
                testfunc = SHA1.SHA1().hash(data).lower()
                standard = hashlib.sha1(data).hexdigest()
        
            self.assertEqual(standard, testfunc)

    def test_06(self):
                print("006")
                filepath = r"D:\github\EFRS\testcase\2.dat"

                testfunc = ""
                with open(filepath, 'rb') as file:
                    data = file.read()
                    testfunc = SHA1.SHA1().hash(data).lower()
                    standard = hashlib.sha1(data).hexdigest()
            
                self.assertEqual(standard, testfunc)

    def test_07(self):
            print("007")
            filepath = r"D:\github\EFRS\testcase\3.md"

            testfunc = ""
            with open(filepath, 'rb') as file:
                data = file.read()
                testfunc = SHA1.SHA1().hash(data).lower()
                standard = hashlib.sha1(data).hexdigest()
        
            self.assertEqual(standard, testfunc)

    def test_08(self):
            print("008")
            filepath = r"D:\github\EFRS\testcase\Xftp.exe"

            testfunc = ""
            with open(filepath, 'rb') as file:
                data = file.read()
                testfunc = SHA1.SHA1().hash(data).lower()
                standard = hashlib.sha1(data).hexdigest()
        
            self.assertEqual(standard, testfunc)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    test = [Test("test_01"),Test("test_02"),Test("test_03"),Test("test_04"),Test("test_05"),Test("test_06"),Test("test_07"),Test("test_08")]

    suite.addTests(test)
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream = f,verbosity=2)  
        runner.run(suite)  
