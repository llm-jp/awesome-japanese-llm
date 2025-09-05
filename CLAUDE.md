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

### Model Table Guidelines
When adding new models to the documentation:

#### Model Classification
- **汎用 (General)**: Models designed for general-purpose language tasks
- **ドメイン特化型 (Domain-specific)**: Models specialized for specific domains (医療/medical, 薬学/pharmacy, 金融/finance, コーディング/coding, etc.)
- Determine classification based on the model's primary training focus and intended use case
- **Important**: Different specialized domains should be treated as separate categories (e.g., 薬学/pharmacy and 医療/medical are distinct domains)

#### Table Ordering
- Models within each section should be ordered by parameter size (largest to smallest)
- For models with the same parameter size, maintain alphabetical order by model name
- Always verify the correct insertion position when adding new entries

#### License Format Standards
- Use consistent capitalization: "Llama 2 Community License", "Llama 3 Community License", "Llama 3.1 Community License"
- Avoid all-caps formats like "META LLAMA 3.1 COMMUNITY LICENSE"
- Match the license format used by similar models in the same table

### Visualization Updates (Deprecated as of 2025)
- The parameter size visualization charts are no longer maintained
- CSV files and Python scripts remain for historical reference but should not be updated
- Focus development efforts on maintaining the model tables in the documentation

### Translation Consistency
- Maintain content parity across all language versions
- Update figure references to use correct language-specific images
- Verify that all model entries are consistently represented

### Dataset/Benchmark Addition Guidelines
When adding new datasets or benchmarks to the documentation:

#### Information Verification
- Always verify dataset details against official sources (Hugging Face, research papers, project websites)
- Cross-check technical specifications like supported languages, data formats, and evaluation metrics
- When research papers are in PDF format and cannot be parsed effectively, rely primarily on official dataset pages (e.g., Hugging Face) for accurate information

#### Developer Attribution Standards
- Use consistent organization naming across all language versions
- Follow existing patterns in the documentation:
  - Universities: Use format like "東北大 自然言語処理研究グループ" rather than just "東北大学"
  - Research labs: Include full lab names when they exist in the documentation
  - Companies: Use official company names as they appear in other entries
- **Language-specific company names**: In Japanese README, use Japanese company names (e.g., "カラクリ" for KARAKURI Inc.), while maintaining original English names in English and French versions

#### Dataset Classification
- Place datasets in appropriate benchmark sections based on their primary evaluation purpose
- Code generation datasets belong in "論理推論能力を測定するベンチマーク/データセット" section
- Verify dataset capabilities and limitations before categorization

#### Multilingual Updates
- When adding entries to the Japanese README, immediately update English and French versions
- Maintain consistent formatting and information across all three language versions
- Ensure translations are accurate and culturally appropriate for each language
- **Critical**: Models must be placed in the exact same position/order across all three language versions (Japanese, English, French)
- Domain names should be consistently translated: 薬学→Pharmacy→Pharmacie, 医療→Medicine→Médecine, etc.

### Model Addition Best Practices
When adding new models to the documentation:

#### Pre-Addition Checklist
1. **Verify model information** from official sources (Hugging Face, research papers, official announcements)
   - **Always check HuggingFace config.json** for accurate technical specifications:
     - Parameter count (may differ from model name, e.g., "2B" model might be 2.45B)
     - Context length (`max_position_embeddings` field)
     - Architecture details
2. **Identify correct model training type and section**:
   - **継続事前学習 (Continual Pre-training)**: Models that undergo additional pre-training on domain-specific data
   - **Instruction Tuning のみ (Instruction Tuning Only)**: Models fine-tuned on instruction/chat data without additional pre-training
   - **Critical distinction**: Fine-tuned domain-specific models belong in "Instruction Tuning → ドメイン特化型", NOT "継続事前学習 → ドメイン特化型"
3. **Identify correct domain classification** - don't assume similar domains are the same (薬学 ≠ 医療)
   - **New model types**: If the model doesn't fit existing categories (e.g., music-language models vs speech-language models), create new sections following the established hierarchy
4. **Check existing model formats** in the target section for:
   - Architecture naming conventions (e.g., "BERT (base, large)" vs "BERT (large)")
   - License format standards
   - HuggingFace availability symbols (◯, △, ？)
5. **Determine insertion position** based on parameter size and domain grouping
   - **Critical**: Use exact parameter counts from config.json, not model names
   - Follow strict descending order by parameter size within each domain
5. **Plan multilingual updates** - prepare translations for all three versions
6. **Check for related research papers** - if the model is based on research, add the original paper to `parts/references_model.md` in chronological order
7. **Verify training details** - distinguish between technical blog posts that explain general methods vs. specific model training details

#### Architecture Format Standards
- Multiple sizes: Use format like "BERT (base, large)" to indicate both variants exist
- Single size: Use format like "BERT (base)" for single variant
- Follow existing patterns in the same table section
- Check other models in the same domain for consistency

#### Domain Grouping Rules
- Models should be grouped by domain first, then ordered by parameter size within each domain
- Specialized domains (薬学, 医療, 金融, etc.) are separate categories
- When adding to a new domain, place it in logical order relative to existing domains

#### Research Paper References
- When adding models based on research papers, always add the original paper to `parts/references_model.md`
- Papers should be ordered chronologically by submission/publication date
- Include venue information (conference/journal) if published, or "-" if arXiv-only
- Verify publication venue and dates from authoritative sources (not just arXiv)

#### Technical Information Verification
- **Parameter counts**: Always use exact values from HuggingFace config.json, not marketing names
- **Context length**: Check `max_position_embeddings` in config.json, not assumptions
- **Training details**: Only include information explicitly stated in official sources
  - If technical blog posts discuss general methods but not specific model details, mark as "訓練詳細不明"
  - Distinguish between method explanations and actual model training procedures
- **Company information**: Verify current company names and any recent mergers/acquisitions
- **Architecture types**: Use exact architecture names from model documentation

## Contributing Notes

The project follows guidelines in CONTRIBUTING.md:
- Focus on models with parameters ≥110M (BERT base size)
- Exclude task-specific fine-tuned models
- Include datasets/benchmarks used by major LLM developers
- Encourage translations into additional languages