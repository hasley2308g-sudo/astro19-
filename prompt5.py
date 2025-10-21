import numpy as np

def main():
    
    x_values = np.linspace(0, 2, 1000)
    sin_values = np.sin(x_values)
    
    print(f"{'x':<0} {'sin(x)':<2}")
    print("-" * 20)
    
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x:<0} {sin_x:<2f}")

if __name__ == "__main__":
    main()
