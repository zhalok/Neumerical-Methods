def func(x):
    return x*x + 2*x - 1;

def secant(initial_guess1,initial_guess2,tolerance,maximum_steps):
    steps = 0;
    guess0=initial_guess1;
    guess1=initial_guess2;

    while steps<maximum_steps:
        neumarator = (guess1-guess0)*func(guess1);
        denominator = func(guess1)-func(guess0);
        guess2 = guess1 - (neumarator/denominator);
        steps += 1;
        if (abs(func(guess2))<tolerance):
            break;
        guess0=guess1
        guess1=guess2;

    return guess2;

initial_geuss1 = float(input("Provide the inital guess0: "));
initial_guess2 = float(input("Provide the inital guess1: " ));
if(initial_geuss1>initial_guess2):
    initial_geuss1,initial_guess2=initial_guess2,initial_geuss1;
maximum_steps = int(input("Provide maximum steps: "));
toleratnce = float(input("Provide tolerance: "));


print(secant(initial_geuss1,initial_guess2,toleratnce,maximum_steps));
