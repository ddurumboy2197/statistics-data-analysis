import statistics

def dataset_tahlili(ro'yxat):
    mean = statistics.mean(ro'yxat)
    median = statistics.median(ro'yxat)
    mode = statistics.mode(ro'yxat)
    stdev = statistics.stdev(ro'yxat)
    
    return mean, median, mode, stdev

# Misol uchun ma'lumotlar
ma'lumotlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean, median, mode, stdev = dataset_tahlili(ma'lumotlar)

print(f"O'rtacha: {mean}")
print(f"Ortacha: {median}")
print(f"Moda: {mode}")
print(f"Standart deviasi: {stdev}")
