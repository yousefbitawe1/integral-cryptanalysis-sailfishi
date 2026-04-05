# Enhancing Security of the Lightweight Block Cipher SAILFISH-I Against Integral Cryptanalysis Using Extra Key Whitening

## Project Information
This repository contains the practical part of our Cryptography and Computer Security course project at An-Najah National University.

**Students:**
- Ameed Fattouh
- Yousef Bitawi

**Supervisor:**
- Dr. Jihad Hammamreh

## Project Idea
This project studies integral cryptanalysis, including the Square Attack, in the context of lightweight block ciphers. It focuses on SAILFISH-I as a case study and proposes an extra key-whitening mechanism to reduce the effectiveness of balanced property exploitation.

## Project Goal
The goal is to compare:
1. The original reduced-round cipher model
2. A modified version with extra key whitening

The experiment checks whether the proposed protection reduces balanced output behavior used in integral cryptanalysis.

## Repository Structure
- `main.py` : runs the experiment
- `original_cipher.py` : original cipher model
- `modified_cipher.py` : modified cipher with extra whitening
- `experiment.py` : plaintext generation and evaluation logic
- `utils.py` : helper functions
- `results/` : experiment notes and outputs
- `report/` : report file

## How to Run
Use Python 3 and run:

```bash
python main.py