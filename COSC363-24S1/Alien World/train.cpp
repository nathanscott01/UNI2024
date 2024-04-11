//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: train.cpp
//
//  COMMENTS:
//
//  ========================================================================

#include <GL/freeglut.h>
#include <cmath>

// ---- Function to compute normal vectors at vertices of a polygonal line ----
void normal(int i)
{
	float xdiff1, zdiff1, xdiff2, zdiff2;
	if (i == 0 || i == 12) glNormal3f(-1, 0, 0);   //default normal along -x direction
	else
	{
		xdiff1 = 1;
		zdiff1 = 0.025 * pow(i, 2) - 0.025 * pow(i - 1, 2);
		xdiff2 = 1;
		zdiff2 = 0.025 * pow(i + 1, 2) - 0.025 * pow(i, 2);
		glNormal3f(-(zdiff1 + zdiff2), 0, (xdiff1 + xdiff2));
	}
}

void drawParabolaRailwayTrack()
{
    glColor4f(0.0, 0.0, 0.3, 1.0);
    glLineWidth(1.0);
    glBegin(GL_QUADS);
    float x1, x2, z1, z2;
    for (int i = -100; i < 100; i++) {
        x1 = i;
        z1 = 0.025 * pow(x1, 2);
        x2 = x1 + 1;
        z2 = 0.025 * pow(x2, 2);

        normal(i);
        glVertex3f(x1, 0, z1); // Bottom-left vertex
        glVertex3f(x2, 0, z2); // Bottom-right vertex
        glVertex3f(x2, 1, z2); // Top-right vertex
        glVertex3f(x1, 1, z1); // Top-left vertex
    }
    glEnd();
}


void drawRailwayTrack()
{
    float distance = -5.1;
    glColor4f(0.0, 0.0, 0.3, 1.0);
    glBegin(GL_QUADS);
    for (int j = 0; j < 2; j++)
    {
        for (int i = -200; i < 485; i++)
		{

			glNormal3f(0., 1., 0.);       //Quad 1 facing up
			glVertex3f(i, 1.0, distance - 0.5);
			glVertex3f(i, 1.0, distance + 0.5);
			glVertex3f(i + 1, 1.0, distance + 0.5);
			glVertex3f(i + 1, 1.0, distance - 0.5);

			glNormal3f(0.0, 0.0, 1.0);   //Quad 2 facing inward
			glVertex3f(i, 1.0, distance + 0.5);
			glVertex3f(i, 0.0, distance + 0.5);
			glNormal3f(0.0, 0.0, 1.0);
			glVertex3f(i + 1, 0.0, distance + 0.5);
			glVertex3f(i + 1, 1.0, distance + 0.5);

			glNormal3f(0.0, 0.0, -1.0);   //Quad 3 facing outward
			glVertex3f(i, 1.0, distance - 0.5);
			glVertex3f(i, 0.0, distance - 0.5);
			glNormal3f(0.0, 0.0, -1.0);
			glVertex3f(i + 1, 0.0, distance - 0.5);
			glVertex3f(i + 1, 1.0, distance - 0.5);
		}
        distance += 10.2;
    }
    glEnd();
}



//--------------- MODEL BASE --------------------------------------
// This is a common base for the locomotive and wagons
// The base is of rectangular shape (20 length x 10 width x 2 height)
// and has wheels and connectors attached.
//-----------------------------------------------------------------
void base()
{
    glColor4f(0.2, 0.2, 0.2, 1.0);   //Base color
    glPushMatrix();
      glTranslatef(0.0, 4.0, 0.0);
      glScalef(20.0, 2.0, 10.0);     //Size 20x10 units, thickness 2 units.
      glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();					//Connector between wagons
      glTranslatef(11.0, 4.0, 0.0);
      glutSolidCube(2.0);
    glPopMatrix();

    //4 Wheels (radius = 2 units)
	//x, z positions of wheels:
//	float wx[4] = {  -8,   8,   -8,    8 };
//	float wz[4] = { 5.1, 5.1, -5.1, -5.1 };
	float wx[2] = {  -8,   8};
	float wz[2] = { 0, 0};
    glColor4f(0.5, 0., 0., 1.0);    //Wheel color
	GLUquadric *q = gluNewQuadric();   //Disc

	for (int i = 0; i < 2; i++)
	{
		glPushMatrix();
		glTranslatef(wx[i], 2.0, wz[i]);
		gluDisk(q, 0.0, 2.0, 20, 2);
		glPopMatrix();
	}
}


