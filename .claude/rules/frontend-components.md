---
paths:
  - ".vitepress/**"
---

# Frontend Component Guidelines

## Implement in TypeScript

- New components and theme logic under `.vitepress/` **must be implemented in TypeScript**, not plain JavaScript.
  - Prefer a standalone `.ts` file using `defineComponent` + the `h()` render function over a `.vue` SFC.
  - If a `.vue` SFC is genuinely necessary (e.g. heavy template/scoped-style needs), its script block must use `<script setup lang="ts">`.
- When converting a `.vue` SFC to a `.ts` file, move `<style scoped>` into a sibling `.css` file and import it from `.vitepress/theme/index.mts`. Because the scope is lost, **rename generic transition/animation class names** (e.g. `fade` → a component-specific prefix like `btt-fade`) to avoid clashing with VitePress default-theme styles.
- Annotate function signatures with return types (e.g. `(): void`).
- After changes, verify with `yarn docs:build`.
