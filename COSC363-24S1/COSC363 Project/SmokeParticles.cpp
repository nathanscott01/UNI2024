//  ========================================================================
//  COSC363 Computer Graphics (2024)
//  Smoke particle system
//  Please see Lab05.pdf for details
//  ========================================================================
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <list>
#include <GL/freeglut.h>
#include "loadBMP.h"
#include <climits>
using namespace std;

//====Globals====
GLUquadric *q;		//Quadric object (required for drawing a cylinder)
GLuint txId;		//Texture id
int tick = 0;		//Timer counter
float x_pos;
float z_pos;
float x_vel;
float z_vel;

struct particle		//A particle 
{
	int t;			//Life time  (0 - 200)
	float col;		//Color  (0 - 1)
	float size;		//Size   (5 - 25)
	float pos[3];	//Position
	float vel[3];	//Velocity
};

list<particle> parList;	//List of particles

void loadTexture()
{
	glGenTextures(1, &txId);
	glBindTexture(GL_TEXTURE_2D, txId);
	loadBMP("Glow.bmp");
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
	glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
}

//-------- Ground Plane ---------
void floor()
{
	glColor3ub(240, 134, 80);
	glNormal3f(0.0, 1.0, 0.0);
	glBegin(GL_QUADS);
		glVertex3i(-500, 0.0, -500);
		glVertex3i(-500, 0.0, 500);
		glVertex3f(500, 0.0, 500);
		glVertex3f(500, 0.0, -500);
	glEnd();
}

//------Draws a smokestack and a shed-----
void smokeStack()
{
	//Smoke stack
	glColor3f(0.7, 0.7, 0.7);
	glPushMatrix();
	   glTranslatef(0, 10, 0);
	   glRotatef(-90.0, 1., 0., 0.);
	   gluCylinder(q, 5, 4, 80, 20, 5);
	glPopMatrix();

	//Factory shed
	glColor3ub(235, 51, 36);
	glBegin(GL_QUAD_STRIP);
		glNormal3f(1, 0, 0);
		glVertex3f(50, 0, 40);
		glVertex3f(50, 0, -40);
		glVertex3f(50, 30, 40);
		glVertex3f(50, 30, -40);
		glNormal3f(-1, 1, 0);
		glVertex3f(7, 20, 40);
		glVertex3f(7, 20, -40);
		glNormal3f(-1, 0, 0);
		glVertex3f(7, 10, 40);
		glVertex3f(7, 10, -40);
		glNormal3f(0, 1, 0);
		glVertex3f(-7, 10, 40);
		glVertex3f(-7, 10, -40);
		glNormal3f(-1, 0, 0);
		glVertex3f(-7, 0, 40);
		glVertex3f(-7, 0, -40);
	glEnd();

	glBegin(GL_QUADS);
		glNormal3f(0, 0, 1);
		glVertex3f(50, 0, 40);
		glVertex3f(50, 30, 40);
		glVertex3f(7, 20, 40);
		glVertex3f(7, 0, 40);
		glVertex3f(7, 0, 40);
		glVertex3f(7, 10, 40);
		glVertex3f(-7, 10, 40);
		glVertex3f(-7, 0, 40);
	glEnd();
}

//------Draws a single particle as two texture mapped quads-----
void drawParticle(float col, float size, float px, float py, float pz)
{
	glEnable(GL_BLEND);
	glDisable(GL_DEPTH_TEST);
	glColor3f(col, col, col);
	glEnable(GL_TEXTURE_2D);
	glBindTexture(GL_TEXTURE_2D, txId);

	glPushMatrix();
		glTranslatef(px, py, pz);
		glScalef(size, size, size);

		glBegin(GL_QUADS);
		//A quad on the xy-plane
			glTexCoord2f(0, 0);
			glVertex3f(-0.5, -0.5, 0);
			glTexCoord2f(1, 0);
			glVertex3f(0.5, -0.5, 0);
			glTexCoord2f(1, 1);
			glVertex3f(0.5, 0.5, 0);
			glTexCoord2f(0, 1);
			glVertex3f(-0.5, 0.5, 0);

		//A quad on the yz-plane
			glTexCoord2f(0, 0);
			glVertex3f(0, -0.5, -0.5);
			glTexCoord2f(1, 0);
			glVertex3f(0, 0.5, -0.5);
			glTexCoord2f(1, 1);
			glVertex3f(0, 0.5, 0.5);
			glTexCoord2f(0, 1);
			glVertex3f(0, -0.5, 0.5);
		glEnd();
	glPopMatrix();

	glDisable(GL_BLEND);
	glDisable(GL_TEXTURE_2D);
	glEnable(GL_DEPTH_TEST);
}


