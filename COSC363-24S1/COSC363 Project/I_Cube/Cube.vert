#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoord;

uniform mat4 mvMatrix;
uniform mat4 mvpMatrix;
uniform mat4 norMatrix;
uniform vec4 lightPos;

out vec2 oTexCoord;
out float diffTerm;

void main()
{
	vec4 posnEye = mvMatrix * vec4(position, 1);
	vec4 normalEye = norMatrix * vec4(normal, 0);
	vec4 lgtVec = normalize(lightPos - posnEye); 

	diffTerm = max(dot(lgtVec, normalEye), 0);

	gl_Position = mvpMatrix * vec4(position, 1);
	oTexCoord = texCoord;
}