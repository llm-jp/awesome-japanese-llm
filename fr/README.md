# Aperçu des grands modèles de langage (LLM) en japonais
[ [**English**](../en/) | Français | [**日本語**](../) ]

<p align="center">
  <img src="../figures/parameter_size_overview.png" alt="LLMs en japonais et en non-japonais par taille de paramètres au fil du temps">
</p>
<figcaption style="font-style: italic; font-size: 0.9em; color: #6b7280; text-align: center;">Evolution du nombre de paramètres des LLMs en japonais et en non-japonais. Pour des informations sur le modèle japonais, nous nous référons à cet article, et pour le modèle non-japonais, nous nous référons au <a href="https://lifearchitect.ai/models-table/" target="_blank" rel="noreferrer">tableau des modèles</a> sur LifeArchitect.ai (notez cependant que certains modèles ont été omis en raison de l'espace limité sur le graphique. De plus, le nombre de paramètres pour le modèle non-japonais inclut des valeurs estimées). Veuillez nous informer de toute correction ou ajout nécessaire.</figcaption>

---

Voici une liste des LLMs disponibles au grand public, axés sur l'apprentissage du japonais, ainsi que leurs critères d'évaluation. Cette liste est maintenue par des bénévoles qui collectent des informations à partir de diverses sources telles que des articles académiques et d'autres ressources publiques.

⚠ Attention:
1. Nous ne pouvons garantir l’exactitude ou l’exhaustivité des informations présentées ici.
2. Certaines informations sont basées sur des conjectures et peuvent ne pas refléter votre cas d'utilisation spécifique.
3. Bien que de nombreux modèles soient publiés sous des licences permissives telles que MIT ou Apache 2.0, **certains modèles sont soumis à des conditions plus restrictives, notamment des clauses d'utilisation non commerciale  (exemple CC BY-NC-SA 4.0) ou d'autres modalités légales et contractuelles**

N'hésitez pas à signaler les erreurs sur la page [issues](https://github.com/llm-jp/awesome-japanese-llm/issues). N'hésitez pas également à contribuer directement avec une pull request.

## Table des matières
- [Modèles IA génératives](#generative)
  - [Modèles développés à partir de zéro](#full-scratch-models)
    - [D'usage général](#generative-scratch-general)
    - [Spécifique à un domaine](#generative-scratch-domain-specific)
  - [Modèles développés à partir d'LLM non-japonais (avec un apprentissage en continue en japonais)](#english-based-models)
    - [D'usage général](#generative-continual-general)
    - [Spécifique à un domaine](#generative-continual-domain-specific)
  - [Modèles développés à partir d'LLM non-japonais (avec un affinement par instructions en japonais)](#instruction-only-models)
    - [D'usage général](#generative-instruction-only-general)
    - [Spécifique à un domaine](#generative-instruction-only-domain-specific)
  - [Modèles fusionnés](#merged-models)
  - [Modèles basés sur des API](#api-based-models)
- [Modèles encodeur](#autoencoding)
  - [D'usage général](#autoencoding-general)
  - [Spécifique à un domaine](#autoencoding-domain-specific)
- [Plongement lexical par mots et par documents](#embeddings)
- [Modèles Vision-Language](#multimodal)
  - [Text+Image vers Text](#multimodal-text-generation)
    - [D'usage général](#multimodal-general)
    - [Spécifique à un domaine](#multimodal-domain-specific)
  - [Text vers Image](#multimodal-text-to-image)
  - [Autres](#multimodal-others)
- [Modèles Speech-Language](#speech)
  - [Reconnaissance automatique de la parole](#speech-asr)
  - [Autres](#speech-others)
- [Standard d'évaluation pour les LLM en japonais](#benchmark-suites)
  - [Benchmarks hybrides](#hybrid-benchmark-suites)
  - [Référence traditionnelle basé sur des tâches de Compréhension du langage naturel (NLU)](#basic-benchmark-suites)
  - [Standard des tâches génératives ouvertes](#open-ended-benchmark-suites)
  - [Benchmarks pour mesurer les capacités de raisonnement logique](#logical-reasoning-benchmark-suites)
  - [Benchmarks pour mesurer la performance dans des domaines spécifiques](#domain-specific-benchmark-suites)
  - [Benchmarks pour modèles d'embeddings](#embeddings-benchmark-suites)
  - [Benchmarks pour modèles vision-language](#vl-benchmark-suites)
- [Références pour les modèles et les architectures](#reference)
- [Références pour les méthodes d'entraînement](#reference-training)
- [Nos contributors](#contributors)
- [Citation](#citation)


<a id="generative"></a>
## Modèles IA génératives

*Pour les modèles multimodal, voir [ci-dessous.](#multimodal-text-generation)*

<a id="full-scratch-models"></a>
### Modèles développés à partir de zéro

<a id="generative-scratch-general"></a>
#### D'usage général

|    |  Architecture  | Longueur Maximale du Contexte | Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Stockmark-100b](https://huggingface.co/stockmark/stockmark-100b) | Llama<br>([**100b**](https://huggingface.co/stockmark/stockmark-100b), [**100b**-instruct-v0.1](https://huggingface.co/stockmark/stockmark-100b-instruct-v0.1)) | 4,096 | Pre-training: RedPajama, Wikipedia en japonais, Japanese mC4, Japanese CommonCrawl, Japanese Patent, Stockmark Web Corpus<br>(**910B** tokens)<br>Instruction Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | Stockmark | MIT |
| [Sarashina1](https://www.sbintuitions.co.jp/news/press/20240614_01/) | GPT-NeoX<br>([**7b**](https://huggingface.co/sbintuitions/sarashina1-7b), [**13b**](https://huggingface.co/sbintuitions/sarashina1-13b), [**65b**](https://huggingface.co/sbintuitions/sarashina1-65b)) | 2,048 | Pre-training: Japanese Common Crawl<br>(**1T** tokens) | SB Intuitions | MIT |
| [CyberAgentLM3 (CALM3)](https://huggingface.co/cyberagent/calm3-22b-chat) | Llama<br>([**22b**-chat](https://huggingface.co/cyberagent/calm3-22b-chat)) | **16,384** | undisclosed<br>(**2.0T** tokens) | CyberAgent | Apache 2.0 |
| [Sarashina2](https://www.sbintuitions.co.jp/news/press/20240614_01/) | Llama<br>([**7b**](https://huggingface.co/sbintuitions/sarashina2-7b), [**13b**](https://huggingface.co/sbintuitions/sarashina2-13b)) | 4,096 | Pre-training: Japanese Common Crawl, SlimPajama, StarCoder<br>(**2.1T** tokens) | SB Intuitions | MIT |
| [LLM-jp-13B v2.0](https://huggingface.co/llm-jp/llm-jp-13b-v2.0) | Llama<br>([**13b**-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-v2.0), [**13b**-instruct-full-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-ichikara_004_001_single-oasst-oasst2-v2.0), [**13b**-instruct-full-ac_001-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-ac_001-dolly-ichikara_004_001_single-oasst-oasst2-v2.0), [**13b**-instruct-full-ac_001_16x-dolly-ichikara_004_001_single-oasst-oasst2-v2.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-ac_001_16x-dolly-ichikara_004_001_single-oasst-oasst2-v2.0)) | 4,096 | Pre-training: [llm-jp-corpus-v2](https://gitlab.llm-jp.nii.ac.jp/datasets/llm-jp-corpus-v2)<br>Instruction Tuning: [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), [answer-carefully](https://liat-aip.sakura.ne.jp/wp/answercarefully-dataset/), Dolly Dataset, OASST1, OASST2 | LLM-jp | Apache 2.0 |
| [Fugaku-LLM](https://www.fujitsu.com/global/about/resources/news/press-releases/2024/0510-01.html) | GPT<br>([**13B**](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B), [**13B**-instruct](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct), [**13B**-instruct-gguf](https://huggingface.co/Fugaku-LLM/Fugaku-LLM-13B-instruct-gguf)) | 2,048 | Pre-training: undisclosed dataset<br>Instruction Tuning: OASST1, Dolly Dataset, GSM8K | Titech, Tohoku Univ., Fujitsu, RIKEN, Nagoya Univ., CyberAgent, Kotoba Technologies | Fugaku-LLM Terms of Use |
| [LLM-jp-13B v1.1](https://llm-jp.nii.ac.jp/blog/2024/02/09/v1.1-tuning.html) | GPT<br>([**13b**-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly_en-dolly_ja-ichikara_003_001-oasst_en-oasst_ja-v1.1), [**13b**-dpo-lora-hh_rlhf_ja-v1.1](https://huggingface.co/llm-jp/llm-jp-13b-dpo-lora-hh_rlhf_ja-v1.1)) | 2,048 | Instruction Tuning (LoRA or Full-parameter FT): Dolly Dataset, OASST1, [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/)<br>DPO (LoRA): HH RLHF | LLM-jp | Apache 2.0 |
| [LLM-jp-13B](https://www.nii.ac.jp/en/news/release/2023/1020.html) | GPT<br>([1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0), [**13b**-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0), [**13b**-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0), [**13b**-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0), [**13b**-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0), [**13b**-instruct-lora-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-v1.0), [**13b**-instruct-lora-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-dolly-oasst-v1.0), [**13b**-instruct-lora-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly-oasst-v1.0)) | 2,048 | Pré-entraînement: [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) (Wikipedia, Japanese mC4, The Pile, Stack) (**300B** tokens)<br>Instruction Tuning (Full-parameter FT or LoRA): jaster, Dolly Dataset, OASST1 | LLM-jp | Apache 2.0 |
| [PLaMo-13B](https://www.preferred.jp/en/news/pr20230928/) | Llama[^1]<br>([**13b**](https://huggingface.co/pfnet/plamo-13b), [**13b**-instruct](https://huggingface.co/pfnet/plamo-13b-instruct), [**13b**-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc)) |base: 4,096<br>instruct, instruct-nc: 8,192 | Pré-entraînement: C4, Project Gutenberg, RedPajama, Japanese Wikipedia, Japanese mC4<br>(**1.5T** tokens)<br>Instruction Tuning: Dolly, HH RLHF, OASST1, wikinews (+Alpaca in NC model)  | Preferred Networks | Apache 2.0<br>(CC BY-NC 4.0 as for NC model) |
| [Stockmark-13b](https://stockmark.co.jp/news/20231027) | Llama<br>([**13b**](https://huggingface.co/stockmark/stockmark-13b), [**13b**-instruct](https://huggingface.co/stockmark/stockmark-13b-instruct)) | 2,048 | Wikipedia en japonais, Japanese CC-100, Japanese mC4, Japanese CommonCrawl, Japanese Patent, Stockmark Web Corpus<br>(**220B** tokens)<br>Instruction Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | Stockmark | base: MIT<br>instruct: CC BY-NC-SA 4.0 |
| [Weblab-10B](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001) | GPT-NeoX <br> ([**10b**](https://huggingface.co/matsuo-lab/weblab-10b), [**10b**-instruction-sft](https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft)) | 2,048 | Japanese mC4, The Pile <br> (**600B** tokens) <br>Instruction Tuning: Alpaca, FLAN | Université de Tokyo Matsuo Lab | CC BY&#x2011;NC 4.0 |
| [Japanese StableLM Alpha](https://stability.ai/blog/stability-ai-new-jplm-japanese-language-model-stablelm) | GPT-NeoX <br> ([base-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b), [instruct-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b), [instruct-alpha-**7b**-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2)) | 2,048 | Wikipédia, Japanese CC&#x2011;100, Japanese mC4, Japanese OSCAR, RedPajama, ensembles de données privés[^2]<br>(**750B** tokens)<br>Instruction Tuning: Dolly, HH&#x2011;RLHF, wikinews,  Alpaca (discarded in v2) | Stability AI | base: Apache 2.0<br>instruct (v1): [Research license](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b/tree/main)<br>instruct (v2): Apache 2.0 |
| [CyberAgentLM2 (CALM2)](https://www.cyberagent.co.jp/news/detail/id=29479) | Llama<br>([**7b**](https://huggingface.co/cyberagent/calm2-7b), [**7b**-chat](https://huggingface.co/cyberagent/calm2-7b-chat), [**7b**-chat-dpo-experimental](https://huggingface.co/cyberagent/calm2-7b-chat-dpo-experimental)) | base: 4,096<br>chat: **32,768** | Ensembles de données japonais et anglais accessibles au public (détails inconnus)<br>(**1.3T** tokens)<br>DPO: Chatbot Arena Conversations JA (calm2) Dataset  | CyberAgent | Apache 2.0<br>(CC BY 4.0 as for DPO model) |
| [OpenCALM](https://www.cyberagent.co.jp/news/detail/id=28817) | GPT-NeoX <br> ([small](https://huggingface.co/cyberagent/open-calm-small), [medium](https://huggingface.co/cyberagent/open-calm-medium), [large](https://huggingface.co/cyberagent/open-calm-large), [**1b(1.4b)**](https://huggingface.co/cyberagent/open-calm-1b), [**3b(2.7b)**](https://huggingface.co/cyberagent/open-calm-3b), [**7b(6.8b)**](https://huggingface.co/cyberagent/open-calm-7b)) | 2,048 | Wikipedia en japonais, Japanese mC4, Japanese CC&#x2011;100 | CyberAgent | CC BY&#x2011;SA 4.0 |
| [Stormy](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/422/1350) | GPT-NeoX <br>([**7b(6.8b)**](https://huggingface.co/izumi-lab/stormy-7b-10ep)) | 2,048 | OpenCALM fine-tuned sur <br>llm-japanese-dataset v0 sans âches de traduction | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |
| [rinna GPT <br> (En-Ja Bilingual)](https://rinna.co.jp/news/2023/07/20230731.html) | GPT-NeoX <br>([**4b(3.8b)**](https://huggingface.co/rinna/bilingual-gpt-neox-4b), [**4b(3.8b)**-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k), [**4b(3.8b)**-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft), [**4b(3.8b)**-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo)) | 8k model: 8,192<br>others: 2,048 |  Wikipedia, Japanese CC&#x2011;100, Japanese C4, RedPajama, The Pile<br>(**524B** tokens)<br>Instruction Tuning: HH&#x2011;RLHF, FLAN<br>PPO: HH&#x2011;RLHF par apprentissage par renforcement  <br>8k: entrainé sur du long texte | rinna | MIT |
| [japanese-large-lm](https://engineering.linecorp.com/ja/blog/3.6b-japanese-language-model-with-improved-dialog-performance-by-instruction-tuning) | GPT-NeoX <br>([**1.7b**](https://huggingface.co/line-corporation/japanese-large-lm-1.7b), [**3.6b**](https://huggingface.co/line-corporation/japanese-large-lm-3.6b), [**1.7b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft), [**3.6b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft)) | 2,048 | Wikipedia en japonais, Japanese CC&#x2011;100, Japanese C4, Japanese OSCAR et ensembles de données privés<br>(**650GB**)<br>Instruction Tuning: OASST1 | LINE | Apache 2.0 |
| [rinna GPT <br> (Japanese only)](https://rinna.co.jp/news/2023/05/20220531.html) | GPT / GPT-NeoX <br>([xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall), [small](https://huggingface.co/rinna/japanese-gpt2-small), [medium](https://huggingface.co/rinna/japanese-gpt2-medium), [**1b**](https://huggingface.co/rinna/japanese-gpt-1b), [neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small), [neox-**3.6b**](https://huggingface.co/rinna/japanese-gpt-neox-3.6b), [neox-**3.6b**-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft), [neox-**3.6b**-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2), [neox-**3.6b**-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)) | ≤ 2,048 | Wikipédia en japonais, Japanese CC&#x2011;100 <br> (1b et plus modèles à ajouter <br>Japanese mC4)<br>Instruction Tuning: HH&#x2011;RLHF, FLAN, SHP <br>PPO: HH&#x2011;RLHF par apprentissage par renforcement | rinna | MIT |
| [RetrievaT5](https://note.com/retrieva/n/n7b4186dc5ada) | T5 <br>([small (short)](https://huggingface.co/retrieva-jp/t5-small-short), [small (medium)](https://huggingface.co/retrieva-jp/t5-small-medium), [small (long)](https://huggingface.co/retrieva-jp/t5-small-long), [base (short)](https://huggingface.co/retrieva-jp/t5-base-short), [base (medium)](https://huggingface.co/retrieva-jp/t5-base-medium), [base (long)](https://huggingface.co/retrieva-jp/t5-base-long), [large (short)](https://huggingface.co/retrieva-jp/t5-large-short), [large (medium)](https://huggingface.co/retrieva-jp/t5-large-medium), [large (long)](https://huggingface.co/retrieva-jp/t5-large-long), [**xl(3b)**](https://huggingface.co/retrieva-jp/t5-xl)) |  | Wikipédia en japonais, Japanese mC4 | Retrieva | CC BY&#x2011;SA 4.0 |
| [Spiral-RetNet-3b-base](https://prtimes.jp/main/html/rd/p/000000014.000120221.html) | RetNet<br>([**3b**](https://huggingface.co/Spiral-AI/Spiral-RetNet-3b-base)) | 2,048 |  Wikipedia, Japanese CC-100, CulturaX | Spiral.AI | MIT |
| [kotomamba-2.8B](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0) | Mamba<br>([**2.8B**-v1.0](https://huggingface.co/kotoba-tech/kotomamba-2.8B-v1.0)) | 2,048 | Wikipedia en japonais, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [ABEJA GPT](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207) | GPT / GPT-NeoX <br>([large](https://huggingface.co/abeja/gpt2-large-japanese), [neox-**2.7b**](https://huggingface.co/abeja/gpt-neox-japanese-2.7b)) |  | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR | ABEJA | MIT |
| [WasedaGPT](https://huggingface.co/nlp-waseda/gpt2-xl-japanese) | GPT <br> ([small](https://huggingface.co/nlp-waseda/gpt2-small-japanese), [**xl(1.5b)**](https://huggingface.co/nlp-waseda/gpt2-xl-japanese)) |  | Wikipédia en japonais, Japanese CC&#x2011;100 | Université de Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 |
| [StockmarkGPT](https://stockmark.co.jp/news/20230808) | GPT-NeoX <br>([**1.4b**](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b)) |  | Wikipédia en japonais (0.88B tokens), Japanese CC&#x2011;100 (10.5B tokens), ensembles de données privés (8.6B tokens) | Stockmark | MIT |
| [YellowbackGPT](https://tech.yellowback.net/posts/gpt-neo-japanese) | GPT-NeoX <br>([**1.3b**](https://huggingface.co/yellowback/gpt-neo-japanese-1.3B)) |  | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR | Yellowback | Apache 2.0 |
| [colorfulscoop GPT](https://huggingface.co/colorfulscoop/gpt2-small-ja) | GPT <br>([small](https://huggingface.co/colorfulscoop/gpt2-small-ja)) |  | Wikipédia en japonais | Colorful Scoop | CC BY&#x2011;SA 3.0 |
| [TitechGPT](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/H9-1.pdf) | GPT <br>([medium](https://huggingface.co/okazaki-lab/japanese-gpt2-medium-unidic), [medium-reversed](https://huggingface.co/okazaki-lab/japanese-reversed-gpt2-medium-unidic)) [^3] |  | Wikipédia en japonais, Japanese CC&#x2011;100 | Titech Okazaki Lab | CC BY&#x2011;SA 4.0 |
| [KyotoUniversityGPT](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) | GPT <br>([small](https://huggingface.co/ku-nlp/gpt2-small-japanese-char), [medium](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char), [large](https://huggingface.co/ku-nlp/gpt2-large-japanese-char)) |  | Wikipédia en japonais (3.2GB), Japanese CC&#x2011;100 (85GB), Japanese OSCAR (54GB) | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 |
| [JapaneseBART](https://huggingface.co/ku-nlp/bart-base-japanese) | BART <br>([base](https://huggingface.co/ku-nlp/bart-base-japanese), [large](https://huggingface.co/ku-nlp/bart-large-japanese)) |  | Wikipédia en japonais (18M sentences) | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 |
| [Megagon Labs T5](https://github.com/megagonlabs/t5-japanese) | T5 <br>([base](https://huggingface.co/megagonlabs/t5-base-japanese-web)) |  | Japanese mC4 (782 GB), Wikipédia en japonais 40b (2 GB) | Megagon Labs <br> (Recruit Co.,Ltd.) | Apache 2.0 |

<a id="generative-scratch-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Japanese Dialog Transformer](https://github.com/nttcslab/japanese-dialog-transformers) | Dialogue | Transformer | Pairs de réponses venant de Twitter | NTT | [License en évaluaiton](https://github.com/nttcslab/japanese-dialog-transformers/blob/main/LICENSE.md) |
| [Japanese News BART](https://tech.stockmark.co.jp/blog/bart-japanese-base-news/) | Affaires |  BART ([base](https://huggingface.co/stockmark/bart-base-japanese-news)) | Articles de l'actualité économique en japonais (21M articles) | Stockmark | MIT |
| [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | Science | BART ([base](https://huggingface.co/EhimeNLP/AcademicBART)) | CiNii Japanese Papers | Université d'Ehime AI Lab | Apache 2.0 |

<a id="english-based-models"></a>
### Modèles développés à partir d'LLM non-japonais (avec un apprentissage en continue en japonais)

<a id="generative-continual-general"></a>
#### D'usage général

|    | Base du Model  |  Données d'entraînement  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [Llama 3 Swallow 70B](https://swallow-llm.github.io/llama3-swallow.en.html)<br>([70B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-70B-v0.1), [70B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-70B-Instruct-v0.1)) | Llama 3 (**70b**) | Pre-training: Algebraic Stack, Wikipedia, RefinedWeb, Swallow Corpus, Cosmopedia, Laboro ParaCorpus, OpenWebMath<br>Instruction Tuning: OASST1 [^17] | Swallow Project | Llama 3 Community License |
| [Swallow 70B](https://swallow-llm.github.io/swallow-llama.en.html)<br>([70b-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-hf), [70b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-hf), [70b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-70b-instruct-v0.1), [70b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-hf), [70b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-70b-NVE-instruct-hf)) | Llama 2 (**70b**) | Pre-training: Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1: OASST1, OASST2 | Swallow Project | Llama 2 Community License |
| [KARAKURI LM](https://medium.com/karakuri/introducing-karakuri-lm-34c79a3bf341)<br>([70b-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-v0.1), [70b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-70b-chat-v0.1)) | Llama 2 (**70b**) | Pre-training: mC4, CC100, OSCAR, RedPajama, undisclosed dataset<br>(**16B** tokens)<br>SteerLM: OASST2, undisclosed dataset | KARAKURI | Llama 2 Community License[^13] |
| [Japanese Stable LM Beta 70B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-70b), [instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b)) | Llama 2 (**70b**) | Pre-training: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(excluding Books3)<br>(**100B** tokens)<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [Swallow-MX 8x7B](https://swallow-llm.github.io/swallow-mistral.ja.html)<br>([8x7b-NVE-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MX-8x7b-NVE-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | Pre-training: Algebraic Stack, Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile, The Vault | Swallow Project | Apache 2.0 |
| [KARAKURI LM 8x7B Instruct v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-instruct-v0.1)<br>([8x7b-instruct-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-instruct-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | trained Swallow-MX 8x7B on the following datasets: Dolly Dataset, OASST2, HelpSteer, glaive-code-assistant-v3, glaive-function-calling-v2, synthetic_text_to_sql, MetaMathQA, orca-math-word-problems-200k, rag-dataset-12000, rag-hallucination-dataset-1000, undisclosed dataset | KARAKURI | Apache 2.0 (?)[^12] |
| [KARAKURI LM 8x7B Chat v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-chat-v0.1)<br>([8x7b-chat-v0.1](https://huggingface.co/karakuri-ai/karakuri-lm-8x7b-chat-v0.1)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**) | trained Swallow-MX 8x7B on OASST2, HelpSteer, and undisclosed datasets using SteerLM | KARAKURI | Apache 2.0 |
| [ABEJA-Mixtral-8x7B-japanese](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese)<br>([8x7B-v0.1-japanese](https://huggingface.co/abeja/Mixtral-8x7B-v0.1-japanese), [8x7B-Instruct-v0.1-japanese](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese), [8x7B-Instruct-v0.1-japanese-alpha](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese-alpha), [8x7B-Instruct-v0.1-japanese-alpha-merged](https://huggingface.co/abeja/Mixtral-8x7B-Instruct-v0.1-japanese-alpha-merged)) | Mixtral-8x7B-Instruct-v0.1 (**46.7b**)<br>\*Le modèle sans "Instruct" dans son nom est basé sur Mixtral-8x7B-v0.1 | Pre-training: Japanese CC,	Redpajama, undisclosed dataset<br>（**450B** tokens） | ABEJA | Apache 2.0 |
| [Nekomata 14B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([14b](https://huggingface.co/rinna/nekomata-14b), [14b-instruction](https://huggingface.co/rinna/nekomata-14b-instruction), [14b-gguf](https://huggingface.co/rinna/nekomata-14b-gguf), [14b-instruction-gguf](https://huggingface.co/rinna/nekomata-14b-instruction-gguf)) | Qwen (**14b**) | Pre-training: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, undisclosed dataset<br>(**66B** tokens)<br>Instruction Tuning: Dolly Dataset, FLAN, subsets of llm-japanese-dataset | rinna | Tongyi Qianwen LICENSE |
| [Swallow 13B](https://swallow-llm.github.io/swallow-llama.en.html)<br>([13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf), [13b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-hf), [13b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-13b-instruct-v0.1), [13b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-NVE-hf)) | Llama 2 (**13b**) | Pre-training: Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1: OASST1, OASST2 | Swallow Project | Llama 2 Community License |
| [LEIA-Swallow-13B](https://arxiv.org/pdf/2402.11485)<br>([13b](https://huggingface.co/leia-llm/Leia-Swallow-13b)) | Llama 2 (**13b**) | additionally trained Swallow 13B using LEIA | Individual ([Ikuya Yamada](https://scholar.google.com/citations?user=M7YivToAAAAJ), [Ryokan Ri](https://scholar.google.co.jp/citations?user=z9is5FAAAAAJ)) | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-13b](https://note.com/elyza/n/n5d42686b60b7)<br>([13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b), [13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct), [13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast), [13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct)) | Llama 2 (**13b**) | Pre-training: Japanese Wikipedia, Japanese OSCAR, and other crawled data<br>(**18B** tokens)<br>Instruction Tuning: undisclosed dataset |ELYZA | Llama 2 Community License |
| [Llama 3 Swallow 8B](https://swallow-llm.github.io/llama3-swallow.en.html)<br>([8B-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-v0.1), [8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1)) | Llama 3 (**8b**) | Pre-training: Algebraic Stack, Wikipedia, RefinedWeb, Swallow Corpus, Cosmopedia, Laboro ParaCorpus, OpenWebMath<br>Instruction Tuning: OASST1 [^17] | Swallow Project | Llama 3 Community License |
| [Llama 3 Youko 8B](https://huggingface.co/rinna/llama-3-youko-8b)<br>([8b](https://huggingface.co/rinna/llama-3-youko-8b)) | Llama 3 (**8b**) | Pre-training: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, undisclosed dataset<br>(**22B** tokens) | rinna | Llama 3 Community License |
| [Llama 3 ELYZA JP 8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B)<br>([8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B), [8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF), [8B-AWQ](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-AWQ)) | Llama 3 (**8b**) | undisclosed | ELYZA | Llama 3 Community License |
| [Llama 3 neoAI 8B Chat v0.1](https://prtimes.jp/main/html/rd/p/000000017.000109048.html)<br>([8B-Chat-v0.1](https://huggingface.co/neoai-inc/Llama-3-neoAI-8B-Chat-v0.1)) | Llama 3 (**8b**) | undisclosed | neoAI | Llama 3 Community License |
| [Swallow 7B](https://swallow-llm.github.io/swallow-llama.en.html)<br>([7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf), [7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf), [7b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-v0.1), [7b-NVE-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-hf), [7b-NVE-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-NVE-instruct-hf), [7b-plus-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-plus-hf)) | Llama 2 (**7b**) | Pre-training: Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1<br>*v0.1: OASST1, OASST2 | Swallow Project | Llama 2 Community License |
| [LEIA-Swallow-7B](https://arxiv.org/pdf/2402.11485)<br>([7b](https://huggingface.co/leia-llm/Leia-Swallow-7b)) | Llama 2 (**7b**) | additionally trained Swallow 7B using LEIA | Individual ([Ikuya Yamada](https://scholar.google.com/citations?user=M7YivToAAAAJ), [Ryokan Ri](https://scholar.google.co.jp/citations?user=z9is5FAAAAAJ)) | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-7b](https://note.com/elyza/n/na405acaca130)<br> ([7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct), [7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast), [7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct)) | Llama 2 (**7b**) | Pre-training: Japanese Wikipedia, Japanese OSCAR, and other crawled data<br>(**18B** tokens)<br>Instruction Tuning: undisclosed dataset |ELYZA | Llama 2 Community License |
| [Youri 7B](https://rinna.co.jp/news/2023/10/20231031.html)<br>([7b](https://huggingface.co/rinna/youri-7b), [7b-instruction](https://huggingface.co/rinna/youri-7b-instruction), [7b-chat](https://huggingface.co/rinna/youri-7b-chat), [7b-gptq](https://huggingface.co/rinna/youri-7b-gptq), [7b-instruction-gptq](https://huggingface.co/rinna/youri-7b-instruction-gptq), [7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq)) | Llama 2 (**7b**) |Pre-training: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, undisclosed dataset<br>(**40B** tokens)<br>Instruction Tuning: Dolly Dataset, FLAN, subsets of llm-japanese-dataset| rinna | Llama 2 Community License |
| [houou-7b](https://corp.moneyforward.com/news/release/corp/20231206-mf-press-1/)<br>([instruction-7b-v1](https://huggingface.co/moneyforward/houou-instruction-7b-v1), [instruction-7b-v2](https://huggingface.co/moneyforward/houou-instruction-7b-v2), [instruction-7b-v3](https://huggingface.co/moneyforward/houou-instruction-7b-v3)) | Llama 2 (**7b**) | Instruction-tuned Youri 7B (base) on [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | MoneyForward | Llama 2 Community License |
| [Japanese Stable LM Beta 7B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-7b), [base-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-ja_vocab-beta-7b), [instruct-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-7b), [instruct-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b)) |  Llama 2 (**7b**) | Pre-training: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(excluding Books3)<br>(**100B** tokens)<br>Instruction Tuning: Dolly Dataset, HH RLHF, OASST1 | Stability AI | Llama 2 Community License |
| [SambaLingo-Japanese](https://sambanova.ai/blog/sambalingo-open-source-language-experts)<br>([Base](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Base), [Chat](https://huggingface.co/sambanovasystems/SambaLingo-Japanese-Chat)) | Llama 2 (**7b**) | Pre-training: CulturaX<br>Instruction Tuning: ultrachat_200k<br>DPO: ultrafeedback, cai-conversation-harmless | SambaNova Systems | Llama 2 Community License (?)[^12] |
| [blue-lizard](https://prtimes.jp/main/html/rd/p/000000010.000125694.html)<br>([blue-lizard](https://huggingface.co/Deepreneur/blue-lizard)) | Llama 2 (**7b**) | undisclosed | Deepreneur | Llama 2 Community License |
| [Swallow-MS 7B](https://swallow-llm.github.io/swallow-mistral.ja.html)<br>([7b-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-v0.1), [7b-instruct-v0.1](https://huggingface.co/tokyotech-llm/Swallow-MS-7b-instruct-v0.1)) | Mistral-7B-v0.1 (**7b**) | Pre-training: Algebraic Stack, Japanese Wikipedia, RefinedWeb, Swallow Corpus, The Pile<br>Instruction Tuning: Dolly Dataset, OASST1 | Swallow Project | Apache 2.0 |
| [RakutenAI-7B](https://global.rakuten.com/corp/news/press/2024/0321_01.html?year=2024&month=3&category=corp)<br>([7B](https://huggingface.co/Rakuten/RakutenAI-7B), [7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct), [7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat)) | Mistral-7B-v0.1 (**7b**) | Pre-training: undisclosed<br>Instruction Tuning: Dolly Dataset, OASST1, datasets converted from the train split of NLU datasets (like jaster), undisclosed dataset | Rakuten | Apache 2.0 |
| [Japanese Stable LM Gamma 7B](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([base-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b), [instruct-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b)) | Mistral-7B-v0.1 (**7b**) | Pre-training: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(excluding Books3)<br>(**100B** tokens)<br>Instruction Tuning: Dolly Dataset, HH RLHF, wikinews subset of llm-japanese-dataset | Stability AI |  Apache 2.0  |
| [ChatNTQ JA 7B](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)<br>([7b-v1.0](https://huggingface.co/NTQAI/chatntq-ja-7b-v1.0)) | Mistral-7B-v0.1 (**7b**) | Instruction-tuned Japanese Stable LM Gamma 7B (base) on their own datasets | NTQ Solution | Apache 2.0  |
| [Shisa Gamma 7B](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)<br>([7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1)) | Mistral-7B-v0.1 (**7b**) | Instruction-tuned Japanese Stable LM Gamma 7B (base) on ultra-orca-boros-en-ja | AUGMXNT | Apache 2.0 (?)[^12]  |
| [Shisa 7B](https://github.com/AUGMXNT/shisa/wiki)<br>([base-7b-v1](https://huggingface.co/augmxnt/shisa-base-7b-v1), [7b-v1](https://huggingface.co/augmxnt/shisa-7b-v1)) | Mistral-7B-v0.1 (**7b**) | Pre-training: shisa-pretrain-en-ja-v1 (**8B** tokens)<br>Instruction Tuning & DPO: ultra-orca-boros-en-ja, shisa-en-ja-dpo-v1  | AUGMXNT |  Apache 2.0  |
| [Karasu](https://note.com/peter_lightblue/n/ne08a7c8cc47a)<br>([7B](https://huggingface.co/lightblue/karasu-7B), [7B-chat](https://huggingface.co/lightblue/karasu-7B-chat), [7B-chat-plus](https://huggingface.co/lightblue/karasu-7B-chat-plus), [7B-chat-plus-unleashed](https://huggingface.co/lightblue/karasu-7B-chat-plus-unleashed)) | Mistral-7B-v0.1 (**7b**) | Additionally trained Shisa 7B (base) on Aozora Bunko, Japanese Law Precedent Dataset, Japanese Wikipedia, Japanese domain webscrapes from the Japanese subset of CulturaX, UltraChat 200k<br>(**7B** tokens)<br>Instruction Tuning: ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, undisclosed dataset | Lightblue |  Apache 2.0 (?)[^12]  |
| [Nekomata 7B](https://rinna.co.jp/news/2023/12/20231221.html)<br>([7b](https://huggingface.co/rinna/nekomata-7b), [7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction), [7b-gguf](https://huggingface.co/rinna/nekomata-7b-gguf), [7b-instruction-gguf](https://huggingface.co/rinna/nekomata-7b-instruction-gguf)) | Qwen (**7b**) | Pre-training: Wikipedia, Japanese C4, Japanese CC-100, Japanese OSCAR, The Pile, undisclosed dataset<br>(**66B** tokens)<br>Instruction Tuning: Dolly Dataset, FLAN, subsets of llm-japanese-dataset | rinna | Tongyi Qianwen LICENSE |
| [lightblue/japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) | MPT (**7b**) | Japanese mC4 | Lightblue | Apache 2.0 (?)[^12] |
| [Japanese Stable LM 3B-4E1T](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base), [3b-4e1t-instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-instruct)) | StableLM-3B-4E1T (**3b**) |Pre-training: Wikipedia, Japanese mC4, Japanese CC-100, Japanese OSCAR, SlimPajama(excluding Books3)<br>(**100B** tokens)<br>Instruction Tuning: Dolly Dataset, HH RLHF, wikinews subset of llm-japanese-dataset | Stability AI |  Apache 2.0  |
| [kotomamba-2.8B-CL](https://huggingface.co/kotoba-tech/kotomamba-2.8B-CL-v1.0) | mamba-2.8b-slimpj<br>(**2.8b**) | Japanese Wikipedia, Swallow Corpus, SlimPajama | Kotoba Technologies | Apache 2.0 |
| [Japanese Stable LM 2 1.6B](https://ja.stability.ai/blog/japanese-stable-lm-2-16b)<br>([base](https://huggingface.co/stabilityai/japanese-stablelm-2-base-1_6b), [instruct](https://huggingface.co/stabilityai/japanese-stablelm-2-instruct-1_6b)) | Stable LM 2 1.6B (**1.6b**) | Pre-training: Wikipedia, CulturaX<br>Instruction Tuning: jaster, [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/), alpaca-gpt4-japanese, ultra-orca-boros-en-ja-v1 | Stability AI | STABILITY AI NON-COMMERCIAL RESEARCH COMMUNITY LICENSE |
| [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) | TinyLlama (**1.1b**) | Pre-training: Japanese OSCAR, Japanese mC4<br>(**3B** tokens) | Lightblue | Apache 2.0 |

<a id="generative-continual-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [AIgroup-CVM-utokyohospital/MedSwallow-70b](https://huggingface.co/AIgroup-CVM-utokyohospital/MedSwallow-70b) | Médecine | Llama 2 (**70b**) | Université de Tokyo - AI Group du Département hospitalier de médecine cardiovasculaire | CC BY-NC-SA 4.0 |
| [nekomata-14b-pfn-qfin](https://arxiv.org/pdf/2404.10555)<br>([qfin](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin), [qfin-inst-merge](https://huggingface.co/pfnet/nekomata-14b-pfn-qfin-inst-merge)) | Finance | Qwen (**14b**) | Preferred Networks | Tongyi Qianwen LICENSE |
| [Watashiha-Llama-2-13B-Ogiri-sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft/blob/main/README_en.md)<br>([sft](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft), [sft-neuron](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-neuron)) | [Oogiri](https://en.wikipedia.org/wiki/Glossary_of_owarai_terms#oogiri)| Llama 2 (**13b**) | Watashiha | Llama 2 Community License |
| [ELYZA-japanese-CodeLlama-7b](https://note.com/elyza/n/n5bce23d7c9c8)<br>([7b](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b-instruct)) | Codage | Code Llama<br>(**7b**) | ELYZA | Llama 2 Community License |
| [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) | Génération de récits | GPT-J (**6b**) | Individuel ([Hiroyuki Osone](https://scholar.google.co.jp/citations?user=6ID5K3oAAAAJ)) | CreativeML OpenRAIL-M License |
| [NovelAI/genji-jp](https://huggingface.co/NovelAI/genji-jp) | Génération de récits | GPT-J (**6b**) | NovelAI |  ？  |

<a id="instruction-only-models"></a>
### Modèles développés à partir d'LLM non-japonais (avec un affinement par instructions en japonais)

<a id="generative-instruction-only-general"></a>
#### D'usage général

|    | Base du Model  |  Données d'entraînement  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [ao-Karasu](https://note.com/peter_lightblue/n/n483d194d3614)<br>([72B](https://huggingface.co/lightblue/ao-karasu-72B)) | Qwen1.5 (**72b**) | ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, Japanese technical blogs, News stories, QA site answers, undisclosed dataset | Lightblue |  Tongyi Qianwen LICENSE (?)[^12] |
| [Llama 3 shisa-v1-llama3-70b](https://huggingface.co/shisa-ai/shisa-v1-llama3-70b)<br>([70b](https://huggingface.co/shisa-ai/shisa-v1-llama3-70b)) | Llama 3 (**70b**) | ultra-orca-boros-en-ja-v1 | Shisa.AI | Llama 3 Community License (?)[^12] |
| [AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese](https://huggingface.co/AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese) | Llama 2 (**70b**) || Université de Tokyo - AI Group du Département hospitalier de médecine cardiovasculaire |  Llama 2 Community License |
| [doshisha-mil/llama-2-70b-chat-4bit-japanese-v1](https://huggingface.co/doshisha-mil/llama-2-70b-chat-4bit-japanese-v1) | Llama 2 (**70b**) || Université de Doshisha Media Informatics Lab | ？ |
| [Qarasu](https://note.com/peter_lightblue/n/ne08a7c8cc47a)<br>([14B-chat-plus-unleashed](https://huggingface.co/lightblue/qarasu-14B-chat-plus-unleashed)) | Qwen (**14b**) | ultra-orca-boros-en-ja-v1, OASST1, ShareGPT, undisclosed dataset | Lightblue | Tongyi Qianwen LICENSE (?)[^12] |
| [Sparticle/llama-2-13b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-13b-chat-japanese-lora) | Llama 2 (**13b**) || Sparticle | ？ |
| [izumi-lab/llama-13b-japanese-lora-v0-1ep](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep) | Llama (**13b**) || Université de Tokyo Izumi Lab |  ？ |
| [Llama 3 Suzume 8B](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese)<br>([8B-japanese](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese), [8B-japanese-gguf](https://huggingface.co/lightblue/suzume-llama-3-8B-japanese-gguf)) | Llama 3 (**8b**) | megagonlabs/instruction_ja, ShareGPT, undisclosed dataset | Lightblue | Llama 3 Community License (?)[^12] |
| [Llama 3 shisa-v1-llama3-8b](https://huggingface.co/shisa-ai/shisa-v1-llama3-8b)<br>([8b](https://huggingface.co/shisa-ai/shisa-v1-llama3-8b)) | Llama 3 (**8b**) | ultra-orca-boros-en-ja-v1 | Shisa.AI | Llama 3 Community License (?)[^12] |
| [ganchengguang/Yoko-7B-Japanese-v1](https://huggingface.co/ganchengguang/Yoko-7B-Japanese-v1) | Llama 2 (**7b**) || Université nationale de Yokohama Mori Lab |  ？  |
| [Sparticle/llama-2-7b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-7b-chat-japanese-lora) | Llama 2 (**7b**) || Sparticle |  ？  |
| [izumi-lab/llama-7b-japanese-lora-v0-5ep](https://huggingface.co/izumi-lab/llama-7b-japanese-lora-v0-5ep) | Llama (**7b**) || Université de Tokyo Izumi Lab |  ？  |
| [lightblue/jod](https://huggingface.co/lightblue/jod) | Mistral-7B-SlimOrca (**7b**) || Lightblue | Apache 2.0 |
| [NTQAI/chatntq-7b-jpntuned](https://huggingface.co/NTQAI/chatntq-7b-jpntuned) | RWKV-4 World (**7b**)|| NTQ Solution |  ？  |

<a id="generative-instruction-only-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [JMedLoRA](https://arxiv.org/pdf/2310.10083.pdf)<br>([llama2-jmedlora-6.89ep](https://huggingface.co/AIgroup-CVM-utokyohospital/llama2-jmedlora-6.89ep)) | Médecine | Llama 2 (**70b**) | Université de Tokyo - AI Group du Département hospitalier de médecine cardiovasculaire | CC BY-NC 4.0 |

<a id="merged-models"></a>
### Modèles fusionnés

|    |  Modèles originaux (LLMs japonais en gras)  | Développeur  | Licence |
|:---|:---:|:---:|:---:|
| [EvoLLM-JP-A](https://sakana.ai/evolutionary-model-merge/)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoLLM-JP-A-v1-7B)) | **Shisa Gamma 7B (v1)**, Arithmo2 Mistral 7B, Abel 7B 002 | Sakana AI | Apache 2.0 |
| [EvoLLM-JP](https://sakana.ai/evolutionary-model-merge/)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoLLM-JP-v1-7B), [v1-10B](https://huggingface.co/SakanaAI/EvoLLM-JP-v1-10B)) | **Shisa Gamma 7B (v1)**, WizardMath-7B-V1.1, Abel 7B 002 | Sakana AI | MICROSOFT RESEARCH LICENSE |

<a id="api-based-models"></a>
### Modèles basés sur des API

|    |  Longueur Maximale du Contexte | Développeur  | Plateforme |
|:---|:---:|:---:|:---:|
| [Solar mini chat ja](https://www.upstage.ai/feed/tech/solar-mini-chat-ja)<br>([solar-1-mini-chat-ja](https://developers.upstage.ai/docs/apis/chat)) | 32,768 | Upstage | self-owned |
| [AI Novelist](https://ai-novel.com/account_api.php) | 2,400 ~ 8,192 | Bit192 | self-owned |
| [LHTM-OPT](https://aws.amazon.com/marketplace/pp/prodview-nw62wpreit442) | | alt Inc. | AWS Marketplace |

<a id="autoencoding"></a>
## Modèles encodeur

<a id="autoencoding-general"></a>
### D'usage général

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? [^4] |
|:---|:---:|:---:|:---:|:---:|:---:|
|  [KyotoUniBERT](https://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)  |  BERT (base, large)  |  Wikipédia en japonais (18M articles)  |  Université de Kyoto Laboratoire de traitement des langues et des médias | Apache 2.0 | △ |
|  [TohokuUniversityBERT](https://github.com/cl-tohoku/bert-japanese)  |  BERT (base, large)  |  base (v1):<br>Wikipédia en japonais (17M articles / 2.6GB)<br>base (v2) & large:<br>Wikipédia en japonais 4.0GB<br>base (v3) & large (v2):<br>Wikipédia en japonais (4.9GB), Japanese CC&#x2011;100 (74.3GB)   |  Université de Tohoku - Groupe TAL | base (v1, v2) & large: CC BY&#x2011;SA 3.0<br>base (v3) & large (v2): Apache 2.0 |◯<br>([base (v1)](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking), [base (v1, char-level)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking), [base (v2)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2), [base (v2, char-level)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2), [large](https://huggingface.co/tohoku-nlp/bert-large-japanese), [large (char-level)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char), [base (v3)](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3), [base (v3, char-level)](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3), [large (v2)](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2), [large (v2, char-level)](https://huggingface.co/tohoku-nlp/bert-large-japanese-char-v2)) |
| [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/index.html)   |  BERT (base)  |  Wikipédia en japonais  |  NICT  | CC BY 4.0 | △ |
| [Laboro BERT](https://github.com/laboroai/Laboro-BERT-Japanese) | BERT (base, large) | Corpus web en japonais <br> (Actualités, blogs, etc) (12GB) | Laboro.AI | CC BY&#x2011;NC 4.0 | ✕ |
| [colorfulscoop BERT](https://huggingface.co/colorfulscoop/bert-base-ja) | BERT (base) | Wikipédia en japonais | Colorful Scoop | CC BY&#x2011;SA 3.0 | [◯](https://huggingface.co/colorfulscoop/bert-base-ja) |
| [UniversityOfTokyoBERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small) | Wikipédia en japonais (2.9GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/izumi-lab/bert-small-japanese) |
| [chiTra (Sudachi Transformers)](https://www.worksap.co.jp/news/2022/0225/) | BERT (base) | NINJAL Web Japanese Corpus (148GB) | NINJAL, WAP Tokushima - Laboratoire IA et TAL | Apache 2.0 | △ |
| [ACCMS BERT](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) | BERT (base) | Wikipédia en japonais (3.3GB) | Université de Kyoto ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) |
| [HitachiBERT](https://aclanthology.org/2023.acl-srw.5.pdf) | BERT (base) | Wikipédia en japonais, Japanese CC&#x2011;100 | Hitachi | CC BY&#x2011;NC&#x2011;SA 4.0 | [◯](https://huggingface.co/hitachi-nlp/bert-base-japanese_jumanpp-bpe)[^6] |
| [Bandai Namco DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) | DistilBERT |  (Distillation de BERT (base) de l'Université du Tohoku)  | Bandai Namco Research | MIT | [◯](https://huggingface.co/bandainamco-mirai/distilbert-base-japanese) |
| [Laboro DistilBERT](https://github.com/laboroai/Laboro-DistilBERT-Japanese) | DistilBERT |  (Distillation of Laboro BERT(base)) | Laboro.AI | CC BY&#x2011;NC 4.0 | [◯](https://huggingface.co/laboro-ai/distilbert-base-japanese) |
| [LINE DistilBERT](https://engineering.linecorp.com/ja/blog/line-distilbert-high-performance-fast-lightweight-japanese-language-model) | DistilBERT | (Distillation de LINE en interne BERT model)| LINE | Apache 2.0 | [◯](https://huggingface.co/line-corporation/line-distilbert-base-japanese) |
| [rinna RoBERTa](https://rinna.co.jp/news/2021/08/20210825.html) | RoBERTa (base) |  Wikipédia en japonais, Japanese CC&#x2011;100 | rinna | MIT | [◯](https://huggingface.co/rinna/japanese-roberta-base) |
| [WasedaRoBERTa](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) | RoBERTa (base, large) | Wikipédia en japonais, Japanese CC&#x2011;100 | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | ◯<br>([base](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp), [large](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp), [large (seq512)](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512-with-auto-jumanpp))[^7] |
| [InformatixRoBERTa](https://github.com/informatix-inc/bert) | RoBERTa (base) | Wikipédia en japonais, Web Articles <br> (25GB) | Informatix | Apache 2.0 | △ |
| [KyotoUniversityRoBERTa](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) | RoBERTa (base, large) | Wikipédia en japonais, Japanese CC&#x2011;100 | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 | ◯<br>([base (char-level)](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm), [large (char-level)](https://huggingface.co/ku-nlp/roberta-large-japanese-char-wwm)) |
| [YokohamaNationalRoBERTa](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) | RoBERTa (base) | Wikipédia en japonais (3.45GB) | Université nationale de Yokohama - Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) |
| [Megagon Labs RoBERTa](https://huggingface.co/megagonlabs/roberta-long-japanese) | RoBERTa (base)[^8] | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit Co.,Ltd.) | MIT | [◯](https://huggingface.co/megagonlabs/roberta-long-japanese)  |
| [ACCMS RoBERTa](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) | RoBERTa (base) | Wikipédia en japonais (3.3GB) + Japanese CC&#x2011;100 (70GB) | Université de Kyoto ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) |
| [CinnamonELECTRA](https://cinnamon.ai/ideas/20200619_research_001/) | ELECTRA (small) | Wikipédia en japonais | Cinnamon | Apache 2.0 | [◯](https://huggingface.co/Cinnamon/electra-small-japanese-discriminator)  |
| [Megagon Labs ELECTRA](https://www.recruit.co.jp/newsroom/pressrelease/2021/0826_9293.html) | ELECTRA (base) | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit Co.,Ltd.) | MIT | [◯](https://huggingface.co/megagonlabs/electra-base-japanese-discriminator)  |
| [UniversityOfTokyoELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small, base) | Wikipédia en japonais (2.9GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/izumi-lab/electra-small-japanese-discriminator), [base](https://huggingface.co/izumi-lab/electra-base-japanese-discriminator))  |
| [JapaneseRoFormer](https://huggingface.co/ganchengguang/Roformer-base-japanese) | RoFormer (base) | Wikipédia en japonais (3.45GB) | Université nationale de Yokohama - Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/Roformer-base-japanese) |
| [JapaneseLUKE](https://www.ousia.jp/ja/page/ja/2022/11/17/luke-japanese/) | LUKE (base, large) | Wikipédia en japonais | Studio Ousia | Apache 2.0 | ◯<br>([base](https://huggingface.co/studio-ousia/luke-japanese-base-lite), [large](https://huggingface.co/studio-ousia/luke-japanese-large-lite)) |
| [KyotoUniversityDeBERTaV2](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | DeBERTaV2 (tiny, base, large) | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR<br> (171GB)  | Université de Kyoto - Laboratoire du traitement des langues et médias | CC BY&#x2011;SA 4.0 | ◯<br>([tiny](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese), [tiny (char-level)](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm), [base](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), [large](https://huggingface.co/ku-nlp/deberta-v2-large-japanese)) | 
| [KyotoUniversityDeBERTaV3](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) | DeBERTaV3 (base) | [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | Kyoto University Language Media Processing Lab | Apache 2.0 | [◯](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) |
| [UniversityOfTokyoDeBERTaV2](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | DeBERTaV2 (small, base) | Wikipédia en japonais, Japanese Wikinews, Japanese CC-100, Japanese mC4, Japanese OSCAR | University of Tokyo Izumi Lab | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/deberta-v2-small-japanese), [base](https://huggingface.co/izumi-lab/deberta-v2-base-japanese)) | 
| [JapaneseBigBird](https://huggingface.co/nlp-waseda/bigbird-base-japanese) | BigBird (base) | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/nlp-waseda/bigbird-base-japanese) |
| [JapaneseLayoutLM](https://huggingface.co/jri-advtechlab/layoutlm-wikipedia-ja) | LayoutLM (base) | Pre-trained on Japanese Wikipedia, initialized with TohokuUniversityBERT | The Japan Research Institute, Limited | CC BY-SA 3.0 | [◯](https://huggingface.co/jri-advtechlab/layoutlm-wikipedia-ja) |

<a id="autoencoding-domain-specific"></a>
### Spécifique à un domaine

|    |  Domaine | Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| [JapaneseNewsBERT](https://qiita.com/mkt3/items/3c1278339ff1bcc0187f) | Affaires | BERT (base) | Articles sur l'économie en japonais(3M articles) | Stockmark | CC BY 4.0 | △ |
| [JapaneseNewsXLNet](https://qiita.com/mkt3/items/4d0ae36f3f212aee8002) | Affaires | XLNet (base) | Articles sur l'économie en japonais (3M articles) | Stockmark | ？ | [◯](https://huggingface.co/hajime9652/xlnet-japanese) <br> ※ Version non officielle |
| [JapaneseNewsALBERT](https://qiita.com/mkt3/items/b41dcf0185e5873f5f75) | Affaires | ALBERT (base) | Articles sur l'économie en japonais (3M articles) | Stockmark | ？ | △ |
| [JapaneseBlogELECTRA](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E2-5.pdf) | Langue familière | ELECTRA (small) | Corpus de blogs en japonais (354M sentences)  | Université de technologie de Kitami - Laboratoire de Masui-Ptaszynski | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ptaszynski/yacis-electra-small-japanese)  |
| [JapaneseSpokenLanguageBERT](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) | Langue parlée | BERT (base) | Formation supplémentaire pour TohokuUniversityBERT en utilisant le Corpus of Spontaneous Japanese (CSJ)<br> (Dans le modèle DAPT, le compte rendu de la diète est également utilisé) | Retrieva | Apache 2.0 | [◯](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) |
| [JapaneseFinancialBERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | Finance |BERT (small, base)[^9] | Wikipédia en japonais, Japanese Financial Corpus (27M sentences/5.2GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |◯<br>([small](https://huggingface.co/izumi-lab/bert-small-japanese-fin), [base](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional)) |
| [JapaneseFinancialELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | Finance | ELECTRA (small) | Wikipédia en japonais (20M sentences/2.9GB), Japanese Financial Corpus (27M sentences/5.2GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |  [◯](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator) |
| [UTH-BERT](https://ai-health.m.u-tokyo.ac.jp/home/research/uth-bert) | Médecine | BERT (base) | Dossiers médicaux en japonais (120M lignes) | Université de Tokyo Hôpital <br>Cours de développement en IA pour la médecine | CC BY&#x2011;NC&#x2011;SA 4.0 | △ |
| [medBERTjp](https://github.com/ou-medinfo/medbertjp) | Médecine | BERT (base) | Wikipédia en japonais, Corpus médical en japonais ("今日の診療プレミアム/Today's Care Premium" Web Version) | Université d'Osaka Hôpital <br> Laboratoire d'information médicale | CC BY&#x2011;NC&#x2011;SA 4.0 | △ |
| [JMedRoBERTa](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf) | Médecine | RoBERTa (base) | Japanese Medical Papers (11M sentences/1.8GB) | Université de Tokyo Aizawa Lab | CC BY&#x2011;NC&#x2011;SA 4.0 | ◯<br>([ManbyoWordPiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece), [SentencePiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece))[^10] |
| [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | Science | RoBERTa (base) | CiNii Japanese Papers (6.3M sentences) | Université d'Ehime Laboratoire IA | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicRoBERTa) |

<a id="embeddings"></a>
## Plongement lexical par mots et par documents

|    | Architecture |  Développeur  |  Licence | 
|:---|:---:|:---:|:---:|
| [JaColBERT](https://arxiv.org/pdf/2312.16144.pdf)<br>([JaColBERT](https://huggingface.co/bclavie/JaColBERT), [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2)) | ColBERT | Individuel ([Benjamin Clavié](https://scholar.google.com/citations?user=vuMln98AAAAJ)) | MIT |
| [Japanese SimCSE](https://arxiv.org/pdf/2310.19349.pdf)<br>([cl-nagoya/unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base), [cl-nagoya/unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large), [cl-nagoya/sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base), [cl-nagoya/sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large)) | SimCSE | Université de Nagoya - Takeda-Sasano Group | CC BY-SA 4.0 |
| [GLuCoSE](https://prtimes.jp/main/html/rd/p/000000123.000022705.html)<br>([pkshatech/GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja)) | Modèle de plongement lexical basé sur LUKE<br>(GLuCoSE) | PKSHA Technology | Apache 2.0 |
||||
| [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) | Sentence-BERT | Colorful Scoop | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/SBERT-JSNLI-base](https://huggingface.co/MU-Kindai/SBERT-JSNLI-base)<br>[MU-Kindai/SBERT-JSNLI-large](https://huggingface.co/MU-Kindai/SBERT-JSNLI-large) | Sentence-BERT | Université de Kindai | ？ |
| [MU-Kindai/Japanese-SimCSE-BERT-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-unsup)<br>[MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-base-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-sup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-sup) | SimCSE | Université de Kindai | MIT |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) | SimCSE | PKSHA Technology | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/Japanese-MixCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-base)<br>[MU-Kindai/Japanese-MixCSE-BERT-large](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-large) | MixCSE | Université de Kindai | MIT |
| [MU-Kindai/Japanese-DiffCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-DiffCSE-BERT-base) | DiffCSE | Université de Kindai | MIT | 

<a id="multimodal"></a>
## Modèles Vision-Language

<a id="multimodal-text-generation"></a>
### Text+Image vers Text

<a id="multimodal-general"></a>
#### D'usage général

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|
| [llava-calm2-siglip](https://www.cyberagent.co.jp/news/detail/id=30344)<br>([llava-calm2-siglip](https://huggingface.co/cyberagent/llava-calm2-siglip)) | LLaVA-1.5 | coversational data generated from MS-COCO and VisualGenome | CyberAgent | Apache 2.0 |
| [EvoVLM-JP](https://sakana.ai/evolutionary-model-merge)<br>([v1-7B](https://huggingface.co/SakanaAI/EvoVLM-JP-v1-7B)) | - | - (merged from Shisa Gamma 7B (v1) and LLaVA-1.6-Mistral-7B) | Sakana AI | Apache 2.0 |
| [Heron](https://github.com/turingmotors/heron)<br>([blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0), [blip-ja-stablelm-base-7b-v1](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1), [blip-ja-stablelm-base-7b-v1-llava-620k](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v1-llava-620k), [git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0), [git-ELYZA-fast-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ELYZA-fast-7b-v0), [git-ja-stablelm-base-7b-v1](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v1)) | BLIP-2 / GIT | v1: LLaVA-Instruct-150K-JA or LLaVA-Instruct-620K-JA<br>v0: LLaVA-Instruct-150K-JA, Japanese STAIR Captions, Japanese Visual Genome VQA dataset | Turing | CC BY-NC 4.0 |
| [Japanese Stable VLM](https://ja.stability.ai/blog/japanese-stable-vlm)<br>([japanese-stable-vlm](https://huggingface.co/stabilityai/japanese-stable-vlm)) | LLaVA-1.5 | Japanese CC12M, STAIR Captions, jeu de données Japanese Visual Genome VQA | Stability AI | STABILITY AI JAPANESE STABLE VLM COMMUNITY LICENSE |
| [Japanese InstructBLIP Alpha](https://ja.stability.ai/blog/japanese-instructblip-alpha)<br>([japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha)) | InstructBLIP | Japanese CC12M, STAIR Captions, jeu de données Japanese Visual Genome VQA | Stability AI | JAPANESE STABLELM RESEARCH LICENSE |
| [rinna MiniGPT-4](https://rinna.co.jp/news/2023/07/20230731.html)<br>([bilingual-gpt-neox-4b-minigpt4](https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4)) | MiniGPT-4 | CC12M, COCO 2014, Visual Genome, STAIR Captions, Japanese Visual Genome VQA dataset | rinna | MIT |

<a id="multimodal-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm](https://huggingface.co/watashiha/Watashiha-Llama-2-13B-Ogiri-sft-vlm) | LLaVA | [Oogiri](https://en.wikipedia.org/wiki/Glossary_of_owarai_terms#oogiri) | Watashiha | Llama 2 Community License |

<a id="multimodal-others"></a>
### Autres

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|
| [LY CLIP](https://techblog.lycorp.co.jp/ja/20240514b)<br>([clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base)) | CLIP | CommonCrawl, CC12M, YFCC100M | LY Corp. | Apache 2.0 |
| [Recruit CLIP](https://blog.recruit.co.jp/data/articles/japanese-clip/)<br>([japanese-clip-vit-b-32-roberta-base](https://huggingface.co/recruit-jp/japanese-clip-vit-b-32-roberta-base)) | CLIP | environ 120 millions de légendes de laion2B-multi | Recruit Co.,Ltd. | CC BY-4.0 |
| [Japanese Stable CLIP](https://ja.stability.ai/blog/japanese-stable-clip)<br>([japanese-stable-clip-vit-l-16](https://huggingface.co/stabilityai/japanese-stable-clip-vit-l-16)) | SigLIP | CC12M traduit en japonais, STAIR Captions | Stability AI | STABILITY AI JAPANESE STABLE CLIP COMMUNITY LICENSE |
| [rinna CLIP](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16)) | CLIP | CC12M traduit en japonais | rinna | Apache 2.0 |
| [rinna CLOOB](https://rinna.co.jp/news/2022/05/20220512.html)<br>([japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16)) | CLOOB | CC12M traduit en japonais | rinna | Apache 2.0 |
| [HAKUHODO Technologies CLIP](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-base)<br>([base](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-base), [deeper](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-deeper), [wider](https://huggingface.co/hakuhodo-tech/japanese-clip-vit-h-14-bert-wider)) | CLIP | about 120 million captions from laion2B-multi | HAKUHODO Technologies | CC BY-NC-SA 4.0 |

<a id="multimodal-text-to-image"></a>
### Text vers Image

|    |  Architecture  |  Training Data  |  Développeur  | License |
|:---|:---:|:---:|:---:|:---:|
| [EvoSDXL-JP](https://huggingface.co/SakanaAI/EvoSDXL-JP-v1)<br>([v1](https://huggingface.co/SakanaAI/EvoSDXL-JP-v1)) | - | - (merged from several diffusion models, including Japanese Stable Diffusion XL) | Sakana AI | Apache 2.0[^14] |
| [Japanese Stable Diffusion XL](https://ja.stability.ai/blog/japanese-stable-diffusion-xl)<br>([japanese-stable-diffusion-xl](https://huggingface.co/stabilityai/japanese-stable-diffusion-xl)) | Stable Diffusion | Inconnu | Stability AI | STABILITY AI JAPANESE STABLE DIFFUSION XL COMMUNITY LICENSE |
| [TohokuUniversity Stable Diffusion](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0)<br>([base](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0), [refiner](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-refiner-1.0)) | Stable Diffusion | Corpus parallèle anglais-japonais de la tâche partagée WMT2023, environ 13 millions de légendes de laion2B-multi | Université de Tohoku - Groupe TAL | CreativeML OpenRAIL-M License |
| [rinna Stable Diffusion](https://rinna.co.jp/news/2022/09/20220909.html)<br>([japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion)) | Stable Diffusion | LAION-5B Japanese Subset (100M images) | rinna | CreativeML OpenRAIL-M License |

<a id="speech"></a>
## Modèles Speech-Language

<a id="speech-asr"></a>
### Reconnaissance automatique de la parole

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|
| [Kotoba-Whisper](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0)<br>([v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0), [v1.0-ggml](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0-ggml), [v1.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0-faster), [v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1)) | Distil-Whisper | ReazonSpeech | Kotoba Technologies | Apache 2.0 |
| [Nue ASR](https://rinna.co.jp/news/2023/12/20231207.html)<br>([nue-asr](https://huggingface.co/rinna/nue-asr)) | Nue ASR<br>(HuBERT + LLM) | ReazonSpeech | rinna | Apache 2.0 |
| [ReazonSpeech](https://research.reazon.jp/projects/ReazonSpeech/)<br>([espnet-v1](https://huggingface.co/reazon-research/reazonspeech-espnet-v1), [espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next), [espnet-v2](https://huggingface.co/reazon-research/reazonspeech-espnet-v2), [nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2)) | ESPnet (Conformer-Transducer) / NeMo (FastConformer-RNNT) | ReazonSpeech | Reazon Holdings | Apache 2.0 |

<a id="speech-others"></a>
### Autres

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|
| [Kotoba-Speech](https://huggingface.co/kotoba-tech/kotoba-speech-v0.1)<br>([v0.1](https://huggingface.co/kotoba-tech/kotoba-speech-v0.1)) | Transformer | undisclosed | Kotoba Technologies | Apache 2.0 |
| [UniversityOfTokyoHuBERT](https://huggingface.co/sarulab-speech/hubert-base-jtube)<br>([base-jtube](https://huggingface.co/sarulab-speech/hubert-base-jtube)) | HuBERT | JTubeSpeech | University of Tokyo<br>Saruwatari & Takamichi Lab | MIT |
| [rinna HuBERT](https://rinna.co.jp/news/2023/04/20230428.html)<br>([base](https://huggingface.co/rinna/japanese-hubert-base), [large](https://huggingface.co/rinna/japanese-hubert-large)) | HuBERT | ReazonSpeech | rinna | Apache 2.0 |


<a id="benchmark-suites"></a>
## Standard d'évaluation pour les LLM en japonais

<a id="hybrid-benchmark-suites"></a>
### Benchmarks hybrides

|   | Description | Développeur |
|:---|:---|:---:|
| [Nejumi LLM Leaderboard Neo](https://api.wandb.ai/links/wandb-japan/dcbaznfb) | Cela compile les résultats d'une évaluation complète par [llm-jp-eval](#llm-jp-eval), qui évalue la compréhension de la langue dans un format de questions-réponses, et [Japanese MT-bench](#jp-mt-bench), qui évalue la capacité générative dans un contexte d'invites de dialogue. | Weights & Biases |

<a id="basic-benchmark-suites"></a>
### Référence traditionnelle basé sur des tâches de Compréhension du langage naturel (NLU)

|   | Description | Développeur |
|:---|:---|:---:|
| <a id="llm-jp-eval"></a> [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | Un outil qui évalue automatiquement les LLM japonais à travers plusieurs jeux de données. <br>La liste complète des jeux de données pris en charge peut être trouvée [ici](https://github.com/llm-jp/llm-jp-eval/tree/main/src/llm_jp_eval/datasets) (qui comprend également des tâches telles que JNLI et JCommonsenseQA de JGLUE). <br>Les résultats de l'évaluation sont compilés sur le [classement llm-jp-eval](http://wandb.me/llm-jp-leaderboard). | LLM-jp |
| [JP Language Model Evaluation Harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | Un fork par Stability AI de [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness). Il s'agit d'un outil pour évaluer automatiquement les LLM japonais à travers plusieurs jeux de données. <br>La liste complète des jeux de données pris en charge peut être trouvée [ici](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable/lm_eval/tasks/ja) (qui comprend également des tâches telles que JNLI et JCommonsenseQA de JGLUE). <br>Il y a un résumé détaillé des résultats de l'évaluation par rinna : [[rinna] Benchmark de Stability-AI/lm-evaluation-harness](https://rinnakk.github.io/research/benchmarks/lm/) | Stability AI |
| [JGLUE](https://github.com/yahoojapan/JGLUE) | Version japonais de [GLUE](https://gluebenchmark.com/) référence suite, avec les tâches MARC-ja, JCoLA, JSTS, JNLI, JSQuAD, et JCommonsenseQA. [JCoLA](https://github.com/osekilab/JCoLA) vient du laboratoire d'Oseki de l'université de Tokyo. Voir [ici](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.317.pdf) and [here (ja only)](https://techblog.yahoo.co.jp/entry/2022122030379907/) pour plus d'informations sur chaque tâches. | Université de Waseda Laboratoire Kawahara et Yahoo |
| [JMMLU](https://github.com/nlp-waseda/JMMLU) | Un benchmark construit comme une version japonaise du [MMLU Benchmark](https://github.com/hendrycks/test), consistant en des questions à choix multiples de divers domaines académiques, y compris les sciences naturelles, les humanités et les sciences sociales. En plus de la traduction du MMLU original, il contient de nouveaux problèmes basés sur le contexte culturel unique du Japon (problèmes spécifiques au Japon). | Université de Waseda Laboratoire Kawahara |
| [Japanese Open LLM Leaderboard](http://wandb.me/llm-jp-openllmleaderboard) | Semblable à [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) de Huggingface, ce classement fournit une vérification sur les LLM japonais. Vous pouvez vérifier la performance des LLM japonais dans des tâches en anglais. | LLM-jp |

<a id="open-ended-benchmark-suites"></a>
### Standard des tâches génératives ouvertes

|   | Description | Développeur |
|:---|:---|:---:|
| <a id="jp-mt-bench"></a> [Japanese MT-bench](https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge) | Version japonaise du [MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) qui interroge sur la capacité à converser en plusieurs tournures. Il inclut 80 questions, 10 de chacune des 8 catégories : écriture, jeu de rôle, raisonnement, maths, codage, extraction, STEM, sciences humaines. Certaines questions ont été modifiées pour s'adapter à la culture japonaise lors de la création de la version japonaise. Il comprend également un script qui réalise une évaluation absolue en 10 niveaux par GPT-4. | Stability AI |
| <a id="rakuda-benchmark"></a> [Rakuda Benchmark](https://github.com/yuzu-ai/japanese-llm-ranking) | Classement basé sur les réponses des modèles avec [40 questions ouvertes](https://huggingface.co/datasets/yuzuai/rakuda-questions) la géographie, l'histoire, la politique, et la société japonaise. Utilise GPT-4 pour évaluer les résultats du modèle par paires, puis classe les modèles en ajustant le maximum de vraisemblance sur le modèle de probabilité d'Elo/Bradley-Terry avec les préférences de GPT-4. | YuzuAI |
| <a id="elyza-tasks"></a> [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | Classement basé sur les réponses des modèles avec [100 tâches complexes et diverses](https://huggingface.co/datasets/elyza/ELYZA-tasks-100), y compris les tâches testant la synthèse, la correction, l'abstraction, l'induction et d'autres compétences. Utilise des humains pour noter les réponses du modèle, puis classe les modèles en fonction de leurs scores moyens. | ELYZA |
| [Japanese Vicuna QA Benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | Il s'agit de la version japonaise de [vicuna-blog-eval](https://github.com/lm-sys/vicuna-blog-eval), qui est le précurseur de MT-Bench. Il comprend 80 questions sur la connaissance générale, le jeu de rôle, le bon sens, l'estimation de Fermi, la pensée contrefactuelle, le codage, les mathématiques, et l'écriture. Il comprend également un script pour une évaluation automatique par GPT-4 (calcul du taux de victoire). Le tableau de classement peut être trouvé [ici](http://wandb.me/llm-jp-vicunaleaderboard). | Université de Kyoto Laboratoire de traitement des langues et des médias |
| <a id="tengu-bench"></a> [Tengu-Bench](https://huggingface.co/datasets/lightblue/tengu_bench) | Comprend 120 questions ouvertes de diverses catégories. Catégories de questions : interprétation des tableaux, puzzles logiques, génération d'idées, appel de fonctions, résumé de longs documents (plus de mille jetons), résumé de conversations, questions fermées sur des longs documents (plus de mille jetons), honorifiques, création de projet, mathématiques, traduction, extraction, contrôle éthique, estimation des coûts, Japon, bavardage, calembours, formatage, construction, affaires, jugement juridique, politique, questions hypothétiques. | Lightblue |
| [Shaberi](https://github.com/lightblue-tech/japanese_llm_eval) | Un cadre qui peut évaluer collectivement le [Japanese MT-bench](#jp-mt-bench), le [Rakuda Benchmark](#rakuda-benchmark), le [ELYZA-tasks-100](#elyza-tasks), et le [Tengu-Bench](#tengu-bench). Il existe également un [fork](https://github.com/shisa-ai/shaberi) de Shisa.AI. | Lightblue |

<a id="logical-reasoning-benchmark-suites"></a>
### Benchmarks pour mesurer les capacités de raisonnement logique

|   | Description | Développeur |
|:---|:---|:---:|
| [JFLD (Japanese Formal Logic Deduction)](https://aclanthology.org/2024.lrec-main.832/) | Un dataset pour évaluer les capacités de raisonnement déductif des LLM japonais (la version japonaise de la [FLD (Formal Logic Deduction)](https://github.com/hitachi-nlp/FLD) proposée par les mêmes auteurs). Il se caractérise par le fait qu'il est composé d'exemples contrefactuels pour évaluer indépendamment des connaissances que possède le LLM. | Hitachi |
| [JHumanEval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) | Une version japonaise du benchmark [HumanEval](https://huggingface.co/datasets/openai_humaneval), qui évalue la capacité à générer du code Python à partir d'instructions en anglais. En créant la version japonaise, le texte a d'abord été traduit automatiquement, puis corrigé manuellement. | Université des Femmes du Japon - Laboratoire Kuramitsu |

<a id="domain-specific-benchmark-suites"></a>
### Benchmarks pour mesurer la performance dans des domaines spécifiques

|   | Description | Développeur |
|:---|:---|:---:|
| [Japanese Language Model Financial Evaluation Harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | Un benchmark pour les LLM japonais dans le secteur financier. Il comprend des tâches telles que l'analyse des sentiments dans la finance (chabsa), des tâches de connaissances de base en analyse de titres (cma_basics), des tâches relatives aux audits dans les examens de comptable public certifié (cpa_audit), des tâches à questions à choix multiple dans les examens de planificateur financier (fp2), et des tâches d'examen blanc pour les examens de vendeurs de titres (security_sales_1). Pour plus de détails, veuillez consulter [ici](https://www.anlp.jp/proceedings/annual_meeting/2024/pdf_dir/C6-4.pdf). | Preferred Networks |
| [Stockmark Business Questions](https://huggingface.co/datasets/stockmark/business-questions) | La collection comprend 50 questions qui approfondissent les connaissances sur des sujets tels que les tendances du marché, l'actualité, les problèmes sociaux et les tendances commerciales. | Stockmark |

<a id="embeddings-benchmark-suites"></a>
### Benchmarks pour modèles d'embeddings

|   | Description | Développeur |
|:---|:---|:---:|
| [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | Un benchmark développé comme la version japonaise de [MTEB](https://github.com/embeddings-benchmark/mteb). Il se compose de tâches telles que le regroupement de documents, la classification de textes, la similarité de phrases, la prédiction d'étiquetage de paires de phrases et l'extraction de texte (une tâche de reclassement a été récemment ajoutée). | SB Intuitions |

<a id="vl-benchmark-suites"></a>
### Benchmarks pour modèles vision-langage

|   | Description | Développeur |
|:---|:---|:---:|
| [Heron VLM Leaderboard powered by Nejumi/WandB](https://wandb.ai/vision-language-leaderboard/heron-leaderboard/reports/Heron-VLM-Leaderboard-powered-by-Nejumi-WandB--Vmlldzo4MjY3OTc5) | Résume les résultats d'évaluation de [Japanese-Heron-Bench](#japanese-heron-bench) et [LLaVA-Bench-In-the-Wild (Japanese)](#llava-bench-in-the-wild). | Turing, Weights & Biases |
| <a id="japanese-heron-bench"></a> [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) | 21 images se voient attribuer un total de 102 questions. Il est caractérisé par des paires image-question qui nécessitent une connaissance liée au Japon. | Turing |
| [JA-VLM-Bench-In-the-Wild](https://huggingface.co/datasets/SakanaAI/JA-VLM-Bench-In-the-Wild) | Un jeu de données préparé indépendamment par Sakana AI pour évaluer EvoVLM-JP-v1-7B. Il se compose de 50 questions attribuées à 42 images. Il se caractérise par des images et des questions qui exigent une connaissance du Japon. | Sakana AI |
| <a id="llava-bench-in-the-wild"></a> [LLaVA-Bench-In-the-Wild (Japanese)](https://github.com/turingmotors/heron/tree/main/playground/data/llava-bench-in-the-wild) | Ceci est la version japonaise de [LLaVA-Bench-In-the-Wild](https://huggingface.co/datasets/liuhaotian/llava-bench-in-the-wild), traduite à l'aide de DeepL. Il se compose de 60 questions attribuées à 24 images. | Turing |
| [LLaVA-Bench (COCO) Japonais](https://github.com/turingmotors/heron/tree/main/playground/data/llava-bench-ja) | Il s'agit de la version japonaise, traduite par DeepL, du jeu de données LLaVA-Bench (COCO) utilisé pour évaluer LLaVA. Il se compose de 30 images, chacune avec 3 types de questions qui leur sont attribuées. | Turing |

<a id="reference"></a>
## Références pour les modèles et les architectures

| Modèle/Architecture | Date | Meeting/Journal | Papier |
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
| DeBERTaV3 | 2021.11.18 | ICLR 2023 | [DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing](https://arxiv.org/abs/2111.09543) |
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
| RetNet | 2023.07.17 | - | [Retentive Network: A Successor to Transformer for Large Language Models](https://arxiv.org/abs/2307.08621) |
| Llama 2 | 2023.07.18 | - | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) |
| Code Llama | 2023.08.24 | - | [Code Llama: Open Foundation Models for Code](https://arxiv.org/abs/2308.12950) |
| Qwen | 2023.09.28 | - | [Qwen Technical Report](https://arxiv.org/abs/2309.16609) |
| LLaVA-1.5 | 2023.10.05 | - | [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) |
| Mistral 7B | 2023.10.10 | - | [Mistral 7B](https://arxiv.org/abs/2310.06825) |
| Mamba | 2023.12.01 | - | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) |
| Nue ASR | 2023.12.06 | ACL 2024 (Findings) | [Integrating Pre-Trained Speech and Language Models for End-to-End Speech Recognition](https://arxiv.org/abs/2312.03668) |
| TinyLlama | 2024.01.04 | - | [TinyLlama: An Open-Source Small Language Model](https://arxiv.org/abs/2401.02385) |
| Mixtral 8x7B | 2024.01.08 | - | [Mixtral of Experts](https://arxiv.org/abs/2401.04088) |
| LEIA | 2024.02.18 | ACL 2024 (Findings) | [LEIA: Facilitating Cross-lingual Knowledge Transfer in Language Models with Entity-based Data Augmentation](https://arxiv.org/abs/2402.11485) |
| EvoLLM-JP, EvoVLM-JP | 2024.03.19 | - | [Evolutionary Optimization of Model Merging Recipes](https://arxiv.org/abs/2403.13187) |
| RakutenAI-7B | 2024.03.21 | - | [RakutenAI-7B: Extending Large Language Models for Japanese](https://arxiv.org/abs/2403.15484) |
| rinna GPT, rinna RoBERTa, Nekomata, Youri, etc. | 2024.04.02 | LREC-COLING 2024 | [Release of Pre-Trained Models for the Japanese Language](https://arxiv.org/abs/2404.01657) |
| SambaLingo-Japanese | 2024.04.08 | - | [SambaLingo: Teaching Large Language Models New Languages](https://arxiv.org/abs/2404.05829) |
| Heron | 2024.04.11 | - | [Heron-Bench: A Benchmark for Evaluating Vision Language Models in Japanese](https://arxiv.org/abs/2404.07824) |
| Stockmark-13b | 2024.04.12 | - | [Pretraining and Updating Language- and Domain-specific Large Language Model: A Case Study in Japanese Business Domain](https://arxiv.org/abs/2404.08262) |
| Swallow | 2024.04.27 | COLM 2024 | [Continual Pre-Training for Cross-Lingual LLM Adaptation: Enhancing Japanese Language Capabilities](https://arxiv.org/abs/2404.17790) |
| LLM-jp-13B | 2024.07.04 | - | [LLM-jp: A Cross-organizational Project for the Research and Development of Fully Open Japanese LLMs](https://arxiv.org/abs/2407.03963) |

<a id="reference-training"></a>
## Références pour les méthodes d'entraînement

| Model/Architecture | Date | Meeting/Journal | Paper |
|:---|:---|:---|:---|
| PPO (RLHF) | 2017.07.20 | - | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) |
| Instruction Tuning<br>(Supervised Fine-tuning; SFT) | 2021.09.03 | ICLR 2022 | [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652) |
| DPO | 2023.05.29 | NeurIPS 2023 | [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) |
| SteerLM | 2023.10.09 | EMNLP 2023 (Findings) | [SteerLM: Attribute Conditioned SFT as an (User-Steerable) Alternative to RLHF](https://aclanthology.org/2023.findings-emnlp.754/) |

<a id="contributors"></a>
## Nos contributeurs

Nous aimons les contributeurs ! N'hésitez pas à contribuer à ce projet.

<a href="https://github.com/llm-jp/awesome-japanese-llm/graphs/contributors" target="_blank" rel="noreferrer">
  <img src="../figures/contributors.svg" alt="contributors" />
</a>

<a id="citation"></a>
## Citation

La synthèse de ce répertoire est également publiée sous forme de prépublication:
[Exploring Open Large Language Models for the Japanese Language: A Practical Guide](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/682/2035)

Lorsque vous référencez ce répertoire, veuillez le citer comme suit:

```
@article{awesomeJapanese2024,
    title={{Exploring Open Large Language Models for the Japanese Language: A Practical Guide}},
    author={Kaito Sugimoto},
    doi={10.51094/jxiv.682},
    journal={Jxiv preprint},
    year={2024}
}
```

---

[^1]: Certaines améliorations de performances ont été apportées au modèle Llama original. Voir [ici](https://tech.preferred.jp/ja/blog/llm-plamo/) pour plus détails.

[^2]: Les détails n'ont pas été rendus publics, mais l'ensemble de données privé comprend des jeux de données de l'équipe japonaise du projet EleutherAI Polyglot et des membres de Stable Community Japan.

[^3]: Ce projet a mené des recherches d'évaluation sur l'utilisation de la génération de droite à gauche au lieu de la génération habituelle de gauche à droite, en publiant des modèles de gauche à droite et de droite à gauche.

[^4]: ○: Le modèle se trouve sur le Model Hub d'HuggingFace et peut être chargé avec la commande `AutoModel.from_pretrained()` . △: Le modèle ne se trouve pas sur le Model Hub mais peut être chargé manuellement avec la bibliothèque de transformateurs HuggingFace. ✕: Le modèle ne se charge pas avec HuggingFace.

[^6]: Ce projet a mené des recherches d'évaluation sur l'analyse morphologique avant la tokenisation et a publié son modèle le plus performant, qui utilisait Juman++ et BPE.

[^7]: nlp-waseda/roberta-base-japanese et nlp-waseda/roberta-large-japanese entrainé avec une longueur de context 128 token, mais nlp-waseda/roberta-large-japanese-seq512 étendu la longueur du contexte à 512.

[^8]: Étendu la longueur du contexte de 128 à 512.

[^9]: Le modèle "Small" s'entraîne sur Wikipédia japonais et le Corpus financier japonais simultanément, tandis que le modèle "Base" prend le TohokuUniversityBERT et dispense un apprentissage supplémentaire sur le Corpus financier japonais.

[^10]: ManbyoWordPiece lance une étape de prétokenization en utilisant MeCab (IPA+Manbyo dictionaries), puis utilise WordPiece pour la tokenization sous-mots, pendant que le modèle SentencePiece segmente le texte directement en utilisant un modèle unigram.

[^12]: Dans l'ajustement des instructions, comme il utilise des données générées par les modèles d'OpenAI, tels que GPT-3.5, GPT-4, etc. pour l'entraînement, il se peut qu'il viole les termes d'OpenAI.

[^13]: Cependant, si une utilisation commerciale de KARAKURI LM est souhaitée, un contact direct avec le développeur, KARAKURI Inc., est requis.

[^14]: Cependant, il appelle à la réflexion pour l'utilisation dans la recherche et l'éducation. De plus, soyez conscient que certaines des licences pour les modèles sources ne sont pas Apache 2.0.

[^15]: Les détails sont disponibles publiquement dans la vidéo suivante: [Présentation des résultats de la phase 1 du projet de développement GENIAC LLM 2024.06.01 @ Fukutake Hall, The University of Tokyo @ 58:22](https://youtu.be/Ju_KgrGhANY?si=zUhZ1S6dznGeF0Gi&t=3502)

[^16]: Cependant, par rapport à BERT (base) habituel, le nombre de couches et de têtes d'attention est inférieur.

[^17]: Avant de procéder à l'ajustement des instructions, un vecteur de chat entre Llama 3 Instruct et Llama 3 Base est ajouté.