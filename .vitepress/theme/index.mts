import DefaultTheme from 'vitepress/theme';
import { onMounted } from 'vue';
import mediumZoom from 'medium-zoom';

import './index.css';

export default {
  ...DefaultTheme,
  setup() {
    onMounted(() => {
      mediumZoom('.main img', { background: 'var(--vp-c-bg)' });
    });
  },
};