# 日本語LLMまとめ
[ [**English**](./README_en.md) | [**Français**](./README_fr.md) | 日本語 ]

<p align="center">
  <img src="figures/parameter_size_overview.png" alt="日本語LLM・英語LLMのパラメータサイズの推移">
</p>
<figcaption style="font-style: italic; font-size: 0.9em; color: #6b7280; text-align: center;">日本語LLM・英語LLMのパラメータ数の推移。日本語モデルの情報は本記事、英語モデルの情報は LifeArchitect.ai の <a href="https://lifearchitect.ai/models-table/">Models table</a> を参照しています（ただし、図のスペース上一部のモデルは省略。また、英語モデルのパラメータ数は推測値を含む）。修正・追加等ありましたらお知らせ下さい。</figcaption>

---

この記事は、一般公開されている日本語LLM（日本語を中心に学習されたLLM）および日本語LLM評価ベンチマークに関する情報をまとめたものです。情報は、有志により収集されており、その一部は論文や公開されているリソースなどから引用しています。

⚠ 以下の点について、あらかじめご理解とご了承をお願いいたします：
1. 本記事の内容は、完全性や正確性を保証するものではありません。これらの情報は予告なく変更されることがあり、また最新の情報を常に提供できるとは限りません。
2. 一部の情報は、推測や個々の利用者の解釈にもとづくものである場合があります。そのため、全ての読者にとって必ずしも正確であるとは限りません。
3. 本記事に記載されているモデルの多くは、MIT や Apache-2.0 といったオープンソースライセンスが適用されています。しかしながら、**一部のモデルには、非営利限定のライセンス（例：CC BY-NC-SA 4.0）や開発元特有のライセンスが適応されており、これらは必ずしもオープンソースとは言えない可能性がある**点にご注意ください。

