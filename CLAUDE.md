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
- **Critical**: Always verify the correct insertion position when adding new entries
  - **Before adding a model, read several lines around the intended position** to confirm the parameter size ordering
  - **Example mistake to avoid**: Placing a 6.5B model after an 8B model but before 7B models
  - **Correct approach**: Place 6.5B model after all 7B/6.8B models and before 4B models
  - Use exact parameter counts (e.g., 6.5B, 6.8B, 7B) to determine the precise position, not just the integer part

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
- **Web content retrieval**: When WebFetch fails to retrieve complete article content, ask the user for key information or manually verify details from reliable sources before making updates

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
- **Evaluation system updates**: When updating benchmark/leaderboard information, verify that the evaluation methodology or categories have changed before copying descriptions from previous versions
- **Consistency verification after corrections**:
  - If you correct information in the Japanese README (e.g., release year), **immediately verify** that the same correction is applied to English and French versions
  - **Do NOT** carry over incorrect information from draft versions when finalizing multilingual updates
  - Double-check numerical values (years, parameter counts, token counts) are identical across all three language versions

### Model Addition Best Practices
When adding new models to the documentation:

#### Pre-Addition Checklist
1. **Verify model information** from official sources (Hugging Face, research papers, official announcements)
   - **Always check HuggingFace config.json AND README.md** for accurate technical specifications:
     - Parameter count (may differ from model name, e.g., "2B" model might be 2.45B)
     - Context length (`max_position_embeddings` field)
     - Architecture details
     - Training methodology (check README for technical details like "Precise-tuning", "Pinpoint Tuning", etc.)
2. **Identify correct model training type and section**:
   - **継続事前学習 (Continual Pre-training)**: Models that undergo additional pre-training on domain-specific data
   - **事後学習のみ (Instruction Tuning / Post-training Only)**: Models fine-tuned on instruction/chat data without additional pre-training
   - **Critical distinction**: Fine-tuned domain-specific models belong in "事後学習のみ → ドメイン特化型", NOT "継続事前学習 → ドメイン特化型"
   - **Key indicators for classification**:
     - **Base model name contains "-Instruct" or "-Chat"**: Usually indicates post-training only (e.g., Qwen2.5-32B-Instruct → post-training)
     - **Base model is a pre-trained model (no -Instruct suffix)**: More likely continual pre-training (e.g., Qwen2.5-32B → may involve continual pre-training)
     - **HuggingFace README mentions "Instruction Tuning", "SFT", "DPO", "Fine-tuning" only**: Post-training only
     - **HuggingFace README mentions "Pre-training", "Continual pre-training", "Additional pre-training"**: Continual pre-training
     - **Technical approaches like "Precise-tuning", "Pinpoint Tuning", "PEFT", "LoRA"**: Usually post-training methods
   - **When in doubt**: Check the HuggingFace README technical details section first, then verify against press releases
3. **Identify correct domain classification** - don't assume similar domains are the same (薬学 ≠ 医療)
   - **New model types**: If the model doesn't fit existing categories (e.g., music-language models vs speech-language models), create new sections following the established hierarchy
4. **Check existing model formats** in the target section for:
   - Architecture naming conventions (e.g., "BERT (base, large)" vs "BERT (large)")
   - License format standards
   - HuggingFace availability symbols (◯, △, ？)
5. **Determine insertion position** based on parameter size and domain grouping
   - **Critical**: Use exact parameter counts from config.json, not model names
   - Follow strict descending order by parameter size within each domain
   - **IMPORTANT: Parameter size takes absolute priority over model family similarity**
     - Even if two models share the same family name (e.g., Sarashina2-Vision 14B and Sarashina2.2-Vision-3B), they should be placed far apart if parameter sizes differ significantly
     - Do NOT place models next to each other just because they have similar names
   - **Before determining position, survey the entire section's parameter size range**:
     1. Read through the entire target section (汎用/General, ドメイン特化型/Domain-specific, etc.)
     2. Identify the largest and smallest parameter sizes in that section
     3. Identify all models with similar parameter sizes (within ±2B range)
     4. Only then determine the exact insertion position
   - **For models with multiple size variants** (e.g., Asagi: 2B, 4B, 8B, 14B):
     - Use the MAXIMUM parameter size for ordering purposes (Asagi is treated as 14B)
   - **Verification step**: After determining position, read 5-10 lines before AND after to confirm correct ordering
