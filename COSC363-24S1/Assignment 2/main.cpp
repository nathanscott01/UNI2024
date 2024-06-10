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
#include "DoubleTruncatedCone.h"
//#include "Torus.h"
#include <algorithm>

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
// Define spotlight properties
//glm::vec3 spotlightPos1(10.0f, 10.0f, -3.0f);
//glm::vec3 spotlightDir1(0.0f, -1.0f, 0.0f); // Pointing downwards
//float spotlightAngle1 = glm::radians(30.0f); // 30-degree cone angle



// Ray Tracer
glm::vec3 trace(Ray ray, int step) {
    glm::vec3 backgroundCol(0);         // Background color is black
    glm::vec3 lightPos(10, 10, -3); // Light position
    glm::vec3 color(0);
    SceneObject *obj;

    ray.closestPt(sceneObjects);            // Compare the ray with all objects in the scene
    if (ray.index == -1) return backgroundCol;  // No intersection
    obj = sceneObjects[ray.index];              // Object on which the closest point of intersection is found

    if (ray.index == 0) {
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
    if ((shadowRay.index > 1) && (shadowRay.dist < lightDist)) {
        if (sceneObjects[shadowRay.index]->isTransparent()) {
            color = color * (0.5f * sceneObjects[shadowRay.index]->getTransparencyCoeff()) + (1.0f - sceneObjects[shadowRay.index]->getTransparencyCoeff()) * obj->getColor();
        } else {
            color = 0.2f * obj->getColor();
        }
    }

    // Reflection
    if (obj->isReflective() && step < MAX_STEPS) {
        float rho = obj->getReflectionCoeff();
        glm::vec3 normalVec = obj->normal(ray.hit);
        glm::vec3 reflectedDir = glm::reflect(ray.dir, normalVec);
        Ray reflectedRay(ray.hit, reflectedDir);
        glm::vec3 reflectedColor = trace(reflectedRay, step + 1);
        color = color + (rho * reflectedColor);
    }

    // Refraction
    if (obj->isRefractive() && step < MAX_STEPS) {
        float eta = obj->getRefractiveIndex();
        glm::vec3 normalVec = obj->normal(ray.hit);
        glm::vec3 refractedDir = glm::refract(ray.dir, normalVec, 1.0f / eta);
        Ray refractedRay(ray.hit, refractedDir);
        glm::vec3 refractedColor = trace(refractedRay, step + 1);
        color = color * (1.0f - obj->getRefractionCoeff()) + refractedColor * obj->getRefractionCoeff();
    }

    // Transparency
    if (obj->isTransparent() && step < MAX_STEPS) {
        float rho = obj->getTransparencyCoeff();
        vector<SceneObject*> sceneObjectsModified;
        SceneObject *obj2;

        for (size_t i = 0; i < sceneObjects.size(); ++i) {
            if (i != ray.index) {
                sceneObjectsModified.push_back(sceneObjects[i]);
            }
        }

        ray.closestPt(sceneObjectsModified);
        obj2 = sceneObjectsModified[ray.index];
        glm::vec3 obj2_color = obj2->lighting(lightPos, -ray.dir, ray.hit);
        color = color + (rho * obj2_color);
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

    Sphere *sphere1 = new Sphere(glm::vec3(2, -3, -90), 3);
    sphere1->setColor(glm::vec3(0, 1, 0));
    sphere1->setSpecularity(false);
    sphere1->setTransparency(true, 0.6);
    sceneObjects.push_back(sphere1);

    Sphere *sphere2 = new Sphere(glm::vec3(7.0, -5, -120.0), 4.0);
	sphere2->setColor(glm::vec3(0, 0, 1));   //Set colour to blue
    sphere2->setSpecularity(false);
    sphere2->setShininess(5);
    sphere2->setReflectivity(true, 0.6);
    sceneObjects.push_back(sphere2);		 //Add sphere to scene objects

    Plane *mirrorplane1 = new Plane(glm::vec3(-20, -5, -145),
                                  glm::vec3(20, -5, -145),
                                  glm::vec3(20, 10, -140),
                                  glm::vec3(-20, 10, -140));
    mirrorplane1->setColor(glm::vec3(0, 0, 0));
    mirrorplane1->setSpecularity(false);
//    mirrorplane1->setShininess(8);
    mirrorplane1->setReflectivity(true, 1);
    sceneObjects.push_back(mirrorplane1);

        // Add a double truncated cone to the scene
    DoubleTruncatedCone* cone = new DoubleTruncatedCone(glm::vec3(-5.0f, -15.0f, -70.0f), 3.0f, 0.0f, 12.0f);
    cone->setColor(glm::vec3(1.0f, 1.0f, 0.0f));
    cone->setRefractivity(true, 0.4f, 1.2f);
    sceneObjects.push_back(cone);


//        // Add a torus to the scene
//    Torus* torus = new Torus(glm::vec3(0.0f, 0.0f, -150.0f), 10.0f, 5.0f, 30.0f);
//    torus->setColor(glm::vec3(0.0f, 1.0f, 0.0f));
//    sceneObjects.push_back(torus);
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
