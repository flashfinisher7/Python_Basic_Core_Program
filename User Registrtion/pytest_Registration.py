"""
Author:anil(mvsanilkumar07@gmail.com)
Date: 2021-09-26 15:07
Last Modified by:anil(mvsanilkumar07@gmail.com)
Last Modified time:2021-09-26 15:20
Title : User Registration problem
"""

import pytest
from User_registration import Name_First,Name_Last,Email_Id,Mobile_Number,User_Password

def test_first_name():
    assert Name_First('Anil')==True
    assert Name_First('ANil')==False
    assert Name_First('anil')==False

def test_last_name():
    assert Name_Last('Kumar')==True
    assert Name_Last('KUmar')==False
    assert Name_Last('KUMAR')==False 

def test_email_id():
    assert Email_Id('anil@bl.co')==True
    assert Email_Id('anil.kumar@bl.co.in')==True
    assert Email_Id('ANIL@bl.co')==False 

def test_mobile_number():
    assert Mobile_Number('00 0000000000')==False
    assert Mobile_Number('81 7989886451')==True
    assert Mobile_Number('80 8234567092')==True

def test_password():
    assert User_Password('A@7nil')==True 
    assert User_Password('ANIL1$')==True
    assert User_Password('&$Anil')==False