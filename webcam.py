import cv2, time, pygame

pygame.init()
count = 0;
while(1):
    activated = False
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SLASH:
                activated = True
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
                if event.key == pygame.K_MINUS:
                    activated = False
