//  ========================================================================
//  COSC363: Computer Graphics (2024);  University of Canterbury.
//
//  FILE NAME: ToyTrain.cpp
//  See Lab03.pdf for details
//  ========================================================================

#include <math.h>
#include <GL/freeglut.h>
#include "RailModels.h"


// Global Variables
int angle = 0;
int zoom = 280;
int pivot = -80;

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

    glEnable(GL_LIGHT1);

    //	Define light's diffuse, specular properties
    glLightfv(GL_LIGHT1, GL_DIFFUSE, white);    //Default, only for LIGHT0
    glLightfv(GL_LIGHT1, GL_SPECULAR, white);   //Default, only for LIGHT0

//  Convert GL_LIGHT1 to spotlight
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 30.0);
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 0);
 
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
   float spotPosn[] = {-10 , 14, 0, 1};
   float spotDir[] = {-1, -1, 0};


   glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();

   gluLookAt (pivot, 50, zoom, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);
   glLightfv(GL_LIGHT0, GL_POSITION, light);

   floor();                 //A tessellated floor plane
   tracks(120, 10);         //Circular tracks with mean radius 120 units, width 10 units

   glPushMatrix();
    glRotatef(angle, 0, 1, 0);
    glTranslatef(0, 1, -120);
    engine();                //Toy train locomotive
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, spotDir);
    glLightfv(GL_LIGHT1, GL_POSITION, spotPosn);
   glPopMatrix();

   for (int i = 1; i < 5; i++)
   {
       glPushMatrix();
        glRotatef(angle + -10.5 * i, 0, 1, 0);
        glTranslatef(0, 1, -120);
        wagon();                // Carriage
       glPopMatrix();
   }

   glutSwapBuffers();       //Double buffered animation
}

void myTimer(int value)
{
    angle++;
    if (angle == 360) angle = 0;
    glutPostRedisplay();
    glutTimerFunc(50, myTimer, 0);
}

void move_camera(int key, int x, int y)
{
    if ((key == GLUT_KEY_UP) && (zoom < 250)) zoom++;
    else if ((key == GLUT_KEY_DOWN) && (zoom > 100)) zoom--;
    else if ((key == GLUT_KEY_LEFT) && (pivot > -150)) pivot--;
    else if ((key == GLUT_KEY_RIGHT) && (pivot < 150)) pivot++;
    glutPostRedisplay();
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
   glutTimerFunc(50, myTimer, 0);
   glutSpecialFunc(move_camera);
   glutMainLoop();
   return 0;
}