//--------------- LOCOMOTIVE --------------------------------
// This simple model of a locomotive consists of the base,
// cabin and boiler
//-----------------------------------------------------------
void engine()
{
    base();

    //Cab
    glColor4f(0.8, 0.8, 0.0, 1.0);
    glPushMatrix();
      glTranslatef(7.0, 8.5, 0.0);
      glScalef(6.0, 7.0, 10.0);
      glutSolidCube(1.0);
    glPopMatrix();

    glPushMatrix();
      glTranslatef(6.0, 14.0, 0.0);
      glScalef(4.0, 4.0, 8.0);
      glutSolidCube(1.0);
    glPopMatrix();

    //Boiler
	GLUquadric *q = gluNewQuadric();   //Cylinder
    glPushMatrix();
      glColor4f(0.5, 0., 0., 1.0);
      glTranslatef(4.0, 10.0, 0.0);
      glRotatef(-90.0, 0., 1., 0.);
      gluCylinder(q, 5.0, 5.0, 14.0, 20, 5);
      glTranslatef(0.0, 0.0, 14.0);
      gluDisk(q, 0.0, 5.0, 20, 3);
      glColor4f(1.0, 1.0, 0.0, 1.0);
      glTranslatef(0.0, 4.0, 0.2);
      gluDisk(q, 0.0, 1.0, 20,2);  //headlight!
    glPopMatrix();

}


//--------------- WAGON ----------------------------------
// This simple model of a rail wagon consists of the base,
// and a cube(!)
//--------------------------------------------------------
void wagon()
{
    base();

    // Set material properties
    GLfloat mat_ambient[] = {0.2, 0.2, 0.2, 1.0}; // Ambient reflection
    GLfloat mat_diffuse[] = {0.2, 0.2, 0.2, 1.0}; // Diffuse reflection
    GLfloat mat_specular[] = {0.0, 0.0, 0.0, 1.0}; // Specular reflection
    GLfloat mat_shininess[] = {0.0}; // Shininess factor (no shininess)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);

    glEnable(GL_LIGHTING);

    glColor4f(0.0, 0.3, 1.0, 1.0);
    glPushMatrix();
      glTranslatef(0.0, 10.0, 0.0);
      glScalef(18.0, 10.0, 10.0);
      glutSolidCube(1.0);
    glPopMatrix();

    glDisable(GL_LIGHTING);
}


void drawTunnel()
{
    // Set material properties
    GLfloat mat_ambient[] = {0.1, 0.1, 0.1, 1.0}; // Ambient reflection
    GLfloat mat_diffuse[] = {0.8, 0.8, 0.8, 1.0}; // Diffuse reflection
    GLfloat mat_specular[] = {1.0, 1.0, 1.0, 1.0}; // Specular reflection
    GLfloat mat_shininess[] = {100.0}; // Shininess factor

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);

//    glEnable(GL_LIGHTING);
    // Roof
    glPushMatrix();
        glTranslatef(0, 22, 0);
        glScalef(50, 3, 12);
        glutSolidCube(2);
    glPopMatrix();

    // Left Side
    glPushMatrix();
        glTranslatef(0, 10, 12);
        glScalef(50, 15, 2);
        glutSolidCube(2);
    glPopMatrix();

    // Right Side
    glPushMatrix();
        glTranslatef(0, 10, -12);
        glScalef(50, 15, 2);
        glutSolidCube(2);
    glPopMatrix();
//    glDisable(GL_LIGHTING);
}


void drawTrainStation(float trainPosx, float trainPosz, float trainAngle, float wagonPosx, float wagonPosz, float wagonAngle, float shadowMat[16])
{
//    glPushMatrix();
//        drawRailwayTrack();
//    glPopMatrix();

    glPushMatrix();
        drawParabolaRailwayTrack();
    glPopMatrix();

    glPushMatrix();
        glTranslatef(trainPosx, 0, trainPosz);
        glRotatef(trainAngle + 180, 0, 1, 0);
        engine();
    glPopMatrix();

    glPushMatrix();
        glTranslatef(wagonPosx, 0, wagonPosz);
        glRotatef(wagonAngle + 180, 0, 1, 0);
        wagon();
    glPopMatrix();

    // Draw Tunnel 1
    glEnable(GL_LIGHTING);
    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
        glTranslatef(-100, 0, 250);
        glRotatef(77, 0, 1, 0);
        drawTunnel();
    glPopMatrix();

    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(-100, 0, 250);
        glRotatef(77, 0, 1, 0);
        glScalef(1, 0.2, 1);
        drawTunnel();
    glPopMatrix();

    // Draw Tunnel 2
    glEnable(GL_LIGHTING);
    glColor3f(0.0, 0.0, 0.0);
    glPushMatrix();
        glTranslatef(100, 0, 250);
        glRotatef(103, 0, 1, 0);
        drawTunnel();
    glPopMatrix();

    glDisable(GL_LIGHTING);
    glColor3f(0.2, 0.2, 0.2);
    glPushMatrix();
        glMultMatrixf(shadowMat);
        glTranslatef(100, 0, 250);
        glRotatef(103, 0, 1, 0);
        glScalef(1, 0.2, 1);
        drawTunnel();
    glPopMatrix();
}

