//  ========================================================================
//  COSC363 Assignment 2
//  Project: Ray Tracing
//
//  Author: Nathan Scott
//  Student ID: 81357713
//  FILENAME: main.cpp
//
//  COMMENTS:
//
//  ========================================================================

// Libraries
#include <iostream>
#include <GL/freeglut.h>
#include <vector>
#include <glm/glm.hpp>
#include "Ray.h"
#include "Sphere.h"
#include "Plane.h"
#include "SceneObject.h"
using namespace std;

// Globals
const float EDIST = 40.0;
const int NUMDIV = 500;
const int MAX_STEPS = 5;
const float XMIN = -10.0;
const float XMAX = 10.0;
const float YMIN = -10.0;
const float YMAX = 10.0;

vector<SceneObject*> sceneObjects;

// Ray Tracer
glm::vec3 trace(Ray ray, int step)
{
    glm::vec3 backgroundCol(0);         // Background color is black
    glm::vec3 lightPos(0, 10, -3); // Light position
    glm::vec3 color(0);
    SceneObject* obj;

    ray.closestPt(sceneObjects);            // Compare the ray with all objects in the scene
    if (ray.index == -1) return backgroundCol;  // No intersection
    obj = sceneObjects[ray.index];              // Object on which the closest point of intersection is found

    if (ray.index == 1)
    {
        // Function to make stripe/checkered pattern
        int stripWidth = 5;
        int iz = (ray.hit.z + 300) / stripWidth;
        int ix = (ray.hit.x + 30) / stripWidth;
        int k = iz % 2;
        int l = ix % 2;
        if (k != l) color = glm::vec3(1, 1, 1);
        else color = glm::vec3(0, 0, 0);
        obj->setColor(color);
    }

    color = obj->lighting(lightPos, -ray.dir, ray.hit);     // Objects color

    // Shadows
    glm::vec3 lightVec = lightPos - ray.hit;
    Ray shadowRay(ray.hit, lightVec);
    shadowRay.closestPt(sceneObjects);
    float lightDist = glm::length(lightVec);
    if ((shadowRay.index > 1) && (shadowRay.dist < lightDist))
    {
        color = 0.2f * obj->getColor();
    }

    // Reflection
    if (obj->isReflective() && step < MAX_STEPS)
    {
        float rho = obj->getReflectionCoeff();
        glm::vec3 normalVec = obj->normal(ray.hit);
        glm::vec3 reflectedDir = glm::reflect(ray.dir, normalVec);
        Ray reflectedRay(ray.hit, reflectedDir);
        glm::vec3 reflectedColor = trace(reflectedRay, step + 1);
        color = color + (rho * reflectedColor);
    }

    return color;
}


void display()
{
    float xp, yp; // Grid point
    float cellX = (XMAX - XMIN) / NUMDIV; // Cell width
    float cellY = (YMAX - YMIN) / NUMDIV; // Cell height
    glm::vec3 eye(0., 0., 0.);

    glClear(GL_COLOR_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glBegin(GL_QUADS);

    for (int i = 0; i < NUMDIV; i++)
    {
        xp = XMIN + i * cellX;
        for (int j = 0; j < NUMDIV; j++)
        {
            yp = YMIN + j * cellY;
            glm::vec3 dir(xp + 0.5 * cellX, yp + 0.5 * cellY, -EDIST);

            Ray ray = Ray(eye, dir);

            glm::vec3 col = trace(ray, 1);  // Trace primary ray and get color
            glColor3f(col.r, col.g, col.b);
            glVertex2f(xp, yp);     // Draw each call with its color value
            glVertex2f(xp + cellX, yp);
            glVertex2f(xp + cellX, yp + cellY);
            glVertex2f(xp, yp + cellY);
        }
    }
    glEnd();
    glFlush();
}


void initialise() {

    glMatrixMode(GL_PROJECTION);
    gluOrtho2D(XMIN, XMAX, YMIN, YMAX);

    glClearColor(0, 0, 0, 1);

    // Draw Scene

    Sphere *sphere1 = new Sphere(glm::vec3(-3.0, 0, -60), 3);
    sphere1->setColor(glm::vec3(0, 0.5, 0.5));
    sphere1->setSpecularity(false);
//    sphere1->setShininess(5);
//    sphere1->setReflectivity(true, 0.8);
    sphere1->setTransparency(true, 0.6);
    sceneObjects.push_back(sphere1);

    Plane *plane1 = new Plane (glm::vec3(-30, -15, -14),
                              glm::vec3(30, -15, -14),
                              glm::vec3(30, -15, -200),
                              glm::vec3(-30, -15, -200));
    plane1->setColor(glm::vec3(0.8, 0.8, 0));
    plane1->setSpecularity(false);
    sceneObjects.push_back(plane1);

    Plane *plane2 = new Plane (glm::vec3(30, 15, -14),
                               glm::vec3(30, 15, -200),
                              glm::vec3(30, -15, -200),
                              glm::vec3(30, -15, -14));
    plane2->setColor(glm::vec3(0, 1, 0));
    plane2->setSpecularity(false);
    sceneObjects.push_back(plane2);

    Plane *plane3 = new Plane (glm::vec3(-30, 15, -14),
                              glm::vec3(30, 15, -14),
                              glm::vec3(30, 15, -200),
                              glm::vec3(-30, 15, -200));
    plane3->setColor(glm::vec3(1, 1, 0.8));
    plane3->setSpecularity(false);
    sceneObjects.push_back(plane3);

    Plane *plane4 = new Plane (glm::vec3(-30, 15, -14),
                               glm::vec3(-30, -15, -14),
                               glm::vec3(-30, -15, -200),
                              glm::vec3(-30, 15, -200));
    plane4->setColor(glm::vec3(1, 0, 0));
    plane4->setSpecularity(false);
    sceneObjects.push_back(plane4);

    Plane *plane5 = new Plane (glm::vec3(-30, 15, -200),
                               glm::vec3(-30, -15, -200),
                               glm::vec3(30, -15, -200),
                              glm::vec3(30, 15, -200));
    plane5->setColor(glm::vec3(1, 1, 1));
    plane5->setSpecularity(false);
    sceneObjects.push_back(plane5);
}


// ------- Initialise main window -------
int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB );
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(20, 20);
    glutCreateWindow("Ray Tracer");
    glutDisplayFunc(display);
    initialise();

    glutMainLoop();
    return 0;
}
