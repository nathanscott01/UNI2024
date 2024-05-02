//  ========================================================================
//  COSC363: Computer Graphics (2024);  University of Canterbury.
//
//  FILE NAME: Shadow.cpp
//  See Lab06.pdf for details.
//  ========================================================================
 
#include <iostream>
#include <cmath> 
#include <GL/freeglut.h>
#include "loadTGA.h"
using namespace std;

float angle = 0.0;  //Rotation angle
GLuint texId;

//-------------------Load glass texture---------------------------------
void loadTexture()
{
	glGenTextures(1, &texId);

	glBindTexture(GL_TEXTURE_2D, texId);
	loadTGA("II_Shadow/glass_texture.tga");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);	
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
}

//-------------------Initialization-------------------------------------
void initialise()
{ 
	loadTexture();
	glClearColor(1., 1., 1., 1.);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	glEnable(GL_COLOR_MATERIAL);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);

	glMatrixMode(GL_PROJECTION);						
	glLoadIdentity();
	gluPerspective(60., 1., 1., 100.);
}

//-------------------Floor Plane------------------------------------
void floor()
{
	float floor_height = -0.1;

	glColor3f(0, 0.5, 1.0);
	glNormal3f(0, 1, 0);

	//Tiles
	glBegin(GL_QUADS);
		glVertex3f(-6, floor_height, 5);
		glVertex3f(-1, floor_height, 5);
		glVertex3f(-1, floor_height, -5);
		glVertex3f(-6, floor_height, -5);
		glVertex3f(1, floor_height, 5);
		glVertex3f(6, floor_height, 5);
		glVertex3f(6, floor_height, -5);
		glVertex3f(1, floor_height, -5);
		glVertex3f(-6, floor_height, 6);
		glVertex3f(6, floor_height, 6);
		glVertex3f(6, floor_height, 5);
		glVertex3f(-6, floor_height, 5);
		glVertex3f(-6, floor_height, -5);
		glVertex3f(6, floor_height, -5);
		glVertex3f(6, floor_height, -6);
		glVertex3f(-6, floor_height, -6);
	glEnd();

	//Glass
	glColor4f(1.0, 1.0, 1.0, 0.3);   //The fourth component is the opacity term
	glEnable(GL_TEXTURE_2D);
	glEnable(GL_BLEND);
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	glBindTexture(GL_TEXTURE_2D, texId);
	glBegin(GL_QUADS);
		glTexCoord2f(0, 0);  glVertex3f(-1, floor_height, 5);
		glTexCoord2f(1, 0);  glVertex3f(1, floor_height, 5);
		glTexCoord2f(1, 1);  glVertex3f(1, floor_height, -5);
		glTexCoord2f(0, 1);  glVertex3f(-1, floor_height, -5);
	glEnd();
	glDisable(GL_TEXTURE_2D);
}


//----------------Display Callback-----------------------------------
void display() 
{
	float light[] = {80, 80, 0, 1};
    float shadowMat[16] = {light[1], 0, 0, 0, -light[0], 0, -light[2], -1,
        0, 0, light[1], 0, 0, 0, 0, light[1]};

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);	

	glMatrixMode(GL_MODELVIEW);								
	glLoadIdentity();
	gluLookAt(0, 5, 10, 0, 0, 0,  0, 1, 0);
	glLightfv(GL_LIGHT0, GL_POSITION, light);

//  Draw Object
	glEnable(GL_LIGHTING);
	glColor3f(1, 0, 1);
	glPushMatrix();
	  glTranslatef(0, 3, 0);
	  glRotatef(angle, 1, 0, 0);
	  glRotatef(angle*2, 0, 1, 0);
	  glColor3f(1, 0, 1);
	  glutSolidTeapot(1);
	glPopMatrix();

// Draw the shadow and the reflection of the teapot here...
    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(0, 3, 0);
        glRotatef(angle, 1, 0, 0);
        glRotatef(angle*2, 0, 1, 0);
        glutSolidTeapot(1);
    glPopMatrix();

    // Invert light's position before drawing reflection
    light[1] = -light[1];
    glLightfv(GL_LIGHT0, GL_POSITION, light); //new position

    //  Draw Object Reflection
	glEnable(GL_LIGHTING);
	glColor3f(1, 0, 1);
	glPushMatrix();
        glScalef(1, -1, 1);
        glTranslatef(0, 3, 0);
        glRotatef(angle, 1, 0, 0);
        glRotatef(angle*2, 0, 1, 0);
        glColor3f(1, 0, 1);
        glutSolidTeapot(1);
	glPopMatrix();

    // Fix light's position before drawing floor
    light[1] = -light[1];
    glLightfv(GL_LIGHT0, GL_POSITION, light); //new position

//  Draw floor
	floor();

	glutSwapBuffers();									
}

//------------------------Timer Callback--------------------------------
void timer(int value)
{
	angle += 0.5;
	if(angle > 360) angle = 0;
	glutPostRedisplay();
	glutTimerFunc(50, timer, 0);
}

//--------------------------Main-----------------------------------------
int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_DEPTH);
   glutInitWindowSize (500, 500); 
   glutInitWindowPosition (100, 100);
   glutCreateWindow ("Teapot's Shadow");
   initialise();

   glutDisplayFunc(display); 
   glutTimerFunc(50, timer, 0);
   glutMainLoop();
   return 0;
}
