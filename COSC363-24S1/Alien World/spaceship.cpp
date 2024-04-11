//  ========================================================================
//  COSC363 Assignment 1
//  Project: Alien World
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: spaceship.cpp
//
//  COMMENTS: Shadows dont work like i thought they did, not for objects moving
//              up and down y axis
//
//  ========================================================================

#define _USE_MATH_DEFINES
#include <cmath>
#include <GL/freeglut.h>

const int N = 131;
float theta;
//GLfloat spotExponent = 2.0f; // Make sure it's a float

float vx_init[N] = { -17.46, -17.28, -17.11, -16.93, -16.75, -16.58, -16.4, -16.23,
                    -16.05, -15.87, -15.7, -15.52, -15.34, -15.17, -14.99, -14.81,
                    -14.64, -14.46, -14.29, -14.11, -13.93, -13.76, -13.58,
                    -13.4,-13.23, -13.05, -12.87, -12.7, -12.52, -12.35, -12.17,
                    -11.99, -11.82, -11.64, -11.46, -11.29, -11.11, -10.93,
                    -10.76, -10.58, -10.41, -10.23, -10.05, -9.88, -9.7,
                    -9.52,-9.35, -9.17, -8.99, -8.82, -8.64, -8.47, -8.29,
                    -8.11,-17.46, -17.28, -17.11, -16.93, -16.75, -16.58, -16.4,
                    -16.23,-16.05, -15.87, -15.7, -15.52, -15.34, -15.17, -14.99,
                    -14.81,-14.64, -14.46, -14.29, -14.11, -13.93, -13.76,
                    -13.58,-13.4,-13.23,-13.05, -12.87, -12.7, -12.52, -12.35,
                    -12.17, -11.99, -11.82, -11.64, -11.46, -11.29, -11.11,
                    -10.93, -10.76, -10.58, -10.41, -10.23, -10.05, -9.88, -9.7,
                    -9.52, -9.35, -9.17, -8.99, -8.82, -8.64, -8.47,
                    -8.29, -8.11, -7.94, -7.76, -7.58, -7.41, -7.23, -7.05,
                    -6.88, -6.7, -6.53, -6.35, -6.17, -6.0, -5.82, -5.64,
                    -5.47, -5.29, -5.11, -4.94, -4.76, -4.59, -4.41, -4.23,
                    -4.06 };

float vy_init[N] = { 0.0, 0.38, 0.53, 0.65, 0.75, 0.84, 0.92, 0.99, 1.06, 1.13,
                     1.19, 1.25, 1.3, 1.35, 1.41, 1.45,1.5, 1.55, 1.59,
                     1.64, 1.68, 1.72, 1.76, 1.8, 1.84, 1.88, 1.92, 1.95,
                     1.99, 2.02, 2.06, 2.09,2.12, 2.16, 2.19, 2.22, 2.25,
                     2.28, 2.32, 2.35, 2.38, 2.41, 2.43, 2.46, 2.49, 2.52,
                     2.55, 2.58,2.6, 2.63, 2.66, 2.68, 2.71, 2.73, -0.0,
                     -0.38, -0.53, -0.65, -0.75, -0.84, -0.92, -0.99, -1.06,
                     -1.13, -1.19, -1.25, -1.3, -1.35, -1.41, -1.45, -1.5,
                     -1.55, -1.59, -1.64, -1.68, -1.72, -1.76,-1.8, -1.84,
                     -1.88, -1.92, -1.95, -1.99, -2.02, -2.06, -2.09, -2.12,
                     -2.16, -2.19, -2.22, -2.25,-2.28, -2.32, -2.35, -2.38,
                     -2.41, -2.43, -2.46, -2.49, -2.52, -2.55, -2.58, -2.6,
                     -2.63, -2.66,-2.68, -2.71, -2.73, 3.21, 3.86, 4.28,
                     4.6, 4.86, 5.08, 5.28, 5.45, 5.6, 5.74, 5.86,
                     5.97,6.06,6.15, 6.22, 6.29, 6.34, 6.39, 6.43,
                     6.46, 6.48, 6.49, 6.5 };

float toRadians = M_PI / 180.0;   //Conversion from degrees to radians
float angStep = 10 * toRadians;  //Rotate base curve in 1 deg steps
int nSlices = 36;				  //360 slices at 1 deg intervals
float vx[N], vy[N], vz[N];   //vertex positions
float wx[N], wy[N], wz[N];
float nx[N], ny[N], nz[N];
float mx[N], my[N], mz[N];

