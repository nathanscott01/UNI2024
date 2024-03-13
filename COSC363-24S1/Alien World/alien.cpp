//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: alien.cpp
//
//  COMMENTS: Set this up so that the drawAlien() function can be accessed from another file.
//	      Add an angle parameter that is pre-defined to 0 degrees so that function is 
//	      drawAlien(angle=0) so that if needed, an animation can be added for movement of
//	      arms and legs.
//
//  ========================================================================

#include <iostream>
#include <GL/freeglut.h>
#include <cmath>


//Global Variables
int cam_hgt = 10;
float angle = 0;


void drawFloor()
{
    glColor3f(0.8, 0.5, 0.);

    for (int i = -500; i <= 500; i++)
    {
        glBegin(GL_LINES);
            glVertex3f(-50, 0, i);
			glVertex3f(50, 0, i);
			glVertex3f(i, 0, -50);
			glVertex3f(i, 0, 50);
        glEnd();
    }
}

void drawLegs()
{
    glColor3f(.5, .2, .5);

    // Draw right leg
    glPushMatrix();
        glTranslatef(-4.5, 4, 0);
        glScalef(1, 8, 1);
        glutSolidCube(1);
    glPopMatrix();

    // Draw right hip
    GLUquadric *rhip;
    rhip = gluNewQuadric();
    gluQuadricDrawStyle(rhip, GLU_FILL);
    glPushMatrix();
        glTranslatef(-2, 7, 0);
        glRotatef(-90, 0, 1, 0);
        gluCylinder(rhip, 1.5, 0.5, 2, 36, 18);
    glPopMatrix();

    // Draw left leg
    glPushMatrix();
        glTranslatef(4.5, 4, 0);
        glScalef(1, 8, 1);
        glutSolidCube(1);
    glPopMatrix();

    // Draw left hip
    GLUquadric *lhip;
    lhip = gluNewQuadric();
    gluQuadricDrawStyle(lhip, GLU_FILL);
    glPushMatrix();
        glTranslatef(2, 7, 0);
        glRotatef(90, 0, 1, 0);
        gluCylinder(lhip, 1.5, 0.5, 2, 36, 18);
    glPopMatrix();
}

void drawBody()
{
    glColor3f(1., 0.78, 0.06);

    glPushMatrix();
    glTranslatef(0, 10, 0);
    glScalef(2.5, 5, 2.5);
    glutSolidSphere(1, 36, 36);
    glPopMatrix();
}


void drawArms()
{
    glColor3f(.5, .2, .5);

    // Right Shoulder
    glPushMatrix();
        glTranslatef(-2, 13, 0);
        glutSolidSphere(0.75, 36, 36);
    glPopMatrix();

    // Right Arm
    glPushMatrix();
        glTranslatef(-3, 12, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();

    // Define the offsets for each ball for hand relative to the center point
    float offsets[4][2] = {{-0.7, 0}, {0.7, 0}, {0, 0.7}, {0, -0.7}};

    // Right Hand
    // Draw four balls symmetrically around the center point
    for (int i = 0; i < 4; ++i) {
        glPushMatrix();
            glTranslatef(-3 + offsets[i][0], 10, offsets[i][1]); // Apply the offset
            glutSolidSphere(0.5, 36, 36);
        glPopMatrix();
    }

    // Left Shoulder
    glPushMatrix();
        glTranslatef(2, 13, 0);
        glutSolidSphere(0.75, 36, 36);
    glPopMatrix();

    // Left Arm
    glPushMatrix();
        glTranslatef(3, 12, 0);
        glScalef(1, 4, 1);
        glutSolidCube(1);
    glPopMatrix();

    // Left Hand
    // Draw four balls symmetrically around the center point
    for (int i = 0; i < 4; ++i) {
        glPushMatrix();
            glTranslatef(3 + offsets[i][0], 10, offsets[i][1]); // Apply the offset
            glutSolidSphere(0.5, 36, 36);
        glPopMatrix();
    }
}


void drawHead()
{
    // Draw head
    glPushMatrix();
        glTranslatef(0, 20, 0);
        glScalef(3, 5, 3);
        glutSolidSphere(1, 36, 36);
    glPopMatrix();

    // Draw Left Antenna
    glColor3f(0, 0.66, 0.34);

    glPushMatrix();
    glTranslatef(-2.5, 25, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3, 26, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3.5, 27, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3.5, 28, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-4, 28, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-4.5, 27, 0);
    glutSolidSphere(0.25, 36, 36);
    glPopMatrix();
}


void drawAlien()
{
    drawLegs();
    drawBody();
    drawArms();
    drawHead();
}


void display()
{
    float light_position[4] = {100., 100., 100., 1.0};

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0, cam_hgt, 12, 0, 0, 0, 0, 1, 0);    // Camera Position
    glLightfv(GL_LIGHT0, GL_POSITION, light_position);                          // Set position of the light

    glRotatef(angle, 0, 1, 0);

    glDisable(GL_LIGHTING);                                                                    // Disable lighting when drawing floor
    drawFloor();

    drawAlien();

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glColor3f(0.0, 0.5, 1.0);
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
    gluPerspective(60, 1, 10, 100);
}


void move_camera(int key, int x, int y)
{
    if ((key == GLUT_KEY_UP) && (cam_hgt < 200)) cam_hgt++;
    else if ((key == GLUT_KEY_DOWN) && (cam_hgt > 2)) cam_hgt--;
    else if (key == GLUT_KEY_LEFT) angle--;
    else if (key == GLUT_KEY_RIGHT) angle++;
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
