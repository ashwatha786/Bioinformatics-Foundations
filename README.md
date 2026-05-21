
# Bioinformatics Foundations: DNA Data Analysis 🧬

Welcome to my portfolio tracking the intersection of **Computer Science** and **Biological Data**. This repository contains production-ready Python scripts designed to process, translate, and visualize genetic sequences.

---

## 🔬 Project 1: Automated Genetic Code Translator (`dna_translator.py`)
This script automates the core biological process of transcription and translation. It accepts a raw DNA sequence, transcribes it into mRNA, and maps 3-letter codons against a complete dictionary of all **64 standard genetic combinations** to output a precise 1-letter amino acid protein chain.

### Core Features:
* Handles full real-world translation incorporating all 20 standard amino acids.
* Utilizes string manipulation for clean sequence transitions.
* Implements loop-based string slicing to read exact 3-base codon frames.

---

## 📊 Project 2: Nucleotide Frequency Visualizer (`bio_visualizer.py`)
Data is only as good as its presentation. This project uses the industry-standard **Matplotlib** engineering library to map out nucleotide distributions. 

By calculating the exact frequency of Adenine, Thymine, Cytosine, and Guanine bases, this tool helps visualize the structural characteristics (such as GC-content) of specific genetic sequences.

### Core Features:
* Generates an automated desktop-rendered categorical bar chart.
* Maps distinct, customized hexadecimal color codes to each nucleotide base.
* Implements visual formatting aids like translucent gridlines (`alpha=0.7`) for rapid data reading.

---

## 🛠️ Environment & Tools
* **Language:** Python 3
* **Primary Libraries:** Matplotlib (Visual Engine)
* **Package Manager:** Pip
