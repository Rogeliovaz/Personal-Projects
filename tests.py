import unittest
from encrypt import Salting, ReverseCipher1, ReverseCipher2, XORCipher, CaesarCipher, VigenereCipher, CustomMappingCipher

class TestSalting(unittest.TestCase):
    
    def test_default(self):
        s1 = Salting('GRAND VALLEY', ' salted')
        self.assertEqual('GRAND VALLEY salted', s1.cipher_text)

    def test_bad_data(self):
        with self.assertRaises(TypeError):
            s2 = Salting('GRAND VALLEY', 5)

        with self.assertRaises(TypeError):
            s3 = Salting(5, 'salted')
        
    def test_decrpyt(self):
        s3 = Salting('GRAND VALLEY', " gvsulakers")
        self.assertEqual('GRAND VALLEY', s3.__str__())

    def test_decrpyt_2(self):
        s4 = Salting('GRAND', ' hello')

class TestReverseCipher1(unittest.TestCase):
    
    def test_encrypt(self):
        rc1 = ReverseCipher1('GRAND VALLEY')
        self.assertEqual('YELLAV DNARG', rc1.cipher_text)

    def test_decrpyt(self):
        rc2 = ReverseCipher1('GRAND VALLEY')
        self.assertEqual('GRAND VALLEY', rc2.__str__())
    
    def test_bad_data(self):
        with self.assertRaises(TypeError):
            rc3 = ReverseCipher1(5)
        
        with self.assertRaises(TypeError):
            rc4 = ReverseCipher1(5.0)

        with self.assertRaises(TypeError):
            rc5 = ReverseCipher1(True)

class TestReverseCipher2(unittest.TestCase):
    
    def test_encrypt_space(self):
        rc = ReverseCipher2('Hello World!')
        self.assertEqual('olleH !dlroW', rc.cipher_text)

    def test_encrypt_no_space(self):
        rc = ReverseCipher2('GRANDVALLEY')
        self.assertEqual('YELLAVDNARG', rc.cipher_text)

    def test_decrpyt(self):
        rc2 = ReverseCipher2('GRAND VALLEY')
        self.assertEqual('GRAND VALLEY', rc2.__str__())
    

    def test_bad_data(self):
        with self.assertRaises(TypeError):
            rc3 = ReverseCipher2(5)
        
        with self.assertRaises(TypeError):
            rc4 = ReverseCipher2(5.0)

        with self.assertRaises(TypeError):
            rc5 = ReverseCipher2([])
        
class TestXORCipher(unittest.TestCase):
    def test_encryption(self):
        xor = XORCipher('Hello, Students', 'gvsu')
        self.assertEqual('ZS&', xor.cipher_text) # FIXME test pass on PL but this one fails ??
    
    def test_decryption(self):
        XOR = XORCipher('Hello, Students', 'gvsu')
        self.assertEqual('Hello, Students', XOR.__str__())

    def test_bad_data_text(self):
        with self.assertRaises(TypeError):
            XOR = XORCipher(6 , 'gvsu')
    
    def test_bad_data_key(self):
        with self.assertRaises(TypeError):
            XOR = XORCipher("Hello, Students" , 78)

class TestCaesarCipher(unittest.TestCase):
    def test_encryption_example_1(self):
        cc = CaesarCipher('HELLO', 3)
        self.assertEqual('KHOOR', cc.cipher_text)
    
    def test_encryption_example_2(self):
        cc = CaesarCipher('GvsuLakers', 6)
        self.assertEqual('MbyaRgqkxy', cc.cipher_text)
    
    def test_text_with_space(self):
        cc = CaesarCipher('Gojo is beholds the six eyes', 6)
        self.assertEqual('Mupu oy hknurjy znk yod keky', cc.cipher_text )
    
    def test_key_more_than_26(self):
        cc = CaesarCipher('HELLO', 100)
        self.assertEqual('DAHHK', cc.cipher_text)

    def test_kwy_less_than_26(self):
        cc = CaesarCipher('BBB', -27)
        self.assertEqual('AAA', cc.cipher_text)

    def test_negative_number(self):
        cc = CaesarCipher('BBB', -1)
        self.assertEqual('AAA', cc.cipher_text)

    def test_empty_string(self):
        cc = CaesarCipher(' ', 3)
        self.assertEqual(' ', cc.cipher_text)

    def test_decrypiton(self):
        cc = CaesarCipher('HELLO', 3)
        self.assertEqual('HELLO', cc.__str__())

    def test_bad_data_text(self):
        with self.assertRaises(TypeError):
            cc = CaesarCipher(5, 5)

    def test_bad_data_key(self):
        with self.assertRaises(TypeError):
            cc = CaesarCipher(5, 'Bad data')
    
class TestVigenereCipher(unittest.TestCase):
    def test_example_1(self):
        vc = VigenereCipher('HELLO', 'KEYKE')
        self.assertEqual("RIJVS", vc.cipher_text)
    
    def test_example_2(self):
        vc = VigenereCipher('Hello Students', '163')
        self.assertEqual("Ikomu Tzxekquy", vc.cipher_text)

    def test_decryption_example_1(self):
        vc = VigenereCipher('HELLO', 'KEYKE')
        self.assertEqual('HELLO', vc.__str__())

    def test_decryption_example_2(self):
        vc = VigenereCipher('Hello Students', '163')
        self.assertEqual("Hello Students", vc.__str__())

class TestCustomMappingCipher(unittest.TestCase):  
    def test_example_1(self):
        cmc = CustomMappingCipher('Hello Students. Welcome to GVSU!')   
        self.assertEqual('gkPP"m5oK&k$o~*m+kP/"Vkmo"my15YQ', cmc.cipher_text)
    


if __name__ == "__main__":
    # Isolated Testing for Salting
    suite_salting = unittest.TestSuite()
    suite_salting.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSalting))
    rc1_runner = unittest.TextTestRunner()
    #rc1_runner.run(suite_salting)

    # Isolated Testing for ReverseCipher1
    suite_rc1 = unittest.TestSuite()
    suite_rc1.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReverseCipher1))
    rc1_runner = unittest.TextTestRunner()
    #rc1_runner.run(suite_rc1)

    # Isolated Testing for ReverseCipher2
    suite_rc2 = unittest.TestSuite()
    suite_rc2.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReverseCipher2))
    rc2_runner = unittest.TextTestRunner()
    rc2_runner.run(suite_rc2)

    # Isoalted Testing for XOCipher
    suite_XOR = unittest.TestSuite()
    suite_XOR.addTest(unittest.TestLoader().loadTestsFromTestCase(TestXORCipher))
    XOR_runner = unittest.TextTestRunner()
    #XOR_runner.run(suite_XOR)

    # Isolated test for CaesarCipher
    suite_cc = unittest.TestSuite()
    suite_cc.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCaesarCipher))
    cc_runner = unittest.TextTestRunner()
    #cc_runner.run(suite_cc)

    # Isolated test for VigenereCipher
    suite_vc = unittest.TestSuite()
    suite_vc.addTest(unittest.TestLoader().loadTestsFromTestCase(TestVigenereCipher))
    vc_runner = unittest.TextTestRunner()
    #cc_runner.run(suite_vc)

    # Isolated test for CustomMappingCipher
    suite_cmc = unittest.TestSuite()
    suite_cmc.addTest(unittest.TestLoader().loadTestsFromTestCase(TestCustomMappingCipher))
    cmc_runner = unittest.TextTestRunner()
    #cmc_runner.run(suite_cmc)
