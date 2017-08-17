#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from gnupg import GPG
from flask import Flask,request

app=Flask(__name__)

@app.route('/decryptMessage',methods=['POST','GET'])
def decryptMessage():
    try:
        Json_in_request=request.form['json']
    except:
       #Check for json
       return json.dumps({'errors':'Bad request parameter'})
   
    try:
        json_decoded=json.loads(Json_in_request)
    except:
        # Check if JSON is parseable
        return json.dumps({'errors':'Couldn`t parse Json'})
        
    try:
        ph=json_decoded['Passphrase']
        msg=json_decoded['Message']
    except:
        #check if the JSON prams are there
        return json.dumps({'errors':'bad Json parameter'})
        
    decrypted_obj=GPG().decrypt(passphrase=ph,message=msg)
    
    if decrypted_obj.ok==False:
        #check if the data is real
        return json.dumps({'errors':'Bad passphrase'})
        
    return json.dumps({'DecryptedMessage':decrypted_obj.data})

@app.route('/encryptMessage',methods=['POST','GET'])
def encryptMessage():
    try:
        Json_in_request=request.form['json']
    except:
       #Check for json
       return json.dumps({'errors':'Bad request parameter'})
   
    try:
        json_decoded=json.loads(Json_in_request)
    except:
        # Check if JSON is parseable
        return json.dumps({'errors':'Couldn`t parse Json'})
        
    try:
        ph=json_decoded['Passphrase']
        msg=json_decoded['Message']
    except:
        #check if the JSON prams are there
        return json.dumps({'errors':'bad Json parameter'})
        
    encrypted_obj=GPG().encrypt(passphrase=ph,data=msg)
    
    return json.dumps({'DecryptedMessage':decrypted_obj.data})

if __name__=='__main__':
   app.run(host='0.0.0.0',port=80)