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


void drawLegs(float theta_r)
{
    glColor3f(.5, .2, .5);

    // Draw right leg
    glPushMatrix();
        glTranslatef(-4.5, 4, 0);
        glRotatef(-theta_r, 1, 0, 0);
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
        glRotatef(theta_r, 1, 0, 0);
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


void drawArms(float theta_r)
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
        glRotatef(theta_r, 1, 0, 0);
        glScalef(1, 6, 1);
        glutSolidCube(1);
    glPopMatrix();

    // Left Shoulder
    glPushMatrix();
        glTranslatef(2, 13, 0);
        glutSolidSphere(0.75, 36, 36);
    glPopMatrix();

    // Left Arm
    glPushMatrix();
        glTranslatef(3, 12, 0);
        glRotatef(-theta_r, 1, 0, 0);
        glScalef(1, 6, 1);
        glutSolidCube(1);
    glPopMatrix();

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
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3, 26, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3.5, 27, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-3.5, 28, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-4, 28, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(-4.5, 27, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    // Draw Right Antenna
    glColor3f(0, 0.66, 0.34);

    glPushMatrix();
    glTranslatef(2.5, 25, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(3, 26, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(3.5, 27, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(3.5, 28, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(4, 28, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(4.5, 27, 0);
    glutSolidSphere(0.5, 36, 36);
    glPopMatrix();
}


void drawAlien(float theta_r)
{
    drawLegs(theta_r);
    drawBody();
    drawArms(theta_r);
    drawHead();
}