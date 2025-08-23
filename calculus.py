import sys

def main():
    func = input()
    x = float(input())
    sigma = float(input())
    eps = 5 * sigma
    eval_x_0 = eval(func)
    x -= sigma
    eval_sigma_minus = eval(func)
    x += 2*sigma
    eval_sigma_plus = eval(func)
    if abs( eval_sigma_minus - eval_x_0 ) < eps and abs( eval_sigma_plus - eval_x_0 ) < eps:
        print('CONTINUOUS')
    else:
        print('DISCONTINUOUS')
    

if __name__ == '__main__':
    main()