//------Creates a new particle and initializes its data fields-----
void newParticle()
{
	particle p = { 0 };

    x_pos = 2 * rand() / (float)RAND_MAX - 1;
    z_pos = 2 * rand() / (float)RAND_MAX - 1;

	p.pos[0] = x_pos;
	p.pos[1] = 91.5;    //This point is at the top end of the smoke stack
	p.pos[2] = z_pos;

    x_vel = 0.3 * (2 * rand() / (float)RAND_MAX);
    z_vel = 0.3 * (2 * rand() / (float)RAND_MAX);

	p.vel[0] = x_vel;
	p.vel[1] = 0.3;
	p.vel[2] = z_vel;

	p.col = 1;
	p.size = 5;

	parList.push_back(p);
}


//-----Updates the particle queue-------
void updateQueue()
{
	const int LIFETIME = 200;
	list<particle>::iterator it;
	particle p;
	int tval;
	float delta;
    float wind_fac = 0.004;
	//Remove particles that have passed lifetime

	if (!parList.empty())
	{
		p = parList.front();
		if (p.t > LIFETIME) parList.pop_front();
	}

	for (it = parList.begin(); it != parList.end(); it++)
	{
		tval = it->t;
		it->t = tval + 1;
		delta = (float)tval / (float)LIFETIME;

		for (int i = 0; i < 3; i++)
        {
            if (i == 0)
                (it->pos[i]) += it->vel[i] + it->pos[1] * wind_fac;
            else
                (it->pos[i]) += it->vel[i];
        }

		it->size = delta * 20 + 5;	//(5 - 25)
		it->col = 1 - delta;		// (1 - 0)
	}

    if(tick % 2 == 0) newParticle();   //Create a new particle every sec.
}

//---------------------------------------------------------------------
void initialize(void) 
{
	loadTexture();
	q = gluNewQuadric();
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);

	glEnable(GL_COLOR_MATERIAL);
 	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
    gluQuadricDrawStyle(q, GLU_FILL);
	glClearColor (0.28, 0.48, 0.67, 1);  //Background colour
	glBlendFunc(GL_SRC_COLOR, GL_ONE_MINUS_SRC_COLOR);
//    glBlendFunc(GL_ONE, GL_ONE);
    glMatrixMode (GL_PROJECTION);
    glLoadIdentity ();
    gluPerspective(60., 1.0, 10.0, 1000.0);
}

//-------------------------------------------------------------------
void display(void)
{
   float lgt_pos[] = {-300, 500, 100, 1};
   float CDR = 3.14159265 / 180.0;

   glClear (GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();

   gluLookAt(-100, 60, 200, 0, 30, 0, 0, 1, 0);
   glLightfv(GL_LIGHT0, GL_POSITION, lgt_pos);

   floor();
   smokeStack();


   list<particle>::iterator it;
   for (it = parList.begin(); it != parList.end(); it++)
   {
	   drawParticle(it->col, it->size, it->pos[0], it->pos[1], it->pos[2]);
   }

   glutSwapBuffers(); 
}

//--------------------------------------------------------------------
void timer(int value)
{
		tick++;
		if (tick == INT_MAX) tick = 0;

		updateQueue();

		glutTimerFunc(50, timer, value);
		glutPostRedisplay();
}


//---------------------------------------------------------------------
int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE|GLUT_DEPTH);
   glutInitWindowSize (1000, 1000); 
   glutInitWindowPosition (10, 10);
   glutCreateWindow ("Smoke Particle System");
   initialize ();

   glutDisplayFunc(display);
   glutTimerFunc(50, timer, 0);
   glutMainLoop();
   return 0;
}
