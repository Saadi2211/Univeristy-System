year_brith:int = 2004
current_year:int = 2024
age:int = current_year - year_brith
print(age)



 #area of rectangle
length:int = 10
width:int = 20
area_of_rectangle:int = length * width
print(area_of_rectangle)


 #area of cube
A = int(2)
Area_of_cube = 6*A**2
print(Area_of_cube)


#fahrenheit to celcius

def fahrenheit_to_celcius(num):
    celcius = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius:", round(celcius,3))


fahrenheit = 55
fahrenheit_to_celcius(fahrenheit)



# Python program to find Area of a circle

def findArea(r):
    PI = 3.142
    return PI * (r*r);

# Driver method
print("Area is %.5f" % findArea(7));





# Python Program to Convert seconds, minutes and seconds

def convert(seconds):
	seconds = seconds % (24 * 3600)
	hour = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	
	return "%d:%02d:%02d" % (hour, minutes, seconds)
	
n = 12345
print(convert(n))






#calculate precentage 

exam_list = [4, 6, -2, 3, -8, 0, -1, 8, 9, 1]

print("The original list is : " + str(exam_list))

res = (len(list(filter(lambda ele: ele > 0, exam_list))) / len(exam_list)) * 100

print("Positive elements percentage : " + str(res))







weight = int(input(51));
height = float(input(5.6));
x = weight/float(height*height);
if x < 5.6:
    print('Underweight')
if x>=5.6 and x<51:
    print("Normal")
if x >= 51 and x < 60:
   print('Overweight')
if x >= 60:
   print('Obesitys')
   
   
   
   
