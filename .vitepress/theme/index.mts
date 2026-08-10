import DefaultTheme from 'vitepress/theme'
import BackToTop from './BackToTop'
import YearFilter from './YearFilter'
import { h } from 'vue'
import './custom.css'
import './back-to-top.css'
import './year-filter.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => [h(YearFilter), h(BackToTop)],
    })
  },
}
