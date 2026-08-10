import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { resolve, dirname } from 'node:path'
import type { SiteConfig } from 'vitepress'

const SITE_URL = 'https://llm-jp.github.io/awesome-japanese-llm'

const SOURCES = [
  { src: 'README.md', out: 'llms-full.txt' },
  { src: 'en/README.md', out: 'en/llms-full.txt' },
  { src: 'fr/README.md', out: 'fr/llms-full.txt' },
] as const

const INDEX = `# 日本語LLMまとめ (Overview of Japanese LLMs)

> 一般公開されている日本語LLM（日本語を中心に学習された大規模言語モデル）および日本語LLM評価ベンチマークの情報を、有志が継続的に収集・更新しているまとめ。モデルごとにアーキテクチャ、パラメータ数、学習データ、開発元、ライセンスを表形式で整理している。

- GitHub リポジトリ: https://github.com/llm-jp/awesome-japanese-llm
- This overview of Japanese LLMs is also available in English and French.

## 全文 (Full content)

- [日本語版 全文](${SITE_URL}/llms-full.txt): 日本語LLM・評価ベンチマーク一覧の全文（日本語）
- [English full text](${SITE_URL}/en/llms-full.txt): Full overview of Japanese LLMs and benchmarks (English)
- [Texte intégral en français](${SITE_URL}/fr/llms-full.txt): Aperçu complet des LLM japonais (français)

## Web 版 (Web pages)

- [日本語版](${SITE_URL}/)
- [English version](${SITE_URL}/en/)
- [Version française](${SITE_URL}/fr/)
`

export const GITHUB_ONLY_BLOCK = /<!-- github-only:start -->[\s\S]*?<!-- github-only:end -->\n?/g

function resolveIncludes(content: string, srcDir: string): string {
  return content.replace(/<!--@include:\s*@\/(.+?)\s*-->/g, (_, path: string) =>
    readFileSync(resolve(srcDir, path), 'utf-8')
  )
}

function cleanForLlms(content: string): string {
  return (
    content
      // Web 版への誘導ブロック（GitHub 閲覧時のみ表示）はプレーンテキストでは不要
      .replace(GITHUB_ONLY_BLOCK, '')
      .replace(/^\[\[toc\]\]\n?/gm, '')
      .replace(/^:::\s*details.*$\n?/gm, '')
      .replace(/^:::\s*\w+\s+(.+)$/gm, '**$1**')
      .replace(/^:::\s*$\n?/gm, '')
      .replace(/<a id="[^"]*"><\/a>\s*/g, '')
      .replace(/\n{3,}/g, '\n\n')
      .trim() + '\n'
  )
}

export function generateLlmsTxt(siteConfig: SiteConfig): void {
  const { srcDir, outDir } = siteConfig
  writeFileSync(resolve(outDir, 'llms.txt'), INDEX)
  for (const { src, out } of SOURCES) {
    const raw = readFileSync(resolve(srcDir, src), 'utf-8')
    const outPath = resolve(outDir, out)
    mkdirSync(dirname(outPath), { recursive: true })
    writeFileSync(outPath, cleanForLlms(resolveIncludes(raw, srcDir)))
  }
}
