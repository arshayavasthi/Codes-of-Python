from gtts import gTTS
import os
mytext="Teri aakhya ka yo kajal mann karein se koi ghayalTu sehad sehad pa dharalein mera pal pal pal yaa pal yaad teri tadapavese haaye"
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome1.mp3")
os.system("mpg3 welcome1.mp3")
