/*----------------------------------------------------------
* COSC363  Ray Tracer
*
*  The DoubleTruncatedCone class
*  This is a subclass of SceneObject, and hence implements the
*  methods intersect() and normal().
-------------------------------------------------------------*/

#include "DoubleTruncatedCone.h"
#include <cmath>

/**
 * Constructor for the double truncated cone.
 * Creates a double truncated cone with the specified center, bottom radius, top radius, and height.
 */
DoubleTruncatedCone::DoubleTruncatedCone(const glm::vec3& c, float r1, float r2, float h)
    : center(c), radius1(r1), radius2(r2), height(h) {}

/**
 * DoubleTruncatedCone's intersection method. The input is a ray.
 */
float DoubleTruncatedCone::intersect(glm::vec3 p0, glm::vec3 dir) {
    glm::vec3 d = p0 - center;
    float tanTheta = (radius1 - radius2) / height;
    float tanTheta2 = tanTheta * tanTheta;

    float a = dir.x * dir.x + dir.z * dir.z - tanTheta2 * dir.y * dir.y;
    float b = 2 * (d.x * dir.x + d.z * dir.z - tanTheta2 * d.y * dir.y + radius1 * tanTheta * dir.y);
    float c = d.x * d.x + d.z * d.z - tanTheta2 * d.y * d.y + 2 * radius1 * tanTheta * d.y - radius1 * radius1;

    float delta = b * b - 4 * a * c;
    if (delta < 0.001) return -1.0; // No intersection

    float t1 = (-b - sqrt(delta)) / (2 * a);
    float t2 = (-b + sqrt(delta)) / (2 * a);
    float t = (t1 > t2) ? t2 : t1; // Choose the smaller t

    if (t < 0) return -1.0;

    glm::vec3 p = p0 + t * dir;
    float y = p.y - center.y;
    if (y < 0 || y > height) return -1.0; // Intersection is outside the truncated cone

    return t;
}

/**
 * Returns the unit normal vector at a given point.
 * Assumption: The input point p lies on the double truncated cone.
 */
glm::vec3 DoubleTruncatedCone::normal(glm::vec3 p) {
    glm::vec3 n;
    float y = p.y - center.y;
    float r = radius1 + (radius2 - radius1) * (y / height);
    n.x = (p.x - center.x) / r;
    n.y = tan((radius1 - radius2) / height);
    n.z = (p.z - center.z) / r;
    return glm::normalize(n);
}
