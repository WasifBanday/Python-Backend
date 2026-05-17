# Write OOP classes to handle the following scenarios:
#   1: A user can create and view 2D coordinates
#   2: A user can find out the distance between 2 coordinates
#   3: A user can find find the distance of a coordinate from origin
#   4: A user can check if a point lies on a given line
#   5: A user can find the distance between a given 2D point and a given line 

# 1: 
class point :
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
# p=point(1,1)
# print(p)

# 2: Distance formula between two coordinates = ((x2​−x1​)**2 + (y2​−y1​)**2 ) ** 0.5 
    def euclidean_distance(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2) ** 0.5
# p1=point(0,0)
# p2=point(10,10)
# print(p1.euclidean_distance(p2))

# 3: Distance formula from origin to point  d=( x2+y2 ) ** 0.5 
    def distance_from_origin(self):
        return (self.x_cod**2 + self.y_cod**2)** 0.5
p=point(0,0)
print(p.distance_from_origin())