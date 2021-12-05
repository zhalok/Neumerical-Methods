def func(x):
    return x*x+2*x-1;

def false_position(x0,x1,e):
    while True:
        x2 = x0+((func(x0)*(x1-x0))/(func(x1)-func(x0)));
        if(func(x2)*func(x0)>0):
            x0=x2;
        else:
            x1=x2;

        if(abs(func(x2))<e):
            break;
    return x2;

guess1 = float(input("Enter the fist guess: "));
guess2 = float(input("Enger the second guess: "));

if(func(guess1)*func(guess2)>0):
    print("You made wrong guess \n please try again");
else:
    if(guess1>guess2):
        guess1,guess2=guess2,guess1;
    tolerancy = float(input("Enter tolerant value: "));

    print(false_position(guess1,guess2,tolerancy));




