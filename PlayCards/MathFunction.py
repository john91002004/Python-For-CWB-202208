def calCombinationAmount(total, chosen): 
    if chosen == 0: 
        return 1
        
    else: 
        if chosen > total/2: 
            chosen = total - chosen 

        numerator = 1 
        for i in range(chosen): 
            numerator *= (total - i) 
        denominator = 1 
        for i in range(chosen): 
            denominator *= (i + 1)
        return numerator / denominator