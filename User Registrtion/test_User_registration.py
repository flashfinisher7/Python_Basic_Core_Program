import unittest 
from User_registration import Name_First,Name_Last,Email_Id,Mobile_Number,User_Password

class UserValidation(unittest.TestCase):

    def test_first_name(self):
        self.assertEqual(Name_First('Anil'),True)
        self.assertEqual(Name_First('ANil'),False)
        self.assertEqual(Name_First('anil'),False)
        self.assertEqual(Name_First('An'),False)
        self.assertEqual(Name_First('Anil7'),False)
        self.assertEqual(Name_First('Anil  '),False)

    def test_last_name(self):
        self.assertEqual(Name_Last('Kumar'),True)
        self.assertEqual(Name_Last('KUmar'),False)
        self.assertEqual(Name_Last('Ku'),False)
        self.assertEqual(Name_Last('Kumar7'),False)
        self.assertEqual(Name_Last('KUMAR'),False)
    
    def test_email_id(self):
        self.assertEqual(Email_Id('anil@bl.co'),True)
        self.assertEqual(Email_Id('anil.kumar@bl.co.in'),True)
        self.assertEqual(Email_Id('ANIL@bl.Co'),False)
        self.assertEqual(Email_Id('An.7i@bl.co.in'),False)
        self.assertEqual(Email_Id('ani@bl.co'),True,)

    def test_mobile_number(self):
        self.assertEqual(Mobile_Number('00 0000000000'),False)
        self.assertEqual(Mobile_Number('91 9494400886'),True)
        self.assertEqual(Mobile_Number('91 9494400886'),True)
        
    
    def test_password(self):
        self.assertEqual(User_Password('A@7nil'),True)
        self.assertEqual(User_Password('ANIL7$'),True)
        self.assertEqual(User_Password('&$Anil'),False)
        self.assertEqual(User_Password('An@k1il'),False)
        self.assertEqual(User_Password('AN123@il'),True)

if __name__ == '__main__':
    unittest.main()