この記事の管理は GitHub で行っています。記事の間違いを発見した場合、あるいはモデルの追加提案を行いたい場合は、[GitHub Issues](https://github.com/llm-jp/awesome-japanese-llm/issues) 経由で報告していただけますと幸いです。

## 目次

- [テキスト生成に主に使うモデル](#generative)
  - [フルスクラッチ事前学習モデル](#full-scratch-models)
    - [汎用](#generative-scratch-general)
    - [ドメイン特化型](#generative-scratch-domain-specific)
  - [英語モデルに日本語で追加事前学習を行ったモデル（継続事前学習モデル）](#english-based-models)
    - [汎用](#generative-continual-general)
    - [ドメイン特化型](#generative-continual-domain-specific)
  - [英語モデルに日本語で指示チューニング (Instruction Tuning) のみ行ったモデル](#instruction-only-models)
    - [汎用](#generative-instruction-only-general)
    - [ドメイン特化型](#generative-instruction-only-domain-specific)
- [入力テキストの処理に主に使うモデル](#autoencoding)
  - [汎用](#autoencoding-general)
  - [ドメイン特化型](#autoencoding-domain-specific)
- [埋め込み (Embeddings) 作成に特化したモデル](#embeddings)
- [視覚言語モデル (Vision-Language Models)](#multimodal)
  - [画像を含むテキスト生成](#multimodal-text-generation)
    - [汎用](#multimodal-general)
    - [ドメイン特化型](#multimodal-domain-specific)
  - [その他](#multimodal-others)
- [音声言語モデル (Speech-Language Models)](#speech)
- [日本語LLM評価ベンチマーク/データセットまとめ](#benchmark-suites)
  - [複合型ベンチマーク](#hybrid-benchmark-suites)
  - [基礎的な自然言語理解 (NLU) を中心に測定するベンチマーク/データセット](#basic-benchmark-suites)
  - [人間らしい応答の生成能力を中心に測定するベンチマーク/データセット](#open-ended-benchmark-suites)
  - [特定ドメインの性能を測定するベンチマーク/データセット](#domain-specific-benchmark-suites)
- [各モデル・アーキテクチャの原論文](#reference)
- [LLMの学習手法の原論文](#reference-training)
- [コントリビューター](#contributors)
- [引用](#citation)


<a id="generative"></a>
## テキスト生成に主に使うモデル

*画像を含むテキスト生成モデルは[こちら](#multimodal-text-generation)*

<a id="full-scratch-models"></a>
### フルスクラッチ事前学習モデル

<a id="generative-scratch-general"></a>
#### 汎用

|    |  アーキテクチャ  |  入出力で扱える<br>トークン数  |  学習テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|:---:|
| [LLM-jp-13B v1.1](https://llm-jp.nii.ac.jp/blog/2024/02/09/v1.1-tuning.html) | GPT<br>([**13b**-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-dpo-lora-hh_rlhf_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-dpo-lora-hh_rlhf_ja-v1.1)) | 2,048 | Instruction Tuning (LoRA or Full-parameter FT): Dolly Dataset, OASST1, [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/)<br>DPO (LoRA): HH RLHF | LLM-jp | Apache 2.0 |
| [LLM-jp-13B](https://www.nii.ac.jp/news/release/2023/1020.html) | GPT<br>([1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0), [**13b**-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0), [**13b**-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0), [**13b**-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0), [**13b**-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0), [**13b**-instruct-lora-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-v1.0), [**13b**-instruct-lora-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-dolly-oasst-v1.0), [**13b**-instruct-lora-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly-oasst-v1.0)) | 2,048 | 事前学習: [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) (Wikipedia, Japanese mC4, The Pile, Stack) (計 **300B** トークン)<br>Instruction Tuning (Full-parameter FT or LoRA): jaster, Dolly Dataset, OASST1 | LLM-jp | Apache 2.0 |
| [PLaMo-13B](https://www.preferred.jp/ja/news/pr20230928/) | Llama[^1]<br>([**13b**](https://huggingface.co/pfnet/plamo-13b), [**13b**-instruct](https://huggingface.co/pfnet/plamo-13b-instruct), [**13b**-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc)) | base: 4,096<br>instruct, instruct-nc: 8,192 | 事前学習: C4, Project Gutenberg, RedPajama, 日本語 Wikipedia, Japanese mC4<br>(計 **1.5T** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1, llm-japanese-datasetのwikinews subset (NCモデルでは商用利用不可の Alpaca Dataset も含めて学習) | Preferred Networks | Apache 2.0<br>(NC モデルは CC BY-NC 4.0) |
| [Stockmark-13b](https://stockmark.co.jp/news/20231027) | Llama<br>([**13b**](https://huggingface.co/stockmark/stockmark-13b), [**13b**-instruct](https://huggingface.co/stockmark/stockmark-13b-instruct)) | 2,048 | 事前学習: 日本語 Wikipedia、Japanese CC-100、Japanese mC4、Japanese CommonCrawl、日本語特許、Stockmark Web Corpus<br>(計 **220B** トークン)<br>Instruction Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | ストックマーク | baseモデル: MIT<br>instructモデル: CC BY-NC-SA 4.0 |
| [Weblab-10B](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001) | GPT<br>([**10b**](https://huggingface.co/matsuo-lab/weblab-10b), [**10b**-instruction-sft](https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft)) | 2,048 | Japanese mC4 + The Pile（計 **600B** トークン）<br>\*instruction-sft モデルは Alpaca Dataset, FLAN でファインチューニング | 東大 松尾研 | CC BY-NC 4.0 |
| [Japanese StableLM Alpha](https://ja.stability.ai/blog/japanese-stablelm-alpha) | GPT<br>([base-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b), [instruct-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b), [instruct-alpha-**7b**-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2)) | 2,048 | Wikipedia, Japanese CC-100, Japanese mC4, Japanese OSCAR, RedPajama<br>(+ 独自のデータセット)[^2]<br>(計 **750B** トークン)<br>\*instruct モデルでは Alpaca Dataset, Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subsetでファインチューニング<br>(v2では商用利用不可の Alpaca Dataset を除外) | Stability AI | baseモデル: Apache 2.0<br>instruct モデル (v1): [独自のライセンス](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b/tree/main)<br>instruct モデル (v2): Apache 2.0 |
| [CALM2](https://www.cyberagent.co.jp/news/detail/id=29479) | Llama<br>([**7b**](https://huggingface.co/cyberagent/calm2-7b), [**7b**-chat](https://huggingface.co/cyberagent/calm2-7b-chat), [**7b**-chat-dpo-experimental](https://huggingface.co/cyberagent/calm2-7b-chat-dpo-experimental)) | base: 4,096<br>chat: **32,768** |一般公開されている日本語・英語のデータセット（詳細不明） (計 **1.3T** トークン)<br>*dpo モデルは Chatbot Arena Conversations JA (calm2) Dataset を用いて DPO で学習 | サイバーエージェント | Apache 2.0<br>(dpo モデルのみ CC BY 4.0) |
| [OpenCALM](https://www.cyberagent.co.jp/news/detail/id=28817) | GPT<br>([small](https://huggingface.co/cyberagent/open-calm-small), [medium](https://huggingface.co/cyberagent/open-calm-medium), [large](https://huggingface.co/cyberagent/open-calm-large), [**1b(1.4b)**](https://huggingface.co/cyberagent/open-calm-1b), [**3b(2.7b)**](https://huggingface.co/cyberagent/open-calm-3b), [**7b(6.8b)**](https://huggingface.co/cyberagent/open-calm-7b)) | 2,048 | 日本語 Wikipedia <br>+ Jpanese mC4<br>+ Japanese CC-100 | サイバーエージェント | CC BY-SA 4.0 |
| [Stormy](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/422/1350) | GPT<br>([**7b(6.8b)**](https://huggingface.co/izumi-lab/stormy-7b-10ep)) | 2,048 | OpenCALM (6.8b) に対して<br>llm-japanese-dataset v0 のうち翻訳タスクを除いたデータで LoRAチューニング | 東大 和泉研 | CC BY-SA 4.0 |
| [rinna GPT <br> (英語やコードも含めて学習されたモデル)](https://rinna.co.jp/news/2023/07/20230731.html) | GPT<br>([**4b(3.8b)**](https://huggingface.co/rinna/bilingual-gpt-neox-4b), [**4b(3.8b)**-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k), [**4b(3.8b)**-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft), [**4b(3.8b)**-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo)) | 8kモデル: 8,192<br>他: 2,048 | Wikipedia, Japanese CC-100, Japanese C4, RedPajama, The Pile<br>(計 **524B** トークン)<br>\*8k モデルでは 4,000トークンを超える長いトークン列でファインチューニング<br>\*instruction-sft モデルでは HH RLHF、FLAN でファインチューニング<br>\*instruction-ppo モデルでは HH RLHF で PPO ベースの強化学習 | rinna | MIT |
| [japanese-large-lm](https://engineering.linecorp.com/ja/blog/3.6b-japanese-language-model-with-improved-dialog-performance-by-instruction-tuning) | GPT<br>([**1.7b**](https://huggingface.co/line-corporation/japanese-large-lm-1.7b), [**3.6b**](https://huggingface.co/line-corporation/japanese-large-lm-3.6b), [**1.7b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft), [**3.6b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft)) | 2,048 | 日本語 Wikipedia, Japanese CC-100, Japanese C4, Japanese OSCAR や独自データなど<br>(計 **650GB**)<br>\*instruction-sft モデルでは OASST1 でファインチューニング | LINE | Apache 2.0 |
| [rinna GPT <br> (日本語のみで学習されたモデル)](https://rinna.co.jp/news/2023/05/20220531.html) | GPT<br>([xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall), [small](https://huggingface.co/rinna/japanese-gpt2-small), [medium](https://huggingface.co/rinna/japanese-gpt2-medium), [**1b**](https://huggingface.co/rinna/japanese-gpt-1b), [neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small), [neox-**3.6b**](https://huggingface.co/rinna/japanese-gpt-neox-3.6b), [neox-**3.6b**-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft), [neox-**3.6b**-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2), [neox-**3.6b**-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)) | ≤ 2,048 | 日本語 Wikipedia <br> + Japanese CC-100 <br> (1b 以降のモデルでは<br>さらに Japanese mC4 を追加)<br>\*instruction-sft, sft-v2 モデルでは HH RLHF、FLAN、SHP データセットでさらにファインチューニング<br>\*instruction-ppo モデルでは HH RLHF でさらに PPO ベースの強化学習 | rinna | MIT |
| [レトリバT5](https://note.com/retrieva/n/n7b4186dc5ada) | T5<br>([small (short)](https://huggingface.co/retrieva-jp/t5-small-short), [small (medium)](https://huggingface.co/retrieva-jp/t5-small-medium), [small (long)](https://huggingface.co/retrieva-jp/t5-small-long), [base (short)](https://huggingface.co/retrieva-jp/t5-base-short), [base (medium)](https://huggingface.co/retrieva-jp/t5-base-medium), [base (long)](https://huggingface.co/retrieva-jp/t5-base-long), [large (short)](https://huggingface.co/retrieva-jp/t5-large-short), [large (medium)](https://huggingface.co/retrieva-jp/t5-large-medium), [large (long)](https://huggingface.co/retrieva-jp/t5-large-long), [**xl(3b)**](https://huggingface.co/retrieva-jp/t5-xl)) | | 日本語 Wikipedia + Japanese mC4 | レトリバ | CC BY-SA 4.0 |
| [kotomamba-2.8B](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0) | Mamba<br>([**2.8B**-v1.0](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0)) | 2,048 | 日本語 Wikipedia, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [ABEJA GPT](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207) | GPT<br>([large](https://huggingface.co/abeja/gpt2-large-japanese), [neox-**2.7b**](https://huggingface.co/abeja/gpt-neox-japanese-2.7b)) | | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | ABEJA | MIT |
| [早大GPT](https://huggingface.co/nlp-waseda/gpt2-xl-japanese) | GPT<br>([small](https://huggingface.co/nlp-waseda/gpt2-small-japanese), [**xl(1.5b)**](https://huggingface.co/nlp-waseda/gpt2-xl-japanese)) | |  日本語 Wikipedia<br> + Japanese CC-100 | 早大 河原研 | CC BY-SA 4.0 |
| [ストックマークGPT](https://stockmark.co.jp/news/20230808) | GPT<br>([**1.4b**](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b)) |  | 日本語 Wikipedia (0.88B トークン)<br>+ Japanese CC-100 (10.5B トークン)<br>+ 独自のWebデータ (8.6B トークン) | ストックマーク | MIT |
| [イエローバックGPT](https://tech.yellowback.net/posts/gpt-neo-japanese) | GPT<br>([**1.3b**](https://huggingface.co/yellowback/gpt-neo-japanese-1.3B)) |  | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | イエローバック | Apache 2.0 |
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
### 英語モデルに日本語で追加事前学習を行ったモデル（継続事前学習モデル）

<a id="generative-continual-general"></a>
#### 汎用

|    | ベースのLLM  | 学習テキスト | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Swallow 70B](https://tokyotech-llm.github.io/swallow-llama)<br>([70b-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-hf), [70b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf), [70b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf), [70b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf)) | Llama 2 (**70b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1 | TokyoTech-LLM | Llama 2 Community License |
| [KARAKURI LM](https://karakuri.ai/seminar/news/karakuri-lm/)<br>([70b-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-v0.1), [70b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-chat-v0.1)) | Llama 2 (**70b**) | 事前学習: mC4, CC100, OSCAR, RedPajama, 独自のデータセット<br>(計 **16B** トークン)<br>SteerLM: OASST2, 独自のデータセット | カラクリ | Llama 2 Community License[^13] |
| [Japanese Stable LM Beta 70B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-70b), [instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b)) | Llama 2 (**70b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [Nekomata 14B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([14b](https://huggingface.co/rinna/nekomata-14b), [14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction), [14b-gguf](https://huggingface.co/rinna/nekomata-14b-gguf), [14b-instruction-gguf](https://huggingface.co/rinna/nekomata-14b-instruction-gguf)) | Qwen (**14b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **66B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Tongyi Qianwen LICENSE |
| [Swallow 13B](https://tokyotech-llm.github.io/swallow-llama)<br>([13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf), [13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf), [13b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf)) | Llama 2 (**13b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1 | TokyoTech-LLM | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-13b](https://note.com/elyza/n/n5d42686b60b7)<br>([13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b), [13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct), [13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast), [13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct)) | Llama 2 (**13b**) | 事前学習: 日本語 Wikipedia, Japanese OSCAR, その他クロールデータなど<br>(計 **18B** トークン)<br>Instruction Tuning: 独自のデータセット | ELYZA | Llama 2 Community License |
| [Swallow 7B](https://tokyotech-llm.github.io/swallow-llama)<br>([7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf), [7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf), [7b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf), [7b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf), [7b-plus-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf)) | Llama 2 (**7b**) | 事前学習: 日本語 Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1 | TokyoTech-LLM | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-7b](https://note.com/elyza/n/na405acaca130)<br> ([7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct), [7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast), [7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct)) | Llama 2 (**7b**) | 事前学習: 日本語 Wikipedia, Japanese OSCAR, その他クロールデータなど<br>(計 **18B** トークン)<br>Instruction Tuning: 独自のデータセット | ELYZA | Llama 2 Community License |
| [Youri 7B](https://rinna.co.jp/news/2023/10/20231031.html)<br>([7b](https://huggingface.co/rinna/youri-7b), [7b-instruction](https://huggingface.co/rinna/youri-7b-instruction), [7b-chat](https://huggingface.co/rinna/youri-7b-chat), [7b-gptq](https://huggingface.co/rinna/youri-7b-gptq), [7b-instruction-gptq](https://huggingface.co/rinna/youri-7b-instruction-gptq), [7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq)) | Llama 2 (**7b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **40B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Llama 2 Community License |
| [houou-7b](https://corp.moneyforward.com/news/release/corp/20231206-mf-press-1/)<br>([instruction-7b-v1](https://huggingface.co/moneyforward/houou-instruction-7b-v1), [instruction-7b-v2](https://huggingface.co/moneyforward/houou-instruction-7b-v2)) | Llama 2 (**7b**) | Youri 7B (base) に対して Instruction Tuning (Full-parameter FT): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | マネーフォワード | Llama 2 Community License |
| [Japanese Stable LM Beta 7B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-7b), [base-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-ja_vocab-beta-7b), [instruct-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-7b), [instruct-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b)) |  Llama 2 (**7b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [SambaLingo-Japanese](https://sambanova.ai/blog/sambalingo-open-source-language-experts)<br>([Base](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Base), [Chat](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Chat)) | Llama 2 (**7b**) | 事前学習: Cultura-X<br>Instruction Tuning: ultrachat_200k<br>DPO: ultrafeedback, cai-conversation-harmless | SambaNova Systems | Llama 2 Community License (?)[^12] |
| [blue-lizard](https://prtimes.jp/main/html/rd/p/000000010.000125694.html)<br>([blue-lizard](https://huggingface.co/Deepreneur/blue-lizard)) | Llama 2 (**7b**) | 不明 | Deepreneur | Llama 2 Community License |
| [Japanese Stable LM Gamma 7B](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([base-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b), [instruct-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b)) | Mistral-7B-v0.1 (**7b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subset | Stability AI |  Apache 2.0  |
| [ChatNTQ JA 7B](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)<br>([7b-v1.0](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)) | Mistral-7B-v0.1 (**7b**) | Japanese Stable LM Gamma 7B (base) に対して独自のデータセットで Instruction Tuning | NTQ Solution | Apache 2.0  |
| [Shisa Gamma 7B](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)<br>([7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)) | Mistral-7B-v0.1 (**7b**) | Japanese Stable LM Gamma 7B (base) に対して ultra-orca-boros-en-ja で Instruction Tuning | AUGMXNT | Apache 2.0 (?)[^12]  |
| [Shisa 7B](https://github.com/AUGMXNT/shisa/wiki)<br>([base-7b-v1](https://huggingface.co/augmxnt/shisa-base-7b-v1), [7b-v1](https://huggingface.co/augmxnt/shisa-7b-v1)) | Mistral-7B-v0.1 (**7b**) | 事前学習: shisa-pretrain-en-ja-v1 (**8B** トークン)<br>Instruction Tuning(Full-parameter FT) & DPO: ultra-orca-boros-en-ja, shisa-en-ja-dpo-v1  | AUGMXNT |  Apache 2.0 (?)[^12]  |
| [Karasu](https://www.lightblue-tech.com/2024/01/15/20240115_news/)<br>([7B](https://huggingface.co/lightblue/karasu-7B), [7B-chat](https://huggingface.co/lightblue/karasu-7B-chat), [7B-chat-plus](https://huggingface.co/lightblue/karasu-7B-chat-plus), [7B-chat-plus-unleashed](https://huggingface.co/lightblue/karasu-7B-chat-plus-unleashed)) | Mistral-7B-v0.1 (**7b**) | Shisa 7B (base) に対して以下のデータセットで追加事前学習: 青空文庫, 日本の法律・判例, 日本語 Wikipedia, CulturaX の日本ドメインのデータ, UltraChat 200k (計 **7B** トークン)<br>Instruction Tuning: ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, 独自のデータセット | Lightblue | Apache 2.0 (?)[^12]  |
| [Nekomata 7B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([7b](https://huggingface.co/rinna/nekomata-7b), [7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction), [7b-gguf](https://huggingface.co/rinna/nekomata-7b-gguf), [7b-instruction-gguf](https://huggingface.co/rinna/nekomata-7b-instruction-gguf)) | Qwen (**7b**) | 事前学習: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, 独自のデータセット<br>(計 **66B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, FLAN, llm-japanese-datasetの一部 | rinna | Tongyi Qianwen LICENSE |
| [lightblue/japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) | MPT (**7b**) | Japanese mC4 | Lightblue | Apache 2.0 |
| [Japanese Stable LM 3B-4E1T](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base), [3b-4e1t-instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-instruct)) | StableLM-3B-4E1T (**3b**) | 事前学習: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(Books3を除外)<br>(計 **100B** トークン)<br>Instruction Tuning (Full-parameter FT): Dolly Dataset, HH RLHF, llm-japanese-datasetのwikinews subset | Stability AI |  Apache 2.0  |
| [kotomamba-2.8B-CL](https://huggingface.co/kotoba-tech/kotomamba-2.8B-CL-v1.0) | mamba-2.8b-slimpj<br>(**2.8b**) | 日本語 Wikipedia, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) | TinyLlama (**1.1b**) | 事前学習: Japanese OSCAR, Japanese mC4<br>(計 **3B** トークン) | Lightblue | Apache 2.0 |

<a id="generative-continual-domain-specific"></a>
#### ドメイン特化型

|    | ドメイン | ベースのLLM  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Watashiha-Llama-2-13B-Ogiri-sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft)<br>([sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft), [sft-neuron](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-neuron)) | 大喜利 | Llama 2 (**13b**) | わたしは | Llama 2 Community License |
| [ELYZA-japanese-CodeLlama-7b](https://note.com/elyza/n/n5bce23d7c9c8)<br>([7b](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b-instruct)) | コーディング |  Code Llama<br>(**7b**) | ELYZA | Llama 2 Community License |
| [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) | 物語生成 | GPT-J (**6b**) | 個人 ([大曽根宏幸](https://scholar.google.co.jp/citations?user=6ID5K3oAAAAJ)) | CreativeML OpenRAIL-M License |
| [NovelAI/genji-jp](https://huggingface.co/NovelAI/genji-jp) | 物語生成 | GPT-J (**6b**) | NovelAI |  ？  |

<a id="instruction-only-models"></a>
### 英語モデルに日本語で指示チューニング (Instruction Tuning) のみ行ったモデル

<a id="generative-instruction-only-general"></a>
#### 汎用

|    | ベースのLLM  | 学習テキスト | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese](https://huggingface.co/AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese) | Llama 2 (**70b**) || 東京大学医学部附属病院 循環器内科 AIグループ | Llama 2 Community License |
| [doshisha-mil/llama-2-70b-chat-4bit-japanese-v1](https://huggingface.co/doshisha-mil/llama-2-70b-chat-4bit-japanese-v1) | Llama 2 (**70b**) || 同志社大学 メディア情報学研究室 | ？ |
| [Qarasu](https://www.lightblue-tech.com/2024/01/15/20240115_news/)<br>([14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed)) | Qwen (**14b**) | ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, 独自のデータセット | Lightblue | Tongyi Qianwen LICENSE (?)[^12] |
| [Sparticle/llama-2-13b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-13b-chat-japanese-lora) | Llama 2 (**13b**) || Sparticle | ？ |
| [izumi-lab/llama-13b-japanese-lora-v0-1ep](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep) | Llama (**13b**) || 東大 和泉研 |  ？ |
| [ganchengguang/Yoko-7B-Japanese-v1](https://huggingface.co/ganchengguang/Yoko-7B-Japanese-v1) | Llama 2 (**7b**) || 横浜国大 森研 |  ？  |
| [Sparticle/llama-2-7b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-7b-chat-japanese-lora) | Llama 2 (**7b**) || Sparticle |  ？  |
| [izumi-lab/llama-7b-japanese-lora-v0-5ep](https://huggingface.co/izumi-lab/llama-7b-japanese-lora-v0-5ep) | Llama (**7b**) || 東大 和泉研 |  ？  |
| [lightblue/jod](https://huggingface.co/lightblue/jod) | Mistral-7B-SlimOrca (**7b**) || Lightblue | Apache 2.0 |
| [NTQAI/chatntq-7b-jpntuned](https://huggingface.co/NTQAI/chatntq-7b-jpntuned) | RWKV-4 World (**7b**) || NTQ Solution |  ？  |

<a id="generative-instruction-only-domain-specific"></a>
#### ドメイン特化型

|    | ドメイン | ベースのLLM  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [JMedLoRA](https://arxiv.org/pdf/2310.10083.pdf)<br>([llama2-jmedlora-6.89ep](https://huggingface.co/AIgroup-CVM-utokyohospital/llama2-jmedlora-6.89ep)) | 医療 | Llama 2 (**70b**) | 東京大学医学部附属病院 循環器内科 AIグループ | CC BY-NC 4.0 |

<a id="autoencoding"></a>
## 入力テキストの処理に主に使うモデル

<a id="autoencoding-general"></a>
### 汎用

|    |  アーキテクチャ  |  学習テキスト  |  開発元  | ライセンス | HuggingFace ですぐ使える？ [^4]  |
|:---|:---:|:---:|:---:|:---:|:---:|
|  [京大BERT](https://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)  |  BERT (base, large)  |  日本語 Wikipedia (約1,800万文)  |  京大 言語メディア研究室  | Apache 2.0 | △ |
|  [東北大BERT](https://github.com/tohoku-nlp/bert-japanese)  |  BERT (base, large)  |  base (v1):<br>日本語 Wikipedia 約1,700万文 (2.6GB)<br>base (v2) & large:<br>日本語 Wikipedia 約3,000万文 (4.0GB)<br>base (v3) & large (v2):<br>日本語 Wikipedia 約3,400万文 (4.9GB)<br>+ 日本語 CC-100 約3億9,200万文 (74.3GB)   |  東北大<br>自然言語処理研究グループ | base (v1, v2) & large: CC BY-SA 3.0<br>base (v3) & large (v2): Apache 2.0 |◯ ([base (v1)](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking), [base (v1, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking), [base (v2)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2), [base (v2, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2), [large](https://huggingface.co/tohoku-nlp/bert-large-japanese), [large (文字レベル)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char), [base (v3)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3), [base (v3, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3), [large (v2)](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2), [large (v2, 文字レベル)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char-v2)) |
| [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/index.html)   |  BERT (base)  |  日本語 Wikipedia  |  NICT  | CC BY 4.0 | △ |
| [colorfulscoop BERT](https://huggingface.co/colorfulscoop/bert-base-ja) | BERT (base) | 日本語 Wikipedia | Colorful Scoop | CC BY-SA 3.0 | [◯](https://huggingface.co/colorfulscoop/bert-base-ja) |
| [東大BERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small) | 日本語 Wikipedia (約2,000万文 (2.9GB)) | 東大 和泉研 | CC BY-SA 4.0 | [◯](https://huggingface.co/izumi-lab/bert-small-japanese) |
| [chiTra (Sudachi Transformers)](https://www.worksap.co.jp/news/2022/0225/) | BERT (base) | 国語研日本語ウェブコーパス (NWJC) (148GB) | NINJAL & ワークス徳島人工知能NLP研 | Apache 2.0 | △ |
| [ACCMS BERT](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) | BERT (base) | 日本語 Wikipedia (3.3GB) | 京大 ACCMS | CC BY-SA 4.0 | [◯](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) |
| [日立BERT](https://aclanthology.org/2023.acl-srw.5.pdf) | BERT (base) | 日本語 Wikipedia <br>+ Japanese CC-100 | 日立製作所 | CC BY-NC-SA 4.0 | [◯](https://huggingface.co/hitachi-nlp/bert-base-japanese_jumanpp-bpe) [^6] |
| [Bandai Namco DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp/blob/main/docs/GUIDE.md) | DistilBERT | - （東北大BERT(base) を親モデルとして知識蒸留） | Bandai Namco Research | MIT | [◯](https://huggingface.co/bandainamco-mirai/distilbert-base-japanese) |
| [LINE DistilBERT](https://engineering.linecorp.com/ja/blog/line-distilbert-high-performance-fast-lightweight-japanese-language-model) | DistilBERT | - （LINE社内のBERTを親モデルとして知識蒸留）| LINE | Apache 2.0 | [◯](https://huggingface.co/line-corporation/line-distilbert-base-japanese) |
| [rinna RoBERTa](https://rinna.co.jp/news/2021/08/20210825.html) | RoBERTa (base) |  日本語 Wikipedia <br>+ Japanese CC-100 | rinna | MIT | [◯](https://huggingface.co/rinna/japanese-roberta-base) |
| [早大RoBERTa](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) | RoBERTa (base, large) | 日本語 Wikipedia <br>+ Japanese CC-100 | 早大 河原研 | CC BY-SA 4.0 | ◯ ([base](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp), [large](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp), [large (seq512)](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512-with-auto-jumanpp)) [^7] |
| [インフォマティクスRoBERTa](https://www.informatix.co.jp/pr-roberta/) | RoBERTa (base) | 日本語 Wikipedia<br> + Web 上の記事 (計25GB) | インフォマティクス | Apache 2.0 | △ |
| [京大RoBERTa](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) | RoBERTa (base, large) | 日本語 Wikipedia <br>+ Japanese CC-100 | 京大 言語メディア研究室 | CC BY-SA 4.0 | ◯ ([base (文字レベル)](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm), [large (文字レベル)](https://huggingface.co/ku-nlp/roberta-large-japanese-char-wwm)) |
| [横浜国大RoBERTa](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) | RoBERTa (base) | 日本語 Wikipedia (3.45GB) | 横浜国大 森研 | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) |
| [Megagon Labs RoBERTa](https://huggingface.co/megagonlabs/roberta-long-japanese) | RoBERTa (base) [^8] | Japanese mC4 (約2億文) | Megagon Labs <br> (リクルート) | MIT | [◯](https://huggingface.co/megagonlabs/roberta-long-japanese)  |
| [ACCMS RoBERTa](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) | RoBERTa (base) | 日本語 Wikipedia (3.3GB) + Japanese CC-100 (70GB) | 京大 ACCMS | CC BY-SA 4.0 | [◯](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) |
| [シナモンELECTRA](https://cinnamon.is/ideas/2020/06/22/20200619_research_001/) | ELECTRA (small) | 日本語 Wikipedia | シナモン | Apache 2.0 | [◯](https://huggingface.co/Cinnamon/electra-small-japanese-discriminator)  |
| [Megagon Labs ELECTRA](https://www.recruit.co.jp/newsroom/pressrelease/2021/0826_9293.html) | ELECTRA (base) | Japanese mC4 (約2億文) | Megagon Labs <br> (リクルート) | MIT | [◯](https://huggingface.co/megagonlabs/electra-base-japanese-discriminator)  |
| [東大ELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small, base) | 日本語 Wikipedia (約2,000万文 (2.9GB)) | 東大 和泉研 | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/electra-small-japanese-discriminator), [base](https://huggingface.co/izumi-lab/electra-base-japanese-discriminator))  |
| [日本語RoFormer](https://huggingface.co/ganchengguang/Roformer-base-japanese) | RoFormer (base) | 日本語 Wikipedia (3.45GB) | 横浜国大 森研 | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/Roformer-base-japanese) |
| [日本語LUKE](https://www.ousia.jp/ja/page/ja/2022/11/17/luke-japanese/) | LUKE (base, large) | 日本語 Wikipedia | Studio Ousia | Apache 2.0 | ◯ ([base](https://huggingface.co/studio-ousia/luke-japanese-base-lite), [large](https://huggingface.co/studio-ousia/luke-japanese-large-lite)) |
| [京大DeBERTaV2](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | DeBERTaV2 (tiny, base, large) | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR<br>（計171GB） | 京大 言語メディア研究室 | CC BY-SA 4.0 | ◯ ([tiny](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese), [tiny (文字レベル)](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm), [base](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), [large](https://huggingface.co/ku-nlp/deberta-v2-large-japanese)) | 
| [東大DeBERTaV2](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | DeBERTaV2 (small, base) | 日本語 Wikipedia, 日本語 Wikinews, Japanese CC-100, Japanese mC4, Japanese OSCAR | 東大 和泉研 | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/deberta-v2-small-japanese), [base](https://huggingface.co/izumi-lab/deberta-v2-base-japanese)) | 
| [日本語BigBird](https://huggingface.co/nlp-waseda/bigbird-base-japanese) | BigBird (base) | 日本語 Wikipedia <br> + Japanese CC-100 <br> + Japanese OSCAR | 早大 河原研 | CC BY-SA 4.0 | [◯](https://huggingface.co/nlp-waseda/bigbird-base-japanese) |
| [日本語LayoutLM](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/Q2-7.pdf) | LayoutLM (base) | 東北大BERT (base, v2) で重みを初期化した上で、日本語 Wikipedia の文章とレイアウトで事前学習 | 日本総合研究所 | CC BY-SA 3.0 | [◯](https://huggingface.co/jri-advtechlab/layoutlm-wikipedia-ja) |

<a id="autoencoding-domain-specific"></a>
### ドメイン特化型

|    |  アーキテクチャ  |  学習テキスト  |  開発元  | ライセンス | HuggingFace ですぐ使える？  |
|:---|:---:|:---:|:---:|:---:|:---:|
| [日本語ニュースBERT](https://qiita.com/mkt3/items/3c1278339ff1bcc0187f) | BERT (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | CC BY 4.0 | △ |
| [日本語ニュースXLNet](https://qiita.com/mkt3/items/4d0ae36f3f212aee8002) |  XLNet (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | ？ | ※ 非公式の HuggingFace 向けに変換されたモデルが[公開されている](https://huggingface.co/hajime9652/xlnet-japanese) |
| [日本語ニュースALBERT](https://qiita.com/mkt3/items/b41dcf0185e5873f5f75) | ALBERT (base) | 日本語ビジネスニュース記事(300万記事) | ストックマーク | ？ | △ |
| [Laboro BERT](https://laboro.ai/activity/column/engineer/laboro-bert/) | BERT (base, large) | 日本語 Web コーパス <br> (ニュースサイトやブログなど<br>計4,307のWebサイト、2,605,280ページ (12GB)) | Laboro.AI | CC BY-NC 4.0 | ✕ |
| [Laboro DistilBERT](https://laboro.ai/activity/column/engineer/laboro-distilbert/) | DistilBERT | - （Laboro BERT(base) を親モデルとして知識蒸留）| Laboro.AI | CC BY-NC 4.0 | [◯](https://huggingface.co/laboro-ai/distilbert-base-japanese) |
| [日本語ブログELECTRA](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E2-5.pdf) | ELECTRA (small) | 日本語ブログコーパス（3億5,400万文） | 北見工大 桝井・プタシンスキ研 | CC BY-SA 4.0 | [◯](https://huggingface.co/ptaszynski/yacis-electra-small-japanese)  |
| [日本語話し言葉BERT](https://tech.retrieva.jp/entry/2021/04/01/114943) | BERT (base) | 東北大BERTに対して日本語話し言葉コーパス（CSJ）を用いて追加学習<br>（DAPTモデルでは国会議事録データも使用） | レトリバ | Apache 2.0 | [◯](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) |
| [日本語金融BERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small, base) [^9] | 日本語 Wikipedia<br> + 日本語金融コーパス (約2,700万文 (5.2GB)) | 東大 和泉研 | CC BY-SA 4.0 |◯ ([small](https://huggingface.co/izumi-lab/bert-small-japanese-fin), [base](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional)) |
| [日本語金融ELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small) | 日本語 Wikipedia (約2,000万文 (2.9GB)) <br> + 日本語金融コーパス (約2,700万文 (5.2GB)) | 東大 和泉研 | CC BY-SA 4.0 |  [◯](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator)  |
| [UTH-BERT](https://ai-health.m.u-tokyo.ac.jp/home/research/uth-bert) | BERT (base) | 日本語診療記録(約1億2,000万行) | 東大病院 <br>医療AI開発学講座 | CC BY-NC-SA 4.0 | △ |
| [medBERTjp](https://github.com/ou-medinfo/medbertjp) | BERT (base) | 日本語 Wikipedia <br> + 日本語医療コーパス（『今日の診療プレミアム』Web版） | 阪大病院 <br> 医療情報学研究室 | CC BY-NC-SA 4.0 | △ |
| [JMedRoBERTa](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf) | RoBERTa (base) | 日本語医学論文 (約1,100万文 (1.8GB)) | 東大 相澤研 | CC BY-NC-SA 4.0 | ◯ ([万病WordPiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece), [SentencePiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece)) [^10] |
| [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | RoBERTa (base) | CiNii の日本語論文 (約628万文) | 愛媛大 人工知能研究室 | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicRoBERTa) |

<a id="embeddings"></a>
## 埋め込み (Embeddings) 作成に特化したモデル

|    | アーキテクチャ |  開発元  |  ライセンス | 
|:---|:---:|:---:|:---:|
| [JaColBERT](https://arxiv.org/pdf/2312.16144.pdf)<br>([bclavie/JaColBERT](https://huggingface.co/bclavie/JaColBERT)) | ColBERT | 個人 ([Benjamin Clavié](https://scholar.google.com/citations?user=vuMln98AAAAJ)) | MIT |
| [Japanese SimCSE](https://github.com/hppRC/simple-simcse-ja)<br>([cl-nagoya/unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base), [cl-nagoya/unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large), [cl-nagoya/sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base), [cl-nagoya/sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large)) | SimCSE | 名大 武田・笹野研 | CC BY-SA 4.0 |
| [GLuCoSE](https://prtimes.jp/main/html/rd/p/000000123.000022705.html)<br>([pkshatech/GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja)) | LUKEベースの文埋め込みモデル<br>(GLuCoSE) | PKSHA Technology | Apache 2.0 |
||||
| [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) | Sentence-BERT | Colorful Scoop | CC BY-SA 4.0 |
| [MU-Kindai/SBERT-JSNLI-base](https://huggingface.co/MU-Kindai/SBERT-JSNLI-base)<br>[MU-Kindai/SBERT-JSNLI-large](https://huggingface.co/MU-Kindai/SBERT-JSNLI-large) | Sentence-BERT | 近畿大学 (研究室不明) | ？ |
| [MU-Kindai/Japanese-SimCSE-BERT-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-unsup)<br>[MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-base-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-sup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-sup) | SimCSE | 近畿大学 (研究室不明) | MIT |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) | SimCSE | PKSHA Technology | CC BY-SA 4.0 |
| [MU-Kindai/Japanese-MixCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-base)<br>[MU-Kindai/Japanese-MixCSE-BERT-large](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-large) | MixCSE | 近畿大学 (研究室不明) | MIT |
| [MU-Kindai/Japanese-DiffCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-DiffCSE-BERT-base) | DiffCSE | 近畿大学 (研究室不明) | MIT | 

<a id="multimodal"></a>
## 視覚言語モデル (Vision-Language Models)

<a id="multimodal-text-generation"></a>
### 画像を含むテキスト生成

<a id="multimodal-general"></a>
#### 汎用

|    |  アーキテクチャ  |  学習画像/テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Heron](https://github.com/turingmotors/heron/blob/main/docs/README_JP.md)<br>([blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0), [blip-ja-stablelm-base-7b-v1](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1), [blip-ja-stablelm-base-7b-v1-llava-620k](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1-llava-620k), [git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0), [git-ELYZA-fast-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ELYZA-fast-7b-v0)) | BLIP-2 または GIT | v1: LLaVA-Instruct-150K-JA または LLaVA-Instruct-620K-JA<br>v0: LLaVA-Instruct-150K-JA, Japanese STAIR Captions, Japanese Visual Genome VQA dataset | Turing | CC BY-NC 4.0 |
| [Japanese Stable VLM](https://ja.stability.ai/blog/japanese-stable-vlm)<br>([japanese-stable-vlm](https://huggingface.co/stabilityai/japanese-stable-vlm)) | LLaVA-1.5 | Japanese CC12M, STAIR Captions, Japanese Visual Genome VQA dataset | Stability AI | STABILITY AI JAPANESE STABLE VLM COMMUNITY LICENSE |
| [Japanese InstructBLIP Alpha](https://ja.stability.ai/blog/japanese-instructblip-alpha)<br>([japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha)) | InstructBLIP | Japanese CC12M, STAIR Captions, Japanese Visual Genome VQA dataset | Stability AI | JAPANESE STABLELM RESEARCH LICENSE |
| [rinna MiniGPT-4](https://rinna.co.jp/news/2023/07/20230731.html)<br>([bilingual-gpt-neox-4b-minigpt4](https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4)) | MiniGPT-4 | CC12M, COCO 2014, Visual Genome, STAIR Captions, Japanese Visual Genome VQA dataset | rinna | MIT |

<a id="multimodal-domain-specific"></a>
#### ドメイン特化型

|    |  アーキテクチャ  |  ドメイン | 開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm) | LLaVA | 大喜利 | わたしは | Llama 2 Community License |

<a id="multimodal-others"></a>
### その他

|    |  アーキテクチャ  |  学習画像/テキスト  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [リクルートCLIP](https://blog.recruit.co.jp/data/articles/japanese-clip/)<br>([japanese-clip-vit-b-32-roberta-base](https://huggingface.co/recruit-jp/japanese-clip-vit-b-32-roberta-base)) | CLIP | laion2B-multi のキャプション約1億2000万件 | リクルート | CC BY-4.0 |
| [Japanese Stable CLIP](https://ja.stability.ai/blog/japanese-stable-clip)<br>([japanese-stable-clip-vit-l-16](https://huggingface.co/stabilityai/japanese-stable-clip-vit-l-16)) | SigLIP | CC12M のキャプションを日本語に翻訳したもの、STAIR Captions | Stability AI | STABILITY AI JAPANESE STABLE CLIP COMMUNITY LICENSE |
| [rinna CLIP](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16)) | CLIP | CC12M のキャプションを日本語に翻訳したもの | rinna | Apache 2.0 |
| [rinna CLOOB](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16)) | CLOOB | CC12M のキャプションを日本語に翻訳したもの | rinna | Apache 2.0 |
| [Japanese Stable Diffusion XL](https://ja.stability.ai/blog/japanese-stable-diffusion-xl)<br>([japanese-stable-diffusion-xl](https://huggingface.co/stabilityai/japanese-stable-diffusion-xl)) | Stable Diffusion | 不明 | Stability AI | STABILITY AI JAPANESE STABLE DIFFUSION XL COMMUNITY LICENSE |
| [東北大Stable Diffusion](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0)<br>([base](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0), [refiner](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-refiner-1.0)) | Stable Diffusion | WMT2023 Shared Task の日英対訳コーパス、laion2B-multi のキャプション約 1,300 万件 | 東北大<br>自然言語処理研究グループ | CreativeML OpenRAIL-M License |
| [rinna Stable Diffusion](https://rinna.co.jp/news/2022/09/20220909.html)<br>([japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion)) | Stable Diffusion |  LAION-5B データセットのうちキャプションが日本語のもの（画像約 1 億枚）| rinna | CreativeML OpenRAIL-M License |

<a id="speech"></a>
## 音声言語モデル (Speech-Language Models)

|    |  アーキテクチャ  |  学習コーパス  |  開発元  | ライセンス |
|:---|:---:|:---:|:---:|:---:|
| [Nue ASR](https://rinna.co.jp/news/2023/12/20231207.html)<br>([nue-asr](https://huggingface.co/rinna/nue-asr)) | Nue ASR<br>(HuBERT + LLM) | ReazonSpeech | rinna | Apache 2.0 |
| [ReazonSpeech](https://research.reazon.jp/projects/ReazonSpeech/)<br>([espnet-v1](https://huggingface.co/reazon-research/reazonspeech-espnet-v1), [espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next), [espnet-v2](https://huggingface.co/reazon-research/reazonspeech-espnet-v2), [nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2)) | ESPnet (Conformer-Transducer) または NeMo (FastConformer-RNNT) | ReazonSpeech | レアゾン・ホールディングス | Apache 2.0 |
| [東大HuBERT](https://huggingface.co/sarulab-speech/hubert-base-jtube)<br>([base-jtube](https://huggingface.co/sarulab-speech/hubert-base-jtube)) | HuBERT | JTubeSpeech | 東大 猿渡・高道研 | MIT |
| [rinna HuBERT](https://rinna.co.jp/news/2023/04/20230428.html)<br>([base](https://huggingface.co/rinna/japanese-hubert-base)) | HuBERT | ReazonSpeech | rinna | Apache 2.0 |

<a id="benchmark-suites"></a>
## 日本語LLM評価ベンチマーク/データセットまとめ

<a id="hybrid-benchmark-suites"></a>
### 複合型ベンチマーク

#### [Nejumi LLMリーダーボード Neo](http://nejumi.ai/) (Weights & Biases)

一問一答形式で言語理解を評価する [llm-jp-eval](#llm-jp-eval) とプロンプト対話で生成能力を評価する [Japanese MT-bench](#jp-mt-bench) による総合評価の結果をまとめている。

<a id="basic-benchmark-suites"></a>
### 基礎的な自然言語理解 (NLU) を中心に測定するベンチマーク/データセット

<a id="llm-jp-eval"></a>
#### [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) (LLM-jp)

複数のデータセットを横断して日本語 LLM を自動評価するツールである。  
対応している全データセット一覧は[こちら](https://github.com/llm-jp/llm-jp-eval/tree/main/src/llm_jp_eval/datasets)から確認できる（この中には JNLI や JCommonsenseQA といった JGLUE のタスクなども含まれている）。  
評価結果は [llm-jp-eval リーダーボード](http://wandb.me/llm-jp-leaderboard) にまとめられている。

#### [JP Language Model Evaluation Harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) (Stability AI)

Stability AI による [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) のフォーク。複数のデータセットを横断して日本語 LLM を自動評価するツールである。  
対応している全データセット一覧は[こちら](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable/lm_eval/tasks/ja)から確認できる（この中には JNLI や JCommonsenseQA といった JGLUE のタスクなども含まれている）。  
rinna による詳細な評価結果まとめがある: [[rinna] Benchmark of Stability-AI/lm-evaluation-harness](https://rinnakk.github.io/research/benchmarks/lm/)

#### [JGLUE](https://github.com/yahoojapan/JGLUE) (早大河原研 & ヤフー)

[GLUE ベンチマーク](https://gluebenchmark.com/)の日本語版として構築されたベンチマーク。MARC-ja, JCoLA, JSTS, JNLI, JSQuAD, JCommonsenseQA の 6 つのタスクを含む（[JCoLA](https://github.com/osekilab/JCoLA) は東大大関研により作成）。各タスクの詳細は[こちら](https://www.jstage.jst.go.jp/article/jnlp/30/1/30_63/_article/-char/ja)や[こちら](https://techblog.yahoo.co.jp/entry/2022122030379907/)を参照

#### [JMMLU](https://github.com/nlp-waseda/JMMLU) (早大河原研)

[MMLU ベンチマーク](https://github.com/hendrycks/test)の日本語版として構築されたベンチマーク。自然科学・人文科学・社会科学の幅広い学術領域から 4 択問題を構成している。元の MMLU を翻訳しただけでなく、日本独自の文化的背景に基づく問題（日本問題）を新たに追加しているのが特徴である。

#### [日本語 Open LLM Leaderboard](http://wandb.me/llm-jp-openllmleaderboard) (LLM-jp)

Huggingface の [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) と同様の検証を日本語 LLM に対して行ったもの。日本語 LLM の英語タスクにおける性能を確認できる。

<a id="open-ended-benchmark-suites"></a>
### 人間らしい応答の生成能力を中心に測定するベンチマーク/データセット

<a id="jp-mt-bench"></a>
#### [Japanese MT-bench](https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge) (Stability AI)

マルチターン会話能力を問う [MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) の日本語版。Writing, Roleplay, Reasoning, Math, Coding, Extraction, STEM, Humanities の 8 つのカテゴリから 10 問ずつ、計 80 問が収録されている。なお、日本語版作成の際には、日本の文化に合うように質問内容に一部修正が加えられている。<br>GPT-4 による 10 段階の絶対評価を行うスクリプトも含まれている。

#### [Rakuda Benchmark](https://github.com/yuzu-ai/japanese-llm-ranking) (YuzuAI)

日本の地理、歴史、政治、社会に関する[40問の自由質問](https://huggingface.co/datasets/yuzuai/rakuda-questions)に対してモデルに出力を行わせる。GPT-4 が同じ質問に対する2つのモデルの出力を比べ、どちらの答えが優れているかを判断することにより、モデルのランク付けを行う。

#### [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) (ELYZA)

複雑な指示・タスクを含む100件の日本語データで、全てのデータに対して評価観点がアノテーションされている。<br>要約を修正し修正箇所を説明するタスク、具体的なエピソードから抽象的な教訓を述べるタスク、ユーザーの意図を汲み役に立つAIアシスタントとして振る舞うタスク、場合分けを必要とする複雑な算数のタスク、未知の言語からパターンを抽出し日本語訳する高度な推論を必要とするタスク、複数の指示を踏まえた上でyoutubeの対話を生成するタスク、架空の生き物や熟語に関する生成・大喜利などの想像力が求められるタスクなどが含まれている。<br>評価結果は[こちら](https://docs.google.com/spreadsheets/d/1mtoy4QAqDPk2f_B0vDogFoOrbA5G42DBEEHdqM4VmDI/edit#gid=1023787356)や[こちら](https://zenn.dev/elyza/articles/5e7d9373c32a98)を参照。また、より新しいモデルを含む評価結果は[こちら](https://note.com/elyza/n/n5d42686b60b7)を参照。

#### [Japanese Vicuna QA Benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) (京大 言語メディア研究室)

MT-Bench の前身である [vicuna-blog-eval](https://github.com/lm-sys/vicuna-blog-eval) の日本語版。一般、知識、ロールプレイ、常識、フェルミ推定、反実仮想、コーディング、数学、ライティングに関する 80 問の質問を収録している。また、GPT-4 による自動評価（勝率計算）のスクリプトも含まれている。リーダーボードは[こちら](http://wandb.me/llm-jp-vicunaleaderboard)

<a id="domain-specific-benchmark-suites"></a>
### 特定ドメインの性能を測定するベンチマーク/データセット

#### [Japanese Language Model Financial Evaluation Harness](https://github.com/pfnet-research/japanese-lm-fin-harness) (Preferred Networks)

金融分野における日本語 LLM のベンチマーク。金融分野における感情分析タスク(chabsa)、証券分析における基礎知識タスク(cma_basics)、公認会計士試験における監査に関するタスク(cpa_audit)、ファイナンシャルプランナー試験の選択肢問題のタスク(fp2)、証券外務員試験の模擬試験タスク(security_sales_1)を含む。詳細は[こちら](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/564/1785)を参照

#### [Stockmark Business Questions](https://huggingface.co/datasets/stockmark/business-questions) (ストックマーク)

市場動向、時事問題、社会課題、ビジネストレンドなどの知識を問う問題が50題収録されている。

<a id="reference"></a>
## 各モデル・アーキテクチャの原論文

| モデル/アーキテクチャ | 初出時期 | 会議/ジャーナル | 論文 |
|:---|:---|:---|:--|
| Transformer | 2017.06.12 | NIPS(NeurIPS) 2017 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| GPT | 2018.06.11 | - | [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | 
| BERT | 2018.10.11 | NAACL 2019 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423/) |
| GPT-2 | 2019.02.14 | - | [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| XLNet | 2019.06.19 | NeurIPS 2019 | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) |
| RoBERTa | 2019.07.26 | - | [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) |
| Sentence-BERT | 2019.08.27 | EMNLP-IJCNLP 2019 | [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://aclanthology.org/D19-1410/) |
| ALBERT | 2019.09.26 | ICLR 2020 | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942) |
| DistilBERT | 2019.10.02 | EMC2 Workshop at NeurIPS 2019 | [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108) |
| T5 | 2019.10.23 | JMLR 2020 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) |
| BART | 2019.10.29 | ACL 2020 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://aclanthology.org/2020.acl-main.703/) |
| LayoutLM | 2019.12.31 | KDD 2020 | [LayoutLM: Pre-training of Text and Layout for Document Image Understanding](https://arxiv.org/abs/1912.13318) |
| ELECTRA | 2020.03.23 | ICLR 2020 | [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555) |
| ColBERT | 2020.04.27 | SIGIR 2020 | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://dl.acm.org/doi/10.1145/3397271.3401075) |
| Conformer | 2020.05.16 | INTERSPEECH 2020 | [Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100) |
| GPT-3 | 2020.05.28 | NeurIPS 2020 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) |
| DeBERTa | 2020.06.05 | ICLR 2021 | [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) |
| BigBird | 2020.07.28 | NeurIPS 2020 | [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) |
| LUKE | 2020.10.02 | EMNLP 2020 | [LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://aclanthology.org/2020.emnlp-main.523/) |
| CLIP | 2021.02.26 | ICML 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) |
| SimCSE | 2021.04.18 | EMNLP 2021 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://aclanthology.org/2021.emnlp-main.552/) |
| RoFormer | 2021.04.20 | - | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) |
| HuBERT | 2021.06.14 | TASLP 2021 | [HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units](https://arxiv.org/abs/2106.07447) |
| CLOOB | 2021.10.21 | NeurIPS 2022 | [CLOOB: Modern Hopfield Networks with InfoLOOB Outperform CLIP](https://arxiv.org/abs/2110.11316) |
| Stable Diffusion | 2021.12.20 | CVPR 2022 | [High-Resolution Image Synthesis With Latent Diffusion Models](https://arxiv.org/abs/2112.10752) |
| BLIP | 2022.01.28 | ICML 2022 | [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086) |
| MixCSE | 2022.02.22 | AAAI 2022 | [Unsupervised Sentence Representation via Contrastive Learning with Mixing Negatives](https://ojs.aaai.org/index.php/AAAI/article/view/21428) |
| InstructGPT | 2022.03.04 | NeurIPS 2022 | [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) |
| GPT-NeoX | 2022.04.14 | BigScience Research Workshop at ACL 2022 | [GPT-NeoX-20B: An Open-Source Autoregressive Language Model](https://aclanthology.org/2022.bigscience-1.9/) |
| DiffCSE | 2022.04.21 | NAACL 2022 | [DiffCSE: Difference-based Contrastive Learning for Sentence Embeddings](https://aclanthology.org/2022.naacl-main.311/) |
| GIT | 2022.05.27 | TMLR 2022 | [GIT: A Generative Image-to-text Transformer for Vision and Language](https://arxiv.org/abs/2205.14100) |
| BLIP-2 | 2023.01.30 | ICML 2023 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) |
| Llama | 2023.02.27 | - | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | 
| GPT-4 | 2023.03.15 | - | [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) |
| SigLIP | 2023.03.27 | ICCV 2023 | [Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/abs/2303.15343) |
| LLaVA | 2023.04.17 | NeurIPS 2023 | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) |
| MiniGPT-4 | 2023.04.20 | - | [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://arxiv.org/abs/2304.10592) |
| Fast Conformer | 2023.05.08 | ASRU 2023 | [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](https://arxiv.org/abs/2305.05084) |
| InstructBLIP | 2023.05.11 | - | [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://arxiv.org/abs/2305.06500) |
| RWKV | 2023.05.22 | - | [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048) |
| Llama 2 | 2023.07.18 | - | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) |
| Code Llama | 2023.08.24 | - | [Code Llama: Open Foundation Models for Code](https://arxiv.org/abs/2308.12950) |
| Qwen | 2023.09.28 | - | [Qwen Technical Report](https://arxiv.org/abs/2309.16609) |
| LLaVA-1.5 | 2023.10.05 | - | [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) |
| Mistral 7B | 2023.10.10 | - | [Mistral 7B](https://arxiv.org/abs/2310.06825) |
| Mamba | 2023.12.01 | - | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) |
| Nue ASR | 2023.12.06 | - | [An Integration of Pre-Trained Speech and Language Models for End-to-End Speech Recognition](https://arxiv.org/abs/2312.03668) |
| TinyLlama | 2024.01.04 | - | [TinyLlama: An Open-Source Small Language Model](https://arxiv.org/abs/2401.02385) |

<a id="reference-training"></a>
## LLMの学習手法の原論文

| 手法 | 初出時期 | 会議/ジャーナル | 論文 |
|:---|:---|:---|:---|
| PPO (RLHF) | 2017.07.20 | - | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) |
| Instruction Tuning<br>(Supervised Fine-tuning; SFT) | 2021.09.03 | ICLR 2022 | [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) |
| DPO | 2023.05.29 | NeurIPS 2023 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) |
| SteerLM | 2023.10.09 | Findings of EMNLP 2023 | [SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF](https://aclanthology.org/2023.findings-emnlp.754/) |

<a id="contributors"></a>
## コントリビューター

このプロジェクトに貢献してくれているコントリビューターのみなさんです！

<a href="https://github.com/llm-jp/awesome-japanese-llm/graphs/contributors">
  <img src="figures/contributors.svg" />
</a>

<a id="citation"></a>
## 引用

このリソースが役立つと感じられましたら、引用をご検討ください:

```
@software{LLM-jp_Overview_of_Japanese_2023,
    author = {{LLM-jp}},
    license = {Apache-2.0},
    month = jul,
    title = {{Overview of Japanese LLMs}},
    url = {https://github.com/llm-jp/awesome-japanese-llm},
    year = {2023}
}
```

---

[^1]: ただし、モデル高速化のため本家の Llama に対してアーキテクチャの変更を加えている。詳しくは以下を参照: [PLaMo-13Bを公開しました](https://tech.preferred.jp/ja/blog/llm-plamo/)

[^2]: 詳細は明記されていないが、プレスリリースには以下のような記述がある: 『学習データには、オープンデータセットに加え、Stability AI Japanが作成した独自のデータセットや、EleutherAI Polyglot project の日本語チーム及び Stable Community Japan のメンバーの協力のもとで作成したデータが含まれています。』

[^3]: 通常の左から右に単語を予測する代わりに、右から左に単語を予測するように訓練された言語モデルの評価を行った研究である。通常方向の言語モデルと逆方向の言語モデルの両方が公開されている。

[^4]: ○: HuggingFace の Model Hub にモデルがアップロードされており、`AutoModel.from_pretrained()` 等ですぐ読み込める。 △: Model Hub にはモデルがアップロードされていないが、HuggingFace (transformers, 旧 pytorch-transformers) の形式に対応している。✕: モデルがHuggingFaceに対応していない。

[^6]: 様々な形態素解析器とサブワード化手法の組み合わせを試した研究である。全ての組み合わせのモデルを掲載するのは大変なので、ここでは実験で最も平均のタスク性能が高い Juman++ + BPE のモデルを代表として掲載している。

[^7]: nlp-waseda/roberta-base-japanese 及び nlp-waseda/roberta-large-japanese はモデル入力の最大トークン長を128で事前学習しているが、nlp-waseda/roberta-large-japanese-seq512 は512で事前学習している

[^8]: ただし、最大系列長が通常の 512 から 1282 まで拡張されており、より長い入力文を扱うことができる

[^9]: small の方は日本語 Wikipedia と日本語金融コーパスを合わせてスクラッチ学習しているが、base の方は東北大BERTに日本語金融コーパスを追加学習しているという違いがある

[^10]: 万病WordPieceモデルは MeCab (IPA辞書+万病辞書) で単語分割した後 WordPiece でサブワード化するモデル、SentencePieceモデルは単語分割せずに直接 Unigram でサブワード化するモデル

[^12]: Instruction Tuning において、GPT-3.5, GPT-4 等の OpenAI のモデルで生成されたデータを使って学習しているため、OpenAI の規約に違反している可能性がある。

[^13]: ただし、KARAKURI LM を商用利用したい場合は、開発元であるカラクリ株式会社に直接連絡が必要であるとしている。