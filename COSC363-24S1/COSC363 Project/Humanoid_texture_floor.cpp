//  ========================================================================
//  COSC363: Computer Graphics (2023);  University of Canterbury.
//
//  FILE NAME: Humanoid.cpp
//  See Lab02.pdf for details
//  ========================================================================
 
#include <iostream>
#include <fstream>
#include <GL/freeglut.h>
#include "I_Walls/loadTGA.h"
using namespace std;



//--Globals ---------------------------------------------------------------
int cam_hgt = 4; //Camera height
GLuint txId[1];   //Texture ids
float angle = 10.0;  //Rotation angle for viewing
float theta = 20;
float theta_delta = 1;
float lpos[4] = {10., 10., 10., 1.0};  //light's position
float shadowMat[16] = {lpos[1], 0, 0, 0, -lpos[0],0,
                       -lpos[2], -1, 0, 0, lpos[1], 0,
                       0, 0, 0, lpos[1]};


//---- Function to load textures ----
void loadTexture()
{
	glGenTextures(1, txId); 	// Create 4 texture ids

	glBindTexture(GL_TEXTURE_2D, txId[0]);
    loadTGA("I_Walls/Floor_Texture.tga");
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);

	glTexEnvi(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE);
}

//--Draws a grid of lines on the floor plane -------------------------------
void drawFloor()
{
	glBindTexture(GL_TEXTURE_2D,  txId[0]);
	glColor3f(1, 1, 1);
	glNormal3f(0, 1, 0);
	glBegin(GL_QUADS);				//A single quad
	    glTexCoord2f(0, 0);
		glVertex3f(-16, -0.1, 16);
		glTexCoord2f(1, 0);
		glVertex3f(16, -0.1, 16);
		glTexCoord2f(1, 1);
		glVertex3f(16, -0.1, -16);
		glTexCoord2f(0, 1);
		glVertex3f(-16, -0.1, -16);
	glEnd();
}



//--Draws a character model constructed using GLUT objects ------------------
void drawModel()
{
	glColor3f(1., 0.78, 0.06);		//Head
	glPushMatrix();
        glTranslatef(0, 7.7, 0);
        glutSolidCube(1.4);
	glPopMatrix();

    // Draw Shadow Head
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(0, 7.7, 0);
        glutSolidCube(1.4);
    glPopMatrix();

	glColor3f(1., 0., 0.);			//Torso
	glPushMatrix();
        glTranslatef(0, 5.5, 0);
        glScalef(3, 3, 1.4);
        glutSolidCube(1);
	glPopMatrix();

    // Draw Shadow Torso
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(0, 5.5, 0);
        glScalef(3, 3, 1.4);
        glutSolidCube(1);
    glPopMatrix();

	glColor3f(0., 0., 1.);			//Right leg
	glPushMatrix();
        glTranslatef(-0.8, 4, 0);
        glRotatef(-theta, 1, 0, 0);
        glTranslatef(0.8, -4, 0);
        glTranslatef(-0.8, 2.2, 0);
        glScalef(1, 4.4, 1);
        glutSolidCube(1);
	glPopMatrix();

    // Draw shadow Right Leg
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(-0.8, 4, 0);
        glRotatef(theta, 1, 0, 0);
        glTranslatef(0.8, -4, 0);
        glTranslatef(-0.8, 2.2, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();


	glColor3f(0., 0., 1.);			//Left leg
	glPushMatrix();
        glTranslatef(0.8, 4, 0);
        glRotatef(theta, 1, 0, 0);
        glTranslatef(-0.8, -4, 0);
        glTranslatef(0.8, 2.2, 0);
        glScalef(1, 4.4, 1);
        glutSolidCube(1);
	glPopMatrix();

    // Draw shadow Left Leg
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(0.8, 4, 0);
        glRotatef(theta, 1, 0, 0);
        glTranslatef(-0.8, -4, 0);
        glTranslatef(0.8, 2.2, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();


	glColor3f(0., 0., 1.);			//Right arm
	glPushMatrix();
        glTranslatef(-2, 6.5, 0);
        glRotatef(theta, 1, 0, 0);
        glTranslatef(2, -6.5, 0);
        glTranslatef(-2, 5, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
	glPopMatrix();

    // Draw shadow Right Arm
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(-2, 6.5, 0);
        glRotatef(theta, 1, 0, 0);
        glTranslatef(2, -6.5, 0);
        glTranslatef(-2, 5, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();


	glColor3f(0., 0., 1.);			//Left arm
	glPushMatrix();
        glTranslatef(2, 6.5, 0);
        glRotatef(-theta, 1, 0, 0);
        glTranslatef(-2, -6.5, 0);
        glTranslatef(2, 5, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
	glPopMatrix();

    // Draw shadow Left Arm
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(2, 6.5, 0);
        glRotatef(-theta, 1, 0, 0);
        glTranslatef(-2, -6.5, 0);
        glTranslatef(2, 5, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();

}


//--Display: ---------------------------------------------------------------
//--This is the main display module containing function calls for generating
//--the scene.
void display()  
{
	float lpos[4] = {10., 10., 10., 1.0};  //light's position

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT); 
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(0, cam_hgt, 10, 0, 4, 0, 0, 1, 0);
	glLightfv(GL_LIGHT0,GL_POSITION, lpos);   //Set light position

    glRotatef(angle, 0.0, 1.0, 0.0);  //Rotate the scene about the y-axis

	glDisable(GL_LIGHTING);			//Disable lighting when drawing floor.
    drawFloor();

	glEnable(GL_LIGHTING);	       //Enable lighting when drawing the model
	drawModel();

	glFlush();
}

//------- Initialize OpenGL parameters -----------------------------------
void initialize()
{

    glEnable(GL_TEXTURE_2D);
    glEnable(GL_ALPHA_TEST);
    glAlphaFunc(GL_GREATER, 0);
	loadTexture();

	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);	//Background colour

	glEnable(GL_LIGHTING);					//Enable OpenGL states
	glEnable(GL_LIGHT0);
 	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
 
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 1000.0);   //Camera Frustum
}

//------------ Special key event callback ---------------------------------
// To enable the use of left and right arrow keys to rotate the scene
void special(int key, int x, int y)
{
    if(key == GLUT_KEY_LEFT) angle--;
    else if(key == GLUT_KEY_RIGHT) angle++;
    glutPostRedisplay();
}

void theta_limit()
{
    if ((theta > 20) || (theta < -20)) theta_delta = theta_delta * -1;
}

void myTimer(int value)
{
    theta = theta + theta_delta;
    theta_limit();
    glutPostRedisplay();
    glutTimerFunc(50, myTimer, 0);
}

//  ------- Main: Initialize glut window and register call backs -----------
int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_SINGLE | GLUT_DEPTH);
   glutInitWindowSize (600, 600); 
   glutInitWindowPosition (10, 10);
   glutCreateWindow ("Humanoid");
   initialize();

   glutDisplayFunc(display);
   glutTimerFunc(50, myTimer, 0);
   glutSpecialFunc(special); 
   glutMainLoop();
   return 0;
}
