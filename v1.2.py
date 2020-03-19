#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import sys
import os



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)          # taster levi
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # Mikroprekidac front levo
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)            # mikroprekidac parking levo
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # mikroprekidac back levo
GPIO.setup(26,GPIO.IN , pull_up_down=GPIO.PUD_DOWN)          # taster desni
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # mikroprekidac front desni
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # mikroprekidac parking desni0
GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)            # mikroprekiadac back desni
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # prazne boce
GPIO.setup(24, GPIO.OUT)                                     # motor desni nazad
GPIO.setup(7,GPIO.OUT)                                       # motor desni nazad
GPIO.setup(5,GPIO.OUT)                                       # motor desni napred
GPIO.setup(25,GPIO.OUT)                                      # motor desni napred

GPIO.setup(10, GPIO.OUT)                                     # motor levi nazad
GPIO.setup(9,GPIO.OUT)                                       # motor levi 0nazad
GPIO.setup(11,GPIO.OUT)                                       # motor levi napred
GPIO.setup(19,GPIO.OUT)                                      # motor levi napred

# iskljucujem sve releje na pocetku programa

GPIO.output(24,1)
GPIO.output(7,1)
GPIO.output(5,1)
GPIO.output(25,1)
GPIO.output(10,1)                                     
GPIO.output(9,1)                                      
GPIO.output(11,1)                                     
GPIO.output(19,1)        
        


def motorLevi():
    
    global prekidac1
    
    if GPIO.input(17) == True and GPIO.input(6) == True and GPIO.input(12) == False:
        GPIO.output(11,0)
        GPIO.output(19,0)
        print("LEVI zaglavio na prednjem i parkingu")
        
        while True:
            
            if GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False:
                GPIO.output(11,1)
                GPIO.output(19,1)
                break
            
    if GPIO.input(17) == True and GPIO.input(6) == True and GPIO.input(12) == True:
        GPIO.output(11,0)
        GPIO.output(19,0)
        print("LEVI zaglavio skroz pozadi")
        
        while True:
            
            if GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False:
                GPIO.output(11,1)
                GPIO.output(19,1)
                break
        
   
    
    
    if GPIO.input(18) == True and GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False: # and prekidac == "pocetak":
        print("LEVI pritisnut prekidac desni, pusten motor napred")
        #time.sleep(1)
        GPIO.output(11,0)
        GPIO.output(19,0)
        prekidac1 = "pocetak"
        
        while True:
            
        
            if GPIO.input(17) == False and GPIO.input(6) == False and GPIO.input(12) == False and prekidac1 == "pocetak":
                print("LEVI Izasao skroz napred i krece da se vraca nazad")
            
                GPIO.output(11,1)
                GPIO.output(19,1)
                GPIO.output(10,0)
                GPIO.output(9,0)
                prekidac1 = "kraj"
            
            if GPIO.input(6) == True and GPIO.input(12) == True and GPIO.input(17) == True and prekidac1 == "kraj":
                print("LEVI dosao do krajnjeg polozaja pozadi i pooceo da se vraca napred")
                
                GPIO.output(10,1)
                GPIO.output(9,1)
                GPIO.output(11,0)
                GPIO.output(19,0)
                prekidac1 = "zavrseno"
                
            
                
            if GPIO.input(17) == True and GPIO.input(12) == False and GPIO.input(6) == False and prekidac1 == "zavrseno":
                print("LEVI ispunjeni uslovi za gasenje motora GASIM MOTOR")
                GPIO.output(10,1)
                GPIO.output(9,1)
                GPIO.output(11,1)
                GPIO.output(19,1)
                print "KRAJJJJJJJ"
                break
       
    else:
        pass
                

def motorDesni():
    
    global prekidac
    
    if GPIO.input(27) == True and GPIO.input(22) == True and GPIO.input(8) == False:
        GPIO.output(25,0)
        GPIO.output(5,0)
        print("DESNI zaglavio na prednjem i parkingu")
        
        while True:
            
            if GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False:
                GPIO.output(25,1)
                GPIO.output(5,1)
                break
            
    if GPIO.input(27) == True and GPIO.input(22) == True and GPIO.input(8) == True:
        GPIO.output(25,0)
        GPIO.output(5,0)
        print("DESNI zaglavio skroz pozadi")
        
        while True:
            
            if GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False:
                GPIO.output(25,1)
                GPIO.output(5,1)
                break
   
    
    
    if GPIO.input(26) == True and GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False: # and prekidac == "pocetak":
        print("DESNI pritisnut prekidac desni, pusten motor napred")
        #time.sleep(1)
        GPIO.output(25,0)
        GPIO.output(5,0)
        prekidac = "pocetak"
        
        while True:
            
        
            if GPIO.input(27) == False and GPIO.input(22) == False and GPIO.input(8) == False and prekidac == "pocetak":
                print("DESNI Izasao skroz napred i krece da se vraca nazad")
            
                GPIO.output(25,1)
                GPIO.output(5,1)
                GPIO.output(24,0)
                GPIO.output(7,0)
                prekidac = "kraj"
            
            if GPIO.input(22) == True and GPIO.input(8) == True and GPIO.input(27) == True and prekidac == "kraj":
                
                print("DESNI dosao do krajnjeg polozaja pozadi i pooceo da se vraca napred")
                
                GPIO.output(24,1)
                GPIO.output(7,1)
                GPIO.output(5,0)
                GPIO.output(25,0)
                prekidac = "zavrseno"
                
            
                
            if GPIO.input(27) == True and GPIO.input(8) == False and GPIO.input(22) == False and prekidac == "zavrseno":
                print("DESNI ispunjeni uslovi za gasenje motora GASIM MOTOR")
                GPIO.output(5,1)
                GPIO.output(25,1)
                GPIO.output(7,1)
                GPIO.output(24,1)
                print "KRAJJJJJJJ"
                break
       
    else:
        pass
        


def punjenjeBoce():
    
    if GPIO.input(13):
        #print("pustam muziku")
        os.system ('omxplayer -o hdmi /home/pi/zvuk.mp3') 
            


while True:
    motorLevi()
    motorDesni()
    #punjenjeBoce()
        
