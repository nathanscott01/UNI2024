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

void drawFloor(GLuint txId[6])
{
    glEnable(GL_TEXTURE_2D);

    glBindTexture(GL_TEXTURE_2D,  txId[6]);
	glColor3f(1, 1, 1);
	glNormal3f(0, 1, 0);
	glBegin(GL_QUADS);				//A single quad
    for (int i = -500; i < 500; i = i + 20)
    {
        for (int j = -500; j < 500; j = j + 20)
        {
            glTexCoord2f(1, 0); glVertex3f(i + 20, 0, j + 20);
            glTexCoord2f(1, 1); glVertex3f(i + 20, 0, j);
            glTexCoord2f(0, 1); glVertex3f(i, 0, j);
            glTexCoord2f(0, 0); glVertex3f(i, 0, j + 20);
        }
    }
	glEnd();

}