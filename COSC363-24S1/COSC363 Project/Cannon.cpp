//  ========================================================================
//  COSC363: Computer Graphics (2023);  University of Canterbury.
//
//  FILE NAME: Cannon.cpp
//  See Lab02.pdf for details
//
//  Program displays the model of a cannon (mesh data from Cannon.off)
//  Use left/right arrow keys to rotate the scene
//  Use up/down arrow keys to move camera up/down
//  ========================================================================

#include <iostream>
#include <fstream>
#include <GL/freeglut.h>
#include <climits>
#include <cmath>


#define SPACEBAR 32

using namespace std;

//--Globals ---------------------------------------------------------------
float *x, *y, *z;        //vertex coordinate arrays
int *t1, *t2, *t3;        //triangles
int nvrt, ntri;            //total number of vertices and triangles
float angle = - 10.0;    //Rotation angle for viewing
float cam_hgt = 100;
bool ready_to_fire = true;  //Cannon ready to fire
float t_elapsed = 0;
float ball_posx;
float ball_posy;


//-- Loads mesh data in OFF format    -------------------------------------
void loadMeshFile(const char *fname) {
    ifstream fp_in;
    int num, ne;

    fp_in.open(fname, ios::in);
    if (! fp_in.is_open()) {
        cout << "Error opening mesh file" << endl;
        exit(1);
    }

    fp_in.ignore(INT_MAX, '\n');                //ignore first line
    fp_in >> nvrt >> ntri >> ne;                // read number of vertices, polygons, edges

    x = new float[nvrt];                        //create arrays
    y = new float[nvrt];
    z = new float[nvrt];

    t1 = new int[ntri];
    t2 = new int[ntri];
    t3 = new int[ntri];

    for (int i = 0; i < nvrt; i ++)                         //read vertex list
        fp_in >> x[i] >> y[i] >> z[i];

    for (int i = 0; i < ntri; i ++)                         //read polygon list
    {
        fp_in >> num >> t1[i] >> t2[i] >> t3[i];
        if (num != 3) {
            cout << "ERROR: Polygon with index " << i << " is not a triangle." << endl;  //not a triangle!!
            exit(1);
        }
    }

    fp_in.close();
    cout << " File successfully read." << endl;
}

//--Function to compute the normal vector of a triangle with index tindx ----------
void normal(int tindx) {
    float x1 = x[t1[tindx]], x2 = x[t2[tindx]], x3 = x[t3[tindx]];
    float y1 = y[t1[tindx]], y2 = y[t2[tindx]], y3 = y[t3[tindx]];
    float z1 = z[t1[tindx]], z2 = z[t2[tindx]], z3 = z[t3[tindx]];
    float nx, ny, nz;
    nx = y1 * (z2 - z3) + y2 * (z3 - z1) + y3 * (z1 - z2);
    ny = z1 * (x2 - x3) + z2 * (x3 - x1) + z3 * (x1 - x2);
    nz = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
    glNormal3f(nx, ny, nz);
}

//--------draws the mesh model of the cannon----------------------------
void drawCannon() {
    glColor3f(0.4, 0.5, 0.4);

    //Construct the object model here using triangles read from OFF file
    glPushMatrix();
    glTranslatef(- 20, 30, 0);               //Send to origin
    glRotatef(30, 0, 0, 1);
    glTranslatef(20, - 30, 0);               //Send to original position
    glBegin(GL_TRIANGLES);
    for (int tindx = 0; tindx < ntri; tindx ++) {
        normal(tindx);
        glVertex3d(x[t1[tindx]], y[t1[tindx]], z[t1[tindx]]);
        glVertex3d(x[t2[tindx]], y[t2[tindx]], z[t2[tindx]]);
        glVertex3d(x[t3[tindx]], y[t3[tindx]], z[t3[tindx]]);
    }
    glEnd();
    glPopMatrix();

}

