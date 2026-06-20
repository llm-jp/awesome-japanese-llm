import { defineComponent, h, ref, onMounted, onUnmounted, Transition } from 'vue'

export default defineComponent({
  name: 'BackToTop',
  setup() {
    const show = ref(false)

    function onScroll(): void {
      show.value = window.scrollY > 300
    }

    function scrollToTop(): void {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    onMounted(() => window.addEventListener('scroll', onScroll))
    onUnmounted(() => window.removeEventListener('scroll', onScroll))

    return () =>
      h(Transition, { name: 'btt-fade' }, () =>
        show.value
          ? h(
              'button',
              {
                class: 'back-to-top',
                'aria-label': 'ページトップに戻る',
                onClick: scrollToTop,
              },
              '↑'
            )
          : null
      )
  },
})
