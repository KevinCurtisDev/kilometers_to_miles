print("How many kilometers did you run today?")

#promt for users input
kl = input() 

#convert kl into a float and divide by 1.60934 to calculate miles
miles = float(kl)/1.60934 

#rounds miles to two decimal places
miles = round(miles, 2) 

#uses interpolation to include the miles "float" in the string
print(f"You ran a total of {kl}, that's equal to {miles} miles") 