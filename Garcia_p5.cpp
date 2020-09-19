/*
Name: Cristobal Garcia
assignment: Garcia_p5.cpp
Class: CS10A
Instructor: Professor Sarkar
Date: 05/13/2020
*/
#include <iostream>
#include <iomanip>
using namespace std;

const int row = 4;
const int col = 6;

void prompt();
void displayRatings(int [][col]);
void avgRating(int [][col]);
void highestRating(int [][col]);
void lowestRating(int [][col]);
void newRatings(int[][col]);


//Main function contains the switch statement that calls functions
int main(){
    
    int choice;
    int scores[row][col] = { {3, 1, 5, 2, 1, 5},
                            {4, 2, 1, 4, 2, 4},
                            {3, 1, 2, 4, 4, 1},
                            {5, 1, 4, 2, 4, 2} };
    
    prompt();
    
    cin >> choice;
    
    while (choice != 6){
        switch (choice) {
            case 1:
                displayRatings(scores);
                cout << "Function #1 Complete. Please enter a new choice: ";
                cin >> choice;
                break;
            case 2:
                avgRating(scores);
                cout << "Function #2 Complete. Please enter a new choice: ";
                cin >> choice;
                break;
            case 3:
                highestRating(scores);
                cout << "Function #3 Complete. Please enter a new choice: ";
                cin >> choice;
                break;
            case 4:
                lowestRating(scores);
                cout << "Function #4 Complete. Please enter a new choice: ";
                cin >> choice;
                break;
            case 5:
                newRatings(scores);
                cout << "Function #5 Complete. Please enter a new choice: ";
                cin >> choice;
                break;
            case 6:
                break;
//Input validation
            default:
                cout << "Invalid input. Enter a new choice here: ";
                cin >> choice;
                break;
        }
    }
    cout << "You have ended the program...\n";
}












//Prints the opening prompt
void prompt(){
    
    cout << "===========================================\n";
    cout << "Movie Rating (2-D Array Processing Program)\n";
    cout << "===========================================\n";
    
    cout << "\nSelect One Option to Preform\n";
    cout << "1. Display current movie ratings\n";
    cout << "2. Show the average rating for each movie\n";
    cout << "3. Show a reviewer's highest rating for a movie (Enter review# 1 - 4)\n";
    cout << "4. Show a movies lowest rating (Enter movie# 100 - 105)\n";
    cout << "5. Enter new ratings (1-5) for movie# 100-105 for four reviewers\n";
    cout << "6. Exit the program\n";
    
    cout << "\nEnter your choice here: ";
}












//Displays the movie ratings
void displayRatings(int array[][col]){
    
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";
    cout << "Film       Movie  Movie  Movie  Movie  Movie  Movie\n";
    cout << "Reviewer * #100 * #101 * #102 * #103 * #104 * #105\n";
    cout << "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n";

    cout << "#1";
    cout << "     ";
    for (int count = 0; count < col; count++) {
        
        cout << setw(7) << array[0][count];
    }
    cout << endl;

    cout << "#2";
    cout << "     ";
    for (int count = 0; count < col; count++) {
        cout << setw(7) << array[1][count];
    }
    cout << endl;
    
    cout << "#3";
    cout << "     ";
    for (int count = 0; count < col; count++) {
        cout << setw(7) << array[2][count];
    }
    cout << endl;

    cout << "#4";
    cout << "     ";
    for (int count = 0; count < col; count++) {
        cout << setw(7) << array[3][count];
    }
    cout << endl;
}
 











//Displays the average for all movies
void avgRating(int array[][col]){
    
    double avg[col];
    double total = 0;
    
    cout << "************************************\n";
 
//This loop calculates the average
    for (int count = 0; count < col; count++) {
                
       for (int cuenta = 0; cuenta < row; cuenta++) {
            
            total += array[cuenta][count];
            
            avg[count] = total / row;
        }
        
        total = 0;
        
        cout << "Avergae Review for Movie #" << (count + 100) <<  ": "  << avg[count];
        cout << endl;
        
    }
}












//Displays the lowest ratings for q movie
void lowestRating(int array[][col]){
    
    int low;
    int movie;
    
    cout << "What movie do you want the lowest score for: ";
    cin >> movie;
    
    //Input validation
    while (movie < 100 || movie > 105) {
        cout << "Invalid input. Enter a number 100-105 here: ";
        cin >> movie;
    }
//To adust for the movies being large
    movie -= 100;
//This loop finds the smallest number
    cout << "*************************\n";
    for (int count = 0; count < col; count++) {
        
        low = array[0][count];
        
        for (int cuenta = 1; cuenta < row; cuenta++) {
            
            if(array[cuenta][count] < low)
                low = array[cuenta][count];
        }
        if(movie == count){
            cout << "Movie #" << (count + 100) << " Lowest Score: " << low;
            cout << endl;
        }
    }
}












//Displays the highest rating from a reviewer
//If there was a tie it picks the rightmost movie by default
void highestRating(int array[][col]){
    
    int high;
    int review;
    int MVcol;
        
    cout << "Which reviewer's highest score do you want: ";
    cin >> review;
    
    //Input validation
    while(review > 5 || review < 1){
        cout << "Invalid Input. Enter a number 1-4 here: ";
        cin >> review;
    }
    //Adjust for it being one off
    review -= 1;
    
    cout << "*****************************\n";
        for (int count = 0; count < row; count++) {
            
            high = array[count][0];
            
            for (int cuenta = 1; cuenta < col; cuenta++) {
                
                if(array[count][cuenta] > high){
                    high = array[count][cuenta];
                }
            }
//This if statement and loop determines which movie is the highest
            if(review == count){
                
                for (int count = 0; count < col; count ++) {
                    
                    if(high == array[review][count])
                        MVcol = count;
                }
                cout << "Reviewer #" << (count + 1) << " Highest Score: " << high;
                cout << "\nFrom Movie #" << (MVcol + 100);
                cout << endl;
            }
        }
}












//Allows the user to input new ratings
void newRatings(int array[][col]){
    
    cout << "*********************************\n";

    for (int count = 0; count < row; count++) {
        
        
        cout << "Enter the scores for reviewer #" << count + 1 << endl;
        
        for (int cuenta = 0; cuenta < col;) {
            
            cout << "Score #" << cuenta + 1 << ": ";
            cin >> array[count][cuenta];

            //Input validation
            if(array[count][cuenta] > 0 && array[count][cuenta] < 6)
                cuenta++;
            else
                cout << "Invalid input enter a number that is 1-5\n";
        }
    }
}
