//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: floor.cpp
//
//  COMMENTS:
//
//  ========================================================================
#include <GL/freeglut.h>
#include <math.h>
#include <iostream>
#include "floor.h"

void drawFloor(GLuint* txId)
{
    float white[4] = { 1., 1., 1., 1. };
	float black[4] = {0};

	glDisable(GL_TEXTURE_2D);
	glNormal3f(0.0, 1.0, 0.0);
    glColor3f(1, 1, 1);
	glBindTexture(GL_TEXTURE_2D, *txId);
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE);
	glEnable(GL_TEXTURE_2D);			//A single quad
    glBegin(GL_QUADS);
    glMaterialfv(GL_FRONT, GL_SPECULAR, black);

    for (int i = -500; i < 500; i += 20)
    {
        for (int j = -500; j < 500; j += 20)
        {
            glTexCoord2f(1, 0); glVertex3f(i + 20, -0.1, j + 20);
            glTexCoord2f(1, 1); glVertex3f(i + 20, -0.1, j);
            glTexCoord2f(0, 1); glVertex3f(i, -0.1, j);
            glTexCoord2f(0, 0); glVertex3f(i, -0.1, j + 20);
        }
    }
	glEnd();
    glDisable(GL_TEXTURE_2D);
    glMaterialfv(GL_FRONT, GL_SPECULAR, white);
}