//----------draw a floor plane-------------------
void drawFloor() {
    bool flag = false;

    glBegin(GL_QUADS);
    glNormal3f(0, 1, 0);
    for (int x = - 400; x <= 400; x += 20) {
        for (int z = - 400; z <= 400; z += 20) {
            if (flag) glColor3f(0.6, 1.0, 0.8);
            else glColor3f(0.8, 1.0, 0.6);
            glVertex3f(x, 0, z);
            glVertex3f(x, 0, z + 20);
            glVertex3f(x + 20, 0, z + 20);
            glVertex3f(x + 20, 0, z);
            flag = ! flag;
        }
    }
    glEnd();
}

void cannonball() {
    float ball_x = 38.88;
    float ball_y = 64;
    float ball_vy = 30 * tan(30 * M_PI / 180);
    float ball_vx = 30;
    float lowest = 5;

    if (ready_to_fire) {
        t_elapsed = 0;
        ball_posx = ball_x;
        ball_posy = ball_y;
//        glutPostRedisplay();
    } else {
        if (ball_posy < lowest) {
            ready_to_fire = true;
        } else {
            ball_posx = ball_x + ball_vx * t_elapsed;
            ball_posy = ball_y + ball_vy * t_elapsed + 0.5 * - 9.8 * pow(t_elapsed, 2);
        }
    }

    glutPostRedisplay();
    glPushMatrix();
    glTranslatef(ball_posx, ball_posy, 0);
    glColor3f(0, 0, 1);
    glutSolidSphere(5, 36, 18);
    glPopMatrix();

}

//--Display: ----------------------------------------------------------------------
//--This is the main display module containing function calls for generating
//--the scene.
void display() {
    float lpos[4] = {100., 100., 100., 1.0};  //light's position

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);    //GL_LINE = Wireframe;   GL_FILL = Solid
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0, cam_hgt, 200, 0, 0, 0, 0, 1, 0);
    glLightfv(GL_LIGHT0, GL_POSITION, lpos);   //set light position

    glRotatef(angle, 0.0, 1.0, 0.0);        //rotate the whole scene

    drawFloor();

    drawCannon();

    //--start here

    // Mounting Brackets

    glColor3f(.5, .2, .5);

    glPushMatrix();
    glTranslatef(- 10, 5, 17);
    glScalef(80, 10, 6);
    glutSolidCube((1));
    glPopMatrix();

    glPushMatrix();
    glTranslatef(- 20, 25, 17);
    glScalef(40, 30, 6);
    glutSolidCube(1);
    glPopMatrix();

    glPushMatrix();
    glTranslatef(- 10, 5, - 17);
    glScalef(80, 10, 6);
    glutSolidCube((1));
    glPopMatrix();

    glPushMatrix();
    glTranslatef(- 20, 25, - 17);
    glScalef(40, 30, 6);
    glutSolidCube(1);
    glPopMatrix();

    // Create Cannonball

    cannonball();

    glFlush();
}

//------- Initialize OpenGL parameters -----------------------------------
void initialize() {
    loadMeshFile("OFF Files/Cannon.off");                //Specify mesh file name here
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);    //Background colour

    glEnable(GL_LIGHTING);                    //Enable OpenGL states
    glEnable(GL_LIGHT0);
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_DEPTH_TEST);
    glEnable(GL_NORMALIZE);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(90, 1, 50, 1000);  //The camera view volume
}

//------------ Special key event callback ---------------------------------
// To enable the use of left and right arrow keys to rotate the scene
void special(int key, int x, int y) {
    if (key == GLUT_KEY_LEFT) angle --;
    else if (key == GLUT_KEY_RIGHT) angle ++;
    else if (key == GLUT_KEY_UP) cam_hgt ++;
    else if (key == GLUT_KEY_DOWN) cam_hgt --;
    else if (key == GLUT_KEY_SHIFT_L) ready_to_fire = false;

    if (cam_hgt > 200) cam_hgt = 200;
    else if (cam_hgt < 10) cam_hgt = 10;

    glutPostRedisplay();
}

void myTimer(int value) {
    t_elapsed += .5;
    glutTimerFunc(50, myTimer, 0);
}


//  ------- Main: Initialize glut window and register call backs -----------
int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(800, 800);
    glutInitWindowPosition(10, 10);
    glutCreateWindow("Cannon");
    initialize();

    glutDisplayFunc(display);
    glutTimerFunc(50, myTimer, 0);
    glutSpecialFunc(special);
    glutMainLoop();
    return 0;
}
