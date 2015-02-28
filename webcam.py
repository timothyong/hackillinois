import cv2, time, pygame, os

pygame.init()
count = 0;
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Tutorial 1')
screen.fill((255, 255, 255))
running = True
while(running):
    activated = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            activated = True
        if event.type == pygame.QUIT:
            running = False
    while(activated):
        time.sleep(5)
        webcam = cv2.VideoCapture()
        webcam.open(0)
        retval, image = webcam.retrieve()
        webcam.release()
        cv2.imwrite("static/images/test{0}.png".format(count), image)
        count += 1
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    activated = False
                    running = False
            if event.type == pygame.QUIT:
                running = False

#for x in os.listdir('./static/images'):
#    os.remove('./static/images/{0}'.format(x))
