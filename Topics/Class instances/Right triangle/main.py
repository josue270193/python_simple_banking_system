class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if hyp * hyp == leg_1 * leg_1 + leg_2 * leg_2:
            self.area = f"{(0.5 * leg_1 * leg_2):.1f}"
        else:
            self.area = "Not right"


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
print(triangle.area)
