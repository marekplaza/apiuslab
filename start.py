#/bin/pyhton3
from multiprocessing.connection import wait
import sys
import os
import time
import subprocess
import shlex
#from sty import fg, bg, ef, rs

s = "ARISTA"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    PURPLE = '\33[95m'

class labs:
   MLAG = "LAB1_MLAG"
   LS = "LAB2_LS"
   VxLAN = "LAB3_VxLAN"
   EVPNL2 = "LAB4_EVPN_L2"
   EVPNL3 = "LAB5_EVPN_L3"
   gRPC = "LAB6_Telemetry_gRPC"


   print("     01. MLAG")
   print("     02. Leaf & Spine")
   print("     03. VxLAN")
   print("     04. EVPN VxLAN L2")
   print("     05. EVPN VxLAN L3")
   print("     06. Telemetria gRPC")

def logo():
   print("                                                                                                          ")
   print("          ..         ...                                                                                  ")
   print("        :!77!.      ~77!^                                                                                 ")
   print("      .~7777~       :!777!:                                                                               ")
   print("     :!777!:  ^!!~.  .~7777^                                                                              ")
   print("   .~7777^  .!777~. .. :!777!:                                   .^~:                                     ")
   print("  .7?777:  :7777^ .!77~ .!777?^                                  5&&#7                                    ")
   print("  .~777!~. .~777~. ^!~: ^!777!.                                  !5PY^                                    ")
   print("    :!7!7!:  :!77!.   .~7!!!^    .^!777~:.~^~:  :~~^.:~777!:     .^^^  .^~~:     .^~~:   .^!777~^         ")
   print("      ^!!!7~. .^^:   ^!!!7~.   .JG#&###&#G##&?  5###G#&##&&#P7   ?&##^ :###Y     :###Y  ?G##BB#&#G7       ")
   print("       .~777!.      ~777!:    :G##G7^:^!5####?  5###BJ~::~JB##5. ?###^ :###Y     :###Y !&##J...7P5Y^      ")
   print("         ^~~^       :~~^.     5&#B:      ?###?  5###~      ~##&? ?###^ :###Y     :B##Y :G###G5Y?7^        ")
   print("                              5##G.      7###?  5###^      ^##&? ?###^ :###Y     ~###Y   ~?YPGB###G^      ")
   print("                              ~###5~...:?B###?  5###G!:..:!G##G: ?###^ .B##B7:.:!G###Y ~?JJ^  .7##&Y      ")
   print("                               ^5#&&BBB#&###&?  5####&#BB#&&BY:  ?&##^  ~G#&&#B#&B##&Y !B&&#GPPB##P:      ")
   print("                                 :7JYYJ?~^777^  5##B~!?YYY?!:    ^777.   .~?JYY?!:777~  .~7JYYYJ7^        ")
   print("                                                5##B:                                                     ")
   print("                                                5&#B:                        T E C H N O L O G I E S      ")
   print("                                                ?P55.                                                     ")
   print("                                                                                                        \n")
 
def clearscreen():
   os.system('cls' if os.name == 'nt' else 'clear')


def header():
   zestaw = "🐳 🧪= 🚀 😍 👍 💻 ✔️"
   print("   Witaj w %s ApiusLAB  🐳 🧪 \n" % (s))
   #print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
   logo()


def go_to_shell(cmd):
   #wejści do shell'a
   #os.system('/bin/bash -c \"echo export MAREK=marek && /bin/bash\"')
   try:
      os.system('/bin/bash -c ./start.sh')
      #input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
   except:
      main()


def go_to_exit():
   #zakończenie programu
   clearscreen()
   header()
   print("     === Dziękujemy! ===\n ")
   time.sleep(0.3)
   #quit()
   clearscreen()
   os.system('exit')

def current_lab(status_laba, labs_name):
   md_table =  str(status_laba[0])
   md_table = str(md_table).replace("+","|")
   md_table = str(md_table).replace("#","Lp")
   md_table = ''.join(md_table.splitlines(keepends=True)[2:])

   #print(md_table)
   result = []

   for n, line in enumerate(md_table[1:-1].split('\n')):
       data = {}
       if n == 0:
           header = [t.strip() for t in line.split('|')[0:-1]]
           #print(header)
       if n > 1:
           values = [t.strip() for t in line.split('|')[1:-1]]
           for col, value in zip(header, values):
            data[col] = value
           result.append(data)
  
   #print(result[0].get("Lab Name") + " oraz " + result[0].get("Topo Path") + labs_name)
   if len(result) != 0:
      result = result[0].get("Lab Name")
   #print("result :" + str(result))
   else:
      result = "diff_lab"
   return result

