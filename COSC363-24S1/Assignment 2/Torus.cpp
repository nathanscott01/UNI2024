/*----------------------------------------------------------
* COSC363  Ray Tracer
*
*  The torus class
*  This is a subclass of SceneObject, and hence implements the
*  methods intersect() and normal().
-------------------------------------------------------------*/

#include "Torus.h"
#include <glm/gtc/matrix_transform.hpp>
#include <vector>
#include <cmath>

/**
 * Constructor for the torus. Creates a torus with the specified center, major radius, minor radius, and rotation angle.
 */
Torus::Torus(const glm::vec3& c, float R, float r, float angle)
    : center(c), majorRadius(R), minorRadius(r)
{
    transform = glm::rotate(glm::mat4(1.0f), glm::radians(angle), glm::vec3(0, 1, 0));
}

/**
 * Torus's intersection method. The input is a ray.
 */
float Torus::intersect(glm::vec3 p0, glm::vec3 dir) {
    // Transform the ray to the torus local space
    glm::vec3 O = glm::vec3(glm::inverse(transform) * glm::vec4(p0 - center, 1.0));
    glm::vec3 D = glm::vec3(glm::inverse(transform) * glm::vec4(dir, 0.0));

    float alpha = glm::dot(D, D);
    float beta = 2.0f * glm::dot(O, D);
    float gamma = glm::dot(O, O) + majorRadius * majorRadius - minorRadius * minorRadius;
    float delta = 4.0f * majorRadius * majorRadius * (D.x * D.x + D.z * D.z);

    // Coefficients for the quartic equation
    float coeffs[5];
    coeffs[0] = alpha * alpha;
    coeffs[1] = 2.0f * alpha * beta;
    coeffs[2] = beta * beta + 2.0f * alpha * gamma - delta;
    coeffs[3] = 2.0f * beta * gamma;
    coeffs[4] = gamma * gamma - delta;

    // Solve the quartic equation (implement or use a library)
    std::vector<float> roots; // Placeholder for roots
    // SolveQuartic(coeffs, roots); // Implement this solver or use an existing library

    // Find the smallest positive root
    float t = -1.0f;
    for (float root : roots) {
        if (root > 0.0f && (t < 0.0f || root < t)) {
            t = root;
        }
    }

    return t > 0.0f ? t : -1.0f;
}

/**
 * Returns the unit normal vector at a given point.
 * Assumption: The input point p lies on the torus.
 */
glm::vec3 Torus::normal(glm::vec3 p) {
    glm::vec3 P = glm::vec3(glm::inverse(transform) * glm::vec4(p - center, 1.0));
    glm::vec3 Q(P.x, 0.0f, P.z);
    Q = glm::normalize(Q) * majorRadius;

    glm::vec3 N = P - Q;
    N = glm::normalize(N);

    return glm::vec3(transform * glm::vec4(N, 0.0));
}
