length = int(input("Enter the length : "))    
width = int(input("Enter the width : "))  

area = length * width
perimeter = 2 * (length + width) 

print(f"Area: {int(area)}" if area.is_integer() else f"Area: {area}")
print(f"Perimeter: {int(perimeter)}" if perimeter.is_integer() else f"Perimeter: {perimeter}")  

