

# 1: 
class point :
    def __init__(self,x,y): # create
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):  # View
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
# p=point(0,0)
# print(p.distance_from_origin())

# 4: Creating new class for checking if the point lies on a plane or not
class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    def point_on_line(Line,point):
        if Line.A * point.x_cod + Line.B * point.y_cod + Line.C == 0 :
            return 'Point lies on the line'
        else :
            return 'Does not lies on line'
    
# L1=Line(1,1,-2)
# P1=point(1,2)
# print(L1)
# print(P1)
# print(L1.point_on_line(P1))

# 5: Formula for shortest distance between line and point   | Ax + By + C | / (A**2 + B**2) ** 0.5 
    def shortest_distance(Line,point):
        return abs(Line.A * point.x_cod + Line.B * point.y_cod + Line.C) / (Line.A**2 + Line.B**2) ** 0.5
# L1=Line(1,1,2)
# p1=point(1,1)
# print(L1.shortest_distance(p1))