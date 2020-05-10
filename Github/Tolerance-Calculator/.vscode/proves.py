def tolerancies(quality):

    if uservalue_quality == "coarse":
        x = uservalue*coarsev*cavityFactor
        return("toleance range is:", x)
    elif uservalue_quality == 'medium':
        x = uservalue*mediumv*cavityFactor
        return("toleance range is:", x)

    elif uservalue_quality == 'high':
        x = uservalue*highv*cavityFactor
        return("toleance range is:", x)
    else:
        return("not entered value")
        coarse.quality = coarse
        medium.quality = medium
        high.quality = high
        coarse = 0.007
        medium = 0.006
        high = 0.003


return(tolerancies(uservalue_quality=input("Enter the quality level : coarse ,medium , high ")
