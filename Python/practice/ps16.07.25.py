# 1. Area of Square
# Question: Calculate the area of a square. - Formula: Area = side × side - Input: - Side = 5 - Output: - Area of square is: 25

# side=int(input('Enter a value: '))
# Square_Area = side * side
# print(Square_Area )

# ________________________________________
# 2. Area of Rectangle
# Question: Calculate the area of a rectangle. - Formula: Area = length × breadth - Input: - Length = 6 - Breadth = 4 - Output: - Area of rectangle is: 24

# length=int(input('Enter length value: '))
# breadth=int(input('Enter breadth value: '))
# Rectangle_Area = length * breadth
# print(Rectangle_Area)

# ________________________________________
# 3. Area of Triangle
# Question: Calculate the area of a triangle using base and height. - Formula: Area = (1/2) × base × height - Input: - Base = 8 - Height = 5 - Output: - Area of triangle is: 20.0

# base=int(input('Enter base value: '))
# height=int(input('Enter height value: '))
# Triangle_Area = (1/2)*base*height
# print(Triangle_Area)

# ________________________________________
# 4. Perimeter of Square
# Question: Calculate the perimeter of a square. - Formula: Perimeter = 4 × side - Input: - Side = 6 - Output: - Perimeter of square is: 24

# side=int(input('Enter a value: '))
# Square_perimeter= 4*side
# print(Square_perimeter)


# ________________________________________
# 5. Perimeter of Rectangle
# Question: Calculate the perimeter of a rectangle. - Formula: Perimeter = 2 × (length + breadth) - Input: - Length = 5 - Breadth = 3 - Output: - Perimeter of rectangle is: 16

# length=int(input('Enter length value: '))
# breadth=int(input('Enter breadth value: '))
# Rectangle_perimeter = 2*(length + breadth)
# print(Rectangle_perimeter)


# ________________________________________
# 6. Perimeter of Triangle
# Question: Calculate the perimeter of a triangle. - Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18

# side1=int(input('Enter a value: '))
# side2=int(input('Enter a value: '))
# side3=int(input('Enter a value: '))
# Triangle_perimeter =side1+side2+side3
# print(Triangle_perimeter )

# ________________________________________
# 7. Break Amount into 1000s, 500s, and Remaining Change
# Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200

total_amount=3700
if total_amount>0:
    notes1000=total_amount//1000
    remaining_notes=total_amount%1000
    print('notes1000',notes1000)
    print('remaining_notes',remaining_notes)
if remaining_notes>0:
    notes500=remaining_notes//500
    remaining_notes=remaining_notes%500
    print('notes500',notes500)
    print('remaining_notes',remaining_notes)
if remaining_notes>0:
    notes200=remaining_notes//200
    remaining_notes=remaining_notes%200
    print('notes200',notes500)
    print('remaining_notes',remaining_notes)


# ________________________________________
# 8. Convert Seconds into Hours, Minutes, and Seconds
# Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12

# sec=int(input('Enter seconds value: '))
# min=int(input('Enter minutes value: '))
# hrs=int(input('Enter hours value: '))
# sec_to_min=sec/60
# sec_to_hrs=sec/3600
# min_to_sec=min*60
# hrs_to_sec=hrs*3600
# print('sec_to_min',sec_to_min)
# print('sec_to_hrs',sec_to_hrs)
# print('min_to_sec',min_to_sec)
# print('hrs_to_sec',hrs_to_sec)

# ________________________________________
# 9. Sum of Marks (Maths, Physics, Chemistry)
# Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263


# Maths=int(input('Enter mat marks: '))
# Physics=int(input('Enter phy marks: '))
# Chemistry=int(input('Enter chem marks: '))
# sum=Maths+Physics+Chemistry
# print(sum)


# ________________________________________
# 10. Average of Marks (Maths, Physics, Chemistry)
# Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67


# Maths=int(input('Enter mat marks: '))
# Physics=int(input('Enter phy marks: '))
# Chemistry=int(input('Enter chem marks: '))
# sum=Maths+Physics+Chemistry
# avg=sum/3
# print('sum',sum)
# print('avg',avg)
