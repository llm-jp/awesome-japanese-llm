import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote'
import { generateLlmsTxt, GITHUB_ONLY_BLOCK } from './llms'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "LLM-jp",
  description: "Overview of Japanese LLMs",
  base: '/awesome-japanese-llm/',
  head: [
    ["meta", { property: "og:image", content: "https://llm-jp.github.io/assets/images/logo2.png" }],
    ["meta", { property: "og:title", content: "日本語LLMまとめ" }],
    ["meta", { property: "twitter:card", content: "summary" }],
    ["meta", { property: "twitter:title", content: "日本語LLMまとめ" }],
    ["meta", { property: "twitter:site", content: "@llm_jp" }],
    ["link", { rel: "icon", href: "/awesome-japanese-llm/favicon.ico" }],
  ],
  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/llm-jp/awesome-japanese-llm' }
    ],

    search: {
      provider: 'local'
    },

    logo: 'https://llm-jp.github.io/assets/images/logo2.png',

    outline: {
      level: 'deep',
    },

    footer: {
      copyright: "Copyright (c) 2023-present LLM-jp, Licensed under the Apache License, Version 2.0."
    }
  },
  rewrites: {
    'README.md': 'index.md',
    'en/README.md': 'en/index.md',
    'fr/README.md': 'fr/index.md',
  },
  markdown: {
    toc: {
      level: [2, 3, 4, 5, 6],
    },
    config: (md) => {
      md.use(footnote)
    }
  },
  lastUpdated: true,
  vite: {
    plugins: [
      {
        name: 'strip-github-only-blocks',
        enforce: 'pre',
        transform(code: string, id: string): string | undefined {
          // GitHub 閲覧時のみ表示するブロック (<!-- github-only:start/end -->) を Web 版から除去する
          if (id.endsWith('README.md')) {
            return code.replace(GITHUB_ONLY_BLOCK, '')
          }
        },
      },
    ],
  },
  buildEnd(siteConfig) {
    generateLlmsTxt(siteConfig)
  },
  locales: {
    root: {
      label: '日本語',
      lang: 'ja-JP',
      themeConfig: {
        nav: [
          { text: 'LLM 勉強会', link: 'https://llm-jp.nii.ac.jp/' },
        ],
        outlineTitle: '目次',
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      themeConfig: {
        nav: [
          { text: 'About Us', link: 'https://llm-jp.nii.ac.jp/en/' },
        ]
      },
      link: '/en'
    },
    fr: {
      label: 'Français',
      lang: 'fr-FR',
      themeConfig: {
        nav: [
          { text: 'About Us', link: 'https://llm-jp.nii.ac.jp/en/' },
        ],
        outlineTitle: 'Table des matières',
      },
      link: '/fr/'
    },
  }
})
