#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest
import requests as r

class testdecryptMessage(unittest.TestCase):
    
    def test_bad_post_pram(self):
        'Test what will happen, If we supply wrong REQUEST parameter(s)'
        self.assertEqual(r.post('http://localhost/decryptMessage',{'json1':'{"Passphrase":"__sss__","Message":"ddd"}'}).content \
        , json.dumps({'errors':'Bad request parameter'}))
    
    def test_bad_json_prams(self):
        'Test what will happen, if we supply the wrong JSON parameters'
        
        self.assertEqual(r.post('http://localhost/decryptMessage',{'json':'{"pass":"__sss__","Msg":"ddd"}'}).content \
        ,json.dumps({'errors':'bad Json parameter'}))
        
    def test_bad_passph(self):
        'Test what will happen, If we supply an random Message'
        
        self.assertEqual(r.post('http://localhost/decryptMessage',{'json':'{"Passphrase":"bad","Message":"bad"}'}).content \
        ,json.dumps({'errors':'Bad passphrase'}))
    
    def test_bad_json(self):
        'Test what will happen, If we supply Broken Json (or text)'
        self.assertEqual(r.post('http://localhost/decryptMessage',{'json':'{"Passphrase""bad json""Message":"bad"}'}).content \
        ,json.dumps({'errors':'Couldn`t parse Json'}))
    
    def test_good_passph(self):
        'Test what will happen, If we supply the right Message and Passphrase'
        passph='pass'
        encrypted_msg='''
-----BEGIN PGP MESSAGE-----
Version: GnuPG v1

jA0EBwMCcTtyjpdgDKRg0jsBULCFVY2WwE8ePmj2iG3RV5JXZH+h9ncyjzvFw+R4
omJnWIH/64Q/928h5ZQhhIJCCWd1b3BcKpiUJg==
=Rj/6
-----END PGP MESSAGE-----'''
        decrypted_msg='hello\n'
        
        self.assertEqual(r.post('http://localhost/decryptMessage',{'json':json.dumps({"Passphrase":passph,"Message":encrypted_msg})}).content,\
        json.dumps({"DecryptedMessage":decrypted_msg}))
    

app_test_suite = unittest.TestLoader().loadTestsFromTestCase(testdecryptMessage)
unittest.TextTestRunner(verbosity=2).run(app_test_suite)
