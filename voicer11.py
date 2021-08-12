from gtts import gTTS
import os
mytext="Jaaney do mujhe yaaron Main kaun tumhara hoon Jaaney do mujhe yaaron Main kaun tumhara hoon Meri koi manzil nahi Main ek awaara hoon Jaaney do mujhe yaaron Main kaun tumhara hooDuniya main mohabbat bhi Hoti hai naseebon se Duniya main mohabbat bhi Hoti hai naseebon se Kya pyaar ameeron ka
Humjaise gareebon se Ye chaand ki duniya hai Main Khota sitaara hoon Jaaney do mujhe yaaro nMain kaun tumhara hoon Aye dost mubarak h oAye dost mubarak hoYe mahal yeh rangralianMujhko toh bulati heinWaapas woh meri galiyaan
Main ek pardesi hoonMain ek banjara hoonJaaney do mujhe yaaron Main kaun tumhara hoon Meri koi manzil nahi Main ek awaara hoon"language='en'myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome1.mp3")
os.system("mpg3 welcome1.mp3")
