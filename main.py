

def main(term):
    first_term, second_term = 0, 1
    if term == 1:
        print(first_term)
    else:
        print(first_term)
        for i in range(2,term*3):
            third_term = first_term + second_term
            first_term = second_term
            second_term = third_term
            if third_term % 2 == 0:
                print(third_term)
main(15)




