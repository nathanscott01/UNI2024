/*----------------------------------------------------------
* COSC363  Ray Tracer
*
*  The DoubleTruncatedCone class
*  This is a subclass of SceneObject, and hence implements the
*  methods intersect() and normal().
-------------------------------------------------------------*/

#ifndef DOUBLETRUNCATEDCONE_H
#define DOUBLETRUNCATEDCONE_H

#include <glm/glm.hpp>
#include "SceneObject.h"

class DoubleTruncatedCone : public SceneObject{
private:
    glm::vec3 center;
    float radius1; // Bottom radius
    float radius2; // Top radius
    float height;

public:
    DoubleTruncatedCone() {};
    DoubleTruncatedCone(const glm::vec3& c, float r1, float r2, float h);

    float intersect(glm::vec3 p0, glm::vec3 dir);
    glm::vec3 normal(glm::vec3 p);
};

#endif
