def func(x):
    return x*x + 2*x - 1;
def func1(x):
    return (1-x*x)/2;

def fixed_point_iteration(inital_guess,maximum_steps,tolerance):
    steps=0;
    value = inital_guess
    while steps<maximum_steps:
        if(abs(func(value))<tolerance):
            break;
        value=func1(value);
        steps+=1;

    return value;

initial_geuss = float(input("Provide the inital guess: "));
maximum_steps = int(input("Provide maximum steps: "));
toleratnce = float(input("Provide tolerance: "));


print(fixed_point_iteration(initial_geuss,maximum_steps,toleratnce));