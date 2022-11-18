#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

try:
	import requests,time,random,string,sys,os,time
	import itertools,threading
	from colorama import Fore,init
except ModuleNotFoundError:
	print ("Module Not Installed Type:bash module.sh")

headers = {
    'authority': 'instagram.qlizz.com',
    'accept': '*/*',
    'accept-language': 'id,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga=GA1.2.684540350.1652173099; _gid=GA1.2.1932374052.1652173099; _gat_gtag_UA_137153197_1=1; __gads=ID=5a201913cb3adcd6-2285e36d20d300f8:T=1652173100:RT=1652173100:S=ALNI_Ma5T99MHBxaAI7ZNxZzKkvhw13pcg; XSRF-TOKEN=eyJpdiI6IitcL21FZlU1XC82WXBRQ1E0ZlNXY0lydz09IiwidmFsdWUiOiJYTm82MGFXQWhHZ1UxQmZZZXI3VTdaQ0syalRhZ3ZEcFVUenI5TmVpTTl6VWMyZHpmNWtFZFlWWWhXVGN2SVlMdFZBR2UwRmcwYnRHeDJhaWxqK045QT09IiwibWFjIjoiZWM1ZjRjMTBlNDQ0NGU3NjgzN2FmMDA1ZTg5NjJiMjBmNTlmMjQ0MDFlNTBlODIxMTkwNGVjYTY5NTk1YTlhMSJ9; laravel_session=eyJpdiI6InNUXC9HUDlQUXdcL3lBdmFQTktWNWJVQT09IiwidmFsdWUiOiI1VEx5T29GR04zZVwvOUlzUVR1T3ZVbG5iK1FQWXcxYlR4ZHhwNkpoK2hzSXRPcEN1c1o3ZWk0SUVKcHpjcGd4bXRnSWVReU1qUURCcG8wUVd1ejA4VGc9PSIsIm1hYyI6ImZkOGNiNmVmNDBkYTFkN2Q4MmY1YmQ1NDFkYTEzMmE5ZWUwNWNmNWQ3NWU2MmU4ODVlZWI5MThmMmVhYjg4M2IifQ%3D%3D',
    'origin': 'https://instagram.qlizz.com',
    'referer': 'https://instagram.qlizz.com/autofollowers',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    'x-requested-with': 'XMLHttpRequest',
}

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

#╦┌┐┌┌─┐┌┬┐┌─┐  ╔═╗┌─┐┬  
#║│││└─┐ │ ├─┤  ╠╣ │ ││  
#╩┘└┘└─┘ ┴ ┴ ┴  ╚  └─┘┴─┘

