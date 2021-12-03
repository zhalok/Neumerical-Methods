def func(x):
    return x*x + 2*x - 1;

def derivative_func(x):
    return 2*x+2;

def newton_raphson(initial_guess,maximum_steps,tolerance):
    steps=0;
    guess = initial_guess;
    while steps<maximum_steps:
        if(abs(func(guess))<tolerance):
            break;
        guess=guess-(func(guess)/derivative_func(guess));
        steps+=1;
    return guess;

initial_geuss = float(input("Provide the inital guess: "));
maximum_steps = int(input("Provide maximum steps: "));
toleratnce = float(input("Provide tolerance: "));


print(newton_raphson(initial_geuss,maximum_steps,toleratnce));
