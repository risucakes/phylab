def convert_values(speed, designed_length, n, m, base_speed=160):
    ratio = speed / base_speed
    converted_length = designed_length / ratio
    converted_ratio = n / converted_length
    converted_m = m / converted_ratio
    
    return converted_length, converted_ratio, converted_m

speed = float(input("Enter speed: "))
designed_length = float(input("Enter designed length (mm): "))
n = float(input("Enter n: "))
m = float(input("Enter m: "))

converted_length, converted_ratio, converted_m = convert_values(speed, designed_length, n, m)

print(f"Converted Ratio: {converted_ratio:.4f}")
print(f"\nConverted Length: {converted_length:.2f} mm")
print(f"Converted m: {converted_m:.2f}")