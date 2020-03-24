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
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # ZAGLAVIO LEVO
GPIO.setup(26,GPIO.IN , pull_up_down=GPIO.PUD_DOWN)          # taster desni
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # mikroprekidac front desni
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # mikroprekidac parking desni0
GPIO.setup(8,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)            # mikroprekiadac back desni
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)           # ZAGLAVIO DESNO
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
    
    
    #Kad pritisnes prekidac, fioka se vrati skroz nazad i ceka 10 sekundi
    
    if GPIO.input(13) == True and GPIO.input(12) == False and GPIO.input(17) == True:
          
        time.sleep(2)
        
        if GPIO.input(13) == True and GPIO.input(12) == False and GPIO.input(17) == True:
            GPIO.output(10,1)                                     
            GPIO.output(9,1)                                      
            GPIO.output(11,1)                                     
            GPIO.output(19,1)
            GPIO.output(10,0)                                     
            GPIO.output(9,0)
            while True:
                if GPIO.input(6) == True and GPIO.input(12) == True:
                    GPIO.output(10,1)                                     
                    GPIO.output(9,1)
                    time.sleep(10)
                    GPIO.output(11,0)                                     
                    GPIO.output(19,0)
                    while True:
                        if GPIO.input(6) == False and GPIO.input(12) == False:
                            GPIO.output(11,1)                                     
                            GPIO.output(19,1)
                            GPIO.output(10,1)    #                                  
                            GPIO.output(9,1)     #
                            prekidac1 = "pocetak"
                            break
                    break
                    
             
    
    if GPIO.input(17) == False and GPIO.input(6) == False and GPIO.input(12) == False:
        GPIO.output(10,0)
        GPIO.output(9,0)
        GPIO.output(11,1)
        GPIO.output(19,1)
        print("LEVI zaglavio skroz napred")
        
        while True:
            
            if GPIO.input(17) == True and GPIO.input(6) == True and GPIO.input(12) == False:
                GPIO.output(10,1)
                GPIO.output(9,1)
                GPIO.output(11,1)
                GPIO.output(19,1)
                break
    #Ako zaglavi na prednjem i parkingu
    
    if GPIO.input(17) == True and GPIO.input(6) == True and GPIO.input(12) == False:
        GPIO.output(11,0)
        GPIO.output(19,0)
        print("LEVI zaglavio na prednjem i parkingu")
        
        while True:
            
            if GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False:
                GPIO.output(11,1)
                GPIO.output(19,1)
                GPIO.output(10,1)
                GPIO.output(9,1)
                break
    #Ako zaglavi skroz pozadi
    
    if GPIO.input(17) == True and GPIO.input(6) == True and GPIO.input(12) == True:
        GPIO.output(11,0)
        GPIO.output(19,0)
        print("LEVI zaglavio skroz pozadi")
        
        while True:
            
            if GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False:
                GPIO.output(11,1)
                GPIO.output(19,1)
                GPIO.output(10,1)
                GPIO.output(9,1)
                break
        
   
    
    
    if GPIO.input(18) == True and GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False: # and prekidac == "pocetak":
        time.sleep(0.2)
        if GPIO.input(18) == True and GPIO.input(17) == True and GPIO.input(6) == False and GPIO.input(12) == False:
            print("LEVI pritisnut prekidac desni, pusten motor napred")
            #time.sleep(1)
            GPIO.output(11,0)
            GPIO.output(19,0)
            prekidac1 = "pocetak"
        
    
       
            
            while True:
                
                if GPIO.input(13) == True :
                    
                    if GPIO.input(13) == True :
                        time.sleep(2)
                        if GPIO.input(13) == True:
                            GPIO.output(10,1)                                     
                            GPIO.output(9,1)                                      
                            GPIO.output(11,1)                                     
                            GPIO.output(19,1)
                            GPIO.output(10,0)                                     
                            GPIO.output(9,0)
                            while True:
                                if GPIO.input(6) == True and GPIO.input(12) == True:
                                    GPIO.output(10,1)                                     
                                    GPIO.output(9,1)
                                    time.sleep(10)
                                    GPIO.output(11,0)                                     
                                    GPIO.output(19,0)
                                    while True:
                                        if GPIO.input(6) == False and GPIO.input(12) == False:
                                            GPIO.output(11,1)                                     
                                            GPIO.output(19,1)
                                            GPIO.output(10,1)                                     
                                            GPIO.output(9,1)
                                            prekidac1 = "pocetak"
                                            break
                                    break
                        break   
                
            
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
                    time.sleep(1)
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
    
    
        #Kad pritisnes prekidac, fioka se vrati skroz nazad i ceka 10 sekundi
    
    if GPIO.input(21) == True and GPIO.input(8) == False:
        time.sleep(2)
        if GPIO.input(21) == True and GPIO.input(8) == False:
            GPIO.output(25,1)                                     
            GPIO.output(5,1)                                      
            GPIO.output(7,1)                                     
            GPIO.output(24,1)
            GPIO.output(24,0)                                     
            GPIO.output(7,0)
            while True:
                if GPIO.input(8) == True and GPIO.input(22) == True:
                    GPIO.output(24,1)                                     
                    GPIO.output(7,1)
                    time.sleep(10)
                    GPIO.output(5,0)                                     
                    GPIO.output(25,0)
                    while True:
                        if GPIO.input(8) == False and GPIO.input(22) == False:
                            GPIO.output(5,1)                                     
                            GPIO.output(25,1)
                            GPIO.output(24,1)                                     
                            GPIO.output(7,1)
                            prekidac = "pocetak"
                            break
                    break
        else:
            pass        
    else:
        pass
    #Ako zaglavi skroz napred
    
    if GPIO.input(27) == False and GPIO.input(22) == False and GPIO.input(8) == False:
        GPIO.output(24,0)
        GPIO.output(7,0)
        GPIO.output(5,1)                                     
        GPIO.output(25,1)
        print("DESNI zaglavio skroz napred")
        
        while True:
            
            if GPIO.input(27) == True and GPIO.input(22) == True and GPIO.input(8) == False:
                GPIO.output(24,1)
                GPIO.output(7,1)
                GPIO.output(25,1)
                GPIO.output(5,1)
                break
    #Ako zaglavi na prednjem i parkingu 
    
    if GPIO.input(27) == True and GPIO.input(22) == True and GPIO.input(8) == False:
        GPIO.output(25,0)
        GPIO.output(5,0)
        GPIO.output(24,1)
        GPIO.output(7,1)
        print("DESNI zaglavio na prednjem i parkingu")
        
        while True:
            
            if GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False:
                GPIO.output(25,1)
                GPIO.output(5,1)
                GPIO.output(24,1)
                GPIO.output(7,1)
                break
    #Ako zaglavi skroz pozadi
            
    if GPIO.input(27) == True and GPIO.input(22) == True and GPIO.input(8) == True:
        GPIO.output(25,0)
        GPIO.output(5,0)
        print("DESNI zaglavio skroz pozadi")
        
        while True:
            
            if GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False:
                GPIO.output(25,1)
                GPIO.output(5,1)
                GPIO.output(24,1)
                GPIO.output(7,1)
                break
   
    
    
    if GPIO.input(26) == True and GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False: # and prekidac == "pocetak":
        time.sleep(0.2)
        if GPIO.input(26) == True and GPIO.input(27) == True and GPIO.input(22) == False and GPIO.input(8) == False:
            print("DESNI pritisnut prekidac desni, pusten motor napred")
            #time.sleep(1)
            GPIO.output(25,0)
            GPIO.output(5,0)
            prekidac = "pocetak"
            
            while True:
                
                
                if GPIO.input(21) == True: 
        
                    if GPIO.input(21) == True : 
                        time.sleep(2)
                        if GPIO.input(21) == True :
                            GPIO.output(25,1)                                     
                            GPIO.output(5,1)                                      
                            GPIO.output(7,1)                                     
                            GPIO.output(24,1)
                            GPIO.output(24,0)                                     
                            GPIO.output(7,0)
                            while True:
                                if GPIO.input(8) == True and GPIO.input(22) == True:
                                    GPIO.output(24,1)                                     
                                    GPIO.output(7,1)
                                    time.sleep(10)
                                    GPIO.output(5,0)                                     
                                    GPIO.output(25,0)
                                    while True:
                                        if GPIO.input(8) == False and GPIO.input(22) == False:
                                            GPIO.output(5,1)                                     
                                            GPIO.output(25,1)
                                            GPIO.output(24,1)                                     
                                            GPIO.output(7,1)
                                            prekidac = "pocetak"
                                            break
                                    break
                    break            
                                
                   
                    
                
                
            
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
                    time.sleep(1)
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
        


            


while True:
    motorLevi()
    motorDesni()
    
        
