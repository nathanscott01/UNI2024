#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoord;

uniform mat4 mvpMatrix;

out vec2 oTexCoord;

void main()
{
	gl_Position = mvpMatrix * vec4(position, 1);
	oTexCoord = texCoord;
}