6. **Plan multilingual updates** - prepare translations for all three versions
7. **Check for related research papers** - if the model is based on research, add the original paper to `parts/references_model.md` in chronological order
8. **Verify training details** - distinguish between technical blog posts that explain general methods vs. specific model training details

#### Architecture Format Standards
- **Architecture column content**: Record the base model architecture (e.g., "Llama", "GPT", "Gemma-based architecture")
  - **Do NOT record attention mechanism details** (e.g., "Hybrid Attention", "Sliding Window Attention") as these are implementation details, not architectures
  - Example: For a model using Gemma architecture with hybrid attention, write "Gemma ベースのアーキテクチャ", NOT "Hybrid Attention"
- **Single row for multiple sizes**: When a model family has multiple parameter sizes (e.g., 2B, 8B, 31B), combine them into a single table row
  - Example format: `([**2b**-base](url1), [**8b**-base](url2), [**31b**-base](url3))`
  - **Do NOT create separate rows** for each size variant
  - Observe existing models (LLM-jp-3, Sarashina2, etc.) to confirm the single-row pattern
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
- **Release year verification**:
  - **Critical**: Do NOT confuse blog publication date with model release year
  - Carefully read official announcements to determine the actual release year
  - Example: A blog published in November 2024 may announce a model released in 2025
  - When in doubt, look for explicit statements like "リリース予定は2025年" or check the model's official release timeline
- **Training details**: Only include information explicitly stated in official sources
  - If technical blog posts discuss general methods but not specific model details, mark as "訓練詳細不明"
  - Distinguish between method explanations and actual model training procedures
  - **Critical**: Distinguish between training data and evaluation benchmarks
    - Evaluation benchmarks (e.g., JDocQA, JGLUE) should NOT be listed as training data
    - Only include datasets explicitly mentioned as used for training/fine-tuning
- **Company information**: Verify current company names and any recent mergers/acquisitions
- **License information**: Always verify the exact, official license name
  - **Critical**: Do NOT guess or abbreviate license names - use the full official name
  - Common mistakes to avoid:
    - Writing "LFM License" when it should be "LFM Open License v1.0"
    - Writing "Llama License" when it should be "Llama 3.1 Community License"
  - Verification sources (in order of priority):
    1. HuggingFace model card's license field
    2. Official model announcement/blog post
    3. LICENSE file in the model repository
  - **For uncommon licenses**: Always look up the full official name
    - Example: HuggingFace API returns "lfm1.0" but the official name is "LFM Open License v1.0"
  - **License format standards**: Match existing patterns in the documentation
    - Use consistent capitalization: "Llama 3 Community License" not "LLAMA 3 COMMUNITY LICENSE"
    - Include version numbers when they exist: "Llama 3.1 Community License" not just "Llama License"
- **Architecture types**: Use exact architecture names from model documentation
  - **Critical**: Do NOT rely solely on config.json `model_type` field for architecture names
    - Example: Qwen2.5 models have `model_type: "qwen2"` in config.json, but should be documented as "Qwen2.5"
    - Always cross-reference with HuggingFace README, model name, and official documentation
  - Read the full blog post/documentation to find architecture references
  - Look for statements like "similar to X model's architecture" or "based on X architecture"