void computeNormal()
{
    float nx_current;
    float ny_current;
    for (int i = 0; i < N; i++)
    {
        if (i == 0)
        {
            nx_current = vy_init[1] - vy_init[0];
            ny_current = -vx_init[1] + vx_init[0];
        }
        else if (i == N - 1)
        {
            nx_current = vy_init[i] - vy_init[i - 1];
            ny_current = -vx_init[i] + vx_init[i - 1];
        }
        else
        {
            nx_current = vy_init[i + 1] - vy_init[i - 1];
            ny_current = -vx_init[i + 1] + vx_init[i - 1];
        }
        float dist = sqrtf(nx_current * nx_current + ny_current * ny_current);
        nx_current /= dist;
        ny_current /= dist;
        nx[i] = nx_current;
        ny[i] = ny_current;
    }
}

void drawCockpit()
{
    glutSolidSphere(4, 36, 36);
}

void drawSweepCurve(GLuint* txId)
{
    float white[4] = { 1., 1., 1., 1. };
    glDisable(GL_TEXTURE_2D);
    glNormal3f(0.0, 1.0, 0.0);

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

    // Set texture parameters for repeating texture
    glBindTexture(GL_TEXTURE_2D, *txId);
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);
    glEnable(GL_TEXTURE_2D);

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    for (int j = 0; j < nSlices; j++) {
        for (int i = 0; i < N; i++) {
            wx[i] = cos(angStep) * vx[i] + sin(angStep) * vz[i];
            wy[i] = vy[i];
            wz[i] = -sin(angStep) * vx[i] + cos(angStep) * vz[i];
            mx[i] = cos(angStep) * nx[i] + sin(angStep) * nz[i];
            my[i] = ny[i];
            mz[i] = -sin(angStep) * nx[i] + cos(angStep) * nz[i];
        }

        glBegin(GL_QUAD_STRIP);

        bool bottom = true;
        int s_coord;

        for (int i = 0; i < N; i++) {
            if (bottom) {
                s_coord = 0;
                bottom = false;
            } else {
                s_coord = 1;
                bottom = true;
            }
            glNormal3f(nx[i], ny[i], nz[i]);
            glTexCoord2f(s_coord, 0);
            glVertex3f(vx[i], vy[i], vz[i]);
            glNormal3f(mx[i], my[i], mz[i]);
            glTexCoord2f(s_coord, 1);
            glVertex3f(wx[i], wy[i], wz[i]);
        }
        glEnd();

        for (int i = 0; i < N; i++) {
            vx[i] = wx[i];
            vy[i] = wy[i];
            vz[i] = wz[i];
            nx[i] = mx[i];
            ny[i] = my[i];
            nz[i] = mz[i];
        }
    }

    glMaterialfv(GL_FRONT, GL_SPECULAR, white);
	glDisable(GL_TEXTURE_2D);
}

void drawSweepCurveShadow()
{
    glDisable(GL_TEXTURE_2D); // Disable texture mapping

    float white[4] = { 1., 1., 1., 1. };
    glMaterialfv(GL_FRONT, GL_SPECULAR, white);

    // Set the normal for the sweep surface
    glNormal3f(0.0, 1.0, 0.0);

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);

    for (int j = 0; j < nSlices; j++) {
        for (int i = 0; i < N; i++) {
            wx[i] = cos(angStep) * vx[i] + sin(angStep) * vz[i];
            wy[i] = vy[i];
            wz[i] = -sin(angStep) * vx[i] + cos(angStep) * vz[i];
            mx[i] = cos(angStep) * nx[i] + sin(angStep) * nz[i];
            my[i] = ny[i];
            mz[i] = -sin(angStep) * nx[i] + cos(angStep) * nz[i];
        }

        glBegin(GL_QUAD_STRIP);

        bool bottom = true;

        for (int i = 0; i < N; i++) {
            if (bottom) {
                bottom = false;
            } else {
                bottom = true;
            }
            // Set the normal for each vertex
            glNormal3f(nx[i], ny[i], nz[i]);
            glVertex3f(vx[i], vy[i], vz[i]);
            glNormal3f(mx[i], my[i], mz[i]);
            glVertex3f(wx[i], wy[i], wz[i]);
        }
        glEnd();

        // Update vertex and normal arrays for the next slice
        for (int i = 0; i < N; i++) {
            vx[i] = wx[i];
            vy[i] = wy[i];
            vz[i] = wz[i];
            nx[i] = mx[i];
            ny[i] = my[i];
            nz[i] = mz[i];
        }
    }
}

void drawSpaceship(GLuint* txId, float shadowMat[16])
{
    computeNormal();

    for (int i = 0; i < N; i++)		//Initialize data everytime the frame is refreshed
	{
		vx[i] = vx_init[i];
		vy[i] = vy_init[i];
		vz[i] = 0;
		nz[i] = 0;
	}

    glPushMatrix();
        drawSweepCurve(txId);
    glPopMatrix();

    glColor3f(1, 0, 0.8);
    glPushMatrix();
        glTranslatef(0, 6.2, 0);
        drawCockpit();
    glPopMatrix();

    glFlush();
}