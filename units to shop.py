def mim_and_average():
    units = [1, 2, 5, 10, 20, 50]
    mxm = 99
    mim = [float('inf')] * (mxm + 1)
    mim[0] = 0
    
    for value in range(1, mxm + 1):
        for unit in units:
            if unit <= value:
                mim[value] = min(mim[value], mim[value - unit] + 1)
    
    total_units_used = sum(mim[1:])
    average_units_used = total_units_used / mxm
    
    return mim[1:], average_units_used

mim, average_units_used = mim_and_average()

for value in range(1, 100):
    print(f"{value}: {mim[value-1]} units used")

print(f"Average number of units used: {average_units_used:.2f}")
