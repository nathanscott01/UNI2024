//  ========================================================================
//  COSC363: Computer Graphics (2024);  University of Canterbury.
//
//  FILE NAME: ToyTrain.cpp
//  See Lab03.pdf for details
//  ========================================================================

#include <math.h>
#include <GL/freeglut.h>
#include "RailModels.h"

//---------------------------------------------------------------------
void initialize(void) 
{
    float white[4]  = {1.0, 1.0, 1.0, 1.0};

	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);

    glMaterialfv(GL_FRONT, GL_SPECULAR, white);
    glMaterialf(GL_FRONT, GL_SHININESS, 50);

//	Define light's diffuse, specular properties
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white);    //Default, only for LIGHT0
    glLightfv(GL_LIGHT0, GL_SPECULAR, white);   //Default, only for LIGHT0
 
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
	glClearColor (0, 0, 0, 1);

    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    gluPerspective(60., 1.0, 10.0, 1000.0);
}

//-------------------------------------------------------------------
void display(void)
{
   float light[] = {0.0f, 50.0f, 0.0f, 1.0f};  //Light's position (directly above the origin)

   glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();

   gluLookAt (-80, 50, 180, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
   glLightfv(GL_LIGHT0, GL_POSITION, light);

   floor();                 //A tessellated floor plane
   tracks(120, 10);         //Circular tracks with mean radius 120 units, width 10 units
   engine();                //Toy train locomotive

   glutSwapBuffers();       //Double buffered animation
}


//---------------------------------------------------------------------
int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_DEPTH);
   glutInitWindowSize (800, 800); 
   glutInitWindowPosition (5, 5);
   glutCreateWindow ("Toy Train");
   initialize ();

   glutDisplayFunc(display); 
   glutMainLoop();
   return 0;
}