def countdown(time_sec):
	try:
		while time_sec:
			mins, secs = divmod(time_sec,60)
			timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Loading \033[1;92m{:02d}:{:02d}'.format(mins,secs)
			print(timeformat,end='\r')
			time.sleep(1)
			time_sec -= 1
		print (f"{W}[{R}•{W}] Adding Followers{abu}....              ")
		time.sleep(5)
	except KeyboardInterrupt:
                print (f"{W}Program Terminated [{R}!{W}]")

def igeh():
    Username = input("\033[1;0m"+"["+Fore.RED+"•\033[1;0m] Username Instagram "+Fore.RED+":\033[1;96m ")
    bruh = {
        'username': user,
        'password': passw,
    }
    s = requests.Session()
    s.post('https://instagram.qlizz.com/login', data=bruh)
    alok = s.get('https://instagram.qlizz.com/autofollowers').text
    #print (alok)
    a = alok.split('name="_token" value="')[1];
    tok = a.split('"')[0];
    data = {
        '_token': tok,
        'link': Username,
        'tool': 'autofollowers',
    }
    while True:
        response = s.post('https://instagram.qlizz.com/send', headers=headers, data=data).text
        print (response)
        countdown(3600)
        #if "Your post is successfully added for free 10 followers. You will get followers in within 1 hour." in response:
        #print ("\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;97m Succesfully Added \033[1;92m10 \033[1;96mFollowers To \033[1;93m"+Username)
        	#countdown(3600)
        #else:
    	    #print (response)
    	    #countdown(3600)
    #print ("*Your response code:* _"+response+"_")

def support():
    os.system("xdg-open https://youtube.com/channel/UCyxWbQIfP1ewwQou-gqZ2Iw")
    print ("\033[1;97mThx For Support Me \033[1;96m:)")

def banner():
	s=requests.Session()
	ip=s.get('https://api.ipify.org').text
	localtime=time.asctime(time.localtime(time.time()))
	os.system("clear")
	print ("\033[1;95m╦\033[1;97m┌┐┌┌─┐┌┬┐┌─┐  \033[1;96m╔═╗\033[1;97m┌─┐┬   \033[1;93m|"+Fore.RED+" » \033[1;97mCreator "+Fore.RED+": \033[1;97mRizky ")
	print ("\033[1;95m║\033[1;97m│││└─┐ │ ├─┤  \033[1;96m╠╣ \033[1;97m│ ││   \033[1;93m|"+Fore.RED+" » \033[1;97mwa "+Fore.RED+": \033[1;97m+6283166155950"+Fore.BLUE+" Executed")
	print ("\033[1;95m╩\033[1;97m┘└┘└─┘ ┴ ┴ ┴  \033[1;96m╚  \033[1;97m└─┘┴─┘ \033[1;93m|"+Fore.RED+" » \033[1;97mStatus  "+Fore.RED+": \033[1;92mAlpha Beta\033[1;96m")
	print ("\033[1;93m  { "+Fore.RED+"•"+Fore.YELLOW+"•"+Fore.GREEN+"• \033[1;95mFree \033[1;96mInstagram \033[1;97mFollower"+Fore.RED+" | \033[1;97mBy OREN "+Fore.GREEN+"•"+Fore.YELLOW+"•"+Fore.RED+"•\033[1;93m }\n")
	print ("\033[1;97mIp Kamu "+Fore.RED+": \033[1;93m"+ip)
	print ("\033[1;97mWaktu "+Fore.RED+": \033[1;93m"+localtime)
	print ("\n\033[1;97m[\033[1;92m01\033[1;97m]"+Fore.RED+".\033[1;97mStart InstaFol\n\033[1;97m[\033[1;92m02\033[1;97m]"+Fore.RED+".\033[1;97mSupport Me\n\033[1;97m[\033[1;92m03\033[1;97m]"+Fore.RED+".\033[1;97mBug Report\n\033[1;97m[\033[1;92m04\033[1;97m]"+Fore.RED+"."+Fore.YELLOW+"Exit\n")

r = random.choice(string.ascii_letters)
an = random.choice(string.ascii_letters)
dom = random.choice(string.ascii_letters)
#user = input("username akun tumbal\ninput> ")
#passw = input("password akun tumbal\ninput> ")
user = f"{dom}ammar-rifa_prikitiw{an}{r}"
passw = f"co{dom}i{an}pyright{r}"
#XenziGay = input("username yang ingin di tambah follower nya, tanpa @\ninput> ")
def mulai():
	banner()
	pilih = input("\033[1;97mPilih ="+Fore.RED+"⟩\033[1;96m ")
	if pilih == "1" or pilih == "01":
	    igeh()
	if pilih == "2" or pilih == "02":
	    support()
	if pilih == "3" or pilih == "03":
	    os.system("xdg-open https://instagram.com/ammarexecuted")
	    print ("\033[1;97mThx For Report Bug Tools \033[1;96m:)")
	if pilih == "4" or pilih == "04":
	    sys.exit("Thx For Using My Tools")

# Loading Starr Tools
def pro():
        mulai()
done = False
def loading():
    for c in itertools.cycle(['Loading [...............]','Loading [█.............█]','Loading [██...........██]','Loading [███.........███]','Loading [████.......████]','Loading [█████.....█████]','Loading [██████...██████]','Loading [███████.███████]','Loading [███████████████]','Loading [███████.███████]','Loading [██████...██████]','Loading [█████.....█████]','Loading [████.......████]','Loading [███.........███]','Loading [██...........██]','Loading [█.............█]','Loading [...............]','Loading [█.............█]','Loading [██...........██]','Loading [███.........███]','Loading [████.......████]','Loading [█████.....█████]','Loading [██████...██████]','Loading [███████.███████]','Loading [███████████████]']):
        if done:
            break
        sys.stdout.write('\r'+c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r              ')
    print ("                                                ")
    pro()
t = threading.Thread(target=loading)
t.start()

time.sleep(2.60)
done = True
