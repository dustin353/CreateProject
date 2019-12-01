# Dustin Choat
# Time Spent 9 hr

#Sources used:
'''
http://thepythongamebook.com/en:pygame:step003
http://thepythongamebook.com/en:pygame:step010
http://thepythongamebook.com/en:pygame:step011
http://thepythongamebook.com/en:pygame:step012
*Royalty Free Music from Bensound*
https://www.bensound.com/royalty-free-music/track/the-lounge
Sound effects:
http://www.wavsource.com/sfx/sfx2.htm
oof sound effect from Roblox
I made the chip drop sound by tapping my phone against my desk
'''
def replay():
    play_again = input('play again? Y/N\n')
    if play_again.lower() == 'y':
        ConnectFour()
        
def ConnectFour():
    import pygame
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()
    screen=pygame.display.set_mode((450,510)) # sets the size for the window that contains the game
    background = pygame.Surface(screen.get_size()) # sets the background to be the size of the game window
    background.fill((255,255,255))     # fill the background white 
    background = background.convert()  # prepare for faster blitting
    ballsurface = pygame.Surface((430,390))     # create a rectangular surface for the ball
    ballsurface.fill((0,0,255)) # colors the connect four frame blue
    ballsurface = ballsurface.convert() # prepare for faster blitting
    ballsurface2 = pygame.Surface((430, 50)) # creates a surface for the checker above the connect four frame
    ballsurface2.fill((255,255,255)) # colors the surface white so it blends in with the background 
    ballsurface2 = ballsurface2.convert() #prepare for faster blitting

    x = 35
    y = 55
    for i in range(6):
        for i in range(7):
            pygame.draw.circle(ballsurface, (255,255,255), (x,y),25) #draws white circle at position
            x += 60
        x = 35
        y += 60
    ballsurface = ballsurface.convert() #prepare for faster blitting
    ballx = 10
    bally = 110
    ballx2 = 10
    bally2 = 50

    #------- blit the surfaces on the screen to make them visible
    screen.blit(background, (0,0))     # blit the background on the screen (overwriting all)
    screen.blit(ballsurface, (ballx, bally))# blit the topleft corner of ball surface at pos (ballx, bally)
    screen.blit(ballsurface2, (ballx2, bally2))# blit the topleft corner of ball surface 2 at pos (ballx2, bally2)
    def write(msg="Connect Four"):
        myfont = pygame.font.SysFont("None", 25)
        mytext = myfont.render(msg, True, (0,0,0))
        mytext = mytext.convert_alpha()
        return mytext
    textsurface = write("Connect Four")
    screen.blit(textsurface, (10,10))
    clock = pygame.time.Clock()
    mainloop = True
    FPS = 30 # desired framerate in frames per second. try out other values !
    playtime = 0.0

    sleep = 0
    x1 = 215
    y1 = 355
    y2 = 355
    unpress = 1
    unpress2 = 1
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    in_play = []
    play_position = ''
    wincheck = []
    win_position = ''
    endgame = 0

    pygame.draw.circle(ballsurface2, (0,0,0), (x1,25),25)
    screen.blit(ballsurface2, (ballx2, bally2))

    chip = pygame.mixer.Sound('chip.wav')
    music = pygame.mixer.music.load('jazz.mp3')
    music1 = True
    oof = pygame.mixer.Sound('oof1.wav')
    pygame.mixer.music.play(-1)

    ##### FUNCTION TO CHECK IF THERE HAS BEEN A WINNER #####
    def win_check(wincheck):
        winner = 0
        #VERTICAL WIN
        if (x1,y1,c1,c2) in wincheck and (x1,(y1+60),c1,c2) in wincheck and (x1,(y1+120),c1,c2) in wincheck and (x1,(y1+180),c1,c2) in wincheck:
            winner = 1
        #HORIZONTAL WIN
        if (35,y1,c1,c2) in wincheck and (95,y1,c1,c2) in wincheck and (155,y1,c1,c2) in wincheck and (215,y1,c1,c2) in wincheck:
            winner = 1
        if (95,y1,c1,c2) in wincheck and (155,y1,c1,c2) in wincheck and (215,y1,c1,c2) in wincheck and (275,y1,c1,c2) in wincheck:
            winner = 1
        if (155,y1,c1,c2) in wincheck and (215,y1,c1,c2) in wincheck and (275,y1,c1,c2) in wincheck and (335,y1,c1,c2) in wincheck:
                        winner = 1
        if (215,y1,c1,c2) in wincheck and (275,y1,c1,c2) in wincheck and (335,y1,c1,c2) in wincheck and (395,y1,c1,c2) in wincheck:
            winner = 1
        #DIAGONAL WIN
        if (x1,y1,c1,c2) in wincheck and ((x1+60),(y1-60),c1,c2) in wincheck and ((x1+120),(y1-120),c1,c2) in wincheck and ((x1+180),(y1-180),c1,c2) in wincheck:
            winner = 1
        if ((x1-60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck and ((x1+60),(y1-60),c1,c2) in wincheck and ((x1+120),(y1-120),c1,c2) in wincheck:
            winner = 1
        if ((x1-120),(y1+120),c1,c2) in wincheck and ((x1-60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck and ((x1+60),(y1-60),c1,c2) in wincheck:
            winner = 1
        if ((x1-180),(y1+180),c1,c2) in wincheck and ((x1-120),(y1+120),c1,c2) in wincheck and ((x1-60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck:
            winner = 1
        if (x1,y1,c1,c2) in wincheck and ((x1-60),(y1-60),c1,c2) in wincheck and ((x1-120),(y1-120),c1,c2) in wincheck and ((x1-180),(y1-180),c1,c2) in wincheck:
            winner = 1
        if ((x1+60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck and ((x1-60),(y1-60),c1,c2) in wincheck and ((x1-120),(y1-120),c1,c2) in wincheck:
            winner = 1
        if ((x1+120),(y1+120),c1,c2) in wincheck and ((x1+60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck and ((x1-60),(y1-60),c1,c2) in wincheck:
            winner = 1
        if ((x1+180),(y1+180),c1,c2) in wincheck and ((x1+120),(y1+120),c1,c2) in wincheck and ((x1+60),(y1+60),c1,c2) in wincheck and (x1,y1,c1,c2) in wincheck:
            winner = 1
        return winner
    ##### FUNCTION TO CHECK IF THERE HAS BEEN A WINNER #####

    while mainloop:
        milliseconds = clock.tick(FPS) # do not go faster than this frame rate
        playtime += milliseconds / 1000.0
        # ----- event handler -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # pygame window closed by user
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # user pressed ESC
        pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                                   " Playtime: {:.2} seconds".format(
                                   clock.get_fps(),playtime))
        pygame.display.flip()      # flip the screen like in a flipbook
        pressedkeys = pygame.key.get_pressed()
        #if pressedkeys[pygame.K_o]:
        #oof.play()
        if pressedkeys[pygame.K_m]:
            if unpress >= 500:
                unpress = 0
                if music1:
                    pygame.mixer.music.stop()
                    music1 = False
                elif not music1:
                    pygame.mixer.music.play(-1)
                    music1 = True
        if pressedkeys[pygame.K_RIGHT]:
            if endgame == 1:
                break
            if x1<395:
                if unpress >= 500:
                    x = 35
                    y = 25
                    for i in range(7):
                        pygame.draw.circle(ballsurface2, (255,255,255), (x,y),25)
                        screen.blit(ballsurface2, (ballx2, bally2))
                        x += 60
                    x1 += 60
                    pygame.draw.circle(ballsurface2, (c1,c2,c3), (x1,25),25)
                    screen.blit(ballsurface2, (ballx2, bally2))
                    unpress = 0
                unpress += 1
        elif pressedkeys[pygame.K_LEFT]:
            if endgame == 1:
                break
            if x1>35:
                if unpress >= 500:
                    x = 35
                    y = 25
                    for i in range(7):
                        pygame.draw.circle(ballsurface2, (255,255,255), (x,y),25)
                        screen.blit(ballsurface2, (ballx2, bally2))
                        x += 60
                    x1 -= 60
                    pygame.draw.circle(ballsurface2, (c1,c2,c3), (x1,25),25)
                    screen.blit(ballsurface2, (ballx2, bally2))
                    unpress = 0
                unpress += 1
        if not pressedkeys[pygame.K_RIGHT] and not pressedkeys[pygame.K_LEFT] and not pressedkeys[pygame.K_m]:
            unpress = 501
        if pressedkeys[pygame.K_DOWN]:
            if endgame == 1:
                break
            if unpress2 >= 500:
                play_position = x1,55
                if play_position not in in_play:
                    play_position = x1,y1
                    while play_position in in_play:
                        y1 -= 60
                        play_position = x1,y1
                    unpress2 = 0
                    y2 = y1
                    pygame.draw.circle(ballsurface, (c1,c2,c3), (x1,y1),25)
                    screen.blit(ballsurface, (ballx, bally))
                    unpress = 0
                    in_play.append(play_position)
                    if c0 == 0:
                        c0 = 1
                        c1 = 255
                    elif c0 == 1:
                        c0 = 0
                        c1 = 0
                    win_position = x1,y1,c1,c2
                    chip.play()
                    wincheck.append(win_position)
                    
                    #print(wincheck)
                    pygame.draw.circle(ballsurface2, (c1,c2,c3), (x1,25),25)
                    screen.blit(ballsurface2, (ballx2, bally2))
                    #IF WIN
                    
                    if win_check(wincheck) == 1:
                        x = 35
                        y = 25
                        for i in range(7):
                            pygame.draw.circle(ballsurface2, (255,255,255), (x,y),25)
                            screen.blit(ballsurface2, (ballx2, bally2))
                            x += 60
                        if c1 == 0:
                            print('Red Wins')
                            def write(msg="Red Wins!"):
                                myfont = pygame.font.SysFont("None", 50)
                                mytext = myfont.render(msg, True, (255,0,0))
                                mytext = mytext.convert_alpha()
                                return mytext
                            textsurface = write("Red Wins!")
                            screen.blit(textsurface, (140,50))
                        elif c1 == 255:
                            print('Black Wins')
                            def write(msg="Black Wins!"):
                                myfont = pygame.font.SysFont("None", 50)
                                mytext = myfont.render(msg, True, (0,0,0))
                                mytext = mytext.convert_alpha()
                                return mytext
                            textsurface = write("Black Wins!")
                            oof.play()
                            screen.blit(textsurface, (125,50))
                        endgame = 1
                    y1 = 355
                    
        if not pressedkeys[pygame.K_DOWN]:
            unpress2 = 501
        
    print("this 'game' was played for %.2f seconds" % playtime)
    if endgame != 1:
        pygame.quit()
    else:
        mainloop = True
        while mainloop:
            milliseconds = clock.tick(FPS) # do not go faster than this frame rate
            playtime += milliseconds / 1000.0
            # ----- event handler -----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False # pygame window closed by user
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False # user pressed ESC
        pygame.quit()
    replay()
#game_choice = input('Which game would you like to play?\n1 - ConnectFour\nGAME> ')
#if game_choice == '1':
ConnectFour()
