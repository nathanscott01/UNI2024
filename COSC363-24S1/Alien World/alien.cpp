//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: alien.cpp
//  ========================================================================

#include <iostream>
#include <GL/freeglut.h>
#include <cmath>


//Global Variables
int cam_hgt = 10;
float theta = 0;
float rads = 0;


void drawFloor()
{
    glColor3f(0.8, 0.5, 0.);

    for (int i = -50; i <= 50; i++)
    {
        glBegin(GL_LINES);
            glVertex3f(-50, -0.75, i);
			glVertex3f(50, -0.75, i);
			glVertex3f(i, -0.75, -50);
			glVertex3f(i, -0.75, 50);
        glEnd();
    }
}

void display()
{
    float light_position[4] = {0., 10., 10., 1.0};

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    gluLookAt(12 * sin(rads), cam_hgt, 12 * cos(rads), 0, 0, 0, 0, 1, 0);    // Camera Position
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);                          // Set position of the light

    glDisable(GL_LIGHTING);                                                                    // Disable lighting when drawing floor
    drawFloor();

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glColor3f(0.0, 0.5, 1.0);
    glutSolidSphere(1);
    glFlush();
}


void initialise()
{
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(30, 1, 10, 1000);
}


void move_camera(int key, int x, int y)
{
    if ((key == GLUT_KEY_UP) && (cam_hgt < 20)) cam_hgt++;
    else if ((key == GLUT_KEY_DOWN) && (cam_hgt > 2)) cam_hgt--;
    else if (key == GLUT_KEY_LEFT)
    {
        theta--;
        rads = theta * M_PI / 180;
    }
    else if (key == GLUT_KEY_RIGHT)
    {
        theta++;
        rads = theta * M_PI / 180;
    }
    glutPostRedisplay();
}


// ------- Initialise main window -------
int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Alien");
    initialise();
    glutDisplayFunc(display);
    glutSpecialFunc(move_camera);
    glutMainLoop();
    return 0;
}
