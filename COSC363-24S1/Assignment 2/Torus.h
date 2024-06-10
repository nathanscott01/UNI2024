#ifndef TORUS_H
#define TORUS_H

#include <glm/glm.hpp>
#include <vector>
#include <math.h>
#include "SceneObject.h"

class Torus : public SceneObject {
private:
    glm::vec3 center;
    float majorRadius;
    float minorRadius;
    glm::mat4 transform; // Transformation matrix for rotating the torus

public:
    Torus(const glm::vec3& c, float R, float r, float angle);

    float intersect(const glm::vec3& rayOrigin, const glm::vec3& rayDir, float& t);
    glm::vec3 normal(const glm::vec3& hitPoint);
};

#endif
