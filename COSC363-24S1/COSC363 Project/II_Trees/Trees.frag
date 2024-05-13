#version 330

uniform sampler2D texRoad;
uniform sampler2D texTree;

uniform int objIndex;

in vec2 oTexCoord;
out vec4 outputColor;

void main() 
{
      if(objIndex == 0)  //Road
      { 
	   outputColor =  vec4(0.2, 0.2, 0.2, 1);
      }
      else if(objIndex == 1)  //Trees
      {
	   outputColor = vec4(1, 0, 0, 0);
      }


}
	