- **Base model identification for derived models**:
  - **For models derived from fine-tuned models**: The "base model" column should list the **original architecture base**, not intermediate fine-tuned models
    - Example: TinyDeepSeek-JP-1.5B is based on Qwen2.5 architecture and trained starting from TinySwallow-1.5B-Instruct (which itself is Qwen2.5-based)
    - Document as: Base = "Qwen2.5", Training details = "TAID distillation on TinySwallow-1.5B-Instruct with ..."
    - This approach makes it clear what the foundational architecture is while showing the actual training starting point
  - **For fine-tuned models derived directly from base models**: Use the base architecture
    - Example: A model fine-tuned directly from "Llama-3.1-8B-Instruct" should list "Llama 3.1" as base
  - Check HuggingFace README for explicit statements about the model architecture and training starting point
  - **Key principle**: Record the foundational architecture in the base model column, and specify the training starting point (if different) in the training details
- **Model placement based on training starting point**:
  - **Critical**: Before adding a model, identify where its training starting point model is located in the documentation
  - New models should be placed in the **same section** as their training starting point (継続事前学習, 事後学習のみ, etc.)
  - Example: If adding a model trained from "TinySwallow-1.5B-Instruct", first grep for TinySwallow to find it's in the 継続事前学習 section, then add the new model in that same section
  - This maintains logical grouping and helps users understand model lineage
  - **Note**: The "base model" column will show the foundational architecture (e.g., Qwen2.5), but section placement follows the training starting point
  - **Verification step**: After determining the section, search for the training starting point model name to confirm its location before adding the new entry

### Vision-Language Model (VLM) Addition Guidelines
When adding new vision-language models to the documentation:

#### VLM Classification
The documentation has three main VLM sections:
1. **スクラッチ学習モデル (Models built from scratch)**: Models trained from scratch or combining components to create a new VLM
   - **汎用 (General purpose)**: VLMs for general multimodal tasks
   - **ドメイン特化型 (Domain-specific)**: VLMs specialized for specific domains
2. **海外モデルに日本語で追加学習を行ったモデル (Foreign models with additional Japanese training)**: Existing foreign VLMs that received additional training on Japanese data
3. **複数のVLM・LLMをマージして作成されたモデル (Models created by merging multiple VLMs/LLMs)**: Models created through model merging techniques

#### Classification Rules
- **スクラッチ学習**: Use this section when:
  - Building a new VLM by combining a Japanese LLM with a vision encoder (even if both components are pre-existing)
  - Example: Combining Llama-3.1-Swallow-70B-Instruct-v0.3 (Japanese LLM) + Qwen2-VL-7B-Instruct (vision encoder) to create a new VLM
- **海外モデルに追加学習**: Use this section when:
  - Taking an existing complete foreign VLM (like InternVL2-26B) and adding Japanese training to it
  - The base model was already a functioning VLM before Japanese training
- **マージ**: Use this section when:
  - Using evolutionary algorithms or other merging techniques to combine multiple existing VLMs/LLMs

#### VLM Training Data Specification
- Clearly separate training data from evaluation benchmarks in the documentation
- Common training data types for VLMs:
  - Image-text pairs datasets
  - Synthetic visual data (charts, graphs, diagrams)
  - Real-world annotated data
  - Multi-stage training: alignment, pre-training, instruction tuning
- Evaluation benchmarks (e.g., JDocQA, Japanese Visual Genome VQA) should NOT be listed as training data unless explicitly used for training

#### VLM Parameter Size Ordering
- **VLMs follow the same strict parameter size ordering as LLMs** (descending order)
- **Model family similarity does NOT override parameter size ordering**
  - Example: Sarashina2-Vision (14B) and Sarashina2.2-Vision-3B (3.8B) should be placed far apart based on their parameter sizes
  - Do NOT place VLMs next to each other just because they share a family name
- **Before adding a VLM, survey the entire汎用/General or ドメイン特化型/Domain-specific section**:
  1. Identify all existing VLMs and their parameter sizes
  2. Determine where the new VLM fits in the descending order
  3. Verify the position by checking several models before and after
- **For VLMs with multiple size variants**, use the maximum parameter size for ordering

## Contributing Notes

The project follows guidelines in CONTRIBUTING.md:
- Focus on models with parameters ≥110M (BERT base size)
- Exclude task-specific fine-tuned models
- Include datasets/benchmarks used by major LLM developers
- Encourage translations into additional languages