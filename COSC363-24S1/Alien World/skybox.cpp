//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: skybox.cpp
//
//  COMMENTS:
//
//  ========================================================================
#include <GL/freeglut.h>

void skyBox(GLuint* txId)
{
    glEnable(GL_TEXTURE_2D);

    // Left Wall
    glBindTexture(GL_TEXTURE_2D, txId[0]);
    glBegin(GL_QUADS);
    glTexCoord2f(0, 0); glVertex3f(-1000, 0, 1000);
	glTexCoord2f(1, 0); glVertex3f(-1000, 0, -1000);
	glTexCoord2f(1, 1); glVertex3f(-1000, 1000, -1000);
	glTexCoord2f(0, 1); glVertex3f(-1000, 1000, 1000);
    glEnd();

    //Back Wall
    glBindTexture(GL_TEXTURE_2D, txId[1]);
    glBegin(GL_QUADS);
    glTexCoord2f(0, 0); glVertex3f(-1000, 0, -1000);
	glTexCoord2f(1, 0); glVertex3f(1000, 0, -1000);
	glTexCoord2f(1, 1); glVertex3f(1000, 1000, -1000);
	glTexCoord2f(0, 1); glVertex3f(-1000, 1000, -1000);
    glEnd();

    //Right Wall
    glBindTexture(GL_TEXTURE_2D, txId[2]);
    glBegin(GL_QUADS);
    glTexCoord2f(0, 0); glVertex3f(1000, 0, -1000);
	glTexCoord2f(1, 0); glVertex3f(1000, 0, 1000);
	glTexCoord2f(1, 1); glVertex3f(1000, 1000, 1000);
	glTexCoord2f(0, 1); glVertex3f(1000, 1000, -1000);
    glEnd();

    //Front Wall
    glBindTexture(GL_TEXTURE_2D, txId[3]);
    glBegin(GL_QUADS);
    glTexCoord2f(0, 0); glVertex3f(1000, 0, 1000);
	glTexCoord2f(1, 0); glVertex3f(-1000, 0, 1000);
	glTexCoord2f(1, 1); glVertex3f(-1000, 1000, 1000);
	glTexCoord2f(0, 1); glVertex3f(1000, 1000, 1000);
    glEnd();

    //Up
    glBindTexture(GL_TEXTURE_2D, txId[4]);
    glBegin(GL_QUADS);
    glTexCoord2f(0, 0); glVertex3f(1000, 1000, -1000);
	glTexCoord2f(1, 0); glVertex3f(1000, 1000, 1000);
	glTexCoord2f(1, 1); glVertex3f(-1000, 1000, 1000);
	glTexCoord2f(0, 1); glVertex3f(-1000, 1000, -1000);
    glEnd();

    //Down
    glBindTexture(GL_TEXTURE_2D, txId[5]);
    glBegin(GL_QUADS);
    glTexCoord2f(1, 0); glVertex3f(-1000, 0, 1000);
	glTexCoord2f(1, 1); glVertex3f(1000, 0, 1000);
	glTexCoord2f(0, 1); glVertex3f(1000, 0, -1000);
	glTexCoord2f(0, 0); glVertex3f(-1000, 0, -1000);
    glEnd();
}