def go_to_clab(command, shellType=False, stdoutType=subprocess.PIPE):
    try:
        process = subprocess.Popen(
            shlex.split(command), shell=shellType, stdout=stdoutType, bufsize=1000)
    except:
        print("ERROR {} while running {}".format(sys.exc_info()[1], command))
        return None
    calosc = []
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            printEnd = ' '
            line = output.strip().decode()
            if ((command.find("inspect") !=-1 or command.find("destroy -a") !=-1) and line.find("no containers found") != -1):
                rc = "Nie ma uruchomionych żadnych kontenerów cEoS"
                #return rc
                ##print("\n%s" % (rc))
                break

            # jesli deploy
            #if (command.find("deploy") !=-1):
            if (line.find("started")!= -1):
               print("Uruchamianie...", end=printEnd)
            if (line.find("Creating lab")!= -1):
               print("✔️\nTworzenie sieci", end=printEnd)
            if (line.find("Creating docker network")!= -1):
               print("✔️\nUruchamianie kontenerów cEoS (cierpliwości, to może zająć kilka minut...)", end=printEnd)
            if (line.find("Adding containerlab host")!= -1):
               print("✔️\nGotowe❗", end=printEnd)
               #print("\nTwoja topologia: \n")
            #if line.startswith('+') or line.startswith('|'):
            #   calosc.append(line)
            #   rc = '\n' + '\n'.join(calosc)
            #   break

            # jesli destroy
            #if (command.find("destroy") !=-1):
            if (command.find("destroy")!= -1 and line.find("Parsing")!=-1):
                print("Wyłączanie...", end=printEnd)
            if (command.find("destroy")!= -1 and line.find("Destroying lab")!= -1):
                print("✔️\nUsuwanie kontenerów", end=printEnd)
            if (command.find("destroy")!= -1 and line.find("Removing containerlab host entries from")!= -1):
                print("✔️\nGotowe❗", end=printEnd)
                rc = ""
            # zbieranie outputu - tabelki
            if line.startswith('+') or line.startswith('|'):
               calosc.append(line)
               rc = '\n' + '\n'.join(calosc)
               

    #rc = process.poll()
    #print('%s' % (calosc.readline()))
    #print("\r\n lab")
        if (command.find("inspect") !=-1 and line.find("no containers found") == -1):
           #calosc.append(line)
           #print("tutaaaj")
           rc = '\n' + '\n'.join(calosc)
           
        #print("\n========== Uruchomione środowiska: \n")
    #print(*calosc, sep="\n")
    #print("wynik" +  str(rc))
        #rc = print(*calosc, sep="\n")
    zmienna = "jaka"
    return (rc, zmienna)

def go_to_screen(labs_name):
   try:
      
      screen_command = "/usr/bin/screen -c ./" + str(labs_name) + "/.screenrc > /dev/null 2>&1"
      os.system('rm -f /root/.ssh/known_hosts')
      #print(screen_command)
      #input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
      os.system(screen_command)
      os.system('killall screen > /dev/null 2>&1')
      #input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)

   except:  
      main()

def mainmenu():
   clearscreen()
   header()
   status_laba = status_lab()
   print("  Status LAB'a: " + bcolors.PURPLE + str(status_laba[0]) + bcolors.ENDC)
   print("")
   print("========== Menu Głowne: Opcje wyboru ==========")
   print("")
   print("  Wybierz LAB'a:")
   print("")
   print("     01. MLAG")
   print("     02. Leaf & Spine")
   print("     03. VxLAN")
   print("     04. EVPN VxLAN L2")
   print("     05. EVPN VxLAN L3")
   print("     06. Telemetria gRPC")
   print("")
   #print(status_laba[0])
   if status_laba[0].find("Nie ma uruchomionych żadnych kontenerów cEoS") ==-1:
      print("     88. Reset")
   print("     99. Wyjście")
   print("")
   user_input = input(" Co chciałbyś zrobić? ").replace(' ', '')

   try: 
      if user_input.lower() == "01":
         labsmenu("MLAG")
      elif user_input.lower() == "02_02":
         labsmenu("LS")
      elif user_input.lower() == "03_03":
         labsmenu("VxLAN")
      elif user_input.lower() == "04_04":
         labsmenu("EVPNL2")
      elif user_input.lower() == "05_05":
         labsmenu("EVPNL3")
      elif user_input.lower() == "06_06":
         labsmenu("gRPC")
      elif user_input.lower() == "99":
         go_to_exit()
      elif ((status_laba[0] is not None) and (user_input.lower() == "88")):
         clearscreen()
         header()
         print("")
         print("========== Menu Głowne: Resetowanie LAB'a ==========")
         print("")
         go_to_clab("clab destroy -a")
         print("")
         input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
         mainmenu()
      else:
         main()
   except KeyboardInterrupt:
      go_to_exit()
      mainmenu()

