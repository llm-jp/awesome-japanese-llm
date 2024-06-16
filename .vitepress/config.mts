import { defineConfig } from 'vitepress'
import footnote from 'markdown-it-footnote'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "LLM-jp",
  description: "Overview of Japanese LLMs",
  base: '/awesome-japanese-llm/',
  themeConfig: {
    socialLinks: [
      { icon: 'github', link: 'https://github.com/llm-jp/awesome-japanese-llm' }
    ],

    search: {
      provider: 'local'
    },

    logo: 'https://llm-jp.nii.ac.jp/assets/images/logo2.png',

    outline: {
      level: [2, 4],
    }
  },
  rewrites: {
    'README.md': 'index.md',
    'en/README.md': 'en/index.md',
    'fr/README.md': 'fr/index.md',
  },
  markdown: {
    config: (md) => {
      md.use(footnote)
    }
  },
  lastUpdated: true,
  locales: {
    root: {
      label: '日本語',
      lang: 'ja-JP',
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en'
    },
    fr: {
      label: 'Français',
      lang: 'fr-FR',
      link: '/fr/'
    },
  }
})
