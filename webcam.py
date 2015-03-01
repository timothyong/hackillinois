import cv2, time, pygame, os
import facial_recognition
from datetime import datetime
from twilio.rest import TwilioRestClient
ACCOUNT_SID = "AC5613e6c128b742fdf0eb79568de94e1e"
AUTH_TOKEN = "2a75e349e7bc974bdf2ef3b13455269f"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

def main():
    pygame.init()
    count = 0;
    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption('Hi')
    screen.fill((255, 255, 255))
    running = True
    results = []
    again = False
    while(running):
        activated = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                activated = True
            if event.type == pygame.QUIT:
                running = False
        while(activated):
            print datetime.now()
            time.sleep(5)
            webcam = cv2.VideoCapture()
            webcam.open(0)
            retval, image = webcam.retrieve()
            webcam.release()
            cv2.imwrite("static/images/test{0}.jpg".format(count), image)
            results.append(facial_recognition.check(image))
            print results[count]
            if results[count] == False and not again:
                client.messages.create(
                    to="9173286623",
                    from_="+13475274066",
                    body="DO NOT RESPOND TO THIS MESSAGE. An unrecognized person is using your laptop. Login and check who at http://perkt.io/results",
                    ) 
                again = True
            count += 1
            print datetime.now()
            #events = pygame.event.get()
            #for event in events:
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_SPACE:
                        #running = False
                        #activated = False
                    
            

if __name__ == "__main__":
      main()          
#for x in os.listdir('./static/images'):
#    os.remove('./static/images/{0}'.format(x))