def labsmenu(lab):
   clearscreen()
   header()
   status_laba = status_lab()
   labs_name = labs.__dict__[lab]
   c_lab = current_lab(status_laba, labs_name)
   print("  Status LAB'a: " + bcolors.PURPLE + str(status_laba[0]) + bcolors.ENDC)
   print("")
   print(" ========== Menu Głowne -> Wybierz LAB'a -> " + str(labs_name) + " ==========")
   print("")
   if (str(labs_name) != str(c_lab)):
      print("     01. Uruchom LAB")
   if (str(labs_name) == str(c_lab)):
      print("     02. Restartuj LAB")
      print("     03. Wyłącz LAB")
   if (str(labs_name) == str(c_lab)):
      print("     04. Screen do wszystkich routerów")
      print("     05. Shell/Bash")
   print("")
   print("     99. Powrót")
   print("")
   user_input = input(" Co chciałbyś zrobić? ").replace(' ', '')

   try: 
      if user_input.lower() == "01":
         clearscreen()
         header()
         print("\n ========== Menu Głowne -> Wybierz LAB'a -> " + str(labs_name) +" ->  Uruchom: ==========\n")
         #os.system("cd ./" + str(labs_name) + "/")
         command = "clab deploy -t ./" + str(labs_name) + "/" + str(labs_name) + ".yaml --reconfigure"
         go_to_clab(command)
         input("\n\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
         labsmenu(lab)
         
      elif user_input.lower() == "02":
         clearscreen()
         header()
         print("\n ========== Menu Głowne -> Wybierz LAB'a -> " + str(labs_name) + " -> Restart: ==========\n")
         #os.system("cd ./" + str(labs_name) + "/")
         command = "clab destroy -t ./" + str(labs_name) + "/" + str(labs_name) + ".yaml --cleanup"
         go_to_clab(command)
         print("\n\n Ponowne uruchamianie: \n")
         command = "clab deploy -t ./" + str(labs_name) + "/" + str(labs_name) + ".yaml --reconfigure"
         go_to_clab(command)
         input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
         labsmenu(lab)
      elif user_input.lower() == "03":
         clearscreen()
         header()
         print("\n ========== Menu Głowne -> Wybierz LAB'a -> " + str(labs_name) + " -> Wyłączanie: ==========\n")
         #os.system("cd ./" + str(labs_name) + "/")
         command = "clab destroy -t ./" + str(labs_name) + "/" + str(labs_name) + ".yaml --cleanup"
         go_to_clab(command)
         input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
         mainmenu()

      elif user_input.lower() == "04":
         go_to_screen(labs_name)
         labsmenu(lab)
      elif user_input.lower() == "05":
         go_to_shell(labs_name)
         labsmenu(lab)

      elif user_input.lower() == "99":
         main()
      else:
         labsmenu(lab)
   except KeyboardInterrupt:
      go_to_exit()

def go_to_exec(lab, command):
   return None


#def check_status():
#   clearscreen()
#   header()
#   print("\n========== Sprawdzanie statusu ==========\n")
#   status_laba = status_lab()
#   print(" " + status_laba)
#   input("\n" + bcolors.WARNING + " Naciśnij Enter by kontynuować" + bcolors.ENDC)
   
   #labsmenu()


def status_lab():
   command = "clab inspect --all"
   output = go_to_clab(command)
   return output

def main():
   mainmenu()







if __name__ == "__main__":
   start_time = time.time()  #debug for timing can be omitted.
   main()
   #print('Time to execute script %s seconds' % (time.time() - start_time))