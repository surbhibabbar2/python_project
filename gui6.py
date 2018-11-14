#SURBHI BABBAR
#16csu376
#OBJECTIVE: automation of mouse pointer
#DESCRIPTION: it basically automates some of the applications
#eg:there are 5 buttons in gui as follows:
#1:facebook: it opens browser and automatically opens facebook account
#2:chrome:opens chrome
#3:music:plays music from library
#4:recycle bin:shows deleted files
#5:frequency of word in a file  
#tkinter is used for making gui
#for finding the cursor positions according to my screen pyautogui is used.

#CODE

import string
from tkinter import *
import pyautogui
root=Tk()
root.geometry("500x200")
def fb(event):
	#click the chrome icon
	pyautogui.moveTo(39,33,duration=3)
	pyautogui.doubleClick(39,33)
	#address bar
	pyautogui.moveTo(804, 562,duration=4)
	pyautogui.click(804, 562)
	#writing fb
	pyautogui.typewrite("FACEBOOK",interval=0.25)	
	pyautogui.typewrite(["enter"])
	#moving to fb link
	pyautogui.moveTo(669, 357,duration=4)
	pyautogui.click(669, 357)
	#enter the password
	pyautogui.moveTo(1416, 158,duration=6)
	pyautogui.typewrite("subro@12",interval=0.25)
	#login click
	pyautogui.moveTo(1574, 158,duration=1)
	pyautogui.click(1574, 158)
	



def cr(event):
	#chrome icon
	pyautogui.moveTo(39,33,duration=2)
	pyautogui.doubleClick(39,33)
	#address bar

	pyautogui.moveTo(804, 562,duration=4)
	pyautogui.click(804, 562)		
	





def mc(event):
	#move to music icon
	pyautogui.moveTo(56, 175,duration=2)
	pyautogui.doubleClick(56, 175)
	#play songs
	pyautogui.moveTo(837, 975,duration=5)
	pyautogui.click(837, 975)




def rb(event):
	#move to rb icon
	pyautogui.moveTo(44, 280,duration=2)
	pyautogui.doubleClick(44, 280)

	



def fy(event):

	
	freq = {} 
	file_obj = open('sample.txt', 'r')
	word_content = file_obj.read().lower() 
	reg_exp = re.findall(r'\b[a-z]{3,15}\b', word_content)

	for word in reg_exp:
		count = freq.get(word, 0) 
		freq[word] = count + 1 

	freq_list = freq.keys()

	for word in freq_list:
		print (word, freq[word])




but1=Button(root,text="FACEBOOK",fg="white",bg="blue")

but2=Button(root,text="CHROME",fg="white",bg="red")

but3=Button(root,text="MUSIC",fg="white",bg="green")

but4=Button(root,text="RECYCLEBIN",fg="white",bg="orange")
but5=Button(root,text="FREQUENCY",fg="white",bg="purple")




but1.bind("<Button-1>",fb)
but2.bind("<Button-1>",cr)
but3.bind("<Button-1>",mc)
but4.bind("<Button-1>",rb)
but5.bind("<Button-1>",fy)

but1.pack(fill=X)
but2.pack(fill=X)
but3.pack(fill=X)
but4.pack(fill=X)
but5.pack(fill=X)
root.mainloop()
