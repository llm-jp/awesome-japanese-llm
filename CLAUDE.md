# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a documentation project that maintains a comprehensive list of Japanese Large Language Models (LLMs) and their evaluation benchmarks. The project uses VitePress for documentation site generation.

## Common Commands

```bash
yarn docs:dev      # Start development server
yarn docs:build    # Build documentation site
yarn docs:preview  # Preview built documentation
```

## Project Structure

- **README.md** - Main Japanese documentation (primary content)
- **en/README.md** - English translation
- **fr/README.md** - French translation
- **parts/references_model.md** - Model reference chronology
- **parts/references_training.md** - Training method references

## Editing Rules

Editing rules for README files are defined in `.claude/rules/` as conditional rules that activate when working with the relevant files.
