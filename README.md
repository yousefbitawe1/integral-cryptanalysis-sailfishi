# Integral Cryptanalysis Defense for SAILFISH-I

## Project Overview

This project studies the vulnerability of the lightweight block cipher **SAILFISH-I** against **Integral Cryptanalysis**, specifically attacks that exploit the **Balanced Property** in structured plaintext sets.

The project proposes a lightweight defense mechanism using **Extra Key Whitening** to disturb balanced propagation and reduce the effectiveness of integral distinguishers.

A reduced-round Python-based simulation was implemented to compare the behavior of:
- The original version
- The modified version with extra key whitening

The experimental results show that the modified version loses the balanced property earlier, which improves resistance against integral-analysis-based attacks.

---

# Objectives

- Study Integral Cryptanalysis on lightweight block ciphers
- Understand the Balanced Property used in Square-style attacks
- Analyze reduced-round behavior of a SAILFISH-I inspired model
- Propose a lightweight defense using Extra Key Whitening
- Compare the original and modified versions experimentally

---

# Project Components

## 1. Project Report

The report contains:
- Introduction
- Literature Review
- Problem Statement
- Proposed Contribution
- Experimental Methodology
- Results and Discussion
- Conclusion and Future Work

File included:
```text
report.docx
```

---

## 2. Presentation Slides

The presentation summarizes:
- Lightweight Cryptography
- Integral Cryptanalysis
- SAILFISH-I
- Proposed Defense Mechanism
- Experimental Methodology
- Results and Conclusions

File included:
```text
presentation.pptx
```

---

## 3. Python Simulation

A reduced-round illustrative simulation implemented in Python to:
- Generate structured plaintext sets
- Analyze balanced output behavior
- Compare original vs modified versions
- Evaluate the effect of extra key whitening

File included:
```text
simulation.py
```

---

# Technologies Used

- Python
- Microsoft Word
- Microsoft PowerPoint
- GitHub

---

# Experimental Methodology

The experiment generates structured plaintext sets where selected values vary systematically while the remaining values stay constant.

The simulation then:
1. Encrypts the plaintexts using the original model
2. Encrypts them again using the modified model
3. Computes XOR-based balanced behavior
4. Compares the propagation of balanced properties across rounds

The modified version applies an additional XOR-based key-whitening layer to disturb structured propagation.

---

# Key Concept: Integral Cryptanalysis

Integral Cryptanalysis is a cryptanalytic technique that analyzes sets of structured plaintexts instead of single plaintext-ciphertext pairs.

Some plaintext values vary through all possible values while the remaining values stay constant. The attacker then tracks how these structured sets propagate through encryption rounds to detect balanced behavior.

One important property is the **Balanced Property**, where the XOR sum of outputs equals zero.

---

# Key Concept: Key Whitening

Key Whitening is an additional XOR operation with key material added before, after, or between encryption rounds to increase confusion and reduce exploitable patterns.

In this project, extra key whitening is used to reduce the effectiveness of Integral Cryptanalysis by disturbing balanced propagation.

---

# Results Summary

The experimental comparison showed that:
- The original version preserves balanced behavior for more rounds
- The modified version disrupts the balanced property earlier
- Integral distinguishers become weaker after applying extra key whitening
- Security resistance is improved while preserving lightweight design principles

---

# Important Note

This project uses a reduced-round illustrative simulation inspired by the structure and security objectives of lightweight block ciphers. It is intended as an academic proof-of-concept experiment rather than a full official implementation of the complete SAILFISH-I cipher.

---

# Repository Contents

```text
report.docx
presentation.pptx
simulation.py
README.md
```

---

# Authors

- Yousef Bitawi

An-Najah National University
