for denom in range(11, 100):
    for numer in range(10, denom):
        numerLeft = numer // 10
        numerRight = numer % 10
        denomLeft = denom // 10
        denomRight = denom % 10
        lambdaTen = ((numerRight == 0) and (denomRight == 0))
        lambdaEleven = ((numerRight == numerLeft) and (denomRight == denomLeft))
        if not (lambdaTen or lambdaEleven):
            for d in range(2, 10):
                for n in range(1, d):
                    lambdaOne = False
                    lambdaThree = False
                    if denomRight != 0:
                        lambdaOne = ((numerLeft == denomLeft) and (numerRight/denomRight == n/d))
                        lambdaThree = ((numerRight == denomLeft) and (numerLeft/denomRight == n/d))
                    lambdaTwo = ((numerLeft == denomRight) and (numerRight/denomLeft == n/d))
                    lambdaFour = ((numerRight == denomRight) and (numerLeft/denomLeft == n/d))
                    lambdaPrime = ((lambdaOne or lambdaTwo) or (lambdaThree or lambdaFour))
                    if ((lambdaPrime) and (numer/denom == n/d)):
                        print(str(numer)+" "+str(denom))
