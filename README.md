GM Counter Characteristics & Counting Statistics Analysis

Geiger–Müller Tube Plateau Curve, Poisson vs Gaussian Fitting, and Chi-Square Hypothesis Testing

📌 Overview

This project analyzes the behavior of a Geiger–Müller (GM) radiation detector through:

GM plateau curve measurement

Operating voltage selection

Counting statistics at 5 s, 10 s, and 20 s

Fitting data to Poisson and Gaussian distributions

Performing chi-square goodness-of-fit tests

Computing right-tail probabilities (p-values)

Visualizing distributions with error bars and theoretical curves

This project demonstrates experimental data analysis, statistical modeling, and scientific Python skills.

⚡ GM Plateau Curve

This plot shows the count rate vs applied voltage for the GM tube.

Figure 1 — GM Plateau Curve:
The plateau region is observed between approximately 480–580 V, where the count rate remains nearly constant. A linear fit gives a small negative slope, indicating stable operation. The operating voltage for all counting measurements was chosen near 540 V.

📊 Counting Statistics Analysis
5-Second Interval

Figure 2 — 5-Second Counting Statistics:
The measured distribution matches the Poisson model extremely well.

Mean = 1.62

Chi-square (Poisson) = 2.72

Right-tail p ≈ 0.84 (excellent fit)
Gaussian approximation is not used due to low mean.

10-Second Interval

Figure 3 — 10-Second Counting Statistics:
The Poisson curve fits the measured distribution better than the Gaussian curve.

Mean = 3.505

Chi-square (Poisson) = 7.44 (p ≈ 0.59)

Chi-square (Gaussian) = 15.69 (p ≈ 0.07)

Poisson still strongly preferred.

20-Second Interval

Figure 4 — 20-Second Counting Statistics:
Even at higher mean counts, Poisson matches better than Gaussian.

Mean = 6.419

Chi-square (Poisson) = 21.23 (p ≈ 0.129)

Chi-square (Gaussian) = 44.44 (p ≈ 9.35×10⁻⁵) → rejected

Poisson model remains valid; Gaussian approximation fails due to insufficiently large mean.

📐 Chi-Square Results Summary
Interval	Mean	χ² (Poisson)	p-value (Poisson)	χ² (Gaussian)	p-value (Gaussian)	Best Fit
5 sec	1.62	2.72	0.8429	—	—	Poisson
10 sec	3.505	7.44	0.5916	15.69	0.0737	Poisson
20 sec	6.419	21.23	0.1294	44.44	9.35×10⁻⁵	Poisson
🧪 Conclusion

GM tube counting behaves as expected: Poisson distribution fits all intervals well.

Gaussian approximation fails, especially for low and moderate mean values.

Plateau region carefully identified at 480–580 V, with 540 V selected as stable operating voltage.

Statistical testing confirms the fundamental properties of radioactive decay (independent random events).
