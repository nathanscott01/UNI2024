#version 330

uniform sampler2D tSampler;

in vec2 oTexCoord;
in float diffTerm;
out vec4 outputColor;

void main() 
{ 
   outputColor = (diffTerm + 0.2) * vec4(0, 1, 0, 1);   //Green
}
