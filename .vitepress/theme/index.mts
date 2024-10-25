import DefaultTheme from 'vitepress/theme';
import { h } from 'vue';

import './index.css';
import {
  NolebaseEnhancedReadabilitiesMenu,
  NolebaseEnhancedReadabilitiesScreenMenu,
} from "@nolebase/vitepress-plugin-enhanced-readabilities/client";
import "@nolebase/vitepress-plugin-enhanced-readabilities/client/style.css";
import type { Options as NolebaseReadOptions } from '@nolebase/vitepress-plugin-enhanced-readabilities/client'
import { InjectionKey as NolebaseReadInjectionKey } from '@nolebase/vitepress-plugin-enhanced-readabilities/client'

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      "nav-screen-content-after": () => h(NolebaseEnhancedReadabilitiesScreenMenu),
      "nav-bar-content-after": () => h(NolebaseEnhancedReadabilitiesMenu),
    });
  },
  enhanceApp({ app }) {
    app.provide(NolebaseReadInjectionKey, {
      layoutSwitch: {
        defaultMode: 3,
      }
    } as NolebaseReadOptions);
  }
};