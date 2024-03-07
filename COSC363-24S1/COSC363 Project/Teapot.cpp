//  ========================================================================
//  COSC363: Computer Graphics (2023);  University of Canterbury.
//
//  FILE NAME: Teapot.cpp
//  See Lab01.pdf for details
//  ========================================================================

#include <iostream>
#include <cmath>
#include <GL/freeglut.h>

//Global Variables
int cam_hgt = 10;
float theta = 0;
float rads = 0;

//--Draws a grid of lines on the floor plane -------------------------------
void drawFloor()
{
	glColor3f(0., 0.5,  0.);			//Floor colour

	for(int i = -50; i <= 50; i ++)
	{
		glBegin(GL_LINES);			//A set of grid lines on the xz-plane
			glVertex3f(-50, -0.75, i);
			glVertex3f(50, -0.75, i);
			glVertex3f(i, -0.75, -50);
			glVertex3f(i, -0.75, 50);
		glEnd();
	}
}

//--Display: ---------------------------------------------------------------
//--This is the main display module containing function calls for generating
//--the scene.
void display(void) 
{ 
	float lpos[4] = {0., 10., 10., 1.0};  //light's position

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

    gluLookAt(12 * sin(rads), cam_hgt, 12 * cos(rads), 0, 0, 0, 0, 1, 0);  //Camera position and orientation

	glLightfv(GL_LIGHT0,GL_POSITION, lpos);   //Set light position

	glDisable(GL_LIGHTING);			//Disable lighting when drawing floor.
    drawFloor();

	glEnable(GL_LIGHTING);			//Enable lighting when drawing the teapot
    glColor3f(0.0, 1.0, 1.0);
//    glRotatef(60, 1, 0, 0);
    glutSolidTeapot(1.0);

	glFlush(); 
} 

//----------------------------------------------------------------------
void initialize(void)
{
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);

	glEnable(GL_LIGHTING);		//Enable OpenGL states
	glEnable(GL_LIGHT0);
 	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(30, 1, 10.0, 1000.0);   //Camera Frustum
}

void move_camera(int key, int x, int y)
{
    if ((key == GLUT_KEY_UP) && (cam_hgt < 20)) cam_hgt++;
    else if ((key == GLUT_KEY_DOWN) && (cam_hgt > 2)) cam_hgt--;
    glutPostRedisplay();
}

void my_timer(int value)
{
    theta++;
    rads = theta * M_PI / 180;
    glutPostRedisplay();
    glutTimerFunc(50, my_timer, 0);
}

//  ------- Main: Initialize glut window and register call backs ------
int main(int argc, char **argv) 
{
	glutInit(&argc, argv);            
	glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH);  
	glutInitWindowSize(600, 600);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Teapot");
	initialize();
	glutDisplayFunc(display);
    glutTimerFunc(50, my_timer, 0);
    glutSpecialFunc(move_camera);
	glutMainLoop();
	return 0; 
}

