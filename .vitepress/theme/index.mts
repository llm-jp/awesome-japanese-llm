import DefaultTheme from 'vitepress/theme'
import BackToTop from './BackToTop'
import { h } from 'vue'
import './custom.css'
import './back-to-top.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(BackToTop),
    })
  },
}
