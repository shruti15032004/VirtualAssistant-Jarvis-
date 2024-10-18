import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    
    engine.say(audio) 

    engine.runAndWait() 
    

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("good Afternoon")
    else :
        speak("Good Evening")
    speak("I am Jarvis ,, please tell me how may i help you")
    
    
def takeCommand():
    
    #it take Microphone input
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...................")
        r.pause_threshold = 1
        audio = r.listen(source)
      
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in') 
        print(f"User said :{query}\n") 
    
    except Exception as e:
        #print(e)
        print("say that again please......")
        return "None"
    return query 
        
def sendEmail(to,content):
     server =smtplib.SMTP("smtp.gmail.com",587)
     server.ehlo()
     server.starttls()
     server.login('roselrakzi@gmail.com','roselrakzi123456789')
     server.sendmail.com('roselrakzi@gamil.com',to,content)
     server.close()
     
          
if __name__=="__main__" :
    
    wishMe()
    if 1:
        query=takeCommand().lower()
    
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("According to Wikipeda")
            print(results)
            speak(results) 
        
        elif 'open youtube' in query :

            webbrowser.open("youtube.com")
            
        elif 'open google' in query :
    
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query :
        
            webbrowser.open("stackoverflow.com")
         
        elif 'play music' in query:
            python_dir='D:\\python\\favorite'
            songs=os.listdir(python_dir)
            print(songs)
            os.startfile(os.path.join(python_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif 'open code' in query:
           code_path="C:\\Users\\shrey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(code_path)
           
        elif' email to shruti' in query:
            try:
                speak("What should i say ?")
                content =takeCommand()
                to ="roselrakzi@gmail.com"
                sendEmail(to,content)
                speak("Email has been Sent !")
            
            except Exception as e:
                print (e)
                speak("Sorry , shruti, I am not able to send this email")