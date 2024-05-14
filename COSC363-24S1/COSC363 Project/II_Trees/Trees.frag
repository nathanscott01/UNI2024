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
	   outputColor =  texture(texRoad, oTexCoord);
      }
      else if(objIndex == 1)  //Trees
      {
	   vec4 treeColor = texture(texTree, oTexCoord);
	   if (treeColor.a == 0) discard;
	   outputColor = treeColor;
      }


}
	
