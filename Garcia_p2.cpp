/*
Name: Cristobal Garcia
assignment: Garcia_p2.cpp
Class: CS10A
Instructor: Professor Sarkar
Date: 04/13/2020
*/
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

void doOneSet(char, int, double&);
int doOneProblem(char, int, int&, int&);
void getProblemsPerSet(int&);
void printReport(int, double, double, double);
void printHeader(char);
int getMaxNum();
int checkAnswer(char, int, int, int);
int calcCorrectAnswer(char, int, int);
int getNumbers(int);

int main(){
    int problemsPerSet;
    double _correct;
    int set1_correct;
    int set2_correct;
    int set3_correct;
    
    //The set_correct variables store the amount of correct answers for there
    //respective set by being after their corresponding function
    
    getProblemsPerSet(problemsPerSet);
    doOneSet('+', problemsPerSet, _correct);
    set1_correct = _correct;
    
    doOneSet('-', problemsPerSet, _correct);
    set2_correct = _correct;
    
    doOneSet('*', problemsPerSet, _correct);
    set3_correct = _correct;
    
    printReport(problemsPerSet, set1_correct, set2_correct, set3_correct);
}





//This function produces the random numbers within the desired range
int getNumbers(int maximum){
    static int count = 0;
    int count2 = 0;
    int randNum;
    
    count++;
    
    srand(time(0));
    
    //This loop makes the random number function repeat so the numbers aren't the same
    while(count > count2){
        randNum = ((rand() % maximum) + 1);
        count2++;
    }
    
    return randNum;
}





//This function calculates the answers to the random problems
int calcCorrectAnswer(char type, int num1, int num2){
    int result;
    
    if(type == '+')
        result = num1 + num2;
    if(type == '-')
        result = num1 - num2;
    if(type == '*')
        result = num1 * num2;
    
    return result;
}




//This function checks if the input anwers are correct and countes the number of right answers
int checkAnswer(char type, int num1, int num2, int Ans){
    static int correctPlus = 0;
    static int correctSub = 0;
    static int correctMulti = 0;
    int realAns;

    if(type == '+'){
    
        realAns = calcCorrectAnswer('+', num1, num2);
        if(realAns == Ans){
            cout << "correct\n";
            correctPlus++;
        }
        else
            cout << "incorrect\n";
        
        return correctPlus;
    }
    if(type == '-'){
        
        realAns = calcCorrectAnswer('-', num1, num2);
        if(realAns == Ans){
            cout << "correct\n";
            correctSub++;
        }
        else
            cout << "incorrect\n";
        
        return correctSub;
    }
    if(type == '*'){
        
        realAns = calcCorrectAnswer('*', num1, num2);
        if(realAns == Ans){
            cout << "correct\n";
            correctMulti++;
        }
        else
            cout << "incorrect\n";
        
        return correctMulti;
    }
    
    
    
    
//This function prints out a single problem and it is later used in a loop
}
int doOneProblem(char type, int max, int &num1, int &num2){

    int Ans;
    
    srand(time(0));
    
    if(type == '+'){
        num1 = getNumbers(max);
        num2 = getNumbers(max);
        cout << num1 << " + " << num2 << " = ";
        cin >> Ans;
    }
    if(type == '-'){
        num1 = ((rand() % max) + 1);
        num2 = ((rand() % max) + 1);
        cout << num1 << " - " << num2 << " = ";
        cin >> Ans;
    }
    if(type == '*'){
        num1 = ((rand() % max) + 1);
        num2 = ((rand() % max) + 1);
        cout << num1 << " * " << num2 << " = ";
        cin >> Ans;
    }

    return Ans;
}




//This function gets the max value a number in a problem can be
int getMaxNum(){
    int maxNum;
    
    cout << "Enter the maximun number for this set: ";
    cin >> maxNum;
    
    return maxNum;
}




//This fucntion prints out the header for each set
void printHeader(char type){
    
    if(type == '+'){
        cout << "Set #1\n";
        cout << "==========\n";
    }
    if(type == '-'){
        cout << "Set #2\n";
        cout << "==========\n";
    }
    if(type == '*'){
        cout << "Set #3\n";
        cout << "==========\n";
    }
}




//This function prints the report at the end illustrating how good the user did
void printReport(int numOfProblems, double correct1, double correct2, double correct3){
    
    cout << "\nSet #1: You got " << correct1 << " correct out of " << numOfProblems;
    cout << " for " << (correct1 / numOfProblems) * 100 << " %\n";
       
    cout << "\nSet #2: You got " << correct2 << " correct out of " << numOfProblems;
    cout << " for " << (correct2 / numOfProblems) * 100 << " %\n";
       
    cout << "\nSet #3: You got " << correct3 << " correct out of " << numOfProblems;
    cout << " for " << (correct3 / numOfProblems) * 100 << " %\n";
    
    cout << "\nOverall you got " << (correct1 + correct2 + correct3) << " correct out of " << (numOfProblems * 3);
    cout << " for " << ((correct1 + correct2 + correct3) / (numOfProblems * 3)) * 100 << "%\n";
}




//This function asks the user how many problems they are per set. There is also added input validation
void getProblemsPerSet(int &problemsPerSet){
    
    cout << "Enter problems per set here (between 3 - 10): ";
    cin >> problemsPerSet;
    
    while(problemsPerSet > 10 || problemsPerSet < 3){
        cout << "You entered a value outside the desired range please try again\n";
        
        cout << "Enter problems per set here (between 3 - 10): ";
        cin >> problemsPerSet;
    }
}




//This function prints out a set of problems either dealing with +, -, or *
void doOneSet(char type, int numOfProblems, double &_correct){
    //default
    int max = 100;
    
    int Ans;
    int num1;
    int num2;
    
    int correct = 0;
    int correct1 = 0;
    int correct2 = 0;
    
    if(type == '+'){
        
        printHeader('+');
        max = getMaxNum();
        
        for (int count = 0; count < numOfProblems; count++) {
            
            Ans = doOneProblem('+', max, num1, num2);
            correct = checkAnswer('+',num1, num2, Ans);
        }
        _correct = correct;
    }
    if(type == '-'){
        
        printHeader('-');
        max = getMaxNum();
        
        for (int count = 0; count < numOfProblems; count++) {
            
            Ans = doOneProblem('-', max, num1, num2);
            
           correct1 = checkAnswer('-', num1, num2, Ans);
        }
        _correct = correct1;
    }
    if(type == '*'){
        
        printHeader('*');
        max = getMaxNum();
        
        for (int count = 0; count < numOfProblems; count++) {
            
            Ans = doOneProblem('*', max, num1, num2);
            
            correct2 = checkAnswer('*', num1, num2, Ans);
        }
        _correct = correct2;
    }
}
