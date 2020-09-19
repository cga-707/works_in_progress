/* Name: Cristobal Garcia
assignment: Garcia_p1.cpp
Class: CS10A
Instructor: Professor Sarkar
Date: 04/05/2020 */
#include <iostream>
#include <string>
using namespace std;

//I grouped the function's prototypes for easier reading.

//I also put a comment before each function explaing what it does
//in order to both explain the function's purpose and show seperation.
//Thank you!!

//Functions Related to drawing individual componets of the rocket
void drawConeE(int);
void drawConeO(int);
void drawEven(int, int);
void drawOdd(int, int);
void drawHori(int);
void drawVertE(int, int);
void drawVertO(int, int);

//Prompt
void promptMessage();

//Functions that draw the Cones and Boxes
void drawCone(int);
void drawBoxes(int, int, int);

//the first function draws the rocket and the second draws the rockets and collets the input
void drawRocket(int, int, int);
void drawRocketCollect();

//Functions that collect the input
int getHeight();
int getWidth();
int getStages();



int main(){
    
    //Only displays the prompt
    promptMessage();
    
    //Collects the input then prints the rocket
    drawRocketCollect();
}




//Draws Boxes
void drawBoxes(int height, int width, int stages){
    for (int count = 0; count < stages; count++) {
        
        if(height % 2 == 0)
            drawEven(height, width);
        else
            drawOdd(height, width);
    }
}

//Collects the input then prints the rocket
void drawRocketCollect(){
    int width, height, stages;
    
    height = getHeight();
    width = getWidth();
    stages = getStages();
    drawRocket(height, width, stages);
}

//Prints rockets and also validates input
void drawRocket(int height, int width, int stages){
    
    while (height < 3 || height > 15) {
        cout << "You entered a value out of range for the height!\n";
        cout << "Enter a value between 3 and 15: ";
        cin >> height;
    }
    while (width < 3 || width > 15) {
        cout << "You entered a value out of range for the width!\n";
        cout << "Enter a value between 3 and 15: ";
        cin >> width;
    }
    while (stages < 3 || stages > 15) {
        cout << "You entered a value out of range for the stages!\n";
        cout << "Enter a value between 3 and 15: ";
        cin >> stages;
    }
    drawCone(width);
    drawBoxes(height, width, stages);
    drawCone(width);
}

//Draws Cone/Thruster
void drawCone(int width){
    
    if(width % 2 == 0)
        drawConeE(width);
    else
        drawConeO(width);
}

//Collects input for stages
int getStages(){
    int getS;
    cout << "Enter a the number of stages: ";
    cin >> getS;
    cout << "================================\n\n";
    return getS;
}

//Collects input for width
int getWidth(){
    int getW;
    cout << "Enter a width for the rocket: ";
    cin >> getW;
    return getW;
}

//Collects input for height
int getHeight(){
    int getH;
    cout << "Enter a height for the rocket: ";
    cin >> getH;
    return getH;
}

//Prints out prompt
void promptMessage(){
    cout << "This program builds a rocket with the input dimensions.\n";
    cout << "Enter only values between 3 and 15.\n";
}
//Draw odd full boxes
void drawOdd(int heightO, int widthO){
    
    drawHori(widthO);
    drawVertO(heightO, widthO);
    drawHori(widthO);
}

//Draws even empty boxes
void drawEven(int heightE, int widthE){
    
    drawHori(widthE);
    drawVertE(heightE, widthE);
    drawHori(widthE);
}
//Drawing a cone for an even width
void drawConeE(int widthCE){
    string block = "*";
    string ispaces = " ";
    string ispaces2 = "";
    string ispaces3 = "";
    
    int modwidthC;
    int coneRows;
    int conePosition;
    
    for (int count = 1; count < ((widthCE / 2) - 1); count++) {
        ispaces += " ";
    }
    cout << ispaces + block + block << endl;
    
    

    modwidthC = (widthCE - 1) / 2;
    coneRows = modwidthC;
    conePosition = modwidthC;
    
    if(widthCE > 4){
        int count = 0;
        for (; count < coneRows; count++) {
            
            for (int count1 = 0; count1 < conePosition - 1; count1++) {
                ispaces2 += " ";
            }
                ispaces3 += "  ";
            cout << ispaces2 + block + ispaces3 + block << endl;
            
            if(ispaces2 == " ")
                ispaces2 = "";
            
            ispaces2 = "";
            conePosition--;
        }
    }
    if(widthCE == 4)
        cout << "*  *\n";
    
}

//Drawing a cone for an even width
void drawConeO(int widthCO){
    string block = "*";
    string ispaces = " ";
    string ispaces2 = "";
    string ispaces3 = " ";
    
    int modwidthC;
    int coneRows;
    int conePosition;

    modwidthC = (widthCO - 1) / 2;
    coneRows = modwidthC;
    conePosition = modwidthC;
    
    for (int count = 0; count < modwidthC - 1; count++) {
        ispaces += " ";
    }
    cout << ispaces + block << endl;
    
    if(widthCO > 3){
        int count = 0;
        for (; count < coneRows; count++) {
            
            for (int count1 = 0; count1 < conePosition - 1; count1++) {
                ispaces2 += " ";
            }
            if(count > 0)
                ispaces3 += "  ";
            cout << ispaces2 + block + ispaces3 + block << endl;
            
            if(ispaces2 == " ")
                ispaces2 = "";
            
            ispaces2 = "";
            conePosition--;
        }
    }
    if(widthCO == 3)
        cout << "* *\n";
}

//Draws Horizontal Lines
void drawHori(int width0){
    string block = "*";
    
    for (int count = 0; count < width0; count++) {
        cout << block;
    }
    cout << endl;
}

//Draws the two horizontal lines in an even box
void drawVertE(int height1E, int width1E){
    string block = "*";
    string spaces = " ";
    
    for (int count = 0; count < (width1E - 3); count++) {
        spaces += " ";
    }
    
    for (int count = 0; count < (height1E - 2); count++) {
        cout << block + spaces + block << endl;
    }
}

//Draws the horitzontal lines in an odd box
void drawVertO(int height1, int width1){
    string block = "*";
    
    for (int count = 0; count < (width1 - 1); count++) {
        block += "*";
    }
    for (int count = 0; count < (height1 - 2); count++) {
        cout << block << endl;
    }
}

