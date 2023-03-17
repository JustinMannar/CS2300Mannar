/*Justin Mannar 
HW 3 CS2060 
This program will take in user input, and check its validity through multiple requirements. If the 
input is invalid, the loop will keep going, only stopping once the inputted value has cleared all requirements.
Once it is considered valid input byt the program, it will be passed into multiple functions to both calculate 
the cost of the parking permit, and print out the required reciept to the parking garage owner
2/17/22
*/

#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define MIN_HOURS_AT_FLAT_RATE 3.0
#define MIN_FLAT_RATE_CHARGE 3.0
#define ADDITIONAL_HOURS_RATE 0.75
#define MAX_HOURS_ALLOWED 24.0
#define MAX_CHARGE 12.00

float validInput();
float cost(float input);
void receipt(int counter, float hours, float cost);


int main() {

	float totalHours = 0;
	float totalCost = 0;
	int carCounter = 1;

	
	float hours = validInput();
	while (hours != -1) {//loop in order to let user enter as many cars as desired
		float income = cost(hours);
		totalHours += hours;
		totalCost += income;
		//puts("\n");
		receipt(carCounter, hours, income);//will call the reciept function each time the loop iterates successfullly
		carCounter++;
		while ((getchar()) != '\n');//clears the buffer
		hours = validInput();//call the hours variable again so that the loop will keep running 

	}
	printf("total cars: %d    total hours: %f    total cost: $%f \n", carCounter - 1, totalHours, totalCost);

	if (hours == -1 && carCounter == 1) {//this if statement checks to see whether or not there were no cars entered. 
		puts("no cars were parked today");//In other words, this statement is only true if the user enters -1 first
	}

}
float validInput() {//does not take any paramters since its only job is to return valid input
	float input = 0;
	float validate = 0;
	
	puts("\n please enter the hours or enter -1 if there are not other cars:");
	validate = scanf("%f", &input);


	//checks return value of scanf, and makes sure that the input is not -1, while also checking to make sure the input is in range.
	while ((validate != 1) || ((input < 0 || input > 24) && (input != -1))) {
		puts("invalid input");
		while ((getchar()) != '\n');//if anything is not valid, this block loops and clears buffer after every input
		printf("please try again: ");
		validate = scanf("%f", &input);//new input is set to the validate variable, and is then checked
	}
	return input;

}

float cost(float input) {
	float price = 0;
	price = MIN_FLAT_RATE_CHARGE + (ceil(input) - MIN_HOURS_AT_FLAT_RATE) * ADDITIONAL_HOURS_RATE;//formula for finding the cost

	if (price > MAX_CHARGE) {//if the cost goes over the max amount, it is always set to the constant
		price = MAX_CHARGE;
	}
	else if (input <= MIN_HOURS_AT_FLAT_RATE) {//if less than minimum hourr constant, always returns the flat charge
		price = MIN_FLAT_RATE_CHARGE;
	}

	return price;
	
}

void receipt(int counter, float input, float price) {//takes in the three output variables of the program
	printf("car number: %d    hours: %f    cost: %f", counter, input, price);
}
