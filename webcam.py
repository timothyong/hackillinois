import cv2, time, pygame, os

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
    while(running):
        activated = False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                activated = True
            if event.type == pygame.QUIT:
                running = False
        again = False
        while(activated):
            time.sleep(5)
            webcam = cv2.VideoCapture()
            webcam.open(0)
            retval, image = webcam.retrieve()
            webcam.release()
            cv2.imwrite("static/images/test{0}.png".format(count), image)
            results.append(check(image))
            if results[count] == False & ~again:
                client.messages.create(
                    to="9173286623",
                    from_="+13475274066",
                    body="DO NOT RESPOND TO THIS MESSAGE. An unrecognized person is using your laptop. Login and check who at http://perkt.io/results",
                    ) 
                again = True
            count += 1
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        activated = False
                        running = False
            

if __name__ == "__main__":
      main()          
#for x in os.listdir('./static/images'):
#    os.remove('./static/images/{0}'.format(x))
