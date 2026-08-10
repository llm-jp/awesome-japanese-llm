import { defineComponent, h, ref, onMounted, watch, nextTick } from 'vue'
import { useData, useRoute } from 'vitepress'

const STORAGE_KEY = 'ajl-year-filter'

/** 「公開年」列を見分けるためのヘッダラベル (JA / EN / FR) */
const YEAR_HEADERS = new Set(['公開年', 'release year', 'année de sortie'])

/** 「すべて表示」を表す閾値 */
const ALL = 0

interface Labels {
  legend: string
  all: string
  since: (year: number) => string
  empty: string
}

const LABELS: Record<string, Labels> = {
  'en-US': {
    legend: 'Release year',
    all: 'All',
    since: (year) => `${year} and later`,
    empty: 'No models match this filter.',
  },
  'fr-FR': {
    legend: 'Année de sortie',
    all: 'Toutes',
    since: (year) => `${year} et après`,
    empty: 'Aucun modèle ne correspond à ce filtre.',
  },
  'ja-JP': {
    legend: '公開年',
    all: 'すべて',
    since: (year) => `${year}年以降`,
    empty: '該当するモデルはありません。',
  },
}

interface YearTable {
  el: HTMLTableElement
  rows: { el: HTMLTableRowElement; year: number }[]
  /** 全行が隠れたときにテーブルの代わりに表示する要素 */
  placeholder: HTMLParagraphElement
}

/** 公開年列を持つテーブルを、各行の公開年つきで集める */
function collectTables(emptyMessage: string): YearTable[] {
  const tables: YearTable[] = []

  document.querySelectorAll<HTMLTableElement>('.vp-doc table').forEach((el) => {
    const headers = Array.from(el.querySelectorAll<HTMLTableCellElement>('thead th'))
    const index = headers.findIndex((th) =>
      YEAR_HEADERS.has((th.textContent ?? '').trim().toLowerCase())
    )
    if (index < 0) return

    const rows: YearTable['rows'] = []
    el.querySelectorAll<HTMLTableRowElement>('tbody tr').forEach((tr) => {
      const matched = (tr.cells[index]?.textContent ?? '').match(/\d{4}/)
      if (matched) rows.push({ el: tr, year: Number(matched[0]) })
    })
    if (rows.length === 0) return

    const placeholder = document.createElement('p')
    placeholder.className = 'year-filter-empty'
    placeholder.textContent = emptyMessage
    placeholder.style.display = 'none'
    el.insertAdjacentElement('afterend', placeholder)

    tables.push({ el, rows, placeholder })
  })

  return tables
}

function loadThreshold(): number {
  const stored = Number(localStorage.getItem(STORAGE_KEY))
  return Number.isFinite(stored) && stored > 0 ? stored : ALL
}

export default defineComponent({
  name: 'YearFilter',
  setup() {
    const { lang } = useData()
    const route = useRoute()
    const tables = ref<YearTable[]>([])
    const years = ref<number[]>([])
    const threshold = ref(ALL)

    function labels(): Labels {
      return LABELS[lang.value] ?? LABELS['ja-JP']
    }

    function apply(): void {
      tables.value.forEach(({ el, rows, placeholder }) => {
        let visible = 0
        rows.forEach((row) => {
          const shown = threshold.value === ALL || row.year >= threshold.value
          row.el.style.display = shown ? '' : 'none'
          if (shown) visible += 1
        })
        // 全行が消えるとヘッダだけのテーブルが残るため、代わりに文言を出す
        el.style.display = visible === 0 ? 'none' : ''
        placeholder.style.display = visible === 0 ? '' : 'none'
      })
    }

    function scan(): void {
      tables.value = collectTables(labels().empty)
      years.value = [
        ...new Set(tables.value.flatMap(({ rows }) => rows.map((row) => row.year))),
      ].sort((a, b) => b - a)
      apply()
    }

    function onChange(event: Event): void {
      threshold.value = Number((event.target as HTMLSelectElement).value)
      localStorage.setItem(STORAGE_KEY, String(threshold.value))
      apply()
    }

    onMounted(() => {
      threshold.value = loadThreshold()
      scan()
    })

    // VitePress は SPA 遷移で本文 DOM を差し替えるため、ページごとに集め直す
    watch(
      () => route.path,
      () => nextTick(scan)
    )

    return () => {
      if (years.value.length === 0) return null

      const { legend, all, since } = labels()

      return h('div', { class: 'year-filter' }, [
        h('label', { class: 'year-filter-legend', for: 'year-filter-select' }, legend),
        h(
          'select',
          {
            id: 'year-filter-select',
            class: 'year-filter-select',
            onChange,
          },
          [
            h('option', { value: String(ALL), selected: threshold.value === ALL }, all),
            ...years.value.map((year) =>
              h('option', { value: String(year), selected: threshold.value === year }, since(year))
            ),
          ]
        ),
      ])
    }
  },
})
