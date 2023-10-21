# Overview of Japanese LLMs
[ English | [**日本語**](./README.md) ]

This repository compiles information on publicly available LLMs trained with a focus on Japanese. It is maintained by volunteers based on public data.

⚠ Warning:
1. We can't guarantee the accuracy or completeness of any information here.
2. Some information is based on conjecture and might not reflect your specific use case.
3. While many models are released under permissive licenses like MIT or Apache 2.0, some are subject to more restrictive terms including non-commercial use clauses (e.g CC BY-NC-SA) or other stipulations.

If you find an error, please open an [issue](https://github.com/llm-jp/awesome-japanese-llm/issues). Feel free to contribute directly with a pull request.

## Table of Contents
- [Text Generation Models](#generative)
  - [General purpose](#generative-general)
  - [Domain specialized](#generative-domain-specific)
  - [Models built off English LLMs](#english-based-models)
- [Encoder Models](#autoencoding)
  - [General purpose](#autoencoding-general)
  - [Domain specialized](#autoencoding-domain-specific)
- [Sentence and Document Embeddings Models](#embeddings)
- [Vision-Language Models](#multimodal)
  - [画像を含むテキスト生成](#multimodal-text-generation)
  - [その他](#multimodal-others)
- [Benchmarks for Japanese LLMs](#benchmark-suites)
- [Model Architecture References](#reference)


<a id="generative"></a>
## Text Generation Models

*For multimodal models, see [below](#multimodal-text-generation)*

<a id="generative-general"></a>
### General purpose
&#x2011;
|    |  Architecture  |  Training Data  |  Developer  | License | HuggingFace? [^1] |
|:---|:---:|:---:|:---:|:---:|:---:|
| [PLaMo-13B](https://www.preferred.jp/ja/news/pr20230928/) | Llama-1[^2] <br>(**13b**) | C4, Project Gutenberg, RedPajama, Japanese Wikipedia, Japanese mC4<br>(**1.5T** tokens) | Preferred Networks | Apache 2.0 | [◯](https://huggingface.co/pfnet/plamo-13b) |
| [Weblab-10B](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001) | GPT-NeoX <br> (**10b**, **10b**&#x2011;instruction&#x2011;sft) | Japanese mC4, The Pile <br>（**600B** tokens) <br>instruction&#x2011;sft: Alpaca, FLAN | University of Tokyo Matsuo Lab | CC BY&#x2011;NC 4.0 |  ◯ <br>([10b](https://huggingface.co/matsuo-lab/weblab-10b), [10b&#x2011;instruction&#x2011;sft](https://huggingface.co/matsuo-lab/weblab-10b-instruction&#x2011;sft)) |
| [Japanese StableLM Alpha](https://ja.stability.ai/blog/japanese-stablelm-alpha) | GPT-NeoX <br> (base-alpha-**7b**, instruct-alpha-**7b**, instruct-alpha-**7b**-v2) | Wikipedia, Japanese CC&#x2011;100, Japanese mC4, Japanese OSCAR, RedPajama, private datasets[^3]<br>(**750B** tokens)<br>Instruct: Dolly, HH&#x2011;RLHF, wikinews,  Alpaca (discarded in v2) | Stability AI | base: Apache 2.0<br>instruct (v1): [Research only](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b/tree/main)<br>instruct (v2): Apache 2.0 | ◯<br>([base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b), [instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b), [instruct-alpha-7b-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2)) |
| [OpenCALM](https://www.cyberagent.co.jp/news/detail/id=28817) | GPT-NeoX <br> (small(160M), medium(400M), large(800M), **1b**, **3b**, **7b**) | Japanese Wikipedia, Japanese mC4, Japanese CC&#x2011;100 | CyberAgent | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/cyberagent/open-calm-small), [medium](https://huggingface.co/cyberagent/open-calm-medium), [large](https://huggingface.co/cyberagent/open-calm-large), [1b](https://huggingface.co/cyberagent/open-calm-1b), [3b](https://huggingface.co/cyberagent/open-calm-3b), [7b](https://huggingface.co/cyberagent/open-calm-7b)) |
| [Stormy](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/422/1350) | GPT-NeoX <br>(**7b**) | OpenCALM fine-tuned on <br>llm-japanese-dataset v0 non-translation tasks | University of Tokyo Izumi-Sakaji Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/izumi-lab/stormy-7b-10ep) |
| [rinna GPT <br> (En-Ja Bilingual)](https://rinna.co.jp/news/2023/07/20230731.html) | GPT-NeoX <br>(**4b**, **4b**-8k, **4b**-instruction&#x2011;sft, **4b**-instruction-ppo) | Wikipedia, Japanese CC&#x2011;100, Japanese C4, RedPajama, The Pile<br>(**524B** Tokens)<br> Instruct: HH&#x2011;RLHF, FLAN<br>PPO: HH&#x2011;RLHF for reinforcement learning  <br>8k: trained with long context| rinna | MIT | ◯<br>([4b](https://huggingface.co/rinna/bilingual-gpt-neox-4b), [4b-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k), [4b-instruction&#x2011;sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction&#x2011;sft), [4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo)) |
| [japanese-large-lm](https://engineering.linecorp.com/ja/blog/3.6b-japanese-language-model-with-improved-dialog-performance-by-instruction-tuning) | GPT-NeoX <br> (**1.7b**, **3.6b**, **1.7b**-instruction&#x2011;sft, **3.6b**-instruction&#x2011;sft) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese C4, Japanese OSCAR and private datasets<br>(**650GB**)<br>Instruct: OASST1 | LINE | Apache 2.0 | ◯<br>([1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b), [3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b), [1.7b-instruction&#x2011;sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction&#x2011;sft), [3.6b-instruction&#x2011;sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction&#x2011;sft)) |
| [rinna GPT <br> (Japanese only)](https://rinna.co.jp/news/2023/05/20220531.html) | GPT-NeoX <br> (xsmall, small, medium, **1b**, neox-small, neox-**3.6b**, neox-**3.6b**-instruction&#x2011;sft, neox-**3.6b**-instruction&#x2011;sft-v2, neox-**3.6b**-instruction-ppo) | Japanese Wikipedia, Japanese CC&#x2011;100 <br> (1b and up models add <br>Japanese mC4)<br>Instruct: HH&#x2011;RLHF, FLAN, SHP <br>PPO: HH&#x2011;RLHF for reinforcement learning | rinna | MIT | ◯<br>([xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall), [small](https://huggingface.co/rinna/japanese-gpt2-small), [medium](https://huggingface.co/rinna/japanese-gpt2-medium), [1b](https://huggingface.co/rinna/japanese-gpt-1b), [neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small), [neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b), [neox-3.6b-instruction&#x2011;sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction&#x2011;sft), [neox-3.6b-instruction&#x2011;sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction&#x2011;sft-v2), [neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)) |
| [RetrievaT5](https://note.com/retrieva/n/n7b4186dc5ada) | T5 <br>(small, base, large, **xl(3b)**) | Japanese Wikipedia, Japanese mC4 | Retrieva | CC BY&#x2011;SA 4.0 | ◯<br>([small (short)](https://huggingface.co/retrieva-jp/t5-small-short), [small (medium)](https://huggingface.co/retrieva-jp/t5-small-medium), [small (long)](https://huggingface.co/retrieva-jp/t5-small-long), [base (short)](https://huggingface.co/retrieva-jp/t5-base-short), [base (medium)](https://huggingface.co/retrieva-jp/t5-base-medium), [base (long)](https://huggingface.co/retrieva-jp/t5-base-long), [large (short)](https://huggingface.co/retrieva-jp/t5-large-short), [large (medium)](https://huggingface.co/retrieva-jp/t5-large-medium), [large (long)](https://huggingface.co/retrieva-jp/t5-large-long), [xl](https://huggingface.co/retrieva-jp/t5-xl)) | 
| [ABEJA GPT](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207) | GPT-NeoX <br>(large, **2.7b**) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR | ABEJA | MIT | ◯<br>([large](https://huggingface.co/abeja/gpt2-large-japanese), [neox-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b)) |
| [WasedaGPT](https://huggingface.co/nlp-waseda/gpt2-xl-japanese) | GPT-NeoX <br> (small, **xl(1.5b)**) | Japanese Wikipedia, Japanese CC&#x2011;100 | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/nlp-waseda/gpt2-small-japanese), [xl](https://huggingface.co/nlp-waseda/gpt2-xl-japanese)) |
| [StockmarkGPT](https://stockmark.co.jp/news/20230808) | GPT-NeoX <br> (**1.4b**) | Japanese Wikipedia (0.88B tokens), Japanese CC&#x2011;100 (10.5B tokens), private data (8.6B tokens) | Stockmark | MIT | [◯](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b) |
| [YellowbackGPT](https://tech.yellowback.net/posts/gpt-neo-japanese) | GPT-NeoX <br> (**1.3b**) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR | Yellowback | Apache 2.0 | [◯](https://huggingface.co/yellowback/gpt-neo-japanese-1.3B) |
| [colorfulscoop GPT](https://huggingface.co/colorfulscoop/gpt2-small-ja) | GPT-NeoX <br> (small) | Japanese Wikipedia | Colorful Scoop | CC BY&#x2011;SA 3.0 | [◯](https://huggingface.co/colorfulscoop/gpt2-small-ja) |
| [TitechGPT](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/H9-1.pdf) | GPT-NeoX <br> (medium) | Japanese Wikipedia, Japanese CC&#x2011;100 | Titech Okazaki Lab | CC BY&#x2011;SA 4.0 |  ◯<br>([medium](https://huggingface.co/okazaki-lab/japanese-gpt2-medium-unidic), [medium-reversed](https://huggingface.co/okazaki-lab/japanese-reversed-gpt2-medium-unidic)) [^4] |
| [KyotoUniversityGPT](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) | GPT-NeoX <br> (small, medium) | Japanese Wikipedia (3.2GB), Japanese CC&#x2011;100 (85GB), Japanese OSCAR (54GB) | Kyoto University Language Media Processing Lab | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/ku-nlp/gpt2-small-japanese-char), [medium](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char)) |
| [JapaneseBART](https://huggingface.co/ku-nlp/bart-base-japanese) | BART <br>(base, large) | Japanese Wikipedia (18M sentences) | Kyoto University Language Media Processing Lab | CC BY&#x2011;SA 4.0 | ◯<br>([base](https://huggingface.co/ku-nlp/bart-base-japanese), [large](https://huggingface.co/ku-nlp/bart-large-japanese)) |
| [Megagon Labs T5](https://github.com/megagonlabs/t5-japanese) | T5 <br> (base) | Japanese mC4 (782 GB), Japanese wiki40b (2 GB) | Megagon Labs <br> (Recruit) | Apache 2.0 | [◯](https://huggingface.co/megagonlabs/t5-base-japanese-web) |

<a id="generative-domain-specific"></a>
### Domain Specialized

|    |  Architecture  |  Training Data  |  Developer  | License | HuggingFace？  |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Japanese Dialog Transformer](https://group.ntt/jp/topics/2021/09/30/transformer.html) | Transformer | Twitter japanese reply pairs | NTT | [Evaluation Licence](https://github.com/nttcslab/japanese-dialog-transformers/blob/main/LICENSE.md) | ✕ |
| [Japanese News BART](https://tech.stockmark.co.jp/blog/bart-japanese-base-news/) | BART (base) | Japanese business news articles（21M articles) | Stockmark | MIT | [◯](https://huggingface.co/stockmark/bart-base-japanese-news) |
| [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | BART (base) | CiNii Japanese Papers | Ehime University AI Lab | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicBART) |

<a id="english-based-models"></a>
### Models built off English LLMs

|    | Base Model  |  Developer  |
|:---|:---:|:---:|
| [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) | GPT-J (6b) | Industrial Dream[^5] |
| [NovelAI/genji-jp](https://huggingface.co/NovelAI/genji-jp) | GPT-J (6b) | NovelAI |
| [AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese](https://huggingface.co/AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese) | Llama 2 (70b) | University of Tokyo Hospital Department of Cardiovascular Medicine AI Group|
| [doshisha-mil/llama-2-70b-chat-4bit-japanese-v1](https://huggingface.co/doshisha-mil/llama-2-70b-chat-4bit-japanese-v1) | Llama 2 (70b) | Doshisha University Media Informatics Lab |
| [Sparticle/llama-2-13b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-13b-chat-japanese-lora) | Llama 2 (13b) | Sparticle |
| [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b)<br>[elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct)<br>[elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast)<br>[elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) | Llama 2 (7b) | ELYZA |
| [ganchengguang/Yoko-7B-Japanese-v1](https://huggingface.co/ganchengguang/Yoko-7B-Japanese-v1) | Llama 2 (7b) | Yokohama National University Mori Lab |
| [Sparticle/llama-2-7b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-7b-chat-japanese-lora) | Llama 2 (7b) | Sparticle |
| [izumi-lab/llama-13b-japanese-lora-v0-1ep](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep) | Llama (13b) | University of Tokyo Izumi-Sakaji Lab |
| [izumi-lab/llama-7b-japanese-lora-v0-5ep](https://huggingface.co/izumi-lab/llama-7b-japanese-lora-v0-5ep) | Llama (7b) | University of Tokyo Izumi-Sakaji Lab |
| [lightblue/japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) | MPT (7b) | Lightblue Technology |
| [NTQAI/chatntq-7b-jpntuned](https://huggingface.co/NTQAI/chatntq-7b-jpntuned) | RWKV-4 World | NTQ Solution |

<a id="autoencoding"></a>
## Encoder models

<a id="autoencoding-general"></a>
### General purpose

|    |  Architecture  |  Training Data  |  Developer  | License | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
|  [KyotoUniBERT](https://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)  |  BERT (base, large)  |  Japanese Wikipedia (18M articles)  |  Kyoto University Language Media Processing Lab | Apache 2.0 | △ |
|  [TohokuUniversityBERT](https://github.com/cl-tohoku/bert-japanese)  |  BERT (base, large)  |  base (v1):<br>Japanese Wikipedia (17M articles / 2.6GB)<br>base (v2) & large:<br>Japanese Wikipedia 4.0GB<br>base (v3) & large (v2):<br>Japanese Wikipedia (4.9GB), Japanese CC&#x2011;100 (74.3GB)   |  東北大<br>自然言語処理研究グループ | base (v1, v2) & large: CC BY&#x2011;SA 3.0<br>base (v3) & large (v2): Apache 2.0 |◯<br>([base (v1)](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking), [base (v1, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-whole-word-masking), [base (v2)](https://huggingface.co/cl-tohoku/bert-base-japanese-v2), [base (v2, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2), [large](https://huggingface.co/cl-tohoku/bert-large-japanese), [large (char-level)](https://huggingface.co/cl-tohoku/bert-large-japanese-char), [base (v3)](https://huggingface.co/cl-tohoku/bert-base-japanese-v3), [base (v3, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v3), [large (v2)](https://huggingface.co/cl-tohoku/bert-large-japanese-v2), [large (v2, char-level)](https://huggingface.co/cl-tohoku/bert-large-japanese-char-v2)) |
| [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/index.html)   |  BERT (base)  |  Japanese Wikipedia  |  NICT  | CC BY 4.0 | △ |
| [colorfulscoop BERT](https://huggingface.co/colorfulscoop/bert-base-ja) | BERT (base) | Japanese Wikipedia | Colorful Scoop | CC BY&#x2011;SA 3.0 | [◯](https://huggingface.co/colorfulscoop/bert-base-ja) |
| [UniversityOfTokyoBERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small) | Japanese Wikipedia (2.9GB) | University of Tokyo Izumi-Sakaji Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/izumi-lab/bert-small-japanese) |
| [chiTra (Sudachi Transformers)](https://www.worksap.co.jp/news/2022/0225/) | BERT (base) | NINJAL Web Japanese Corpus (148GB) | NINJAL & WAP Tokushima Laboratory of AI and NLP | Apache 2.0 | △ |
| [ACCMS BERT](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) | BERT (base) | Japanese Wikipedia (3.3GB) | Kyoto University ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) |
| [HitachiBERT](https://arxiv.org/pdf/2306.09572.pdf) | BERT (base) | Japanese Wikipedia, Japanese CC&#x2011;100 | Hitachi | CC BY-NC-SA 4.0 | [◯](https://huggingface.co/hitachi-nlp/bert-base-japanese_jumanpp-bpe) [^6] |
| [Bandai Namco DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp/blob/main/docs/GUIDE.md) | DistilBERT | （Distillation of TohokuUniversityBERT(base)） | Bandai Namco Research | MIT | [◯](https://huggingface.co/bandainamco-mirai/distilbert-base-japanese) |
| [LINE DistilBERT](https://engineering.linecorp.com/ja/blog/line-distilbert-high-performance-fast-lightweight-japanese-language-model) | DistilBERT |（Distillation of LINE internal BERT model)| LINE | Apache 2.0 | [◯](https://huggingface.co/line-corporation/line-distilbert-base-japanese) |
| [rinna RoBERTa](https://rinna.co.jp/news/2021/08/20210825.html) | RoBERTa (base) |  Japanese Wikipedia, Japanese CC&#x2011;100 | rinna | MIT | [◯](https://huggingface.co/rinna/japanese-roberta-base) |
| [早大RoBERTa](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) | RoBERTa (base, large) | Japanese Wikipedia, Japanese CC&#x2011;100 | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | ◯<br>([base](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp), [large](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp), [large (seq512)](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512-with-auto-jumanpp)) [^7] |
| [InformatixRoBERTa](https://www.informatix.co.jp/pr-roberta/) | RoBERTa (base) | Japanese Wikipedia, Web Articles <br> (25GB) | Informatix | Apache 2.0 | △ |
| [KyotoUniversityRoBERTa](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) | RoBERTa (base, large) | Japanese Wikipedia, Japanese CC&#x2011;100 | Kyoto University Language Media Processing Lab | CC BY&#x2011;SA 4.0 | ◯<br>([base (char-level)](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm), [large (char-level)](https://huggingface.co/ku-nlp/roberta-large-japanese-char-wwm)) |
| [YokohamaNationalRoBERTa](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) | RoBERTa (base) | Japanese Wikipedia (3.45GB) | Yokohama National University Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) |
| [Megagon Labs RoBERTa](https://huggingface.co/megagonlabs/roberta-long-japanese) | RoBERTa (base)[^8] | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit) | MIT | [◯](https://huggingface.co/megagonlabs/roberta-long-japanese)  |
| [ACCMS RoBERTa](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) | RoBERTa (base) | Japanese Wikipedia (3.3GB) + Japanese CC&#x2011;100 (70GB) | Kyoto University ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) |
| [CinnamonELECTRA](https://cinnamon.is/ideas/2020/06/22/20200619_research_001/) | ELECTRA (small) | Japanese Wikipedia | Cinnamon | Apache 2.0 | [◯](https://huggingface.co/Cinnamon/electra-small-japanese-discriminator)  |
| [Megagon Labs ELECTRA](https://www.recruit.co.jp/newsroom/pressrelease/2021/0826_9293.html) | ELECTRA (base) | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit) | MIT | [◯](https://huggingface.co/megagonlabs/electra-base-japanese-discriminator)  |
| [UniversityOfTokyoELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small, base) | Japanese Wikipedia (2.9GB) | University of Tokyo Izumi-Sakaji Lab | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/izumi-lab/electra-small-japanese-discriminator), [base](https://huggingface.co/izumi-lab/electra-base-japanese-discriminator))  |
| [JapaneseRoFormer](https://huggingface.co/ganchengguang/Roformer-base-japanese) | RoFormer (base) | Japanese Wikipedia (3.45GB) | Yokohama National University Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/Roformer-base-japanese) |
| [JapaneseLUKE](https://www.ousia.jp/ja/page/ja/2022/11/17/luke-japanese/) | LUKE (base, large) | Japanese Wikipedia | Studio Ousia | Apache 2.0 | ◯<br>([base](https://huggingface.co/studio-ousia/luke-japanese-base-lite), [large](https://huggingface.co/studio-ousia/luke-japanese-large-lite)) |
| [JapaneseDeBERTa V2](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | DeBERTa (tiny, base, large) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR<br>（171GB） | Kyoto University Language Media Processing Lab | CC BY&#x2011;SA 4.0 | ◯<br>([tiny](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese), [tiny (char-level)](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm), [base](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), [large](https://huggingface.co/ku-nlp/deberta-v2-large-japanese)) | 
| [JapaneseBigBird](https://huggingface.co/nlp-waseda/bigbird-base-japanese) | BigBird (base) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/nlp-waseda/bigbird-base-japanese) |

<a id="autoencoding-domain-specific"></a>
### Domain Specialized

|    |  Architecture  |  Training Data  |  Developer  | License | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
| [JapaneseNewsBERT](https://qiita.com/mkt3/items/3c1278339ff1bcc0187f) | BERT (base) | Japanese Business Articles (3M) | Stockmark | CC BY 4.0 | △ |
| [JapaneseNewsXLNet](https://qiita.com/mkt3/items/4d0ae36f3f212aee8002) |  XLNet (base) | Japanese Business Articles (3M) | Stockmark | ？ | ※ 非公式の HuggingFace 向けに変換されたモデルが[公開されている](https://huggingface.co/hajime9652/xlnet-japanese) |
| [JapaneseNewsALBERT](https://qiita.com/mkt3/items/b41dcf0185e5873f5f75) | ALBERT (base) | Japanese Business Articles (3M) | Stockmark | ？ | △ |
| [Laboro BERT](https://laboro.ai/activity/column/engineer/laboro-bert/) | BERT (base, large) | Japanese Web コーパス <br> (Newsサイトやブログなど<br>計4,307のWebサイト, 2,605,280ページ (12GB)) | Laboro.AI | CC BY-NC 4.0 | |
| [Laboro DistilBERT](https://laboro.ai/activity/column/engineer/laboro-distilbert/) | DistilBERT | - （Laboro BERT(base) を親モデルとして知識蒸留）| Laboro.AI | CC BY-NC 4.0 | [◯](https://huggingface.co/laboro-ai/distilbert-base-japanese) |
| [JapaneseブログELECTRA](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E2-5.pdf) | ELECTRA (small) | Japaneseブログコーパス（3億5,400万文） | 北見工大 桝井・プタシンスキ研 | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ptaszynski/yacis-electra-small-japanese)  |
| [Japanese金融BERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small, base) [^9] | Japanese Wikipedia, Japanese金融コーパス (約2,700万文 (5.2GB)) | University of Tokyo Izumi-Sakaji Lab | CC BY&#x2011;SA 4.0 |◯<br>([small](https://huggingface.co/izumi-lab/bert-small-japanese-fin), [base](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional)) |
| [Japanese金融ELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small) | Japanese Wikipedia (約2,000万文 (2.9GB)), Japanese金融コーパス (約2,700万文 (5.2GB)) | University of Tokyo Izumi-Sakaji Lab | CC BY&#x2011;SA 4.0 |  [◯](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator)  |
| [UTH-BERT](https://ai-health.m.u-tokyo.ac.jp/home/research/uth-bert) | BERT (base) | Japanese診療記録(約1億2,000万行) | University of Tokyo Hospital <br>Medical AI Development Course | CC BY-NC-SA 4.0 | △ |
| [medBERTjp](https://github.com/ou-medinfo/medbertjp) | BERT (base) | Japanese Wikipedia, Japanese医療コーパス（『今日の診療プレミアム』Web版） | 阪大病院 <br> 医療情報学研究室 | CC BY-NC-SA 4.0 | △ |
| [JMedRoBERTa](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf) | RoBERTa (base) | Japanese Medical Papers (約1,100万文 (1.8GB)) | University of Tokyo Aizawa Lab | CC BY-NC-SA 4.0 | ◯<br>([万病WordPiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece), [SentencePiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece)) [^10] |
| [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | RoBERTa (base) | CiNii のJapanese論文 (約628万文) | Ehime University AI Lab | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicRoBERTa) |

<a id="embeddings"></a>
## Sentence and Document Embeddings Models

|    | Architecture |  Developer  |  License | 
|:---|:---:|:---:|:---:|
| [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) | Sentence-BERT | Colorful Scoop | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/SBERT-JSNLI-base](https://huggingface.co/MU-Kindai/SBERT-JSNLI-base)<br>[MU-Kindai/SBERT-JSNLI-large](https://huggingface.co/MU-Kindai/SBERT-JSNLI-large) | Sentence-BERT | Kindai University | ？ |
| [MU-Kindai/Japanese-SimCSE-BERT-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-unsup)<br>[MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-base-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-sup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-sup) | SimCSE | Kindai University | MIT |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) | SimCSE | PKSHA Technology | CC BY&#x2011;SA 4.0 |
| [cl-nagoya/unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base)<br>[cl-nagoya/unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large)<br>[cl-nagoya/sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base)<br>[cl-nagoya/sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large) | SimCSE | Nagoya University Takeda-Sasano Group | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/Japanese-MixCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-base)<br>[MU-Kindai/Japanese-MixCSE-BERT-large](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-large) | MixCSE | Kindai University | MIT |
| [MU-Kindai/Japanese-DiffCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-DiffCSE-BERT-base) | DiffCSE | Kindai University | MIT | 
| [pkshatech/GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) | 独自 (GLuCoSE) | PKSHA Technology | Apache 2.0 |

<a id="multimodal"></a>
## 視覚言語モデル (Vision-Language Models)

<a id="multimodal-text-generation"></a>
### 画像を含むテキスト生成

|    |  Architecture  |  Training Data  |  Developer  | License | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Heron](https://prtimes.jp/main/html/rd/p/000000034.000098132.html) | BLIP または GIT | LLaVA-Instruct-150K-JA, Japanese STAIR Captions, Japanese Visual Genome VQA dataset | Turing | CC BY-NC 4.0 | ◯<br>([blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0), [git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0), [git-ELYZA-fast-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ELYZA-fast-7b-v0)) |
| [Japanese InstructBLIP Alpha](https://ja.stability.ai/blog/japanese-instructblip-alpha) | InstructBLIP | Japanese CC12M, STAIR Captions, Japanese Visual Genome VQA dataset | Stability AI | [独自のライセンス](https://huggingface.co/stabilityai/japanese-instructblip-alpha/blob/main/LICENSE) |  [◯](https://huggingface.co/stabilityai/japanese-instructblip-alpha) |
| [rinna MiniGPT-4](https://rinna.co.jp/news/2023/07/20230731.html) [^11] | MiniGPT-4 | CC12M, COCO 2014, Visual Genome, STAIR Captions, Japanese Visual Genome VQA dataset | rinna | MIT | [◯](https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4) |

<a id="multimodal-others"></a>
### その他

|    |  モデル  |  学習画像/テキスト  |  開発元  | ライセンス | HuggingFace ですぐ使える？  |
|:---|:---:|:---:|:---:|:---:|:---:|
| [JapaneseCLIP](https://rinna.co.jp/news/2022/05/20220512.html) | CLIP <br>(画像エンコーダは  google/vit-base-patch16-224 で重みが初期化された ViT-B/16, <br>テキストエンコーダは rinna RoBERTa で重みが初期化された RoBERTa(base)) | CC12M のキャプションをJapaneseに翻訳したもの | rinna | Apache 2.0 | [◯](https://huggingface.co/rinna/japanese-clip-vit-b-16) |
| [JapaneseCLOOB](https://rinna.co.jp/news/2022/05/20220512.html) | CLOOB <br>(画像エンコーダは  google/vit-base-patch16-224 で重みが初期化された ViT-B/16, <br>テキストエンコーダは rinna RoBERTa で重みが初期化された RoBERTa(base)) | CC12M のキャプションをJapaneseに翻訳したもの | rinna | Apache 2.0 | [◯](https://huggingface.co/rinna/japanese-cloob-vit-b-16) |
| [Japanese Stable Diffusion](https://rinna.co.jp/news/2022/09/20220909.html) | Stable Diffusion (最初にテキストエンコーダのみJapaneseキャプション付き画像を用いて追加学習を行い, 次にテキストエンコーダと生成モデルのパラメータを同時に更新する追加学習を行う) |  LAION-5B データセットのうちキャプションがJapaneseのもの（画像約 1 億枚）| rinna | [The CreativeML OpenRAIL M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) | [◯](https://huggingface.co/rinna/japanese-stable-diffusion) |

<a id="benchmark-suites"></a>
## （参考）JapaneseLLMベンチマークまとめ

#### 基礎的な自然言語理解 (NLU) を中心に測定するベンチマーク

- [JGLUE](https://github.com/yahoojapan/JGLUE) (早大河原研 & ヤフー)
  - [GLUE ベンチマーク](https://gluebenchmark.com/)のJapanese版として構築されたベンチマーク。MARC-ja, JCoLA, JSTS, JNLI, JSQuAD, JCommonsenseQA の 6 つのタスクを含む（[JCoLA](https://github.com/osekilab/JCoLA) は東大大関研により作成）。各タスクの詳細は[こちら](https://www.jstage.jst.go.jp/article/jnlp/30/1/30_63/_article/-char/ja)や[こちら](https://techblog.yahoo.co.jp/entry/2022122030379907/)を参照
- [JP Language Model Evaluation Harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) (Stability AI)
  - Stability AI による [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) のフォーク。JGLUE を含む様々なJapaneseタスクに対するモデルの few-shot 評価をまとめている
- [Nejumi LLMリーダーボード](https://wandb.ai/wandb/LLM_evaluation_Japan/reports/LLM-JGLUE---Vmlldzo0NTUzMDE2?accessToken=u1ttt89al8oo5p5j12eq3nldxh0378os9qjjh14ha1yg88nvs5irmuao044b6eqa) (Weights & Biases)
  - JGLUE に対するモデルの zero-shot 評価をまとめている

#### 人間らしい応答の生成能力を中心に測定するベンチマーク

- [Rakuda Benchmark](https://yuzuai.jp/benchmark)
  - 日本の地理, 歴史, 政治, 社会に関する[40問の自由質問](https://huggingface.co/datasets/yuzuai/rakuda-questions)に対してモデルに出力を行わせる。GPT-4 が同じ質問に対する2つのモデルの出力を比べ, どちらの答えが優れているかを判断することにより, モデルのランク付けを行う
- [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) (ELYZA)
  - 複雑な指示・タスクを含む100件のJapaneseデータで, 全てのデータに対して評価観点がアノテーションされている。<br>要約を修正し修正箇所を説明するタスク, 具体的なエピソードから抽象的な教訓を述べるタスク, ユーザーの意図を汲み役に立つAIアシスタントとして振る舞うタスク, 場合分けを必要とする複雑な算数のタスク, 未知の言語からパターンを抽出しJapanese訳する高度な推論を必要とするタスク, 複数の指示を踏まえた上でyoutubeの対話を生成するタスク, 架空の生き物や熟語に関する生成・大喜利などの想像力が求められるタスクなどが含まれている。<br>
  モデルの評価結果は[こちら](https://docs.google.com/spreadsheets/d/1mtoy4QAqDPk2f_B0vDogFoOrbA5G42DBEEHdqM4VmDI/edit#gid=1023787356)や[こちら](https://zenn.dev/elyza/articles/5e7d9373c32a98)を参照

<a id="reference"></a>
## Architecture References

| Architecture | Date | Meeting/Journal | Paper |
|:---|:---|:---|:--|
| Transformer | 2017.06.12 | NIPS(NeurIPS) 2017 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| GPT | 2018.06.11 | - | [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | 
| BERT | 2018.10.11 | NAACL 2019 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423/) |
| GPT-2 | 2019.02.14 | - | [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| XLNet | 2019.06.19 | NeurIPS 2019 | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://arxiv.org/abs/1906.08237) |
| RoBERTa | 2019.07.26 | - | [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) |
| ALBERT | 2019.09.26 | ICLR 2020 | [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942) |
| DistilBERT | 2019.10.02 | EMC2 Workshop at NeurIPS 2019 | [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108) |
| T5 | 2019.10.23 | JMLR 2020 | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683) | 
| BART | 2019.10.29 | ACL 2020 | [BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://aclanthology.org/2020.acl-main.703/) |
| ELECTRA | 2020.03.23 | ICLR 2020 | [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555) | 
| GPT-3 | 2020.05.28 | NeurIPS 2020 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) |
| DeBERTa | 2020.06.05 | ICLR 2021 | [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) |
| BigBird | 2020.07.28 | NeurIPS 2020 | [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) |
| LUKE | 2020.10.02 | EMNLP 2020 | [LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://aclanthology.org/2020.emnlp-main.523/) |
| CLIP | 2021.02.26 | ICML 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) |
| RoFormer | 2021.04.20 | - | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) |
| CLOOB | 2021.10.21 | NeurIPS 2022 | [CLOOB: Modern Hopfield Networks with InfoLOOB Outperform CLIP](https://arxiv.org/abs/2110.11316) |
| Stable Diffusion | 2021.12.20 | CVPR 2022 | [High-Resolution Image Synthesis With Latent Diffusion Models](https://arxiv.org/abs/2112.10752) |
| BLIP | 2022.01.28 | ICML 2022 | [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://arxiv.org/abs/2201.12086) |
| InstructGPT | 2022.03.04 | NeurIPS 2022 | [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) |
| GPT-NeoX | 2022.04.14 | BigScience Research Workshop at ACL 2022 | [GPT-NeoX-20B: An Open-Source Autoregressive Language Model](https://aclanthology.org/2022.bigscience-1.9/) |
| GIT | 2022.05.27 | TMLR 2022 | [GIT: A Generative Image-to-text Transformer for Vision and Language](https://arxiv.org/abs/2205.14100) |
| BLIP-2 | 2023.01.30 | ICML 2023 | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597) |
| Llama | 2023.02.27 | - | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | 
| GPT-4 | 2023.03.15 | - | [GPT-4 Technical Report](https://arxiv.org/abs/2303.08774) |
| MiniGPT-4 | 2023.04.20 | - | [MiniGPT-4: Enhancing Vision-Language Understanding with Advanced Large Language Models](https://arxiv.org/abs/2304.10592) |
| InstructBLIP | 2023.05.11 | - | [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://arxiv.org/abs/2305.06500) |
| RWKV | 2023.05.22 | - | [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048) |
| Llama 2 | 2023.07.18 | - | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) |

---

[^1]: ○: HuggingFace の Model Hub にモデルがアップロードされており, `AutoModel.from_pretrained()` 等ですぐ読み込める。 △: Model Hub にはモデルがアップロードされていないが, HuggingFace (transformers, 旧 pytorch-transformers) の形式に対応している

[^2]: ただし, モデル高速化のため本家の Llama に対してアーキテクチャの変更を加えている。詳しくは以下を参照: [PLaMo-13Bを公開しました](https://tech.preferred.jp/ja/blog/llm-plamo/)

[^3]: 詳細は明記されていないが, プレスリリースには以下のような記述がある: 『学習データには, オープンデータセットに加え, Stability AI Japanが作成した独自のデータセットや, EleutherAI Polyglot project のJapaneseチーム及び Stable Community Japan のメンバーの協力のもとで作成したデータが含まれています。』

[^4]: 通常の左から右に単語を予測する代わりに, 右から左に単語を予測するように訓練された言語モデルの評価を行った研究である。通常方向の言語モデルと逆方向の言語モデルの両方が公開されている。

[^5]: 実質的な開発者は代表を勤める大曽根宏幸氏 （[個人ページのリンク](https://soneo1127.github.io/)）で, [AI Buncho](https://bun-cho.work/) の運営も行っている

[^6]: 様々な形態素解析器とサブワード化手法の組み合わせを試した研究である。全ての組み合わせのモデルを掲載するのは大変なので, ここでは実験で最も平均のタスク性能が高い Juman++ + BPE のモデルを代表として掲載している。

[^7]: nlp-waseda/roberta-base-japanese 及び nlp-waseda/roberta-large-japanese はモデル入力の最大トークン長を128で事前学習しているが, nlp-waseda/roberta-large-japanese-seq512 は512で事前学習している

[^8]: ただし, 最大系列長が通常の 512 から 1282 まで拡張されており, より長い入力文を扱うことができる

[^9]: small の方はJapanese Wikipedia とJapanese金融コーパスを合わせてスクラッチ学習しているが, base の方は東北大BERTにJapanese金融コーパスを追加学習しているという違いがある

[^10]: 万病WordPieceモデルは MeCab (IPA辞書+万病辞書) で単語分割した後 WordPiece でサブワード化するモデル, SentencePieceモデルは単語分割せずに直接 Unigram でサブワード化するモデル

[^11]: 以下の記事が詳しい（この記事での MiniGPT-4 の実装例は LLM 部分 を rinna/bilingual-gpt-neox-4b ではなく rinna/japanese-gpt-neox-3.6b としている点に注意）: [Japanese MiniGPT-4: rinna 3.6bとBLIP-2を組み合わせてマルチモーダルチャットのモデルを作る](https://zenn.dev/rinna/articles/5fad41e3f2a401)
