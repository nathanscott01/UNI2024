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
#include <math.h>
#include "loadTGA.h"
#include "alien.h"
#include "skybox.h"
#include "floor.h"
#include "spaceship.h"
#include "train.h"
using namespace std;

#define GL_CLAMP_TO_EDGE 0x812F

//Global Variables
GLuint txId[8];     //Texture ID's
GLfloat spotExponent = 2.0f; // Make sure it's a float
float angle = 0;
float rads;
float look_x, look_z = -1., eye_x, eye_z;
float trainPosx = -100;
float trainPosz;
float trainAngle;
float wagonPosx = -130;
float wagonPosz;
float wagonAngle;
float train_theta;
float wagon_theta;
float theta_r = 20;
float theta_delta = 1;
float alien_z = -10;
float alien_delta = 0.2;
float spaceship_y = -1;
bool max_height = true;
bool up_cycle = true;
float lgt_pos[] = { 5.0f, 50.0f, 5.0f, 1.0f };
float shadowMat[16] = {lgt_pos[1], 0, 0, 0, -lgt_pos[0],0,
                       -lgt_pos[2], -1, 0, 0, lgt_pos[1], 0,
                       0, 0, 0, lgt_pos[1]};


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

    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);

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
}



void display()
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	gluLookAt(eye_x, 0, eye_z, look_x, 0, look_z, 0, 1, 0);
	glLightfv(GL_LIGHT0, GL_POSITION, lgt_pos); //light position

    // Alien 1
    glPushMatrix();
        glTranslatef(-17, -3, alien_z);
        glScalef(0.14, 0.14, 0.14);
        drawAlien(theta_r);
    glPopMatrix();

    // Alien 2
    glPushMatrix();
        glTranslatef(17, -3, alien_z);
        glScalef(0.14, 0.14, 0.14);
        drawAlien(theta_r);
    glPopMatrix();

    // Draw Skybox
    glPushMatrix();
        glTranslatef(0, -500, 0);
        skyBox(txId);
    glPopMatrix();

    //  Draw Floor
    glDisable(GL_LIGHTING);
    glPushMatrix();
        glTranslatef(0, -5, 0);
        drawFloor(&txId[6]);
    glPopMatrix();
    glEnable(GL_LIGHTING);

    // Draw Spaceship
    glPushMatrix();
        glTranslatef(0, spaceship_y, -30);
        drawSpaceship(&txId[7], shadowMat);
    glPopMatrix();

//     Draw Train Station
    glPushMatrix();
        glScalef(0.2, 0.2, 0.2);
        glTranslatef(0, -23, -50);
        drawTrainStation(trainPosx, trainPosz, trainAngle, wagonPosx, wagonPosz, wagonAngle, shadowMat);
    glPopMatrix();

    glutSwapBuffers();
}


void initialise()
{
	float grey[4] = { 0.2, 0.2, 0.2, 1.0 };
	float white[4] = { 1.0, 1.0, 1.0, 1.0 };

	loadGLTextures();

	glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE);
	glEnable(GL_COLOR_MATERIAL);

	glMaterialfv(GL_FRONT, GL_SPECULAR, white);
	glMaterialf(GL_FRONT, GL_SHININESS, 50);

	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_LIGHT1);

//		Define light's ambient, diffuse, specular properties
	glLightfv(GL_LIGHT0, GL_AMBIENT, grey);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, grey);
	glLightfv(GL_LIGHT0, GL_SPECULAR, white);

	glLightfv(GL_LIGHT1, GL_AMBIENT, grey);
	glLightfv(GL_LIGHT1, GL_DIFFUSE, white);
	glLightfv(GL_LIGHT1, GL_SPECULAR, white);

	glEnable(GL_DEPTH_TEST);
	glEnable(GL_TEXTURE_2D);
	glEnable(GL_NORMALIZE);
	glClearColor(0.0, 0.0, 0.0, 0.0);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(80.0, 1.0, 1.0, 3000.0);   //Perspective projection
}


void liftOff(int value)
{
    if (!max_height)
    {
        up_cycle = true;
        spaceship_y += 1;
        glutPostRedisplay();
        if (spaceship_y < 100)
        {
            glutTimerFunc(10, liftOff, 0);
        }
        else
        {
            spaceship_y = 0; // Reset spaceship position
            max_height = true;
            glutTimerFunc(10, liftOff, 0);
        }
    }
    else
    {
        if (up_cycle)
        {
            spaceship_y += 0.15;
            if (spaceship_y >= 1) up_cycle = false;
        } else {
            spaceship_y -= 0.15;
            if (spaceship_y <= -1) up_cycle = true;
        }
        glutTimerFunc(50, liftOff, 0);
    }
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
    else if (key == GLUT_KEY_SHIFT_L)
    {
        max_height = false;
    }

	look_x = eye_x + 100 * sin(rads);
	look_z = eye_z - 100 * cos(rads);
	glutPostRedisplay();
}


void trainTimer(int value)
{
    trainPosx++;
    wagonPosx++;
    trainPosz = 0.025 * pow(trainPosx, 2);
    wagonPosz = 0.025 * pow(wagonPosx, 2);
    if (trainPosx == 100) trainPosx = -100;
    if (wagonPosx == 90) wagonPosx = -110;
    train_theta = -atan(0.05 * trainPosx);
    trainAngle = train_theta * 180 / M_PI;
    wagon_theta = -atan(0.05 * wagonPosx);
    wagonAngle = wagon_theta * 180 / M_PI;
    glutPostRedisplay();
    glutTimerFunc(1, trainTimer, 0);
}

void theta_limit()
{
    if ((theta_r > 20) || (theta_r < -20)) theta_delta = theta_delta * -1;
    if ((alien_z > 15) || (alien_z < -12)) alien_delta = alien_delta * -1;
}

void myTimer(int value)
{
    alien_z = alien_z + alien_delta;
    theta_r = theta_r + theta_delta;
    theta_limit();
    glutPostRedisplay();
    glutTimerFunc(20, myTimer, 0);
}


 // ------- Initialise main window -------
int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(0, 0);
    glutCreateWindow("Alien");
    initialise();
    glutDisplayFunc(display);
    glutTimerFunc(1, trainTimer, 0);
    glutTimerFunc(10, liftOff, 0);
    glutTimerFunc(20, myTimer, 0);
    glutSpecialFunc(move_camera);
    glutMainLoop();
    return 0;
}
