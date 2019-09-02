# Jakub Kolasinski
# SSW-567 HW01
import unittest
a = int(input('Enter the "A" length of the triangle: '))
b = int(input('Enter the "B" length of the triangle: '))
c = int(input('Enter the "C" length of the triangle: '))

def classify_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if a == b == c:
            return 'Equilateral'
        elif (a*a) + (b*b) == (c*c):
            return 'Right'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'Not a triangle'

print(classify_triangle(a, b, c))

#def printclassify_triangle(a,b,c):
    #print(classify_triangle('a','b','c') + classify_triangle(a,b,c))

class TestTriangles(unittest.TestCase):
    def testEquilateral(self):
        self.assertEqual(classify_triangle(1,1,1), 'Equilateral')
        self.assertNotEqual(classify_triangle(1,1,3), 'Not Equilateral')
    
    def testRight(self):
        self.assertEqual(classify_triangle(3,4,5), 'Right')
        self.assertNotEqual(classify_triangle(3, 4, 6), 'Not Right')
 
    def testIsosceles(self):
        self.assertEqual(classify_triangle(1,1,2), 'Isosceles')
        self.assertNotEqual(classify_triangle(1, 1, 2), 'Not Isosceles')
   
    def testScalene(self):
        self.assertEqual(classify_triangle(1,2,3), 'Scalene')
        self.assertNotEqual(classify_triangle(1,1,1), 'Not Scalene')
    
    def testNotatriangle(self):
        self.assertEqual(classify_triangle(1,0,1), 'Not a triangle')
        self.assertNotEqual(classify_triangle(1,1,1), 'Triangle')

if __name__ == '__main__':
    #printclassify_triangle(1,1,1)
    #printclassify_triangle(3,0,1)
    #printclassify_triangle(1,4,5)
    #printclassify_triangle(3,4,3)
    unittest.main(exit=False)




