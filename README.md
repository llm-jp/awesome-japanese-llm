# 日本語LLMまとめ
[ [**English**](./en/) | [**Français**](./fr/) | 日本語 ]

<p align="center">
  <img src="./figures/parameter_size_overview_ja.png" alt="日本語LLM・海外LLMのパラメータサイズの推移">
</p>
<figcaption style="font-style: italic; font-size: 0.9em; color: #6b7280; text-align: center;">日本語LLM・海外LLMのパラメータ数の推移。日本語モデルの情報は本記事、海外モデルの情報は LifeArchitect.ai の <a href="https://lifearchitect.ai/models-table/" target="_blank" rel="noreferrer">Models table</a> を参照しています（ただし、図のスペース上一部のモデルは省略。また、海外モデルのパラメータ数は推測値を含む）。修正・追加等ありましたらお知らせ下さい。</figcaption>

---

この記事は、一般公開されている日本語LLM（日本語を中心に学習されたLLM）および日本語LLM評価ベンチマークに関する情報をまとめたものです。情報は、有志により収集されており、その一部は論文や公開されているリソースなどから引用しています。

::: warning 以下の点について、あらかじめご理解とご了承をお願いいたします
1. 本記事の内容は、完全性や正確性を保証するものではありません。これらの情報は予告なく変更されることがあり、また最新の情報を常に提供できるとは限りません。
2. 一部の情報は、推測や個々の利用者の解釈にもとづくものである場合があります。そのため、全ての読者にとって必ずしも正確であるとは限りません。
3. 本記事に記載されているモデルの多くは、MIT や Apache-2.0 といったオープンソースライセンスが適用されています。しかしながら、**一部のモデルには、非営利限定のライセンス（例：CC BY-NC-SA 4.0）や開発元特有のライセンスが適応されており、これらは必ずしもオープンソースとは言えない可能性がある**点にご注意ください。
4. 個人が開発したモデルに関する記述では、作成者の敬称は省略させていただいております。
:::

