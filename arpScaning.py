import configparser
from scapy.all import *

def arping():
    macs={}
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.2.0/24"),timeout=2)
    for snd, rcv in ans:
        macs[rcv.sprintf(r"%Ether.src%")] = rcv.sprintf(r"%ARP.psrc%")
	print rcv.src +" "+rcv.psrc
    return macs

def createList(macs):
    addresses = open("onlineDevices.txt","w")
    for i,j in macs.iteritems():
        addresses.write(i+"?"+j+"\n")
    addresses.close()

def oldListe():
    l=open("onlineDevices.txt","r")
    List=l.readlines()
    oldList={}
    for i in range(len(List)):
        mac,ip=List[i].split("?")
	ip=ip[:-1]
        oldList[mac]=ip	
        
    l.close()
    return oldList

def newListCr(newText):
    l=open("onlineDevices.txt","w")
    l.seek(0)
    l.truncate()
    l.close()
    createList(newText)	
    
        
def checkList():
    newList={}
    oldList={}
    newList=arping()
    oldList=oldListe()
    oldMacs=list(oldList.keys())
    newMacs=list(newList.keys())
    newText={}
    answers = ["y","Y","N","n"]
    
    for i in range(len(newList)):	
        if newMacs[i] in oldMacs:	    
            if newList[newMacs[i]]==oldList[newMacs[i]]:		
                newText[newMacs[i]]=newList[newMacs[i]]
                continue
            else:
                while (1):
                    answer = raw_input("\n Aginizda %s MAC adresli cihaz farkli bir IP adresine sahip. Listede degisikligi kaydetmek ister misiniz? (y/n): " %newMacs[i])
                    if (answer=="y" or answer=="Y"):
                        newText[newMacs[i]]=newList[newMacs[i]]
                        break
                    elif(answer=="n" or answer=="N"):
                        newText[newMacs[i]]=oldList[newMacs[i]]
                        break
                    else:
                        print ('Yanlis tusa bastiniz lutfen y veya n tuslarina basiniz')
        else:
            while 1:
                answer = raw_input("\nAginizda %s MAC adresli yeni bir cihaz bulundu. Listeye cihazi kaydetmek ister misiniz? (y/n): " %newMacs[i])
                if (answer=="y" or answer=="Y"):
                    newText[newMacs[i]]=newList[newMacs[i]]
                    break
                elif(answer=="n" or answer=="N"):
                    break
                else:
                    print ('Yanlis tusa bastiniz lutfen y veya n tuslarina basiniz')
    newListCr(newText)

def main():
    config=configparser.ConfigParser()
    config.read('config.conf')
    isFirstTime=config['DEFAULT']['isFirstTime']
    if(isFirstTime==True):
	config['DEFAULT']['isFirstTime']=False
        arp=arping()
	createList(arp)
    else:
	checkList()


if __name__ =="__main__": main()

