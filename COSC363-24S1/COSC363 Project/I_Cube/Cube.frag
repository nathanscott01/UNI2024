#version 330

uniform sampler2D tSampler;

in vec2 oTexCoord;
in float diffTerm;
out vec4 outputColor;

void main() 
{
   vec4 texColor = texture(tSampler, oTexCoord);
   // outputColor = (diffTerm + 0.2) * vec4(0, 1, 0, 1);   //Green
   if ((texColor.g == 0) && (texColor.b == 0)) discard;
   outputColor = (diffTerm + 0.2) * texColor;
}
