# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation project that maintains a comprehensive list of Japanese Large Language Models (LLMs) and their evaluation benchmarks. The project uses VitePress for documentation site generation and includes Python scripts for data visualization.

## Common Commands

### Documentation Development
```bash
# Start development server
npm run docs:dev

# Build documentation site
npm run docs:build

# Preview built documentation
npm run docs:preview
```

### Python Visualization Scripts (Legacy - Not Updated Since 2025)
```bash
# Navigate to scripts directory
cd figures/scripts

# Install Python dependencies (using Poetry)
poetry install

# Generate parameter size overview charts (DEPRECATED)
poetry run python parameter_size_overview_generate.py

# Retrieve data for visualization (DEPRECATED)
poetry run python parameter_size_overview_retrieve.py
```

**Note**: The parameter size visualization charts are no longer being updated as of 2025. This decision reflects the shift in LLM development focus from parameter count increases to improvements in training methods and datasets.

## Project Structure

### Core Documentation Files
- **README.md** - Main Japanese documentation (primary content)
- **en/README.md** - English translation
- **fr/README.md** - French translation
- **parts/references_model.md** - Model reference chronology
- **parts/references_training.md** - Training method references

### Visualization Components
- **figures/scripts/** - Python scripts for generating charts
  - `parameter_size_overview_generate.py` - Main chart generation script
  - `parameter_size_overview_retrieve.py` - Data retrieval automation
  - `parameter_size_overview.csv` - English model data
  - `parameter_size_overview_ja.csv` - Japanese model data
  - `pyproject.toml` - Poetry configuration for Python dependencies

### Generated Assets
- **figures/parameter_size_overview_ja.png** - Japanese version of parameter size chart
- **figures/parameter_size_overview_en.png** - English version of parameter size chart

## Content Structure

The documentation follows a structured format with:
- Model tables organized by categories (full-scratch, continual learning, etc.)
- Columns for release year, architecture, parameters, training data, developer, and licensing
- Multilingual support with consistent content across languages
- Comprehensive model references with links to papers and resources

## Development Guidelines

### Content Updates
- Model information should be verified against official sources
- Parameter counts should include both billion (B) and specific numbers
- Training data information should be as detailed as possible
- License information must be accurate and up-to-date

### Visualization Updates (Deprecated as of 2025)
- The parameter size visualization charts are no longer maintained
- CSV files and Python scripts remain for historical reference but should not be updated
- Focus development efforts on maintaining the model tables in the documentation

### Translation Consistency
- Maintain content parity across all language versions
- Update figure references to use correct language-specific images
- Verify that all model entries are consistently represented

## Contributing Notes

The project follows guidelines in CONTRIBUTING.md:
- Focus on models with parameters ≥110M (BERT base size)
- Exclude task-specific fine-tuned models
- Include datasets/benchmarks used by major LLM developers
- Encourage translations into additional languages