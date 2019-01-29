import numpy as np


# Write your angular_dist function here.
def angular_dist(ra1, dec1, ra2, dec2):
    ra1_rad, dec1_rad, ra2_rad, dec2_rad = np.radians(ra1), np.radians(dec1), np.radians(ra2), np.radians(dec2)

    a = np.sin(np.abs(dec1_rad - dec2_rad) / 2) ** 2
    b = np.cos(dec1_rad) * np.cos(dec2_rad) * np.sin(np.abs(ra1_rad - ra2_rad) / 2) ** 2
    d = 2 * np.arcsin(np.sqrt(a + b))
    return np.degrees(d)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your function with the first example in the question.
    print(angular_dist(21.07, 0.1, 21.15, 8.2))

    # Run your function with the second example in the question
    print(angular_dist(10.3, -3, 24.3, -29))
