#made by Shourya Deep Bera
from subprocess import sys, call
try:
    from alexachatbot.alexaAI import reply
except:
    print("The required package is not found")
    print("Downloading the required package")
    print("Please wait...")
    try:
        call([sys.executable,"-m", "pip", "--disable-pip-version-check", "-q", "install", "alexachatbot"])
        from alexachatbot.alexaAI import reply
        print("Sucessfully downloaded and installed the required package")
    except:
        print("Some error occured, could not install the required package")
        print("Please install the required package manually")
        print("by executing command <pip install alexachatbot>")
        print("Then rerun the code")
        quit()


print(" ______CHAT-BOT V-1.1______ ")
print("    By User-Unknown005")
while(True):
    y=str(input("YOU :  "))
    ly=y.lower()
    if "go offline" in ly:
        quit()
    rep=reply(y)
    print("BOT :  {}".format(rep))