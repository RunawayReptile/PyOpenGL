import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from objloader import *

def main():
    pygame.init()
    pygame.display.set_caption("Rendering Engine")
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|pygame.RESIZABLE)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    x = 0
    y = 0
    z = 0
    #MODEL-LOADING#
    glMatrixMode(GL_PROJECTION) # <---- specify projection matrix
    glMatrixMode(GL_MODELVIEW)
    model = OBJ("model.obj")
    #MODEL-LOADING#
    while True:
        #MOUSE#
        MX,MY = pygame.mouse.get_pos()
        pygame.mouse.set_pos(400,300)
        pygame.mouse.set_visible(False)
        if MX < 400:
            glRotatef(-.5, 0, 1, 0)
        if MX > 400:
            glRotatef(.5, 0, 1, 0)
        if MY < 300:
            glRotatef(-.5, 1, 0, 0)
        if MY > 300:
            glRotatef(.5, 1, 0, 0)
        #MOUSE#
        glTranslatef(x,y,z)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    z = 0.1
                if event.key == pygame.K_a:
                    x = 0.1
                if event.key == pygame.K_s:
                    z = -0.1
                if event.key == pygame.K_d:
                    x = -0.1
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    z = 0
                if event.key == pygame.K_a:
                    x = 0
                if event.key == pygame.K_s:
                    z = 0
                if event.key == pygame.K_d:
                    x = 0
                
        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #MODEL-LOADING#
        glPushMatrix()
        glTranslatef(0, 0, 0)
        model.render()
        glPopMatrix()
        #MODEL-LOADING#
        pygame.display.flip()
        pygame.time.wait(10)
        
#TKINTER#
from tkinter import *
root = Tk()
root.state("zoomed")
root.title("OpenGL")
def run():
    root.destroy()
    main()
def experimental():
    EFeatures.config(text="Experimental Features: Enabled")
EFeatures = Button(root, text="Experimental Features: Disabled", font=("Impact"),command=experimental)
Play = Button(root, text="Run", font=("Impact"),command=run)
Play.place(relx=0.5, rely=0.5, anchor=CENTER)
Version = Label(root, text="Version 1.0.0", font=("Impact"))
Label = Label(root, text="Rendering Engine", font=("Impact", 50))
Label.place(relx=0.5, rely=.1, anchor=N)
Version.place(relx=0.1, rely=0.1, anchor=SW)
EFeatures.place(relx=0.5, rely=.4, anchor=N)
root.mainloop()
#TKINTER#