この記事の管理は GitHub で行っています。記事の間違いを発見した場合、あるいはモデルの追加提案を行いたい場合は、[GitHub Issues](https://github.com/llm-jp/awesome-japanese-llm/issues) 経由で報告していただけますと幸いです。

::: details 目次
[[toc]]
:::

<a id="generative"></a>
## テキスト生成に主に使うモデル

*画像を含むテキスト生成モデルは[こちら](#multimodal-text-generation)*

<a id="full-scratch-models"></a>
### フルスクラッチ学習モデル

<a id="generative-scratch-general"></a>
#### 汎用

|    |  アーキテクチャ  |  入出力で扱える<br>トークン数  |  学習テキスト  |  開発元  | ライセンス / 利用規約 |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Sarashina2-8x70B](https://www.sbintuitions.co.jp/news/press/20241108_01/) | MoE<br>([8x70b (**465b**)](https://huggingface.co/sbintuitions/sarashina2-8x70b)) | 8,192 | Sarashina2 (70B) に対して Sparse Upcycling で学習 | SB Intuitions | Sarashina Model NonCommercial License |
| [LLM-jp-3 172B](https://www.nii.ac.jp/news/release/2024/1224.html) | Llama<br>([**172b**](https://huggingface.co/llm-jp/llm-jp-3-172b), [**172b**-instruct2](https://huggingface.co/llm-jp/llm-jp-3-172b-instruct2), [**172b**-instruct3](https://huggingface.co/llm-jp/llm-jp-3-172b-instruct3)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)<br>(計 **2.1T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), [magpie-sft-v1.0](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0), Daring-Anteater, FLAN, ichikara-instruction-format, AutoMultiTurnByCalm3-22B, ramdom-to-fixed-multiturn-Calm3, wizardlm8x22b-logical-math-coding-sft-ja, wizardlm8x22b-logical-math-coding-sft_additional-ja, Synthetic-JP-EN-Coding-Dataset-567k<br>DPO (instruct3 only): [aya-ja-evol-inst](https://huggingface.co/datasets/llm-jp/aya-ja-evol-inst), [ac-self-inst](https://huggingface.co/datasets/llm-jp/ac-self-inst) | 大規模言語モデル研究開発センター | 事前学習済みモデル: LLM-jp-3 172B Terms of Use<br>事後学習済みモデル: llm-jp-3-172b-instruct3利用許諾契約 |
| [LLM-jp-3 172B beta2](https://llmc.nii.ac.jp/topics/llm-jp-3-172b-beta2/) | Llama<br>([**172b**-beta2](https://huggingface.co/llm-jp/llm-jp-3-172b-beta2), [**172b**-beta2-instruct2](https://huggingface.co/llm-jp/llm-jp-3-172b-beta2-instruct2)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)の一部<br>(計 **1.4T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), [magpie-sft-v1.0](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0), Daring-Anteater, FLAN, ichikara-instruction-format, AutoMultiTurnByCalm3-22B, ramdom-to-fixed-multiturn-Calm3, wizardlm8x22b-logical-math-coding-sft-ja, wizardlm8x22b-logical-math-coding-sft_additional-ja, Synthetic-JP-EN-Coding-Dataset-567k | 大規模言語モデル研究開発センター | LLM-jp-3 172B beta2 Terms of Use |
| [LLM-jp-3 172B beta1](https://www.nii.ac.jp/news/release/2024/0917.html) | Llama<br>([**172b**-beta1](https://huggingface.co/llm-jp/llm-jp-3-172b-beta1), [**172b**-beta1-instruct](https://huggingface.co/llm-jp/llm-jp-3-172b-beta1-instruct)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)の一部<br>(計 **0.7T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), Dolly Dataset, OASST1, OASST2, Aya Dataset, 	ichikara-instruction-format, Daring-Anteater, FLAN | 大規模言語モデル研究開発センター | LLM-jp-3 172B beta1 Terms of Use |
| [LLM-jp-3 172B alpha](https://llmc.nii.ac.jp/topics/llm-jp-3-172b-alpha1-alpha2/) | Llama<br>([**172b**-alpha1](https://huggingface.co/llm-jp/llm-jp-3-172b-alpha1), [**172b**-alpha1-instruct](https://huggingface.co/llm-jp/llm-jp-3-172b-alpha1-instruct), [**172b**-alpha2](https://huggingface.co/llm-jp/llm-jp-3-172b-alpha2), [**172b**-alpha2-instruct](https://huggingface.co/llm-jp/llm-jp-3-172b-alpha2-instruct)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)の一部<br>(alpha1: 計 **0.7T** トークン, alpha2: 計 **1.4T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), Dolly Dataset, OASST1, OASST2, Aya Dataset, 	ichikara-instruction-format, Daring-Anteater, FLAN | 大規模言語モデル研究開発センター | Apache 2.0 |
| [Stockmark-2-100B-Instruct-beta](https://stockmark.co.jp/news/20250318) | Llama<br>([**100B**-Instruct-beta](https://huggingface.co/stockmark/Stockmark-2-100B-Instruct-beta), [**100B**-Instruct-beta-AWQ](https://huggingface.co/stockmark/Stockmark-2-100B-Instruct-beta-AWQ)) | 4,096 | 事前学習: 計 **1.5T** トークン<br>Instruction Tuning<br>DPO | ストックマーク | MIT |
| [Stockmark-100b](https://stockmark.co.jp/news/20240516) | Llama<br>([**100b**](https://huggingface.co/stockmark/stockmark-100b), [**100b**-instruct-v0.1](https://huggingface.co/stockmark/stockmark-100b-instruct-v0.1)) | 4,096 | 事前学習: RedPajama, 日本語 Wikipedia, Japanese mC4, Japanese CommonCrawl, 日本語特許, Stockmark Web Corpus<br>(計 **910B** トークン)<br>Instruction Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | ストックマーク | MIT |
| [PLaMo-100B-Pretrained](https://www.preferred.jp/ja/news/pr20241015/) | Llama[^22]<br>([**100b**](https://huggingface.co/pfnet/plamo-100b)) | 4,096 | 事前学習: Japanese CommonCrawl, RefinedWeb, 独自のデータセット<br>(計: **2.0T** トークン) | Preferred Elements (Preferred Networks) | PLaMo Non-Commercial License |
| [LLM-jp-3 MoE](https://llm-jp.nii.ac.jp/ja/blog/blog-603/) | MoE<br>([8x1.8b (**9.3b**)](https://huggingface.co/llm-jp/llm-jp-3-8x1.8b), [8x1.8b (**9.3b**)-instruct2](https://huggingface.co/llm-jp/llm-jp-3-8x1.8b-instruct2), [8x1.8b (**9.3b**)-instruct3](https://huggingface.co/llm-jp/llm-jp-3-8x1.8b-instruct3), [8x13b (**73b**)](https://huggingface.co/llm-jp/llm-jp-3-8x13b), [8x13b (**73b**)-instruct2](https://huggingface.co/llm-jp/llm-jp-3-8x13b-instruct2), [8x13b (**73b**)-instruct3](https://huggingface.co/llm-jp/llm-jp-3-8x13b-instruct3)) | 4,096 | LLM-jp-3 (1.8b, 13b) に対して Drop-Upcycling で学習 | 大規模言語モデル研究開発センター | Apache 2.0 |
| [Sarashina2](https://www.sbintuitions.co.jp/news/press/20240614_01/) | Llama<br>([**7b**](https://huggingface.co/sbintuitions/sarashina2-7b), [**13b**](https://huggingface.co/sbintuitions/sarashina2-13b), [**70b**](https://huggingface.co/sbintuitions/sarashina2-70b)) | 7b, 13b: 4,096<br>70b: 8,192 | 事前学習: Japanese Common Crawl, SlimPajama, StarCoder<br>(計 **2.1T** トークン) | SB Intuitions | MIT |
| [Sarashina1](https://www.sbintuitions.co.jp/news/press/20240614_01/) | GPT-NeoX<br>([**7b**](https://huggingface.co/sbintuitions/sarashina1-7b), [**13b**](https://huggingface.co/sbintuitions/sarashina1-13b), [**65b**](https://huggingface.co/sbintuitions/sarashina1-65b)) | 2,048 | 事前学習: Japanese Common Crawl<br>(計 **1T** トークン) | SB Intuitions | MIT |
| [Tanuki-8×8B](https://weblab.t.u-tokyo.ac.jp/2024-08-30/) | MoE (**47b**)<br>([v1.0](https://huggingface.co/weblab-GENIAC/Tanuki-8x8B-dpo-v1.0), [v1.0-AWQ](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8x8B-dpo-v1.0-AWQ), [v1.0-GPTQ-4bit](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8x8B-dpo-v1.0-GPTQ-4bit), [v1.0-GPTQ-8bit](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8x8B-dpo-v1.0-GPTQ-8bit), [v1.0-GGUF](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8x8B-dpo-v1.0-GGUF)) | 4,096 | 事前学習: 様々な Web 上のデータ, 合成データ（計 **1.7T** トークン）<br>SFT, DPO: 様々な合成データ [^19] | 松尾研LLM開発プロジェクト | Apache 2.0 |
| [CyberAgentLM3 (CALM3)](https://www.cyberagent.co.jp/news/detail/id=30463) | Llama<br>([**22b**-chat](https://huggingface.co/cyberagent/calm3-22b-chat), [**22b**-chat-selfimprove-experimental](https://huggingface.co/cyberagent/calm3-22b-chat-selfimprove-experimental)) | **16,384** | 不明<br>(計 **2.0T** トークン) | サイバーエージェント | Apache 2.0 |
| [LLM-jp-3 13B instruct3](https://llm-jp.nii.ac.jp/blog/2025/02/05/instruct3.html) | Llama<br>([150m](https://huggingface.co/llm-jp/llm-jp-3-150m), [150m-instruct2](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct2), [150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3), [440m](https://huggingface.co/llm-jp/llm-jp-3-440m), [440m-instruct2](https://huggingface.co/llm-jp/llm-jp-3-440m-instruct2), [440m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-440m-instruct3), [980m](https://huggingface.co/llm-jp/llm-jp-3-980m), [980m-instruct2](https://huggingface.co/llm-jp/llm-jp-3-980m-instruct2), [980m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-980m-instruct3), [**1.8b**-instrcut2](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct2), [**1.8b**-instruct3](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct3), [**3.7b**-instruct2](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct2), [**3.7b**-instruct3](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct3), [**7.2b**-instruct2](https://huggingface.co/llm-jp/llm-jp-3-7.2b-instruct2), [**7.2b**-instruct3](https://huggingface.co/llm-jp/llm-jp-3-7.2b-instruct3), [**13b**-instruct2](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct2), [**13b**-instruct3](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct3)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)<br>(計 **2.1T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), [magpie-sft-v1.0](https://huggingface.co/datasets/llm-jp/magpie-sft-v1.0), Daring-Anteater, FLAN, ichikara-instruction-format, AutoMultiTurnByCalm3-22B, ramdom-to-fixed-multiturn-Calm3, wizardlm8x22b-logical-math-coding-sft-ja, Synthetic-JP-EN-Coding-Dataset-567k<br>DPO (instruct3 only): [aya-ja-evol-inst](https://huggingface.co/datasets/llm-jp/aya-ja-evol-inst), [ac-self-inst](https://huggingface.co/datasets/llm-jp/ac-self-inst) | 大規模言語モデル研究開発センター | Apache 2.0 |
| [LLM-jp-3 13B](https://llmc.nii.ac.jp/topics/post-707/) | Llama<br>([**1.8b**](https://huggingface.co/llm-jp/llm-jp-3-1.8b), [**1.8b**-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct), [**3.7b**](https://huggingface.co/llm-jp/llm-jp-3-3.7b), [**3.7b**-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct), [**7.2b**](https://huggingface.co/llm-jp/llm-jp-3-7.2b), [**7.2b**-instruct](https://huggingface.co/llm-jp/llm-jp-3-7.2b-instruct), [**13b**](https://huggingface.co/llm-jp/llm-jp-3-13b), [**13b**-instruct](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct)) | 4,096 | 事前学習: [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3)<br>(計 **2.1T** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), FLAN, 	ichikara-instruction-format, AutoMultiTurnByCalm3-22B, ramdom-to-fixed-multiturn-Calm3, wizardlm8x22b-logical-math-coding-sft_additional-ja, Synthetic-JP-EN-Coding-Dataset-567k | 大規模言語モデル研究開発センター | Apache 2.0 |
| [llm-jp-3-3.7b-instruct-EZO](https://huggingface.co/AXCXEPT/llm-jp-3-3.7b-instruct-EZO-Common) | Llama<br>([**3.7b**-instruct-EZO-Common](https://huggingface.co/AXCXEPT/llm-jp-3-3.7b-instruct-EZO-Common), [**3.7b**-instruct-EZO-Humanities](https://huggingface.co/AXCXEPT/llm-jp-3-3.7b-instruct-EZO-Humanities)) | 4,096 | LLM-jp-3 (3.7B) に対して追加学習 | Axcxept | Apache 2.0 |
| [LLM-jp-13B v2.0](https://www.nii.ac.jp/news/release/2024/0430.html) | Llama<br>([**13b**-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-v2.0), [**13b**-instruct-full-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-ichikara_004_001_single-oasst-oasst2-v2.0), [**13b**-instruct-full-ac_001-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-ac_001-dolly-ichikara_004_001_single-oasst-oasst2-v2.0), [**13b**-instruct-full-ac_001_16x-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-ac_001_16x-dolly-ichikara_004_001_single-oasst-oasst2-v2.0)) | 4,096 | 事前学習: [llm-jp-corpus-v2](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v2)<br>(計 **260B** トークン)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [AnswerCarefully Dataset](https://llmc.nii.ac.jp/answercarefully-dataset/), Dolly Dataset, OASST1, OASST2 | LLM-jp | Apache 2.0 |
| [Fugaku-LLM](https://pr.fujitsu.com/jp/news/2024/05/10.html) | GPT<br>([**13B**](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B), [**13B**-instruct](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct), [**13B**-instruct-gguf](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct-gguf)) | 2,048 | 事前学習: 独自<br>Instruction Tuning: OASST1, Dolly Dataset, GSM8K | 東工大, 東北大, 富士通, 理研, 名大, サイバーエージェント, Kotoba Technologies | Fugaku-LLM Terms of Use |
| [LLM-jp-13B v1.1](https://llm-jp.nii.ac.jp/blog/2024/02/09/v1.1-tuning.html) | GPT<br>([**13b**-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-dpo-lora-hh_rlhf_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-dpo-lora-hh_rlhf_ja-v1.1)) | 2,048 | Instruction Tuning (LoRA or Full-parameter FT): Dolly Dataset, OASST1, [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/)<br>DPO (LoRA): HH RLHF | LLM-jp | Apache 2.0 |
| [LLM-jp-13B](https://www.nii.ac.jp/news/release/2023/1020.html) | GPT<br>([1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0), [**13b**-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0), [**13b**-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0), [**13b**-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0), [**13b**-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0), [**13b**-instruct-lora-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-v1.0), [**13b**-instruct-lora-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-dolly-oasst-v1.0), [**13b**-instruct-lora-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly-oasst-v1.0)) | 2,048 | 事前学習: [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) (Wikipedia, Japanese mC4, The Pile, Stack) (計 **300B** トークン)<br>Instruction Tuning (Full-parameter FT or LoRA): jaster, Dolly Dataset, OASST1 | LLM-jp | Apache 2.0 |
| [PLaMo-13B](https://www.preferred.jp/ja/news/pr20230928/) | Llama[^1]<br>([**13b**](https://huggingface.co/pfnet/plamo-13b), [**13b**-instruct](https://huggingface.co/pfnet/plamo-13b-instruct), [**13b**-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc)) | base: 4,096<br>instruct, instruct-nc: 8,192 | 事前学習: C4, Project Gutenberg, RedPajama, 日本語 Wikipedia, Japanese mC4<br>(計 **1.5T** トークン)<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1, llm-japanese-datasetのwikinews subset (NCモデルでは商用利用不可の Alpaca Dataset も含めて学習) | Preferred Networks | Apache 2.0<br>(NC モデルは CC BY-NC 4.0) |
| [Stockmark-13b](https://stockmark.co.jp/news/20231027) | Llama<br>([**13b**](https://huggingface.co/stockmark/stockmark-13b), [**13b**-instruct](https://huggingface.co/stockmark/stockmark-13b-instruct)) | 2,048 | 事前学習: 日本語 Wikipedia、Japanese CC-100、Japanese mC4、Japanese CommonCrawl、日本語特許、Stockmark Web Corpus<br>(計 **220B** トークン)<br>Instruction Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | ストックマーク | baseモデル: MIT<br>instructモデル: CC BY-NC-SA 4.0 |
| [Weblab-10B](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001) | GPT-NeoX<br>([**10b**](https://huggingface.co/matsuo-lab/weblab-10b), [**10b**-instruction-sft](https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft)) | 2,048 | Japanese mC4 + The Pile（計 **600B** トークン）<br>\*instruction-sft モデルは Alpaca Dataset, FLAN でファインチューニング | 東大 松尾研 | CC BY-NC 4.0 |
| [PLaMo 2 8B](https://tech.preferred.jp/ja/blog/plamo-2-8b/) | Samba ベースのアーキテクチャ<br>([**8b**](https://huggingface.co/pfnet/plamo-2-8b)) | | 日本語、英語等のデータ<br>（計 **6T** トークン） | Preferred Elements (Preferred Networks) | PLaMo community license |
| [Tanuki-8B](https://weblab.t.u-tokyo.ac.jp/2024-08-30/) | Tanuki (**8b**)<br>([v1.0](https://huggingface.co/weblab-GENIAC/Tanuki-8B-dpo-v1.0), [v1.0-AWQ](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8B-dpo-v1.0-AWQ), [v1.0-GPTQ-4bit](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8B-dpo-v1.0-GPTQ-4bit), [v1.0-GPTQ-8bit](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8B-dpo-v1.0-GPTQ-8bit), [v1.0-GGUF](https://huggingface.co/team-hatakeyama-phase2/Tanuki-8B-dpo-v1.0-GGUF)) | 4,096 | 事前学習: 様々な Web 上のデータ, 合成データ（計 **1.3T** トークン）<br>SFT, DPO: 様々な合成データ [^19] | 松尾研LLM開発プロジェクト | Apache 2.0 |
| [Japanese StableLM Alpha](https://ja.stability.ai/blog/japanese-stablelm-alpha) | GPT-NeoX<br>([base-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b), [instruct-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b), [instruct-alpha-**7b**-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2)) | 2,048 | Wikipedia, Japanese CC-100, Japanese mC4, Japanese OSCAR, RedPajama<br>(+ 独自のデータセット)[^2]<br>(計 **750B** トークン)<br>\*instruct モデルでは Alpaca Dataset, Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subsetでファインチューニング<br>(v2では商用利用不可の Alpaca Dataset を除外) | Stability AI | baseモデル: Apache 2.0<br>instruct モデル (v1): [独自のライセンス](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b/tree/main)<br>instruct モデル (v2): Apache 2.0 |
| [CyberAgentLM2 (CALM2)](https://www.cyberagent.co.jp/news/detail/id=29479) | Llama<br>([**7b**](https://huggingface.co/cyberagent/calm2-7b), [**7b**-chat](https://huggingface.co/cyberagent/calm2-7b-chat), [**7b**-chat-dpo-experimental](https://huggingface.co/cyberagent/calm2-7b-chat-dpo-experimental)) | base: 4,096<br>chat: **32,768** |一般公開されている日本語・英語のデータセット（詳細不明） (計 **1.3T** トークン)<br>*dpo モデルは Chatbot Arena Conversations JA (calm2) Dataset を用いて DPO で学習 | サイバーエージェント | Apache 2.0<br>(dpo モデルのみ CC BY 4.0) |
| [OpenCALM](https://www.cyberagent.co.jp/news/detail/id=28817) | GPT-NeoX<br>([small](https://huggingface.co/cyberagent/open-calm-small), [medium](https://huggingface.co/cyberagent/open-calm-medium), [large](https://huggingface.co/cyberagent/open-calm-large), [**1b(1.4b)**](https://huggingface.co/cyberagent/open-calm-1b), [**3b(2.7b)**](https://huggingface.co/cyberagent/open-calm-3b), [**7b(6.8b)**](https://huggingface.co/cyberagent/open-calm-7b)) | 2,048 | 日本語 Wikipedia <br>+ Jpanese mC4<br>+ Japanese CC-100 | サイバーエージェント | CC BY-SA 4.0 |
| [Stormy](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/422/1350) | GPT-NeoX<br>([**7b(6.8b)**](https://huggingface.co/izumi-lab/stormy-7b-10ep)) | 2,048 | OpenCALM (6.8b) に対して<br>llm-japanese-dataset v0 のうち翻訳タスクを除いたデータで LoRAチューニング | 東大 和泉研 | CC BY-SA 4.0 |
| [rinna GPT <br> (英語やコードも含めて学習されたモデル)](https://rinna.co.jp/news/2023/07/20230731.html) | GPT-NeoX<br>([**4b(3.8b)**](https://huggingface.co/rinna/bilingual-gpt-neox-4b), [**4b(3.8b)**-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k), [**4b(3.8b)**-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft), [**4b(3.8b)**-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo)) | 8kモデル: 8,192<br>他: 2,048 | Wikipedia, Japanese CC-100, Japanese C4, RedPajama, The Pile<br>(計 **524B** トークン)<br>\*8k モデルでは 4,000トークンを超える長いトークン列でファインチューニング<br>\*instruction-sft モデルでは HH RLHF、FLAN でファインチューニング<br>\*instruction-ppo モデルでは HH RLHF で PPO ベースの強化学習 | rinna | MIT |
| [japanese-large-lm](https://engineering.linecorp.com/ja/blog/3.6b-japanese-language-model-with-improved-dialog-performance-by-instruction-tuning) | GPT-NeoX<br>([**1.7b**](https://huggingface.co/line-corporation/japanese-large-lm-1.7b), [**3.6b**](https://huggingface.co/line-corporation/japanese-large-lm-3.6b), [**1.7b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft), [**3.6b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft)) | 2,048 | 日本語 Wikipedia, Japanese CC-100, Japanese C4, Japanese OSCAR や独自データなど<br>(計 **650GB**)<br>\*instruction-sft モデルでは OASST1 でファインチューニング | LINE | Apache 2.0 |
| [rinna GPT <br> (日本語のみで学習されたモデル)](https://rinna.co.jp/news/2023/05/20220531.html) | GPT または GPT-NeoX<br>([xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall), [small](https://huggingface.co/rinna/japanese-gpt2-small), [medium](https://huggingface.co/rinna/japanese-gpt2-medium), [**1b**](https://huggingface.co/rinna/japanese-gpt-1b), [neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small), [neox-**3.6b**](https://huggingface.co/rinna/japanese-gpt-neox-3.6b), [neox-**3.6b**-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft), [neox-**3.6b**-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2), [neox-**3.6b**-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)) | ≤ 2,048 | 日本語 Wikipedia <br> + Japanese CC-100 <br> (1b 以降のモデルでは<br>さらに Japanese mC4 を追加)<br>\*instruction-sft, sft-v2 モデルでは HH RLHF、FLAN、SHP データセットでさらにファインチューニング<br>\*instruction-ppo モデルでは HH RLHF でさらに PPO ベースの強化学習 | rinna | MIT |
| [Sarashina2.2](https://www.sbintuitions.co.jp/blog/entry/2025/03/07/093143) | Llama<br>([0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b), [0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1), [**1b**](https://huggingface.co/sbintuitions/sarashina2.2-1b), [**1b**-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1), [**3b**](https://huggingface.co/sbintuitions/sarashina2.2-3b), [**3b**-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1)) | 8,192 || SB Intuitions | MIT |
| [レトリバT5](https://note.com/retrieva/n/n7b4186dc5ada) | T5<br>([small (short)](https://huggingface.co/retrieva-jp/t5-small-short), [small (medium)](https://huggingface.co/retrieva-jp/t5-small-medium), [small (long)](https://huggingface.co/retrieva-jp/t5-small-long), [base (short)](https://huggingface.co/retrieva-jp/t5-base-short), [base (medium)](https://huggingface.co/retrieva-jp/t5-base-medium), [base (long)](https://huggingface.co/retrieva-jp/t5-base-long), [large (short)](https://huggingface.co/retrieva-jp/t5-large-short), [large (medium)](https://huggingface.co/retrieva-jp/t5-large-medium), [large (long)](https://huggingface.co/retrieva-jp/t5-large-long), [**xl(3b)**](https://huggingface.co/retrieva-jp/t5-xl)) | | 日本語 Wikipedia + Japanese mC4 | レトリバ | CC BY-SA 4.0 |
| [Spiral-RetNet-3b-base](https://prtimes.jp/main/html/rd/p/000000014.000120221.html) | RetNet<br>([**3b**](https://huggingface.co/Spiral-AI/Spiral-RetNet-3b-base)) | 2,048 |  Wikipedia, Japanese CC-100, CulturaX | Spiral.AI | MIT |
| [kotomamba-2.8B](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0) | Mamba<br>([**2.8B**-v1.0](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0)) | 2,048 | 日本語 Wikipedia, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [ABEJA GPT](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207) | GPT または GPT-NeoX<br>([large](https://huggingface.co/abeja/gpt2-large-japanese), [neox-**2.7b**](https://huggingface.co/abeja/gpt-neox-japanese-2.7b)) | | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | ABEJA | MIT |
| [Rakuten AI 2.0 mini](https://corp.rakuten.co.jp/news/press/2025/0212_02.html) | Mistral<br>([mini(**1.5b**)](https://huggingface.co/Rakuten/RakutenAI-2.0-mini), [mini(**1.5b**)-instruct](https://huggingface.co/Rakuten/RakutenAI-2.0-mini-instruct)) | **131,072** ||楽天|Apache 2.0|
| [早大GPT](https://huggingface.co/nlp-waseda/gpt2-xl-japanese) | GPT<br>([small](https://huggingface.co/nlp-waseda/gpt2-small-japanese), [**xl(1.5b)**](https://huggingface.co/nlp-waseda/gpt2-xl-japanese)) | |  日本語 Wikipedia<br> + Japanese CC-100 | 早大 河原研 | CC BY-SA 4.0 |
| [ストックマークGPT](https://stockmark.co.jp/news/20230808) | GPT-NeoX<br>([**1.4b**](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b)) |  | 日本語 Wikipedia (0.88B トークン)<br>+ Japanese CC-100 (10.5B トークン)<br>+ 独自のWebデータ (8.6B トークン) | ストックマーク | MIT |
| [イエローバックGPT](https://tech.yellowback.net/posts/gpt-neo-japanese) | GPT-NeoX<br>([**1.3b**](https://huggingface.co/yellowback/gpt-neo-japanese-1.3B)) |  | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | イエローバック | Apache 2.0 |
| [PLaMo 2 1B](https://tech.preferred.jp/ja/blog/plamo-2/) | Samba ベースのアーキテクチャ<br>([**1b**](https://huggingface.co/pfnet/plamo-2-1b)) | | 日本語、英語等のデータ<br>（計 **4T** トークン） | Preferred Elements (Preferred Networks) | Apache 2.0 |
| [Sarashina2.1-1B](https://huggingface.co/sbintuitions/sarashina2.1-1b) | Llama<br>([**1b**](https://huggingface.co/sbintuitions/sarashina2.1-1b)) | 8,192 | Web 上などの日本語・英語データ（計 **10T** トークン） | SB Intuitions | Sarashina Model NonCommercial License |
| [colorfulscoop GPT](https://huggingface.co/colorfulscoop/gpt2-small-ja) | GPT<br>([small](https://huggingface.co/colorfulscoop/gpt2-small-ja)) | |  日本語 Wikipedia | Colorful Scoop | CC BY-SA 3.0 |
| [東工大GPT](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/H9-1.pdf) | GPT<br>([medium](https://huggingface.co/okazaki-lab/japanese-gpt2-medium-unidic), [medium (逆方向)](https://huggingface.co/okazaki-lab/japanese-reversed-gpt2-medium-unidic)) [^3] | |  日本語 Wikipedia + Japanese CC-100 | 東工大 岡崎研 | CC BY-SA 4.0 |
| [京大GPT](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) | GPT<br>([small (文字レベル)](https://huggingface.co/ku-nlp/gpt2-small-japanese-char), [medium (文字レベル)](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char), [large (文字レベル)](https://huggingface.co/ku-nlp/gpt2-large-japanese-char)) | | 日本語 Wikipedia (約2,700万文 (3.2GB)) <br>+ Japanese CC-100 (約6億1,900万文 (85GB)) <br>+ Japanese OSCAR (約3億2,600万文 (54GB)) | 京大 言語メディア研究室 | CC BY-SA 4.0 |
| [日本語BART](https://huggingface.co/ku-nlp/bart-base-japanese) | BART<br>([base](https://huggingface.co/ku-nlp/bart-base-japanese), [large](https://huggingface.co/ku-nlp/bart-large-japanese)) | |  日本語 Wikipedia (約1,800万文) | 京大 言語メディア研究室 | CC BY-SA 4.0 |
| [Megagon Labs T5](https://github.com/megagonlabs/t5-japanese) | T5<br>([base](https://huggingface.co/megagonlabs/t5-base-japanese-web)) | |  Japanese mC4 (87,425,304 ページ (782 GB))<br>+ Japanese wiki40b (828,236 記事 (2 GB)) | Megagon Labs <br> (リクルート) | Apache 2.0 |

<a id="generative-scratch-domain-specific"></a>
#### ドメイン特化型

|    | ドメイン | アーキテクチャ  |  学習テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|:---:|
| [日本語対話Transformer](https://group.ntt/jp/topics/2021/09/30/transformer.html) | 対話 |Transformer | Twitter 上の日本語リプライのペア | NTT | [独自のライセンス](https://github.com/nttcslab/japanese-dialog-transformers/blob/main/LICENSE.md) |
| [日本語ニュースBART](https://tech.stockmark.co.jp/blog/bart-japanese-base-news/) | ビジネス | BART ([base](https://huggingface.co/stockmark/bart-base-japanese-news)) | 日本語ビジネスニュース記事（約2,100万記事 (2.9億文)） | ストックマーク | MIT |
| [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | 学術 | BART ([base](https://huggingface.co/EhimeNLP/AcademicBART)) | CiNii の日本語論文 | 愛媛大 人工知能研究室 | Apache 2.0 |

<a id="english-based-models"></a>
### 海外モデルに日本語で継続事前学習を行ったモデル

<a id="generative-continual-general"></a>
#### 汎用

|    | ベースのLLM  | 学習テキスト | 開発元  | ライセンス / 利用規約 |
|:---|:---:|:---:|:---:|:---:|
| [Llama 3.3 Swallow 70B](https://swallow-llm.github.io/llama3.3-swallow.ja.html)<br>([70B-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-v0.4), [70B-Instruct-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4)) | Llama 3.3 (**70b**) | 事前学習: Wikipedia, DCLM-baseline-1.0, Swallow Corpus Version 2, Cosmopedia, Laboro ParaCorpus, FineMath-4+, Swallow Code Version 0.3<br>Instruction Tuning: Gemma-2-LMSYS-Chat-1M-Synth, Swallow-Magpie-Ultra-v0.1, Swallow-Gemma-Magpie-v0.1, Swallow-Code-v0.3-Instruct-style | Swallowプロジェクト | Llama 3.3 Community License & Gemma Terms of Use |
| [Llama 3.1 Swallow 70B](https://swallow-llm.github.io/llama3.1-swallow.ja.html)<br>([70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-v0.1), [70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.1), [70B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-70B-Instruct-v0.3)) | Llama 3.1 (**70b**) | 事前学習: The Stack v2, Wikipedia, DCLM-baseline-1.0, Swallow Corpus Version 2, Cosmopedia, Laboro ParaCorpus<br>Instruction Tuning: lmsys-chat-1m-synth-ja-wo-pii-and-template-instructions, lmsys-chat-1m-synth-en-wo-pii-and-template-instructions, filtered-magpie-ultra-ja, filtered-magpie-ultra-en, gemma-magpie | Swallowプロジェクト | Llama 3.1 Community License<br>(Instructモデルは Gemma Terms of Use も適用) |
| [cyberagent/Llama-3.1-70B-Japanese-Instruct-2407](https://huggingface.co/cyberagent/Llama-3.1-70B-Japanese-Instruct-2407) | Llama 3.1 (**70b**) | 不明 | サイバーエージェント | Llama 3.1 Community License |
| [Llama 3 Swallow 70B](https://swallow-llm.github.io/llama3-swallow.ja.html)<br>([70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-70B-v0.1), [70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-70B-Instruct-v0.1)) | Llama 3 (**70b**) | 事前学習: Algebraic Stack, Wikipedia, RefinedWeb, Swallow Corpus, Cosmopedia, Laboro ParaCorpus, OpenWebMath<br>Instruction Tuning: OASST1 [^17] | Swallowプロジェクト | Llama 3 Community License |
| [turing-motors/Llama-3-heron-brain-70B-v0.3](https://huggingface.co/turing-motors/Llama-3-heron-brain-70B-v0.3) | Llama 3 (**70b**) | Llama 3 Swallow 70B に対して追加学習（詳細不明） | Turing | Llama 3 Community License |
| [Llama 3 Youko 70B](https://rinna.co.jp/news/2024/07/20240725.html)<br>([70b](https://huggingface.co/rinna/llama-3-youko-70b), [70b-instruct](https://huggingface.co/rinna/llama-3-youko-70b-instruct), [70b-gptq](https://huggingface.co/rinna/llama-3-youko-70b-gptq), [70b-instruct-gptq](https://huggingface.co/rinna/llama-3-youko-70b-instruct-gptq)) | Llama 3 (**70b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **5B** トークン)<br>Instruction Tuning: 独自のデータセット[^11] | rinna | Llama 3 Community License |
| [Swallow 70B](https://swallow-llm.github.io/swallow-llama.ja.html)<br>([70b-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-hf), [70b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf), [70b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-v0.1), [70b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf), [70b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf)) | Llama 2 (**70b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1モデルでは OASST1, OASST2 を使用 | Swallowプロジェクト | Llama 2 Community License |
| [KARAKURI LM](https://karakuri.ai/seminar/news/karakuri-lm/)<br>([70b-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-v0.1), [70b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-chat-v0.1)) | Llama 2 (**70b**) | 事前学習: mC4, CC100, OSCAR, RedPajama, 独自のデータセット<br>(計 **16B** トークン)<br>SteerLM: OASST2, 独自のデータセット | カラクリ | Llama 2 Community License[^13] |
| [Japanese Stable LM Beta 70B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-70b), [instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b)) | Llama 2 (**70b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [Swallow-MX 8x7B](https://swallow-llm.github.io/swallow-mistral.ja.html)<br>([8x7b-NVE-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MX-8x7b-NVE-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | 事前学習: Algebraic Stack, Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile, The Vault | Swallowプロジェクト | Apache 2.0 |
| [KARAKURI LM 8x7B Instruct v0.1](https://karakuri.ai/seminar/news/karakuri-lm-8x7b-instruct-v0-1/)<br>([8x7b-instruct-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-instruct-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | Swallow-MX 8x7B に対して以下のデータセットで学習: Dolly Dataset, OASST2, HelpSteer, glaive-code-assistant-v3, glaive-function-calling-v2, synthetic_text_to_sql, MetaMathQA, orca-math-word-problems-200k, rag-dataset-12000, rag-hallucination-dataset-1000, 独自のデータセット | カラクリ | Apache 2.0 (?)[^12] |
| [KARAKURI LM 8x7B Chat v0.1](https://karakuri.ai/seminar/news/aws_trainium_moe/)<br>([8x7b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-chat-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | Swallow-MX 8x7B に対して<br>SteerLM: OASST2, HelpSteer, 独自のデータセット | カラクリ | Apache 2.0 |
| [ABEJA-Mixtral-8x7B-japanese](https://tech-blog.abeja.asia/entry/abeja-nedo-project-part1-202404)<br>([8x7B-v0.1-japanese](https://huggingface.co/abeja/Mixtral-8x7B-v0.1-japanese), [8x7B-Instruct-v0.1-japanese](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese), [8x7B-Instruct-v0.1-japanese-alpha](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese-alpha), [8x7B-Instruct-v0.1-japanese-alpha-merged](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese-alpha-merged)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**)<br>\*Instructが名前に付いていないモデルのみ Mixtral-8x7B-v0.1 がベース |  事前学習: Japanese CC,	Redpajama, 独自<br>（計 **450B** トークン） | ABEJA | Apache 2.0 |
| [Qwen2.5 Bakeneko 32B](https://rinna.co.jp/news/2025/02/20250213.html)<br>([qwen2.5-bakeneko-32b](https://huggingface.co/rinna/qwen2.5-bakeneko-32b), [qwen2.5-bakeneko-32b-instruct](https://huggingface.co/rinna/qwen2.5-bakeneko-32b-instruct), [deepseek-r1-distill-qwen2.5-bakeneko-32b](https://huggingface.co/rinna/deepseek-r1-distill-qwen2.5-bakeneko-32b), [qwq-bakeneko-32b](https://huggingface.co/rinna/qwq-bakeneko-32b), [qwen2.5-bakeneko-32b-instruct-v2](https://huggingface.co/rinna/qwen2.5-bakeneko-32b-instruct-v2)) | Qwen 2.5 (**32b**) || rinna | Apache 2.0 |
| [ABEJA-Qwen2.5-32b-Japanese-v0.1](https://tech-blog.abeja.asia/entry/geniac2-qwen25-32b-v0.1)<br>([32b-Japanese-v0.1](https://huggingface.co/abeja/ABEJA-Qwen2.5-32b-Japanese-v0.1)) | Qwen 2.5 (**32b**) | 事前学習: Common Crawl, Cosmopedia, 独自<br>（計 **100B** トークン）<br>+ Chat Vector | ABEJA | Apache 2.0 |
| [Nekomata 14B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([14b](https://huggingface.co/rinna/nekomata-14b), [14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction), [14b-gguf](https://huggingface.co/rinna/nekomata-14b-gguf), [14b-instruction-gguf](https://huggingface.co/rinna/nekomata-14b-instruction-gguf)) | Qwen (**14b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **66B** トークン)<br>Instruction Tuning: Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Tongyi Qianwen LICENSE |
| [Swallow 13B](https://swallow-llm.github.io/swallow-llama.ja.html)<br>([13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf), [13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf), [13b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-v0.1), [13b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf)) | Llama 2 (**13b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1モデルでは OASST1, OASST2 を使用 | Swallowプロジェクト | Llama 2 Community License |
| [LEIA-Swallow-13B](https://www.ousia.jp/ja/page/ja/2024/04/24/leia/)<br>([13b](https://huggingface.co/leia-llm/Leia-Swallow-13b)) | Llama 2 (**13b**) | Swallow 13B に対して LEIA で追加学習 | 個人 ([山田育矢](https://scholar.google.com/citations?user=M7YivToAAAAJ), [李凌寒](https://scholar.google.co.jp/citations?user=z9is5FAAAAAJ)) | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-13b](https://note.com/elyza/n/n5d42686b60b7)<br>([13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b), [13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct), [13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast), [13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct)) | Llama 2 (**13b**) | 事前学習: 日本語 Wikipedia, Japanese OSCAR, その他クロールデータなど<br>(計 **18B** トークン)<br>Instruction Tuning: 独自のデータセット | ELYZA | Llama 2 Community License |
| [cyberagent/Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) | Mistral NeMo (**12b**) | 不明 | サイバーエージェント | Apache 2.0 |
| [Llama 3.1 Swallow 8B](https://swallow-llm.github.io/llama3.1-swallow.ja.html)<br>([8B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.1), [8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.1), [8B-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.2), [8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2), [8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)) | Llama 3.1 (**8b**) | 事前学習: The Stack v2, Wikipedia, DCLM-baseline-1.0, Swallow Corpus Version 2, Cosmopedia, Laboro ParaCorpus<br>Instruction Tuning: lmsys-chat-1m-synth-ja-wo-pii-and-template-instructions, lmsys-chat-1m-synth-en-wo-pii-and-template-instructions, filtered-magpie-ultra-ja, filtered-magpie-ultra-en, gemma-magpie | Swallowプロジェクト | Llama 3.1 Community License<br>(Instructモデルは Gemma Terms of Use も適用) |
| [Llama 3 Swallow 8B](https://swallow-llm.github.io/llama3-swallow.ja.html)<br>([8B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-v0.1), [8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1)) | Llama 3 (**8b**) | 事前学習: Algebraic Stack, Wikipedia, RefinedWeb, Swallow Corpus, Cosmopedia, Laboro ParaCorpus, OpenWebMath<br>Instruction Tuning: OASST1 [^17] | Swallowプロジェクト | Llama 3 Community License |
| [turing-motors/Llama-3-heron-brain-8B-v0.3](https://huggingface.co/turing-motors/Llama-3-heron-brain-8B-v0.3) | Llama 3 (**8b**) | Llama 3 Swallow 8B に対して追加学習（詳細不明） | Turing | Llama 3 Community License |
| [Llama 3 Youko 8B](https://rinna.co.jp/news/2024/07/20240725.html)<br>([8b](https://huggingface.co/rinna/llama-3-youko-8b), [8b-instruct](https://huggingface.co/rinna/llama-3-youko-8b-instruct), [8b-gptq](https://huggingface.co/rinna/llama-3-youko-8b-gptq), [8b-instruct-gptq](https://huggingface.co/rinna/llama-3-youko-8b-instruct-gptq)) | Llama 3 (**8b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **22B** トークン)<br>Instruction Tuning[^11]: Aya Dataset (Japanese subset), FLAN, Dolly Dataset, HH RLHF, OASST1, OASST2, MetaMathQA, CodeAlpaca Dataset, 独自のデータセット<br>DPO: HelpSteer, HelpSteer2, 独自のデータセット | rinna | Llama 3 Community License |
| [Llama 3 ELYZA JP 8B](https://note.com/elyza/n/n360b6084fdbd)<br>([8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B), [8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF), [8B-AWQ](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-AWQ)) | Llama 3 (**8b**) | 不明 | ELYZA | Llama 3 Community License |
| [Llama 3 neoAI 8B Chat v0.1](https://prtimes.jp/main/html/rd/p/000000017.000109048.html)<br>([8B-Chat-v0.1](https://huggingface.co/neoai-inc/Llama-3-neoAI-8B-Chat-v0.1)) | Llama 3 (**8b**) | 不明 | neoAI | Llama 3 Community License |
| [Llama 3 tedllm](https://www.teldevice.co.jp/pro_info/2024/press_241023.php)<br>([v0](https://huggingface.co/tokyo-electron-device-ai/llama3-tedllm-8b-v0)) | Llama 3 (**8b**) | 事前学習: 日本語の一般コーパス | 東京エレクトロン デバイス | Llama 3 Community License |
| [Swallow 7B](https://swallow-llm.github.io/swallow-llama.ja.html)<br>([7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf), [7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf), [7b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-v0.1), [7b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf), [7b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf), [7b-plus-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf)) | Llama 2 (**7b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1モデルでは OASST1, OASST2 を使用 | Swallowプロジェクト | Llama 2 Community License |
| [LEIA-Swallow-7B](https://www.ousia.jp/ja/page/ja/2024/04/24/leia/)<br>([7b](https://huggingface.co/leia-llm/Leia-Swallow-7b)) | Llama 2 (**7b**) | Swallow 7B に対して LEIA で追加学習 | 個人 ([山田育矢](https://scholar.google.com/citations?user=M7YivToAAAAJ), [李凌寒](https://scholar.google.co.jp/citations?user=z9is5FAAAAAJ)) | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-7b](https://note.com/elyza/n/na405acaca130)<br> ([7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct), [7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast), [7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct)) | Llama 2 (**7b**) | 事前学習: 日本語 Wikipedia, Japanese OSCAR, その他クロールデータなど<br>(計 **18B** トークン)<br>Instruction Tuning: 独自のデータセット | ELYZA | Llama 2 Community License |
| [Youri 7B](https://rinna.co.jp/news/2023/10/20231031.html)<br>([7b](https://huggingface.co/rinna/youri-7b), [7b-instruction](https://huggingface.co/rinna/youri-7b-instruction), [7b-chat](https://huggingface.co/rinna/youri-7b-chat), [7b-gptq](https://huggingface.co/rinna/youri-7b-gptq), [7b-instruction-gptq](https://huggingface.co/rinna/youri-7b-instruction-gptq), [7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq)) | Llama 2 (**7b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **40B** トークン)<br>Instruction Tuning: Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Llama 2 Community License |
| [houou-7b](https://corp.moneyforward.com/news/release/corp/20231206-mf-press-1/)<br>([instruction-7b-v1](https://huggingface.co/moneyforward/houou-instruction-7b-v1), [instruction-7b-v2](https://huggingface.co/moneyforward/houou-instruction-7b-v2), [instruction-7b-v3](https://huggingface.co/moneyforward/houou-instruction-7b-v3)) | Llama 2 (**7b**) | Youri 7B (base) に対して Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | マネーフォワード | Llama 2 Community License |
| [Japanese Stable LM Beta 7B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-7b), [base-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-ja_vocab-beta-7b), [instruct-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-7b), [instruct-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b)) |  Llama 2 (**7b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [SambaLingo-Japanese](https://sambanova.ai/blog/sambalingo-open-source-language-experts)<br>([Base](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Base), [Chat](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Chat)) | Llama 2 (**7b**) | 事前学習: CulturaX<br>Instruction Tuning: ultrachat_200k<br>DPO: ultrafeedback, cai-conversation-harmless | SambaNova Systems | Llama 2 Community License (?)[^12] |
| [blue-lizard](https://prtimes.jp/main/html/rd/p/000000010.000125694.html)<br>([blue-lizard](https://huggingface.co/Deepreneur/blue-lizard)) | Llama 2 (**7b**) | 不明 | Deepreneur | Llama 2 Community License |
| [Swallow-MS 7B](https://swallow-llm.github.io/swallow-mistral.ja.html)<br>([7b-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-v0.1), [7b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-instruct-v0.1)) | Mistral-7B-v0.1 (**7b**) | 事前学習: Algebraic Stack, Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, OASST1 | Swallowプロジェクト | Apache 2.0 |
| [Rakuten AI 2.0](https://corp.rakuten.co.jp/news/press/2025/0212_02.html)<br>([8x7B](https://huggingface.co/Rakuten/RakutenAI-2.0-8x7B), [8x7B-instruct](https://huggingface.co/Rakuten/RakutenAI-2.0-8x7B-instruct)) | Mistral-7B-v0.1 (**7b**) | | 楽天 | Apache 2.0 |
| [RakutenAI-7B](https://corp.rakuten.co.jp/news/press/2024/0321_01.html?year=2024&month=3&category=corp)<br>([7B](https://huggingface.co/Rakuten/RakutenAI-7B), [7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct), [7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat)) | Mistral-7B-v0.1 (**7b**) | 事前学習: 不明<br>Instruction Tuning: Dolly Dataset, OASST1, （jasterと同様に）言語理解データセットの訓練データを Instruction Tuning 用に変換したもの, 独自のデータセット | 楽天 | Apache 2.0 |
| [Japanese Stable LM Gamma 7B](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([base-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b), [instruct-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b)) | Mistral-7B-v0.1 (**7b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning: Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subset | Stability AI |  Apache 2.0  |
| [ChatNTQ JA 7B](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)<br>([7b-v1.0](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)) | Mistral-7B-v0.1 (**7b**) | Japanese Stable LM Gamma 7B (base) に対して独自のデータセットで Instruction Tuning | NTQ Solution | Apache 2.0  |
| [Shisa Gamma 7B](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)<br>([7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)) | Mistral-7B-v0.1 (**7b**) | Japanese Stable LM Gamma 7B (base) に対して ultra-orca-boros-en-ja で Instruction Tuning | AUGMXNT | Apache 2.0 (?)[^12]  |
| [Shisa 7B](https://github.com/AUGMXNT/shisa/wiki)<br>([base-7b-v1](https://huggingface.co/augmxnt/shisa-base-7b-v1), [7b-v1](https://huggingface.co/augmxnt/shisa-7b-v1)) | Mistral-7B-v0.1 (**7b**) | 事前学習: shisa-pretrain-en-ja-v1 (**8B** トークン)<br>Instruction Tuning & DPO: ultra-orca-boros-en-ja, shisa-en-ja-dpo-v1  | AUGMXNT |  Apache 2.0 (?)[^12]  |
| [Karasu](https://www.lightblue-tech.com/2024/01/15/20240115_news/)<br>([7B](https://huggingface.co/lightblue/karasu-7B), [7B-chat](https://huggingface.co/lightblue/karasu-7B-chat), [7B-chat-plus](https://huggingface.co/lightblue/karasu-7B-chat-plus), [7B-chat-plus-unleashed](https://huggingface.co/lightblue/karasu-7B-chat-plus-unleashed)) | Mistral-7B-v0.1 (**7b**) | Shisa 7B (base) に対して以下のデータセットで追加事前学習: 青空文庫, 日本の法律・判例, 日本語 Wikipedia, CulturaX の日本ドメインのデータ, UltraChat 200k (計 **7B** トークン)<br>Instruction Tuning: ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, 独自のデータセット | Lightblue | Apache 2.0 (?)[^12]  |
| [Nekomata 7B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([7b](https://huggingface.co/rinna/nekomata-7b), [7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction), [7b-gguf](https://huggingface.co/rinna/nekomata-7b-gguf), [7b-instruction-gguf](https://huggingface.co/rinna/nekomata-7b-instruction-gguf)) | Qwen (**7b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **66B** トークン)<br>Instruction Tuning: Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Tongyi Qianwen LICENSE |
| [lightblue/japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) | MPT (**7b**) | Japanese mC4 | Lightblue | Apache 2.0 |
| [Japanese Stable LM 3B-4E1T](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base), [3b-4e1t-instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-instruct)) | StableLM-3B-4E1T (**3b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning: Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subset | Stability AI |  Apache 2.0  |
| [kotomamba-2.8B-CL](https://huggingface.co/kotoba-tech/kotomamba-2.8B-CL-v1.0) | mamba-2.8b-slimpj<br>(**2.8b**) | 日本語 Wikipedia, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [Gemma 2 Baku 2B](https://rinna.co.jp/news/2024/10/20241003.html)<br>([2b](https://huggingface.co/rinna/gemma-2-baku-2b), [2b-it](https://huggingface.co/rinna/gemma-2-baku-2b-it)) | Gemma 2 (**2b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **80B** トークン)<br>OPRO: 独自のデータセット [^20] | rinna | Gemma Terms of Use |
| [Japanese Stable LM 2 1.6B](https://ja.stability.ai/blog/japanese-stable-lm-2-16b)<br>([base](https://huggingface.co/stabilityai/japanese-stablelm-2-base-1_6b), [instruct](https://huggingface.co/stabilityai/japanese-stablelm-2-instruct-1_6b)) | Stable LM 2 1.6B (**1.6b**) | 事前学習: Wikipedia, CulturaX<br>Instruction Tuning: jaster, [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), alpaca-gpt4-japanese, ultra-orca-boros-en-ja-v1 | Stability AI | STABILITY AI NON-COMMERCIAL RESEARCH COMMUNITY LICENSE |
| [TinySwallow-1.5B](https://sakana.ai/taid-jp/)<br>([1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B), [1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct), [1.5B-Instruct-q4f32_1-MLC](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct-q4f32_1-MLC), [1.5B-Insturct-GGUF](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct-GGUF)) | Qwen2.5 (**1.5b**) | 事前学習: Qwen2.5 (32b) を教師として TAID で学習<br>Instruction Tuning: Gemma-2-LMSYS-Chat-1M-Synth, swallow-magpie-ultra-v0.1, swallow-gemma-magpie-v0.1 | Sakana AI, Swallowプロジェクト | Apache 2.0 |
| [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) | TinyLlama (**1.1b**) | 事前学習: Japanese OSCAR, Japanese mC4<br>(計 **3B** トークン) | Lightblue | Apache 2.0 |

<a id="generative-continual-domain-specific"></a>
#### ドメイン特化型

|    | ドメイン | ベースのLLM  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [pfnet/Preferred-MedLLM-Qwen-72B](https://huggingface.co/pfnet/Preferred-MedLLM-Qwen-72B) | 医療 | Qwen2.5 (**72b**) | Preferred Networks | Qwen LICENSE |
| [Llama3-Preferred-MedSwallow-70B](https://tech.preferred.jp/ja/blog/llama3-preferred-medswallow-70b/)<br>([70B](https://huggingface.co/pfnet/Llama3-Preferred-MedSwallow-70B)) | 医療 | Llama 3 (**70b**) | Preferred Networks | Llama 3 Community License |
| [AIgroup-CVM-utokyohospital/MedSwallow-70b](https://huggingface.co/AIgroup-CVM-utokyohospital/MedSwallow-70b) | 医療 | Llama 2 (**70b**) | 東京大学医学部附属病院 循環器内科 AIグループ | CC BY-NC-SA 4.0 |
| [nekomata-14b-pfn-qfin](https://tech.preferred.jp/ja/blog/qfin-llm-continual-pretraining/)<br>([qfin](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin), [qfin-inst-merge](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin-inst-merge)) | 金融 | Qwen (**14b**) | Preferred Networks | Tongyi Qianwen LICENSE |
| [Watashiha-Llama-2-13B-Ogiri-sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft)<br>([sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft), [sft-neuron](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-neuron)) | 大喜利 | Llama 2 (**13b**) | わたしは | Llama 2 Community License |
| [ELYZA-japanese-CodeLlama-7b](https://note.com/elyza/n/n5bce23d7c9c8)<br>([7b](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b-instruct)) | コーディング |  Code Llama<br>(**7b**) | ELYZA | Llama 2 Community License |
| [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) | 物語生成 | GPT-J (**6b**) | 個人 ([大曽根宏幸](https://scholar.google.co.jp/citations?user=6ID5K3oAAAAJ)) | CreativeML OpenRAIL-M License |
| [NovelAI/genji-jp](https://huggingface.co/NovelAI/genji-jp) | 物語生成 | GPT-J (**6b**) | NovelAI |  ？  |

<a id="instruction-only-models"></a>
### 海外モデルに日本語で事後学習のみ行ったモデル

<a id="generative-instruction-only-general"></a>
#### 汎用

|    | ベースのLLM  | 学習テキスト | 開発元  | ライセンス / 利用規約 |
|:---|:---:|:---:|:---:|:---:|
| [AXCXEPT/EZO-Qwen2.5-72B-Instruct](https://huggingface.co/AXCXEPT/EZO-Qwen2.5-72B-Instruct)<br>[AXCXEPT/EZO-AutoCoTRAG-Qwen2.5-72B-Instruct_q4](https://huggingface.co/AXCXEPT/EZO-AutoCoTRAG-Qwen2.5-72B-Instruct_q4) | Qwen2.5 (**72b**) || Axcxept | Qwen License |
| [ao-Karasu](https://note.com/lightblue_tech/n/nfda12435b262)<br>([72B](https://huggingface.co/lightblue/ao-karasu-72B)) | Qwen1.5 (**72b**) | ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, 日本語の公開技術ブログ, ニュース記事, QAサイトの回答, 独自のデータセット | Lightblue |  Tongyi Qianwen LICENSE (?)[^12] |
| [AXCXEPT/Llama-3.1-70B-EZO-1.1-it](https://huggingface.co/AXCXEPT/Llama-3.1-70B-EZO-1.1-it) | Llama 3.1 (**70b**) || Axcxept | Llama 3.1 Community License |
| [Llama 3 shisa-v1-llama3-70b](https://huggingface.co/shisa-ai/shisa-v1-llama3-70b)<br>([70b](https://huggingface.co/shisa-ai/shisa-v1-llama3-70b)) | Llama 3 (**70b**) | ultra-orca-boros-en-ja-v1 | Shisa.AI | Llama 3 Community License (?)[^12] |
| [AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese](https://huggingface.co/AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese) | Llama 2 (**70b**) || 東京大学医学部附属病院 循環器内科 AIグループ | Llama 2 Community License |
| [doshisha-mil/llama-2-70b-chat-4bit-japanese-v1](https://huggingface.co/doshisha-mil/llama-2-70b-chat-4bit-japanese-v1) | Llama 2 (**70b**) || 同志社大学 メディア情報学研究室 | ？ |
| [cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese) | DeepSeek-R1-Distill-Qwen (**32b**) || サイバーエージェント | MIT |
| [karakuri-ai/karakuri-lm-32b-thinking-2501-exp](https://huggingface.co/karakuri-ai/karakuri-lm-32b-thinking-2501-exp) | QwQ (**32b**) || カラクリ | Apache 2.0 |
| [AXCXEPT/EZO-Qwen2.5-32B-Instruct](https://huggingface.co/AXCXEPT/EZO-Qwen2.5-32B-Instruct)<br>[AXCXEPT/EZO-AutoCoTRAG-Qwen2.5-32B-Instruct](https://huggingface.co/AXCXEPT/EZO-AutoCoTRAG-Qwen2.5-32B-Instruct) | Qwen2.5 (**32b**) || Axcxept | Apache 2.0 |
| [cyberagent/DeepSeek-R1-Distill-Qwen-14B-Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-14B-Japanese) | DeepSeek-R1-Distill-Qwen (**14b**) || サイバーエージェント | MIT |
| [EZO-Phi-4](https://huggingface.co/collections/AXCXEPT/ezo-phi-4-678a461c325df99089b387f3)<br>([phi-4-open-R1-Distill-EZOv1](https://huggingface.co/AXCXEPT/phi-4-open-R1-Distill-EZOv1), [phi-4-deepseek-R1K-RL-EZO](https://huggingface.co/AXCXEPT/phi-4-deepseek-R1K-RL-EZO)) | Phi-4 (**14b**) || Axcxept | MIT |
| [Qarasu](https://www.lightblue-tech.com/2024/01/15/20240115_news/)<br>([14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed)) | Qwen (**14b**) | ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, 独自のデータセット | Lightblue | Tongyi Qianwen LICENSE (?)[^12] |
| [Sparticle/llama-2-13b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-13b-chat-japanese-lora) | Llama 2 (**13b**) || Sparticle | ？ |
| [izumi-lab/llama-13b-japanese-lora-v0-1ep](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep) | Llama (**13b**) || 東大 和泉研 |  ？ |
| [AXCXEPT/EZO-Common-9B-gemma-2-it](https://huggingface.co/AXCXEPT/EZO-Common-9B-gemma-2-it) | Gemma 2 (**9b**) || Axcxept | Gemma Terms of Use |
| [AXCXEPT/EZO-Humanities-9B-gemma-2-it](https://huggingface.co/AXCXEPT/EZO-Humanities-9B-gemma-2-it) |Gemma 2 (**9b**) || Axcxept | Gemma Terms of Use |
| [AXCXEPT/Llama-3.1-8B-EZO-1.1-it](https://huggingface.co/AXCXEPT/Llama-3.1-8B-EZO-1.1-it) |Llama 3.1 (**8b**) || Axcxept | Llama 3.1 Community License |
| [Llama 3 Suzume 8B](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese)<br>([8B-japanese](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese), [8B-japanese-gguf](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese-gguf)) | Llama 3 (**8b**) | megagonlabs/instruction_ja, ShareGPT,  独自のデータセット | Lightblue | Llama 3 Community License (?)[^12] |
| [Llama 3 shisa-v1-llama3-8b](https://huggingface.co/shisa-ai/shisa-v1-llama3-8b)<br>([8b](https://huggingface.co/shisa-ai/shisa-v1-llama3-8b)) | Llama 3 (**8b**) | ultra-orca-boros-en-ja-v1 | Shisa.AI | Llama 3 Community License (?)[^12] |
| [AXCXEPT/Llama-3-EZO-8b-Common-it](https://huggingface.co/AXCXEPT/Llama-3-EZO-8b-Common-it) |Llama 3 (**8b**) || Axcxept | Llama 3 Community License |
| [lightblue/DeepSeek-R1-Distill-Qwen-7B-Japanese](https://huggingface.co/lightblue/DeepSeek-R1-Distill-Qwen-7B-Japanese) | DeepSeek-R1-Distill-Qwen (**7b**) || Lightblue | Apache 2.0 |
| [Karasu DPO](https://note.com/lightblue_tech/n/n6967ff462f4a)<br>([7B](https://huggingface.co/lightblue/Karasu-DPO-7B)) | Qwen 2.5 (**7b**) || Lightblue | Apache 2.0 |
| [ganchengguang/Yoko-7B-Japanese-v1](https://huggingface.co/ganchengguang/Yoko-7B-Japanese-v1) | Llama 2 (**7b**) || 横浜国大 森研 |  ？  |
| [Sparticle/llama-2-7b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-7b-chat-japanese-lora) | Llama 2 (**7b**) || Sparticle |  ？  |
| [izumi-lab/llama-7b-japanese-lora-v0-5ep](https://huggingface.co/izumi-lab/llama-7b-japanese-lora-v0-5ep) | Llama (**7b**) || 東大 和泉研 |  ？  |
| [lightblue/jod](https://huggingface.co/lightblue/jod) | Mistral-7B-SlimOrca (**7b**) || Lightblue | Apache 2.0 |
| [NTQAI/chatntq-7b-jpntuned](https://huggingface.co/NTQAI/chatntq-7b-jpntuned) | RWKV-4 World (**7b**) || NTQ Solution |  ？  |
| [Borea](https://prtimes.jp/main/html/rd/p/000000008.000129878.html)<br>([Jp](https://huggingface.co/AXCXEPT/Borea-Phi-3.5-mini-Instruct-Jp), [Common](https://huggingface.co/AXCXEPT/Borea-Phi-3.5-mini-Instruct-Common), [Coding](https://huggingface.co/AXCXEPT/Borea-Phi-3.5-mini-Instruct-Coding)) | Phi-3.5 (**3.8b**) | | Axcxept | MIT |
| [AXCXEPT/EZO-Llama-3.2-3B-Instruct-dpoE](https://huggingface.co/AXCXEPT/EZO-Llama-3.2-3B-Instruct-dpoE) | Llama 3.2 (**3b**) || Axcxept | Llama 3.2 Community License |
| [日本語版 Gemma 2 2B](https://developers-jp.googleblog.com/2024/10/gemma-2-for-japan.html)<br>([2b-jpn-it](https://huggingface.co/google/gemma-2-2b-jpn-it)) | Gemma 2 (**2b**) || Google | Gemma Terms of Use |
| [AXCXEPT/EZO-gemma-2-2b-jpn-it](https://huggingface.co/AXCXEPT/EZO-gemma-2-2b-jpn-it) | Gemma 2 (**2b**) || Axcxept | Gemma Terms of Use |
| [AXCXEPT/EZO-Common-T2-2B-gemma-2-it](https://huggingface.co/AXCXEPT/EZO-Common-T2-2B-gemma-2-it) | Gemma 2 (**2b**) || Axcxept | Gemma Terms of Use |

<a id="generative-instruction-only-domain-specific"></a>
#### ドメイン特化型

|    | ドメイン | ベースのLLM  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [JMedLoRA](https://arxiv.org/pdf/2310.10083.pdf)<br>([llama2-jmedlora-6.89ep](https://huggingface.co/AIgroup-CVM-utokyohospital/llama2-jmedlora-6.89ep)) | 医療 | Llama 2 (**70b**) | 東京大学医学部附属病院 循環器内科 AIグループ | CC BY-NC 4.0 |

<a id="merged-models"></a>
### 複数のLLMをマージして作成されたモデル

|    |  マージ元のLLM（太字は日本語LLM）  | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|
 [EQUES/MedLLama3-JP-v2](https://huggingface.co/EQUES/MedLLama3-JP-v2) | **Llama 3 Swallow 8B (Instruct)**, OpenBioLLM-8B, MMed-Llama 3 8B, **Llama 3 ELYZA JP 8B** | EQUES | Llama 3 Community License |
| [EvoLLM-JP-A](https://sakana.ai/evolutionary-model-merge-jp/)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoLLM-JP-A-v1-7B)) | **Shisa Gamma 7B (v1)**, Arithmo2 Mistral 7B, Abel 7B 002 | Sakana AI | Apache 2.0 |
| [EvoLLM-JP](https://sakana.ai/evolutionary-model-merge-jp/)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoLLM-JP-v1-7B), [v1-10B](https://huggingface.co/SakanaAI/EvoLLM-JP-v1-10B)) | **Shisa Gamma 7B (v1)**, WizardMath-7B-V1.1, Abel 7B 002 | Sakana AI | MICROSOFT RESEARCH LICENSE |

<a id="api-based-models"></a>
### APIとして提供されているモデル

|    |  入出力で扱える<br>トークン数 | 開発元  |  プラットフォーム |
|:---|:---:|:---:|:---:|
| [Solar mini chat ja](https://www.upstage.ai/blog/en/solar-mini-chat-ja)<br>([solar-1-mini-chat-ja](https://developers.upstage.ai/docs/apis/chat)) | 32,768 | Upstage | 独自 |
| [AIのべりすと](https://ai-novel.com/account_api.php) | 2,400 ~ 8,192 | Bit192 | 独自 |
| [LHTM-OPT](https://aws.amazon.com/jp/blogs/psa/how-to-deploy-japanese-llm-lhtm-opt-on-aws-marketplace-developed-by-alt/) | | オルツ | AWS Marketplace |
| [tsuzumi](https://www.nttdata.com/global/ja/news/topics/2024/112000/)<br>([tsuzumi-7b](https://learn.microsoft.com/ja-jp/azure/ai-studio/how-to/deploy-models-tsuzumi)) | | NTT | Azure AI Foundry |


<a id="autoencoding"></a>
## 入力テキストの処理に主に使うモデル

<a id="autoencoding-general"></a>
### 汎用

|    |  アーキテクチャ  |  入力で扱えるトークン数  |  学習テキスト  |  開発元  | ライセンス | HuggingFace ですぐ使える？ [^4]  |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| [ModernBERT-Ja](https://huggingface.co/sbintuitions/modernbert-ja-310m) | ModernBERT | **8,192** | 日本語・英語データ | SB Intuitions | MIT | ◯ ([30m](https://huggingface.co/sbintuitions/modernbert-ja-30m), [70m](https://huggingface.co/sbintuitions/modernbert-ja-70m), [130m](https://huggingface.co/sbintuitions/modernbert-ja-130m), [310m](https://huggingface.co/sbintuitions/modernbert-ja-310m)) |
|  [京大BERT](https://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)  |  BERT (base, large)  | 512 |  日本語 Wikipedia (約1,800万文)  |  京大 言語メディア研究室  | Apache 2.0 | △ |
|  [東北大BERT](https://github.com/cl-tohoku/bert-japanese)  |  BERT (base, large)  | 512 |  base (v1):<br>日本語 Wikipedia 約1,700万文 (2.6GB)<br>base (v2) & large:<br>日本語 Wikipedia 約3,000万文 (4.0GB)<br>base (v3) & large (v2):<br>日本語 Wikipedia 約3,400万文 (4.9GB)<br>+ 日本語 CC-100 約3億9,200万文 (74.3GB)   |  東北大<br>自然言語処理研究グループ | base (v1, v2) & large: CC BY-SA 3.0<br>base (v3) & large (v2): Apache 2.0 |◯ ([base (v1)](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking), [base (v1, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking), [base (v2)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2), [base (v2, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2), [large](https://huggingface.co/tohoku-nlp/bert-large-japanese), [large (文字レベル)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char), [base (v3)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3), [base (v3, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3), [large (v2)](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2), [large (v2, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char-v2)) |
| [TohokuNLP BERT-alpha 500M](https://huggingface.co/tohoku-nlp/tohokunlp-bert-500m-sq8192-alpha)  | Llama ベースのエンコーダ[^23] | **4,096**<br>または<br>**8,192** | [llm-jp-corpus-v3](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v3) の日本語サブセット | 東北大<br>自然言語処理研究グループ | Apache 2.0 | ◯ ([sq4096-alpha](https://huggingface.co/tohoku-nlp/tohokunlp-bert-500m-sq4096-alpha), [sq8192-alpha](https://huggingface.co/tohoku-nlp/tohokunlp-bert-500m-sq8192-alpha)) |
| [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/index.html)   |  BERT (base)  | 512 |  日本語 Wikipedia  |  NICT  | CC BY 4.0 | △ |
| [Laboro BERT](https://github.com/laboroai/Laboro-BERT-Japanese) | BERT (base, large) | 512 | 日本語 Web コーパス <br> (ニュースサイトやブログなど<br>計4,307のWebサイト、2,605,280ページ (12GB)) | Laboro.AI | CC BY-NC 4.0 | ✕ |
| [colorfulscoop BERT](https://huggingface.co/colorfulscoop/bert-base-ja) | BERT (base) | 512 | 日本語 Wikipedia | Colorful Scoop | CC BY-SA 3.0 | [◯](https://huggingface.co/colorfulscoop/bert-base-ja) |
| [東大BERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small) | 512 | 日本語 Wikipedia (約2,000万文 (2.9GB)) | 東大 和泉研 | CC BY-SA 4.0 | [◯](https://huggingface.co/izumi-lab/bert-small-japanese) |
| [chiTra (Sudachi Transformers)](https://www.worksap.co.jp/news/2022/0225/) | BERT (base) | 512 | 国語研日本語ウェブコーパス (NWJC) (148GB) | NINJAL, ワークス徳島人工知能NLP研 | Apache 2.0 | △ |
| [ACCMS BERT](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) | BERT (base) | 512 | 日本語 Wikipedia (3.3GB) | 京大 ACCMS | CC BY-SA 4.0 | [◯](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) |
| [日立BERT](https://aclanthology.org/2023.acl-srw.5.pdf) | BERT (base) | 512 | 日本語 Wikipedia <br>+ Japanese CC-100 | 日立製作所 | CC BY-NC-SA 4.0 | [◯](https://huggingface.co/hitachi-nlp/bert-base-japanese_jumanpp-bpe) [^6] |
| [RetrievaBERT](https://note.com/retrieva/n/n715bea2c2cd1) | BERT [^5] | **2,048** | Japanese CommonCrawl, RefinedWeb, Chinese Wikipedia, Korean Wikipedia, The Stack | レトリバ | Apache 2.0 | [◯](https://huggingface.co/retrieva-jp/bert-1.3b) |
| [Bandai Namco DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp/blob/main/docs/GUIDE.md) | DistilBERT | 512 | - （東北大BERT(base) を親モデルとして知識蒸留） | Bandai Namco Research | MIT | [◯](https://huggingface.co/bandainamco-mirai/distilbert-base-japanese) |
| [Laboro DistilBERT](https://github.com/laboroai/Laboro-DistilBERT-Japanese) | DistilBERT | 512 | - （Laboro BERT(base) を親モデルとして知識蒸留）| Laboro.AI | CC BY-NC 4.0 | [◯](https://huggingface.co/laboro-ai/distilbert-base-japanese) |
| [LINE DistilBERT](https://engineering.linecorp.com/ja/blog/line-distilbert-high-performance-fast-lightweight-japanese-language-model) | DistilBERT | 512 | - （LINE社内のBERTを親モデルとして知識蒸留）| LINE | Apache 2.0 | [◯](https://huggingface.co/line-corporation/line-distilbert-base-japanese) |
| [rinna RoBERTa](https://rinna.co.jp/news/2021/08/20210825.html) | RoBERTa (base) | 512 |  日本語 Wikipedia <br>+ Japanese CC-100 | rinna | MIT | [◯](https://huggingface.co/rinna/japanese-roberta-base) |
| [早大RoBERTa](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) | RoBERTa (base, large) | 512 | 日本語 Wikipedia <br>+ Japanese CC-100 | 早大 河原研 | CC BY-SA 4.0 | ◯ ([base](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp), [large](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp), [large (seq512)](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512-with-auto-jumanpp)) [^7] |
| [インフォマティクスRoBERTa](https://www.informatix.co.jp/pr-roberta/) | RoBERTa (base) | 512 | 日本語 Wikipedia<br> + Web 上の記事 (計25GB) | インフォマティクス | Apache 2.0 | △ |
| [京大RoBERTa](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) | RoBERTa (base, large) | 512 | 日本語 Wikipedia <br>+ Japanese CC-100 | 京大 言語メディア研究室 | CC BY-SA 4.0 | ◯ ([base (文字レベル)](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm), [large (文字レベル)](https://huggingface.co/ku-nlp/roberta-large-japanese-char-wwm)) |
| [横浜国大RoBERTa](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) | RoBERTa (base) | 512 | 日本語 Wikipedia (3.45GB) | 横浜国大 森研 | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) |
| [Megagon Labs RoBERTa](https://huggingface.co/megagonlabs/roberta-long-japanese) | RoBERTa (base) [^8] | **1,282** | Japanese mC4 (約2億文) | Megagon Labs <br> (リクルート) | MIT | [◯](https://huggingface.co/megagonlabs/roberta-long-japanese)  |
| [ACCMS RoBERTa](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) | RoBERTa (base) | 512 | 日本語 Wikipedia (3.3GB) + Japanese CC-100 (70GB) | 京大 ACCMS | CC BY-SA 4.0 | [◯](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) |
| [シナモンELECTRA](https://cinnamon.ai/ideas/20200619_research_001/) | ELECTRA (small) | 512 | 日本語 Wikipedia | シナモン | Apache 2.0 | [◯](https://huggingface.co/Cinnamon/electra-small-japanese-discriminator)  |
| [Megagon Labs ELECTRA](https://www.recruit.co.jp/newsroom/pressrelease/2021/0826_9293.html) | ELECTRA (base) | 512 | Japanese mC4 (約2億文) | Megagon Labs <br> (リクルート) | MIT | [◯](https://huggingface.co/megagonlabs/electra-base-japanese-discriminator)  |
| [東大ELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small, base) | 512 | 日本語 Wikipedia (約2,000万文 (2.9GB)) | 東大 和泉研 | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/electra-small-japanese-discriminator), [base](https://huggingface.co/izumi-lab/electra-base-japanese-discriminator))  |
| [日本語RoFormer](https://huggingface.co/ganchengguang/Roformer-base-japanese) | RoFormer (base) | 512 | 日本語 Wikipedia (3.45GB) | 横浜国大 森研 | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/Roformer-base-japanese) |
| [日本語LUKE](https://www.ousia.jp/ja/page/ja/2022/11/17/luke-japanese/) | LUKE (base, large) | 512 | 日本語 Wikipedia | Studio Ousia | Apache 2.0 | ◯ ([base](https://huggingface.co/studio-ousia/luke-japanese-base-lite), [large](https://huggingface.co/studio-ousia/luke-japanese-large-lite)) |
| [京大DeBERTaV2](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | DeBERTaV2 (tiny, base, large) | 512 | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR<br>（計171GB） | 京大 言語メディア研究室 | CC BY-SA 4.0 | ◯ ([tiny](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese), [tiny (文字レベル)](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm), [base](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), [large](https://huggingface.co/ku-nlp/deberta-v2-large-japanese)) |
| [京大DeBERTaV3](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) | DeBERTaV3 (base) | 512 | [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | 京大 言語メディア研究室 | Apache 2.0 | [◯](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) |
| [東大DeBERTaV2](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | DeBERTaV2 (small, base) | 512 | 日本語 Wikipedia, 日本語 Wikinews, Japanese CC-100, Japanese mC4, Japanese OSCAR | 東大 和泉研 | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/deberta-v2-small-japanese), [base](https://huggingface.co/izumi-lab/deberta-v2-base-japanese)) |
| [GLOBIS DeBERTaV3](https://qiita.com/akeyhero/items/d7c215ceac37b7d3290a) | DeBERTaV3 (xsmall, base, large) | 512 | Wikipedia, WikiBooks, 青空文庫, Japanese CC-100, Japanese mC4, Japanese OSCAR | グロービス | CC BY-SA 4.0 | ◯ ([xsmall](https://huggingface.co/globis-university/deberta-v3-japanese-xsmall), [base](https://huggingface.co/globis-university/deberta-v3-japanese-base), [large](https://huggingface.co/globis-university/deberta-v3-japanese-large)) |
| [日本語BigBird](https://huggingface.co/nlp-waseda/bigbird-base-japanese) | BigBird (base) | **4,096** | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | 早大 河原研 | CC BY-SA 4.0 | [◯](https://huggingface.co/nlp-waseda/bigbird-base-japanese) |
| [日本語LayoutLM](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/Q2-7.pdf) | LayoutLM (base) | 512 | 東北大BERT (base, v2) で重みを初期化した上で、日本語 Wikipedia の文章とレイアウトで事前学習 | 日本総合研究所 | CC BY-SA 3.0 | [◯](https://huggingface.co/jri-advtechlab/layoutlm-wikipedia-ja) |

<a id="autoencoding-domain-specific"></a>
### ドメイン特化型

|    |  ドメイン  |  アーキテクチャ  |  学習テキスト  |  開発元  | ライセンス | HuggingFace ですぐ使える？  |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| [日本語ブログELECTRA](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E2-5.pdf) | 口語 | ELECTRA (small) | 日本語ブログコーパス（3億5,400万文） | 北見工大 桝井・プタシンスキ研 | CC BY-SA 4.0 | [◯](https://huggingface.co/ptaszynski/yacis-electra-small-japanese)  |
| [日本語話し言葉BERT](https://retrieva.jp/news/date_202103151100/) | 話し言葉 | BERT (base) | 東北大BERTに対して日本語話し言葉コーパス（CSJ）を用いて追加学習<br>（DAPTモデルでは国会議事録データも使用） | レトリバ | Apache 2.0 | [◯](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) |
| [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | 学術 | RoBERTa (base) | CiNii の日本語論文 (約628万文) | 愛媛大 人工知能研究室 | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicRoBERTa) |
| [local-politics-BERT](http://local-politics.jp/%e5%85%ac%e9%96%8b%e7%89%a9/local-politics-bert/) | 政治 | BERT (base) | Wikipedia, 国会会議録, 地方議会会議録 | 地方議会会議録コーパスプロジェクト | CC BY-SA 4.0 | ◯ ([SC-min](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-scratch), [SC-minwiki](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-wikipedia-scratch), [SC-2M-wiki](https://huggingface.co/local-politics-jp/bert-base-japanese-wikipedia-scratch-2m), [SC-2M-min](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-scratch-2m), [SC-2M-minwiki](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-wikipedia-scratch-2m), [FP-min](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-further), [FP-minwiki](https://huggingface.co/local-politics-jp/bert-base-japanese-minutes-wikipedia-further)) [^18] |
| [UBKE-LUKE](https://tech.uzabase.com/entry/2024/12/24/173942) | 経済 | LUKE (base) | 日本語 Wikipedia, 有価証券報告書, 経済ニュース記事 | ユーザベース | CC BY-NC | [◯](https://huggingface.co/uzabase/UBKE-LUKE) |
| [日本語金融BERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | 金融 | BERT (small, base) [^9] | 日本語 Wikipedia<br> + 日本語金融コーパス (約2,700万文 (5.2GB)) | 東大 和泉研 | CC BY-SA 4.0 |◯ ([small](https://huggingface.co/izumi-lab/bert-small-japanese-fin), [base](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional)) |
| [日本語金融ELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | 金融 | ELECTRA (small) | 日本語 Wikipedia (約2,000万文 (2.9GB)) <br> + 日本語金融コーパス (約2,700万文 (5.2GB)) | 東大 和泉研 | CC BY-SA 4.0 |  [◯](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator)  |
| [日本語ニュースBERT](https://qiita.com/mkt3/items/3c1278339ff1bcc0187f) | ビジネス | BERT (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | CC BY 4.0 | △ |
| [日本語ニュースXLNet](https://qiita.com/mkt3/items/4d0ae36f3f212aee8002) |  ビジネス  | XLNet (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | ？ | ※ 非公式の HuggingFace 向けに変換されたモデルが[公開されている](https://huggingface.co/hajime9652/xlnet-japanese) |
| [日本語ニュースALBERT](https://qiita.com/mkt3/items/b41dcf0185e5873f5f75) | ビジネス  | ALBERT (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | ？ | △ |
| [みんぱくBERT](https://proceedings-of-deim.github.io/DEIM2022/papers/F43-4.pdf) | 文化財 | BERT (base) | 東北大BERTに対して国立民族学博物館の文化財データで追加学習 | 兵庫県立大学 大島研 | MIT | ◯ ([minpaku-v1](https://huggingface.co/ohshimalab/bert-base-minpaku-v1), [minpaku-v3](https://huggingface.co/ohshimalab/bert-base-minpaku-v3), [minpaku-v3-no-additional-token](https://huggingface.co/ohshimalab/bert-base-minpaku-v3-no-additional-token)) |
| [UTH-BERT](https://ai-health.m.u-tokyo.ac.jp/home/research/uth-bert) | 医療 | BERT (base) | 日本語診療記録(約1億2,000万行) | 東大病院 <br>医療AI開発学講座 | CC BY-NC-SA 4.0 | △ |
| [medBERTjp](https://github.com/ou-medinfo/medbertjp) | 医療 | BERT (base) | 日本語 Wikipedia <br> + 日本語医療コーパス（『今日の診療プレミアム』Web版） | 阪大病院 <br> 医療情報学研究室 | CC BY-NC-SA 4.0 | △ |
| [JMedRoBERTa](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf) | 医療 | RoBERTa (base) | 日本語医学論文 (約1,100万文 (1.8GB)) | NII 相澤研 | CC BY-NC-SA 4.0 | ◯ ([万病WordPiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece), [SentencePiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece)) [^10] |

<a id="embeddings"></a>
## 埋め込み (Embeddings) 作成に特化したモデル [^21]

### Bi-Encoders

#### Single-representation bi-encoders

|    | 入力で扱えるトークン数 | 開発元  |  ライセンス |
|:---|:---:|:---:|:---:|
| [Ruri-v3](https://huggingface.co/collections/cl-nagoya/ruri-v3-67f382536e80902074ec6252)<br>([v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m), [v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m), [v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m), [v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m)) | 8,192 | 名大 笹野研 | Apache 2.0 |
| [sbintuitions/sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) | 8,192 | SB Intuitions | Sarashina Model NonCommercial License |
| [AMBER](https://retrieva.jp/news/202503101100/)<br>([base](https://huggingface.co/retrieva-jp/amber-base), [large](https://huggingface.co/retrieva-jp/amber-large)) | 512 | レトリバ | Apache 2.0 |
| [RoSEtta](https://prtimes.jp/main/html/rd/p/000000169.000022705.html)<br>([base-ja](https://huggingface.co/pkshatech/RoSEtta-base-ja)) | 1,024 | PKSHA Technology | Apache 2.0 |
| [GLuCoSE v2](https://prtimes.jp/main/html/rd/p/000000169.000022705.html)<br>([base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2)) | 512 | PKSHA Technology | Apache 2.0 |
| [Ruri](https://arxiv.org/abs/2409.07737)<br>([small](https://huggingface.co/cl-nagoya/ruri-small), [base](https://huggingface.co/cl-nagoya/ruri-base), [large](https://huggingface.co/cl-nagoya/ruri-large), [small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2), [base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2), [large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2)) | 512 | 名大 笹野研 | Apache 2.0 |
| [Japanese SimCSE](https://github.com/hppRC/simple-simcse-ja)<br>([unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base), [unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large), [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base), [sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large)) | 512 | 名大 笹野研 | CC BY-SA 4.0 |
| [GLuCoSE](https://prtimes.jp/main/html/rd/p/000000123.000022705.html)<br>([base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja)) | 512 | PKSHA Technology | Apache 2.0 |
| [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) || Colorful Scoop | CC BY-SA 4.0 |
| [MU-Kindai/SBERT-JSNLI-base](https://huggingface.co/MU-Kindai/SBERT-JSNLI-base)<br>[MU-Kindai/SBERT-JSNLI-large](https://huggingface.co/MU-Kindai/SBERT-JSNLI-large) || 近畿大学 (研究室不明) | ？ |
| [MU-Kindai/Japanese-SimCSE-BERT-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-unsup)<br>[MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-base-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-sup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-sup) || 近畿大学 (研究室不明) | MIT |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) || PKSHA Technology | CC BY-SA 4.0 |
| [MU-Kindai/Japanese-MixCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-base)<br>[MU-Kindai/Japanese-MixCSE-BERT-large](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-large) || 近畿大学 (研究室不明) | MIT |
| [MU-Kindai/Japanese-DiffCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-DiffCSE-BERT-base) || 近畿大学 (研究室不明) | MIT |
| [bclavie/fio-base-japanese-v0.1](https://huggingface.co/bclavie/fio-base-japanese-v0.1) || 個人 ([Benjamin Clavié](https://scholar.google.com/citations?user=vuMln98AAAAJ)) | |
| [cl-nagoya/shioriha-large-pt](https://huggingface.co/cl-nagoya/shioriha-large-pt) || 名大 笹野研 | |

#### Multi-representation bi-encoders

|    |  開発元  |  ライセンス |
|:---|:---:|:---:|
| [JaColBERTv2.5](https://www.answer.ai/posts/2024-08-02-jacolbert-v25.html)<br>([JaColBERTv2.4](https://huggingface.co/answerdotai/JaColBERTv2.4), [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5)) | Answer.AI | MIT |
| [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2)<br>([JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2)) | 個人 ([Benjamin Clavié](https://scholar.google.com/citations?user=vuMln98AAAAJ)) | MIT |
| [JaColBERT](https://arxiv.org/pdf/2312.16144.pdf)<br>([JaColBERT](https://huggingface.co/bclavie/JaColBERT)) | 個人 ([Benjamin Clavié](https://scholar.google.com/citations?user=vuMln98AAAAJ)) | MIT |

### Cross-Encoders

|    |  開発元  |  ライセンス |
|:---|:---:|:---:|
| [Ruri-v3 Reranker](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m)<br>([310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m)) | 名大 笹野研 | Apache 2.0 |
| [Ruri-Reranker](https://arxiv.org/abs/2409.07737)<br>([stage1-small](https://huggingface.co/cl-nagoya/ruri-reranker-stage1-small), [stage1-base](https://huggingface.co/cl-nagoya/ruri-reranker-stage1-base), [stage1-large](https://huggingface.co/cl-nagoya/ruri-reranker-stage1-large), [small](https://huggingface.co/cl-nagoya/ruri-reranker-small), [base](https://huggingface.co/cl-nagoya/ruri-reranker-base), [large](https://huggingface.co/cl-nagoya/ruri-reranker-large)) | 名大 笹野研 | Apache 2.0 |
| [hotchpotch/japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1)<br>[hotchpotch/japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1)<br>[hotchpotch/japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1)<br>[hotchpotch/japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1)<br>[hotchpotch/japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) | 個人 (舘野祐一) | MIT |

<a id="multimodal"></a>
## 視覚言語モデル (Vision-Language Models)

<a id="multimodal-text-generation"></a>
### 画像+テキストからのテキスト生成

#### スクラッチ学習モデル

**汎用**

|    |  アーキテクチャ |  学習画像/テキスト  |  開発元  | ライセンス / 利用規約 |
|:---|:---:|:---:|:---:|:---:|
| [Sarashina2-Vision](https://www.sbintuitions.co.jp/blog/entry/2025/03/17/111659)<br>([8b](https://huggingface.co/sbintuitions/sarashina2-vision-8b), [14b](https://huggingface.co/sbintuitions/sarashina2-vision-14b)) | Sarashina2 + Qwen2-VL + 2-layer MLP || SB Intuitions | MIT |
| [Asagi](https://uehara-mech.github.io/asagi-vlm?v=1)<br>([2B](https://huggingface.co/MIL-UT/Asagi-2B), [4B](https://huggingface.co/MIL-UT/Asagi-4B), [8B](https://huggingface.co/MIL-UT/Asagi-8B), [14B](https://huggingface.co/MIL-UT/Asagi-14B)) | LLaVA || 東大 原田研 | Apache 2.0 |
| [llava-calm2-siglip](https://www.cyberagent.co.jp/news/detail/id=30344)<br>([llava-calm2-siglip](https://huggingface.co/cyberagent/llava-calm2-siglip)) | LLaVA | MS-COCO と VisualGenome から生成された対話データ | サイバーエージェント | Apache 2.0 |
| [LLM-jp-3 VILA 14B](https://llmc.nii.ac.jp/topics/llm-jp-3-vila-14b/)<br>([14b](https://huggingface.co/llm-jp/llm-jp-3-vila-14b)) | LLaVA | [Japanese image text pairs](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-japanese-image-text-pairs), LLaVA-Pretrain, [Japanese interleaved data](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-japanese-interleaved-data), coyo (subset), mmc4-core (subset), [llava-instruct-ja](https://huggingface.co/datasets/llm-jp/llava-instruct-ja), [japanese-photos-conv](https://huggingface.co/datasets/llm-jp/japanese-photos-conversation), ja-vg-vqa, synthdog-ja, LLaVA-1.5 instruction data (subset) | 大規模言語モデル研究開発センター | Apache 2.0 & OpenAI Terms of Use |
| [Heron](https://github.com/turingmotors/heron/blob/main/docs/README_JP.md)<br>([blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0), [blip-ja-stablelm-base-7b-v1](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1), [blip-ja-stablelm-base-7b-v1-llava-620k](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1-llava-620k), [git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0), [git-ELYZA-fast-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ELYZA-fast-7b-v0), [git-ja-stablelm-base-7b-v1](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v1)) | BLIP-2 または GIT | v1: LLaVA-Instruct-150K-JA または LLaVA-Instruct-620K-JA<br>v0: LLaVA-Instruct-150K-JA, Japanese STAIR Captions, Japanese Visual Genome VQA dataset | Turing | CC BY-NC 4.0 |
| [Japanese Stable VLM](https://ja.stability.ai/blog/japanese-stable-vlm)<br>([japanese-stable-vlm](https://huggingface.co/stabilityai/japanese-stable-vlm)) | LLaVA | Japanese CC12M, STAIR Captions, Japanese Visual Genome VQA dataset | Stability AI | STABILITY AI JAPANESE STABLE VLM COMMUNITY LICENSE |
| [Japanese InstructBLIP Alpha](https://ja.stability.ai/blog/japanese-instructblip-alpha)<br>([japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha)) | InstructBLIP | Japanese CC12M, STAIR Captions, Japanese Visual Genome VQA dataset | Stability AI | JAPANESE STABLELM RESEARCH LICENSE |
| [rinna MiniGPT-4](https://rinna.co.jp/news/2023/07/20230731.html)<br>([bilingual-gpt-neox-4b-minigpt4](https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4)) | MiniGPT-4 | CC12M, COCO 2014, Visual Genome, STAIR Captions, Japanese Visual Genome VQA dataset | rinna | MIT |

**ドメイン特化型**

|    |  アーキテクチャ  |  ドメイン | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm) | LLaVA | 大喜利 | わたしは | Llama 2 Community License |

#### 海外モデルに日本語で追加学習を行ったモデル

|    |  ベースのVLM  |  学習画像/テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [AXCXEPT/EZO-InternVL2-26B](https://huggingface.co/AXCXEPT/EZO-InternVL2-26B) | InternVL2 | - | 　Axcxept | MIT |

#### 複数のVLM・LLMをマージして作成されたモデル

|    |  マージ元のLLM・VLM（太字は日本語LLM）  | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|
| [Llama-3-EvoVLM-JP-v2](https://sakana.ai/evovlm-jp/)<br>([v2](https://huggingface.co/SakanaAI/Llama-3-EvoVLM-JP-v2)) | Mantis-8B-SigLIP-Llama-3, **Llama-3-ELYZA-JP-8B**, Bunny-v1.1-Llama-3-8B-V | Sakana AI | Llama 3 Community License |
| [AXCXEPT/Llama-3-EZO-VLM-1](https://huggingface.co/AXCXEPT/Llama-3-EZO-VLM-1) | - (Llama-3-EvoVLM-JP-v2 に対して追加学習) | Axcxept | Llama 3 Community License |
| [EvoVLM-JP](https://sakana.ai/evolutionary-model-merge-jp/)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoVLM-JP-v1-7B)) | **Shisa Gamma 7B (v1)**, LLaVA-1.6-Mistral-7B | Sakana AI | Apache 2.0 |

<a id="multimodal-text-to-image"></a>
### テキストからの画像生成

<a id="multimodal-text-to-image-general"></a>
#### 汎用

|    |  アーキテクチャ  |  学習画像/テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [CommonArt β](https://note.com/aipicasso/n/nf17f876839b2)<br>([commonart-beta](https://huggingface.co/aipicasso/commonart-beta)) | PixArt-Σ | CommonCatalog-cc-by, Megalith-10M, Smithonian Open Access, ArtBench (CC-0 only) | AI Picasso | Apache 2.0 |
| [EvoSDXL-JP](https://sakana.ai/evosdxl-jp/)<br>([v1](https://huggingface.co/SakanaAI/EvoSDXL-JP-v1)) | Stable Diffusion | - （Japanese Stable Diffusion XL を含む複数の画像生成モデルをマージ） | Sakana AI | Apache 2.0[^14] |
| [Japanese Stable Diffusion XL](https://ja.stability.ai/blog/japanese-stable-diffusion-xl)<br>([japanese-stable-diffusion-xl](https://huggingface.co/stabilityai/japanese-stable-diffusion-xl)) | Stable Diffusion | 不明 | Stability AI | STABILITY AI JAPANESE STABLE DIFFUSION XL COMMUNITY LICENSE |
| [東北大Stable Diffusion](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0)<br>([base](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0), [refiner](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-refiner-1.0)) | Stable Diffusion | WMT2023 Shared Task の日英対訳コーパス、laion2B-multi のキャプション約 1,300 万件 | 東北大<br>自然言語処理研究グループ | CreativeML OpenRAIL-M License |
| [rinna Stable Diffusion](https://rinna.co.jp/news/2022/09/20220909.html)<br>([japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion)) | Stable Diffusion |  LAION-5B データセットのうちキャプションが日本語のもの（画像約 1 億枚）| rinna | CreativeML OpenRAIL-M License |

<a id="multimodal-text-to-image-domain-specific"></a>
#### ドメイン特化型

|    |  アーキテクチャ  |  ドメイン  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Evo-Nishikie](https://sakana.ai/evo-ukiyoe/)<br>([v1](https://huggingface.co/SakanaAI/Evo-Nishikie-v1)) | Stable Diffusion (ControlNet) | 浮世絵 | Sakana AI | Apache 2.0[^14] |
| [Evo-Ukiyoe](https://sakana.ai/evo-ukiyoe/)<br>([v1](https://huggingface.co/SakanaAI/Evo-Ukiyoe-v1)) | Stable Diffusion | 浮世絵 | Sakana AI | Apache 2.0[^14] |

### テキストからの動画生成

| | アーキテクチャ | 学習データ | 開発元 | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [AIdeaLab VideoJP](https://aidealab.com/news/QSvdcQfA)<br>([AIdeaLab-VideoJP](https://huggingface.co/aidealab/AIdeaLab-VideoJP)) | CogVideoX | Pixabay, FineVideo | AIdeaLab | Apache 2.0 |

<a id="multimodal-others"></a>
### その他

|    |  アーキテクチャ  |  学習画像/テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [llm-jp-clip](https://huggingface.co/llm-jp/llm-jp-clip-vit-base-patch16)<br>([llm-jp-clip-vit-base-patch16](https://huggingface.co/llm-jp/llm-jp-clip-vit-base-patch16), [llm-jp-clip-vit-large-patch14](https://huggingface.co/llm-jp/llm-jp-clip-vit-large-patch14)) | CLIP | ReLAION-5Bの英語サブセットのキャプション約15億件の翻訳 | 大規模言語モデル研究開発センター | Apache 2.0 |
| [LINEヤフーCLIP](https://techblog.lycorp.co.jp/ja/20240514b)<br>([clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base)) | CLIP | CommonCrawl, CC12M, YFCC100M | LINEヤフー | Apache 2.0 |
| [リクルートCLIP](https://blog.recruit.co.jp/data/articles/japanese-clip/)<br>([japanese-clip-vit-b-32-roberta-base](https://huggingface.co/recruit-jp/japanese-clip-vit-b-32-roberta-base)) | CLIP | laion2B-multi のキャプション約1億2000万件 | リクルート | CC BY-4.0 |
| [Japanese Stable CLIP](https://ja.stability.ai/blog/japanese-stable-clip)<br>([japanese-stable-clip-vit-l-16](https://huggingface.co/stabilityai/japanese-stable-clip-vit-l-16)) | SigLIP | CC12M のキャプションを日本語に翻訳したもの、STAIR Captions | Stability AI | STABILITY AI JAPANESE STABLE CLIP COMMUNITY LICENSE |
| [rinna CLIP](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16)) | CLIP | CC12M のキャプションを日本語に翻訳したもの | rinna | Apache 2.0 |
| [rinna CLOOB](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16)) | CLOOB | CC12M のキャプションを日本語に翻訳したもの | rinna | Apache 2.0 |
| [博報堂テクノロジーズCLIP](https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/B6-5.pdf)<br>([base](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-base), [deeper](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-deeper), [wider](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-wider)) | CLIP | laion2B-multi のキャプション約1億2000万件 | 博報堂テクノロジーズ | CC BY-NC-SA 4.0 |

<a id="speech"></a>
## 音声言語モデル (Speech-Language Models)

<a id="speech-asr"></a>
### 音声認識

|    |  アーキテクチャ  |  学習コーパス  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Kotoba-Whisper](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0)<br>([v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0), [v1.0-ggml](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0-ggml), [v1.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0-faster), [v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1), [bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0), [bilingual-v1.0-ggml](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0-ggml), [bilingual-v1.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0-faster), [v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0), [v2.0-ggml](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-ggml), [v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster), [v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1), [v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2)) | Distil-Whisper | ReazonSpeech<br>(+ Multilingual LibriSpeech) | Kotoba Technologies | Apache 2.0 |
| [Nue ASR](https://rinna.co.jp/news/2023/12/20231207.html)<br>([nue-asr](https://huggingface.co/rinna/nue-asr)) | Nue ASR<br>(HuBERT + LLM) | ReazonSpeech | rinna | Apache 2.0 |
| [ReazonSpeech](https://research.reazon.jp/projects/ReazonSpeech/)<br>([espnet-v1](https://huggingface.co/reazon-research/reazonspeech-espnet-v1), [espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next), [espnet-v2](https://huggingface.co/reazon-research/reazonspeech-espnet-v2), [nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2)) | ESPnet (Conformer-Transducer) または NeMo (FastConformer-RNNT) | ReazonSpeech | レアゾン・ホールディングス | Apache 2.0 |

<a id="speech-others"></a>
### その他

|    |  アーキテクチャ  |  学習コーパス  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [J-Moshi](https://github.com/nu-dialogue/j-moshi)<br>([j-moshi](https://huggingface.co/nu-dialogue/j-moshi), [j-moshi-ext](https://huggingface.co/nu-dialogue/j-moshi-ext)) | Transformerベースのテキスト・音声基盤モデル (Moshi) | 音声対話コーパス（J-CHAT, 日本語Callhome, CSJ, 旅行代理店対話コーパス, 独自の雑談対話コーパス, 独自の相談対話コーパス）, テキスト対話コーパス（日本語PersonaChat, 日本語EmpatheticDialogues, 日本語日常対話コーパス, RealPersonaChat） | 名大 東中研 | CC BY-NC 4.0 |
| [Kotoba-Speech](https://huggingface.co/kotoba-tech/kotoba-speech-v0.1)<br>([v0.1](https://huggingface.co/kotoba-tech/kotoba-speech-v0.1)) | Transformer | 不明 | Kotoba Technologies | Apache 2.0 |
| [くしなだ](https://www.aist.go.jp/aist_j/press_release/pr2025/pr20250310/pr20250310.html)<br>([base](https://huggingface.co/imprt/kushinada-hubert-base), [large](https://huggingface.co/imprt/kushinada-hubert-large)) | HuBERT | 約6万時間の日本語テレビ放送音声 | 産総研 知的メディア処理研究チーム | Apache 2.0 |
| [東大HuBERT](https://huggingface.co/sarulab-speech/hubert-base-jtube)<br>([base-jtube](https://huggingface.co/sarulab-speech/hubert-base-jtube)) | HuBERT | JTubeSpeech | 東大 猿渡・高道研 | MIT |
| [rinna HuBERT](https://rinna.co.jp/news/2023/04/20230428.html)<br>([base](https://huggingface.co/rinna/japanese-hubert-base), [large](https://huggingface.co/rinna/japanese-hubert-large)) | HuBERT | ReazonSpeech | rinna | Apache 2.0 |
| [いざなみ](https://www.aist.go.jp/aist_j/press_release/pr2025/pr20250310/pr20250310.html)<br>([base](https://huggingface.co/imprt/izanami-wav2vec2-base), [large](https://huggingface.co/imprt/izanami-wav2vec2-large)) | wav2vec 2.0 | 約6万時間の日本語テレビ放送音声 | 産総研 知的メディア処理研究チーム | Apache 2.0 |
| [Reazon wav2vec 2.0](https://research.reazon.jp/blog/2024-10-21-Wav2Vec2-base-release.html)<br>([base](https://huggingface.co/reazon-research/japanese-wav2vec2-base), [large](https://huggingface.co/reazon-research/japanese-wav2vec2-large)) | wav2vec 2.0 | ReazonSpeech | レアゾン・ホールディングス | Apache 2.0 |
| [rinna wav2vec 2.0](https://rinna.co.jp/news/2024/03/20240307.html)<br>([base](https://huggingface.co/rinna/japanese-wav2vec2-base)) | wav2vec 2.0 | ReazonSpeech | rinna | Apache 2.0 |

<a id="benchmark-suites"></a>
## 日本語LLM評価ベンチマーク/データセットまとめ

<a id="hybrid-benchmark-suites"></a>
### 複合型ベンチマーク

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [Nejumi LLMリーダーボード3](https://api.wandb.ai/links/wandb-japan/psrsl8gu) | LLM の日本語能力を言語理解能力、応用能力、アライメント（制御性、安全性を含む）の 3 つの観点で評価している。詳しくは[こちらの記事](https://note.com/wandb_jp/n/nd4e54c2020ce)を参照 | Weights & Biases |
| [Swallow LLM Leaderboard](https://swallow-llm.github.io/leaderboard/index-chat.ja.html) | 様々な LLM を日本語理解・生成タスク、日本語マルチターン対話タスク、英語理解・生成タスクの 3 種類から総合的に評価している。また、既存の LLM 評価ツールを統合・改修した評価スクリプトである [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) を合わせて公開している。 | Swallowプロジェクト |

<a id="basic-benchmark-suites"></a>
### 基本的な自然言語処理タスクの性能を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [オープン日本語LLMリーダーボード](https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard) | [llm-jp-eval](#llm-jp-eval) を活用し、16種類のタスクで日本語の大規模言語モデルを評価している。| LLM-jp, Hugging Face |
| <a id="llm-jp-eval"></a> [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | 複数のデータセットを横断して日本語 LLM を自動評価するツールである。<br>対応している全データセット一覧は[こちら](https://github.com/llm-jp/llm-jp-eval/tree/main/src/llm_jp_eval/jaster)から確認できる（この中には JNLI や JCommonsenseQA といった JGLUE のタスクなども含まれている）。 | LLM-jp |
| [JP Language Model Evaluation Harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | Stability AI による [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) のフォーク。複数のデータセットを横断して日本語 LLM を自動評価するツールである。<br>対応している全データセット一覧は[こちら](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable/lm_eval/tasks/ja)から確認できる（この中には JNLI や JCommonsenseQA といった JGLUE のタスクなども含まれている）。<br>rinna による詳細な評価結果まとめがある: [[rinna] Benchmark of Stability-AI/lm-evaluation-harness](https://rinnakk.github.io/research/benchmarks/lm/) | Stability AI |
| [JGLUE](https://github.com/yahoojapan/JGLUE) | [GLUE ベンチマーク](https://gluebenchmark.com/)の日本語版として構築されたベンチマーク。MARC-ja, JCoLA, JSTS, JNLI, JSQuAD, JCommonsenseQA の 6 つのタスクを含む（[JCoLA](https://github.com/osekilab/JCoLA) は東大大関研により作成）。各タスクの詳細は[こちら](https://www.jstage.jst.go.jp/article/jnlp/30/1/30_63/_article/-char/ja)や[こちら](https://techblog.yahoo.co.jp/entry/2022122030379907/)を参照 | 早大 河原研, ヤフー |
| <a id="jmmlu"></a> [JMMLU](https://github.com/nlp-waseda/JMMLU) | [MMLU ベンチマーク](https://github.com/hendrycks/test)の日本語版として構築されたベンチマーク。自然科学・人文科学・社会科学の幅広い学術領域から 4 択問題を構成している。元の MMLU を翻訳しただけでなく、日本独自の文化的背景に基づく問題（日本問題）を新たに追加しているのが特徴である。 | 早大 河原研 |
<!-- | [日本語 Open LLM Leaderboard](http://wandb.me/llm-jp-openllmleaderboard) | Huggingface の [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) と同様の検証を日本語 LLM に対して行ったもの。日本語 LLM の英語タスクにおける性能を確認できる。 | LLM-jp | -->

<a id="open-ended-benchmark-suites"></a>
### テキスト生成能力を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| <a id="jp-mt-bench"></a> [Japanese MT-bench](https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge) | マルチターン会話能力を問う [MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) の日本語版。Writing, Roleplay, Reasoning, Math, Coding, Extraction, STEM, Humanities の 8 つのカテゴリから 10 問ずつ、計 80 問が収録されている。なお、日本語版作成の際には、日本の文化に合うように質問内容に一部修正が加えられている。<br>GPT-4 による 10 段階の絶対評価を行うスクリプトも含まれている。 | Stability AI |
| <a id="elyza-tasks"></a> [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 複雑な指示・タスクを含む100件の日本語データで、全てのデータに対して評価観点がアノテーションされている。<br>要約を修正し修正箇所を説明するタスク、具体的なエピソードから抽象的な教訓を述べるタスク、ユーザーの意図を汲み役に立つAIアシスタントとして振る舞うタスク、場合分けを必要とする複雑な算数のタスク、未知の言語からパターンを抽出し日本語訳する高度な推論を必要とするタスク、複数の指示を踏まえた上でyoutubeの対話を生成するタスク、架空の生き物や熟語に関する生成・大喜利などの想像力が求められるタスクなどが含まれている。 | ELYZA |
| [Preferred Generation Benchmark<br>(pfgen-bench)](https://github.com/pfnet-research/pfgen-bench) | 50 問の日本語圏特有の常識問題をもとに、LLMの日本語生成能力を Fluency(流暢さ)、Truthfulness(真実性)、Helpfulness(有用性)の3つの評価軸から計測するベンチマーク。n-gram やルールベースでの指標の計算を行うことにより、LLM-as-a-Judge を行わずに評価を実施しているのが特徴である。 | Preferred Elements (Preferred Networks) |
| <a id="rakuda-benchmark"></a> [Rakuda Benchmark](https://github.com/yuzu-ai/japanese-llm-ranking) | 日本の地理、歴史、政治、社会に関する[40問の自由質問](https://huggingface.co/datasets/yuzuai/rakuda-questions)に対してモデルに出力を行わせる。GPT-4 が同じ質問に対する2つのモデルの出力を比べ、どちらの答えが優れているかを判断することにより、モデルのランク付けを行う。 | YuzuAI |
| [Japanese Vicuna QA Benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | MT-Bench の前身である [vicuna-blog-eval](https://github.com/lm-sys/vicuna-blog-eval) の日本語版。一般、知識、ロールプレイ、常識、フェルミ推定、反実仮想、コーディング、数学、ライティングに関する 80 問の質問を収録している。また、GPT-4 による自動評価（勝率計算）のスクリプトも含まれている。リーダーボードは[こちら](http://wandb.me/llm-jp-vicunaleaderboard) | 京大 言語メディア研究室 |
| <a id="tengu-bench"></a> [Tengu-Bench](https://huggingface.co/datasets/lightblue/tengu_bench) | 様々なカテゴリから成る 120 問の自由質問が収録されている。質問のカテゴリは以下の通り: 表の読み取り、論理パズル、アイデア生成、Function calling、長い文書要約（千トークン以上）、会話要約、長い文書のClosed QA（千トークン以上）、敬語、プロジェクト作成、数学、翻訳、抽出、倫理的制御、コスト見積、日本、雑談、ダジャレ、フォーマット、建設、ビジネス、法律判断、政治、架空の質問 | Lightblue |
| [Shaberi](https://github.com/lightblue-tech/japanese_llm_eval) | [Japanese MT-bench](#jp-mt-bench)、[Rakuda Benchmark](#rakuda-benchmark)、[ELYZA-tasks-100](#elyza-tasks)、[Tengu-Bench](#tengu-bench) の評価をまとめて行うことができるフレームワーク。なお、Shisa.AI による[フォーク](https://github.com/shisa-ai/shaberi)も存在する | Lightblue |

<a id="domain-specific-benchmark-suites"></a>
### 特定ドメインの性能を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [Japanese Language Model Financial Evaluation Harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | 金融分野における日本語 LLM のベンチマーク。金融分野における感情分析タスク(chabsa)、証券分析における基礎知識タスク(cma_basics)、公認会計士試験における監査に関するタスク(cpa_audit)、ファイナンシャルプランナー試験の選択肢問題のタスク(fp2)、証券外務員試験の模擬試験タスク(security_sales_1)を含む。詳細は[こちら](https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/C6-4.pdf)を参照 | Preferred Networks |
| [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | 金融分野における日本語 LLM の生成能力を測定するためのベンチマーク。 | Preferred Networks |
| [Stockmark Business Questions](https://huggingface.co/datasets/stockmark/business-questions) | 市場動向、時事問題、社会課題、ビジネストレンドなどの知識を問う問題が50題収録されている。 | ストックマーク |
| <a id="jmedllm"></a> [JMED-LLM](https://github.com/sociocom/JMED-LLM) | 日本語医療分野における LLM の評価用データセット。これまでに開発されてきた日本語の医療言語処理タスクを LLM ベンチマーク用にまとめている。 | NAIST ソーシャル・コンピューティング研究室 |
| [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 日本語医療分野の LLM ベンチマーク。選択肢問題、機械翻訳、固有表現抽出、文書分類、文類似度計算の 5 種類、計 20 個のデータセットが収録されている（一部のデータセットは [JMMLU](#jmmlu) の医療分野問題や [JMED-LLM](#jmedllm) から借用されている）。また、JMedBench での評価を簡単に行うためのツール [med-eval](https://github.com/nii-nlp/med-eval) が開発されている。 | NII 相澤研 |
| [Japanese Medical Language Model Evaluation Harness](https://github.com/stardust-coder/japanese-lm-med-harness) | ワンコマンドで実行可能な医療分野に特化したLLMの日英能力評価プログラム。 | 個人 ([​助田一晟](https://scholar.google.co.jp/citations?user=Dc_v0BsAAAAJ)) |
| [karakuri-bench](https://huggingface.co/datasets/karakuri-ai/karakuri-bench-v0.1) | 日本語 LLM のカスタマーサポートにおける性能を測定するためのデータセット。 | カラクリ |

<a id="factuality-safety-benchmark-suites"></a>
### 事実性・安全性を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [JTruthfulQA](https://github.com/nlp-waseda/JTruthfulQA) | LLM の事実性を評価するデータセット [TruthfulQA](https://github.com/sylinrl/TruthfulQA) の日本語版。迷信などの、一部の人々に信じられているが事実とは言えない事象に関する質問群と、日本固有の知識に関する質問群が、一から収集されている。 | 早大 河原研 |
| [JCommonsenseMorality](https://github.com/Language-Media-Lab/commonsense-moral-ja/blob/main/README_JP.md) | 日本語の常識道徳に関するデータセット。行為を表す文に対して、道徳的に間違っているか許容できるかの 2 値ラベルが割り当てられている。 | 北大 言語メディア学研究室 |
| [JBBQ](https://github.com/ynklab/JBBQ_data) | 社会性バイアスQAデータセット [BBQ](https://github.com/nyu-mll/BBQ) を、日本の文化・慣習を踏まえて翻訳、修正、問題追加を行い作成されたデータセット。 | 東大 谷中研 |

<a id="logical-reasoning-benchmark-suites"></a>
### 論理推論能力を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [JFLD (Japanese Formal Logic Deduction)](https://aclanthology.org/2024.lrec-main.832/) | 日本語 LLM の演繹推論能力を問うデータセット（同著者らが提案している [FLD (Formal Logic Deduction)](https://github.com/hitachi-nlp/FLD) の日本語版）。LLM が持つ知識と切り分けて評価を行うために、反実仮想的なサンプルから構成されているのが特徴である。 | 日立製作所 |
| [JHumanEval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) | 英語の指示から Python コードの生成能力を評価するベンチマークである [HumanEval](https://huggingface.co/datasets/openai_humaneval) の日本語版。日本語版を作成する際には、まず機械翻訳にかけたあと、人手での修正を行っている。 | 日本女子大 倉光研 |

<a id="controllabilitiy-benchmark-suites"></a>
### 制約付きの生成能力を測定するベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [LCTG Bench](https://github.com/CyberAgentAILab/LCTG-Bench) | 日本語 LLM の制御性ベンチマーク。出力のフォーマット、文字数、キーワード、NGワードの 4 つの観点から、LLM が制約を守って出力を行えているかを評価する。生成されたテキストの品質も合わせて評価する。 | サイバーエージェント |

<a id="embeddings-benchmark-suites"></a>
### 埋め込みモデルのベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [JMTEB](https://www.sbintuitions.co.jp/blog/entry/2024/05/16/130848) | [MTEB](https://github.com/embeddings-benchmark/mteb)の日本語版として作成されたベンチマーク。<br>文書クラスタリング、文書分類、文間類似度、文ペアラベル予測、文書抽出の5種類のタスクから構成されている（その後、リランキングタスクが新たに追加）。 | SB Intuitions |
| [JQaRA](https://github.com/hotchpotch/JQaRA/) | 日本語の文書抽出・リランキング精度評価のためのデータセット。1,667件の質問文それぞれに対し、候補となる100件のドキュメントが割り当てられており、そのうち1件以上が質問文に回答できる内容になっている。質問文は [JAQKET](https://www.nlp.ecei.tohoku.ac.jp/projects/jaqket/) を、候補のドキュメントは日本語 Wikipedia を用いている。 | 個人 (舘野祐一) |
| [JaCWIR](https://github.com/hotchpotch/JaCWIR) | Wikipedia 以外のドメインで文書抽出・リランキングの評価を行えることを目指して作成されたデータセット。5,000件の質問文それぞれに対し、その質問文が作成される元になった 1 件の Webページと、質問文とは関係のない 99 件の Web ページが割り当てられている。| 個人 (舘野祐一) |

<a id="vl-benchmark-suites"></a>
### 視覚言語モデル (Vision-Language Models) のベンチマーク/データセット

|   | 説明 | 開発元 |
|:---|:---|:---:|
| [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | 日本語VLMの性能を複数のベンチマークタスクで評価するためのツール | 大規模言語モデル研究開発センター |
| [JMMMU](https://mmmu-japanese-benchmark.github.io/JMMMU/) | [MMMU ベンチマーク](https://mmmu-benchmark.github.io/)の日本語版として構築されたベンチマーク。720 件の MMMU の翻訳版の問題と 600 件の日本文化特有の新規の問題から構成される。 | 東大 相澤研 |
| [JDocQA](https://github.com/mizuumi/JDocQA) | 日本語ドキュメント（パンフレット、スライド、レポート、Web サイト）をもとに構築された、合計 11,600 件の質問から構成される質問応答データセット。解答不能問題を含め、様々な質問形式の質問が収録されている。 | NAIST 渡辺研 |
| [Heron VLM リーダーボード powered by nejumi@WandB](https://api.wandb.ai/links/vision-language-leaderboard/h2lxge4n) | [Japanese-Heron-Bench](#japanese-heron-bench) と [LLaVA-Bench-In-the-Wild (Japanese)](#llava-bench-in-the-wild) の評価結果をまとめている。 | Turing, Weights & Biases |
| <a id="japanese-heron-bench"></a> [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) | 21 枚の画像に対して計 102 問の質問が割り当てられている。日本に関する知識を要求する画像・質問になっているのが特徴である。 | Turing |
| [JA-VLM-Bench-In-the-Wild](https://huggingface.co/datasets/SakanaAI/JA-VLM-Bench-In-the-Wild) | Sakana AI が EvoVLM-JP-v1-7B の評価のために独自に用意したデータセット。42 枚の画像に対して計 50 問の質問が割り当てられている。日本に関する知識を要求する画像・質問になっているのが特徴である。 | Sakana AI |
| [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) | 複数の画像に対する日本語での質疑応答能力を評価するデータセット。 | Sakana AI |
| <a id="llava-bench-in-the-wild"></a> [LLaVA-Bench-In-the-Wild (Japanese)](https://github.com/turingmotors/heron/tree/main/playground/data/llava-bench-in-the-wild) | [LLaVA-Bench-In-the-Wild](https://huggingface.co/datasets/liuhaotian/llava-bench-in-the-wild) を DeepL で日本語に訳したもの。24 枚の画像に対して計 60 問の質問が割り当てられている。 | Turing |
| [LLaVA-Bench (COCO) Japanese](https://github.com/turingmotors/heron/tree/main/playground/data/llava-bench-ja) | LLaVA の評価に使われた LLaVA-Bench (COCO) データセットを DeepL で日本語に訳したもの。30 枚の画像に対して各 3 種類の質問が割り当てられている。 | Turing |
| [Japanese Visual Genome VQA dataset](https://github.com/yahoojapan/ja-vg-vqa) | [Visual Genome dataset](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) の画像をもとにアノテーションされた質問応答データセット。このデータセットの 500 件を切り出した [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) が VLM の評価ベンチマークとして用いられることもある。 | ヤフー |

<a id="reference"></a>
## 各モデル・アーキテクチャの原論文

<!--@include: @/parts/references_model.md-->

<a id="reference-training"></a>
## LLMの学習手法の原論文

<!--@include: @/parts/references_training.md-->

<a id="contributors"></a>
## コントリビューター

このプロジェクトに貢献してくれているコントリビューターのみなさんです！

<a href="https://github.com/llm-jp/awesome-japanese-llm/graphs/contributors" target="_blank" rel="noreferrer">
  <img loading="lazy" src="./figures/contributors.svg" alt="コントリビューター" />
</a>

<a id="citation"></a>
## 引用

このリポジトリの要約はプレプリントとしても公開されています:
[Exploring Open Large Language Models for the Japanese Language: A Practical Guide](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/682/2035)

このリポジトリについて言及する場合は、以下の通り引用してください:

```
@article{awesomeJapanese2024,
    title={{Exploring Open Large Language Models for the Japanese Language: A Practical Guide}},
    author={Kaito Sugimoto},
    doi={10.51094/jxiv.682},
    journal={Jxiv preprint},
    year={2024}
}
```

[^1]: ただし、モデル高速化のため本家の Llama に対してアーキテクチャの変更を加えている。詳しくは以下を参照: [PLaMo-13Bを公開しました](https://tech.preferred.jp/ja/blog/llm-plamo/)

[^2]: 詳細は明記されていないが、プレスリリースには以下のような記述がある: 『学習データには、オープンデータセットに加え、Stability AI Japanが作成した独自のデータセットや、EleutherAI Polyglot project の日本語チーム及び Stable Community Japan のメンバーの協力のもとで作成したデータが含まれています。』

[^3]: 通常の左から右に単語を予測する代わりに、右から左に単語を予測するように訓練された言語モデルの評価を行った研究である。通常方向の言語モデルと逆方向の言語モデルの両方が公開されている。

[^4]: ○: HuggingFace の Model Hub にモデルがアップロードされており、`AutoModel.from_pretrained()` 等ですぐ読み込める。 △: Model Hub にはモデルがアップロードされていないが、HuggingFace (transformers, 旧 pytorch-transformers) の形式に対応している。✕: モデルがHuggingFaceに対応していない。

[^5]: ただし、最大系列長が 2048 に拡張されているほか、元の BERT に対して様々なアーキテクチャの変更が施されている。詳しくは HuggingFace リポジトリの README を参照。

[^6]: 様々な形態素解析器とサブワード化手法の組み合わせを試した研究である。全ての組み合わせのモデルを掲載するのは大変なので、ここでは実験で最も平均のタスク性能が高い Juman++ + BPE のモデルを代表として掲載している。

[^7]: nlp-waseda/roberta-base-japanese 及び nlp-waseda/roberta-large-japanese はモデル入力の最大トークン長を128で事前学習しているが、nlp-waseda/roberta-large-japanese-seq512 は512で事前学習している

[^8]: ただし、最大系列長が通常の 512 から 1282 まで拡張されており、より長い入力文を扱うことができる

[^9]: small の方は日本語 Wikipedia と日本語金融コーパスを合わせてスクラッチ学習しているが、base の方は東北大BERTに日本語金融コーパスを追加学習しているという違いがある

[^10]: 万病WordPieceモデルは MeCab (IPA辞書+万病辞書) で単語分割した後 WordPiece でサブワード化するモデル、SentencePieceモデルは単語分割せずに直接 Unigram でサブワード化するモデル

[^11]: Instruction Tuning を行った後に、Llama 3 Instruct と Llama 3 Base の差分の Chat Vector を加えている。

[^12]: Instruction Tuning において、GPT-3.5, GPT-4 等の OpenAI のモデルで生成されたデータを使って学習しているため、OpenAI の規約に違反している可能性がある。

[^13]: ただし、KARAKURI LM を商用利用したい場合は、開発元であるカラクリ株式会社に直接連絡が必要であるとしている。

[^14]: ただし、研究および教育を目的とした利用を念頭に置くよう呼びかけている。また、マージ元のモデルのいくつかのライセンスは Apache 2.0 ではない点にも注意すること。

[^15]: 詳細は以下のビデオで公開されている: [松尾研 GENIAC LLM開発プロジェクト 第1フェーズ結果発表会 2024.06.01 @ 東京大学 福武ホール @ 58:22](https://youtu.be/Ju_KgrGhANY?si=zUhZ1S6dznGeF0Gi&t=3502)

[^16]: ただし、通常の BERT (base) と比べて Layer や Attention Head の数が少ない。

[^17]: Instruction Tuning を行う前に、Llama 3 Instruct と Llama 3 Base の差分の Chat Vector を加えている。

[^18]: それぞれのモデルの詳細は作者らの[論文](https://www.jstage.jst.go.jp/article/jnlp/31/2/31_707/_pdf/-char/ja)の第4章を参照。なお、SC-2M-wiki モデルは Wikipedia でのみ事前学習されているため、厳密にはドメイン特化型モデルではない。

[^19]: 詳細は以下の記事を参照: [大規模言語モデルTanuki-8B, 8x8Bの位置づけや開発指針など](https://zenn.dev/matsuolab/articles/377f7ae8b1169e), [大規模言語モデルを開発するにあたっての事前・事後学習の戦略メモー特に合成データについてー](https://zenn.dev/matsuolab/articles/34036f017fae9e)

[^20]: ORPO を行う前に、Gemma 2 Instruct と Gemma 2 Base の差分の Chat Vector を加えている。

[^21]: 埋め込みモデルの分類は [Dense Text Retrieval based on Pretrained Language Models: A Survey (Zhao+, 2022)](https://arxiv.org/abs/2211.14876) を参考に行った。Bi-Encoder は 2つの入力を個別にモデルに入力し、それぞれベクトル化した上で、それらの内積やコサイン類似度を入力の近さとして定式化するアーキテクチャである。それに対し、Cross-Encoder は 2 つの入力を組み合わせたものをモデルに入力し、モデル内部で近さを直接計算するアーキテクチャである。情報抽出の分野では、Cross-Encoder の方が計算コストがかかるが、入力の近さをよりきめ細かくモデルが計算することが期待されるため、抽出結果の順序を再検討するリランカーとして用いられることも多い。なお、Bi-Encoder の中でも、入力を単一のベクトルではなく（トークンごとなどの）複数のベクトルとして表現するタイプのもの（例: ColBERT）があるため、Single-representation bi-encoders と Multi-representation bi-encoders にさらに細分化している。

[^22]: 一部アーキテクチャの変更を加えている。詳しくは以下を参照: [1,000億パラメータ規模の独自LLM「PLaMo-100B」の事前学習](https://tech.preferred.jp/ja/blog/plamo-100b/)

[^23]: Llama から Causal Attention を取り除くことにより、エンコーダ型モデルとして利用している。