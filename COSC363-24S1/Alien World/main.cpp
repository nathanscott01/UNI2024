//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: main.cpp
//
//  COMMENTS:
//
//  ========================================================================

#include <iostream>
#include <GL/freeglut.h>
#include <cmath>
#include "loadTGA.h"
#include "alien.h"
#include "skybox.h"
#include "floor.h"
#include "spaceship.h"
using namespace std;

#define GL_CLAMP_TO_EDGE 0x812F

//Global Variables
GLuint txId[8];     //Texture ID's
float angle = 0;
float rads;
float look_x, look_z = -1., eye_x, eye_z;

void loadGLTextures()
{
    glGenTextures(8, txId);

    //Load Left
    glBindTexture(GL_TEXTURE_2D, txId[0]);
    loadTGA("Space Skybox/stormydays_lf.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Front
    glBindTexture(GL_TEXTURE_2D, txId[1]);
    loadTGA("Space Skybox/stormydays_bk.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Right
    glBindTexture(GL_TEXTURE_2D, txId[2]);
    loadTGA("Space Skybox/stormydays_rt.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Back
    glBindTexture(GL_TEXTURE_2D, txId[3]);
    loadTGA("Space Skybox/stormydays_ft.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Up
    glBindTexture(GL_TEXTURE_2D, txId[4]);
    loadTGA("Space Skybox/stormydays_up.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Down
    glBindTexture(GL_TEXTURE_2D, txId[5]);
    loadTGA("Space Skybox/stormydays_dn.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    //Load Stone Floor
    glBindTexture(GL_TEXTURE_2D, txId[6]);
    loadTGA("Textures/Floor_Texture.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    //Load Metal
    glBindTexture(GL_TEXTURE_2D, txId[7]);
    loadTGA("Textures/metal_plate.tga");
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);
}

void display()
{
    float lgt_pos[] = { 5.0f, 50.0f, 100.0f, 1.0f };

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(eye_x, 0, eye_z, look_x, 0, look_z, 0, 1, 0);    // Camera Position
    glLightfv(GL_LIGHT0, GL_POSITION, lgt_pos);                          // Set position of the light

    //  Draw Floor
    glDisable(GL_LIGHTING);
    glPushMatrix();
        glTranslatef(0, -5, 0);
        drawFloor(txId);
    glPopMatrix();
    glEnable(GL_LIGHTING);

//    glPushMatrix();
//    drawAlien();
//    glPopMatrix();

    //  Draw Skybox
    glPushMatrix();
        glTranslatef(0, -500, 0);
        skyBox(txId);
    glPopMatrix();

    // Draw Spaceship
    glPushMatrix();
        glTranslatef(-40, 0, -40);
        drawSpaceship(txId);
    glPopMatrix();

    glutSwapBuffers();
}


void initialise()
{
    float grey[4] = {0.2, 0.2, 0.2, 1.0};
    float white[4] = {1.0, 1.0, 1.0, 1.0};
    loadGLTextures();

    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_LIGHT1);

    glLightfv(GL_LIGHT0, GL_AMBIENT, grey);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, white);
    glLightfv(GL_LIGHT0, GL_SPECULAR, white);

    glLightfv(GL_LIGHT1, GL_AMBIENT, grey);
    glLightfv(GL_LIGHT1, GL_DIFFUSE, white);
    glLightfv(GL_LIGHT1, GL_SPECULAR, white);

    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);

    glEnable(GL_COLOR_MATERIAL);
    glMaterialfv(GL_FRONT, GL_SPECULAR, white);
    glMaterialf(GL_FRONT, GL_SHININESS, 50);

    glEnable(GL_DEPTH_TEST);
    glEnable(GL_TEXTURE_2D);
    glEnable(GL_NORMALIZE);
    glClearColor(0.0, 0.0, 0.0, 0.0);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(80, 1, 1, 3000);
}


void move_camera(int key, int x, int y)
{
	if (key == GLUT_KEY_LEFT)
    {
        angle -= 5; //Change direction
        rads = angle * M_PI / 180;
    }
	else if (key == GLUT_KEY_RIGHT)
    {
        angle += 5;
        rads = angle * M_PI / 180;
    }
	else if (key == GLUT_KEY_DOWN)
	{
		//Move backward
		if (eye_x > -100 && eye_x < 100 && eye_z > -100 && eye_z < 100) {
			eye_x -= 1 * sin(rads);
			eye_z += 1 * cos(rads);
		}
		else
		{
			eye_x = 0 * sin(rads);
			eye_z = 0 * cos(rads);
		}
	}
	else if (key == GLUT_KEY_UP)
	{
		//Move forward
		if (eye_x > -100 && eye_x < 100 && eye_z > -100 && eye_z < 100) {
			eye_x += 1 * sin(rads);
			eye_z -= 1 * cos(rads);
		}
		else
		{
			eye_x = 0 * sin(rads);
			eye_z = 0 * cos(rads);
		}
	}

	look_x = eye_x + 100 * sin(rads);
	look_z = eye_z - 100 * cos(rads);
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
