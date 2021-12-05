def func(x):
    return x*x + 2*x - 1;

def bisection(left,right,tolerant_value):


    while True:
        mid = (left+right)/2;
        if(func(mid)*func(right)):
            right=mid;
        else:
            left=mid;
        if(abs(func(mid))<tolerant_value):
            break;
    print('\nRequired Root is : %0.10f' % mid)

guess1 = int(input("Provide guess1: "));
guess2 = int(input("Provide guess2: "));

if(func(guess1)*func(guess2)>0):
    print("You made a wrong guess \n please make a guess again");
else:
    tolerant = float(input("Provide a tolerant value: "));
    guess1,guess2=guess2,guess1;

    bisection(guess1,guess2,tolerant);




