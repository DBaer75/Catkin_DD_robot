
import curses
import time as t
import rospy

try:
    #set up curses
    stdscr = curses.initscr() 
    curses.cbreak()
    curses.noecho()
    curses.halfdelay(6) #sets to trigger exception after no input for (TenthsSeconds)
    statusScr = curses.newwin(10,35,2,45)
    statusHeader = curses.newwin(1,35,0,45)
    statusHeader.clear()
    statusHeader.addstr(0,5,'CURRENT COMMAND')
    statusHeader.refresh()
    instructionsScr = curses.newwin(10,35,0,0)
    instructionsScr.clear()
    instructionsScr.addstr(0,10,'COMMANDS')
    instructionsScr.addstr(3,10,'SPACE = stop')
    instructionsScr.addstr(2,10,'w = forward')
    instructionsScr.addstr(3,0,'a = left')
    instructionsScr.addstr(3,25,'d = right')
    instructionsScr.addstr(4,10,'s = back')
    instructionsScr.addstr(6,10,'q = quit')
    instructionsScr.refresh()

    prevKey  = -1

    while True:
        try:
            currKey = statusScr.getch()
        except KeyboardInterrupt:
            break
        except:
            currKey = -1  
        if (currKey == ord('q')):
                break  # Exit the while loop
        if (prevKey != currKey):
            statusScr.clear()
            if (currKey == -1)|(currKey == 32): #spacebar or catch no input if exception
                statusScr.addstr(1,10,'stop')
            elif (currKey == ord('w')):
                #print('fwd')
                statusScr.addstr(0,10,'forward')
            elif (currKey == ord('a')):
                #print('lft')
                statusScr.addstr(1,0,'left')
            elif (currKey == ord('s')):
                #print('bwd')
                statusScr.addstr(2,10,'back')
            elif (currKey == ord('d')):
                #print('rtt')
                statusScr.addstr(1,25,'right')
            statusScr.refresh()
            prevKey = currKey    
                 
finally:
    #shut down curses
    curses.nocbreak()
    curses.echo()
    curses.endwin()

