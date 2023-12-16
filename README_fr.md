# Aperçu des grands modèles de langage (LLM) en japonais
[ [**English**](./README_en.md) | Français | [**日本語**](./README.md) ]

<p align="center">
  <img src="figures/parameter_size_overview.png" alt="LLMs en japonais et en anglais par taille de paramètres au fil du temps">
</p>
<figcaption style="font-style: italic; font-size: 0.9em; color: #6b7280; text-align: center;">Evolution du nombre de paramètres des LLMs en japonais et en anglais. Pour des informations sur le modèle japonais, nous nous référons à cet article, et pour le modèle anglais, nous nous référons au <a href="https://lifearchitect.ai/models-table/">tableau des modèles</a> sur LifeArchitect.ai (notez cependant que certains modèles ont été omis en raison de l'espace limité sur le graphique. De plus, le nombre de paramètres pour le modèle anglais inclut des valeurs estimées). Veuillez nous informer de toute correction ou ajout nécessaire.</figcaption>

---

Voici une liste pour les LLMs avec un apprentissage pour la langue japonaise pour le grand public. Cette liste est maintenue par des bénévoles sur les bases de données publiques.

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
  - [Modèles développés à partir d'LLM en anglais (avec un apprentissage en continue en japonais)](#english-based-models)
    - [D'usage général](#generative-continual-general)
    - [Spécifique à un domaine](#generative-continual-domain-specific)
  - [Modèles développés à partir d'LLM en anglais (avec un affinement par instructions en japonais)](#instruction-only-models)
    - [D'usage général](#generative-instruction-only-general)
    - [Spécifique à un domaine](#generative-instruction-only-domain-specific)
- [Modèles encodeur](#autoencoding)
  - [D'usage général](#autoencoding-general)
  - [Spécifique à un domaine](#autoencoding-domain-specific)
- [Plongement lexical par mots et par documents](#embeddings)
- [Modèles Vision-Language](#multimodal)
  - [Text+Image vers Text](#multimodal-text-generation)
  - [Autres](#multimodal-others)
- [Standard d'évaluation pour les LLM en japonais](#benchmark-suites)
- [Références par architecture des modèles](#reference)
- [Nos contributors](#contributors)


<a id="generative"></a>
## Modèles IA génératives

*Pour les modèles multimodal, voir [ci-dessous.](#multimodal-text-generation)*

<a id="full-scratch-models"></a>
### Modèles développés à partir de zéro

<a id="generative-scratch-general"></a>
#### D'usage général

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|
| [LLM-jp-13B](https://www.nii.ac.jp/en/news/release/2023/1020.html) | GPT<br>([1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0), [**13b**-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0), [**13b**-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0), [**13b**-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0), [**13b**-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0), [**13b**-instruct-lora-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-v1.0), [**13b**-instruct-lora-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-jaster-dolly-oasst-v1.0), [**13b**-instruct-lora-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-lora-dolly-oasst-v1.0)) | Pré-entraînement: [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) (Wikipedia, Japanese mC4, The Pile, Stack) (**300B** tokens)<br>Instruction Tuning (SFT or LoRA): jaster, Dolly Dataset, OASST1 | LLM-jp | Apache 2.0 |
| [PLaMo-13B](https://www.preferred.jp/en/news/pr20230928/) | Llama[^1]<br>([**13b**](https://huggingface.co/pfnet/plamo-13b), [**13b**-instruct](https://huggingface.co/pfnet/plamo-13b-instruct), [**13b**-instruct-nc](https://huggingface.co/pfnet/plamo-13b-instruct-nc)) | Pré-entraînement: C4, Project Gutenberg, RedPajama, Japanese Wikipedia, Japanese mC4<br>(**1.5T** tokens)<br>SFT: Dolly, HH RLHF, OASST1, wikinews (+Alpaca in NC model)  | Preferred Networks | Apache 2.0<br>(CC BY-NC 4.0 as for NC model) |
| [Stockmark-13b](https://stockmark.co.jp/news/20231027) | Llama<br>([**13b**](https://huggingface.co/stockmark/stockmark-13b), [**13b**-instruct](https://huggingface.co/stockmark/stockmark-13b-instruct)) | Wikipedia en japonais, Japanese CC-100, Japanese mC4, Japanese CommonCrawl, Japanese Patent, Stockmark Web Corpus<br>(**220B** tokens)<br>Instruct Tuning (LoRA): [ichikara-instruction](https://liat-aip.sakura.ne.jp/wp/llm%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%A9%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%87%E3%83%BC%E3%82%BF%E4%BD%9C%E6%88%90/) | Stockmark | base: MIT<br>instruct: CC BY-NC-SA 4.0 |
| [Weblab-10B](https://www.t.u-tokyo.ac.jp/press/pr2023-08-18-001) | GPT-NeoX <br> ([**10b**](https://huggingface.co/matsuo-lab/weblab-10b), [**10b**-instruction-sft](https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft)) | Japanese mC4, The Pile <br> (**600B** tokens) <br>SFT: Alpaca, FLAN | Université de Tokyo Matsuo Lab | CC BY&#x2011;NC 4.0 |
| [Japanese StableLM Alpha](https://stability.ai/blog/stability-ai-new-jplm-japanese-language-model-stablelm) | GPT-NeoX <br> ([base-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b), [instruct-alpha-**7b**](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b), [instruct-alpha-**7b**-v2](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b-v2)) | Wikipédia, Japanese CC&#x2011;100, Japanese mC4, Japanese OSCAR, RedPajama, ensembles de données privés[^2]<br>(**750B** tokens)<br>SFT: Dolly, HH&#x2011;RLHF, wikinews,  Alpaca (discarded in v2) | Stability AI | base: Apache 2.0<br>instruct (v1): [Research license](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b/tree/main)<br>instruct (v2): Apache 2.0 |
| [CALM2](https://www.cyberagent.co.jp/news/detail/id=29479) | Llama<br>([**7b**](https://huggingface.co/cyberagent/calm2-7b), [**7b**-chat](https://huggingface.co/cyberagent/calm2-7b-chat)) | Ensembles de données japonais et anglais accessibles au public (détails inconnus)<br>(**1.3T** tokens)  | CyberAgent | Apache 2.0 |
| [OpenCALM](https://www.cyberagent.co.jp/news/detail/id=28817) | GPT-NeoX <br> ([small](https://huggingface.co/cyberagent/open-calm-small), [medium](https://huggingface.co/cyberagent/open-calm-medium), [large](https://huggingface.co/cyberagent/open-calm-large), [**1b(1.4b)**](https://huggingface.co/cyberagent/open-calm-1b), [**3b(2.7b)**](https://huggingface.co/cyberagent/open-calm-3b), [**7b(6.8b)**](https://huggingface.co/cyberagent/open-calm-7b)) | Wikipedia en japonais, Japanese mC4, Japanese CC&#x2011;100 | CyberAgent | CC BY&#x2011;SA 4.0 |
| [Stormy](https://jxiv.jst.go.jp/index.php/jxiv/preprint/view/422/1350) | GPT-NeoX <br>([**7b(6.8b)**](https://huggingface.co/izumi-lab/stormy-7b-10ep)) | OpenCALM fine-tuned sur <br>llm-japanese-dataset v0 sans âches de traduction | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |
| [rinna GPT <br> (En-Ja Bilingual)](https://rinna.co.jp/news/2023/07/20230731.html) | GPT-NeoX <br>([**4b(3.8b)**](https://huggingface.co/rinna/bilingual-gpt-neox-4b), [**4b(3.8b)**-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k), [**4b(3.8b)**-instruction-sft](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft), [**4b(3.8b)**-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo)) | Wikipedia, Japanese CC&#x2011;100, Japanese C4, RedPajama, The Pile<br>(**524B** tokens)<br> SFT: HH&#x2011;RLHF, FLAN<br>PPO: HH&#x2011;RLHF par apprentissage par renforcement  <br>8k: entrainé sur du long texte | rinna | MIT |
| [japanese-large-lm](https://engineering.linecorp.com/ja/blog/3.6b-japanese-language-model-with-improved-dialog-performance-by-instruction-tuning) | GPT-NeoX <br>([**1.7b**](https://huggingface.co/line-corporation/japanese-large-lm-1.7b), [**3.6b**](https://huggingface.co/line-corporation/japanese-large-lm-3.6b), [**1.7b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft), [**3.6b**-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft)) | Wikipedia en japonais, Japanese CC&#x2011;100, Japanese C4, Japanese OSCAR et ensembles de données privés<br>(**650GB**)<br>SFT: OASST1 | LINE | Apache 2.0 |
| [rinna GPT <br> (Japanese only)](https://rinna.co.jp/news/2023/05/20220531.html) | GPT-NeoX <br>([xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall), [small](https://huggingface.co/rinna/japanese-gpt2-small), [medium](https://huggingface.co/rinna/japanese-gpt2-medium), [**1b**](https://huggingface.co/rinna/japanese-gpt-1b), [neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small), [neox-**3.6b**](https://huggingface.co/rinna/japanese-gpt-neox-3.6b), [neox-**3.6b**-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft), [neox-**3.6b**-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2), [neox-**3.6b**-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo)) | Wikipédia en japonais, Japanese CC&#x2011;100 <br> (1b et plus modèles à ajouter <br>Japanese mC4)<br>SFT: HH&#x2011;RLHF, FLAN, SHP <br>PPO: HH&#x2011;RLHF par apprentissage par renforcement | rinna | MIT |
| [RetrievaT5](https://note.com/retrieva/n/n7b4186dc5ada) | T5 <br>([small (short)](https://huggingface.co/retrieva-jp/t5-small-short), [small (medium)](https://huggingface.co/retrieva-jp/t5-small-medium), [small (long)](https://huggingface.co/retrieva-jp/t5-small-long), [base (short)](https://huggingface.co/retrieva-jp/t5-base-short), [base (medium)](https://huggingface.co/retrieva-jp/t5-base-medium), [base (long)](https://huggingface.co/retrieva-jp/t5-base-long), [large (short)](https://huggingface.co/retrieva-jp/t5-large-short), [large (medium)](https://huggingface.co/retrieva-jp/t5-large-medium), [large (long)](https://huggingface.co/retrieva-jp/t5-large-long), [**xl(3b)**](https://huggingface.co/retrieva-jp/t5-xl)) | Wikipédia en japonais, Japanese mC4 | Retrieva | CC BY&#x2011;SA 4.0 |
| [ABEJA GPT](https://tech-blog.abeja.asia/entry/abeja-gpt-project-202207) | GPT-NeoX <br>([large](https://huggingface.co/abeja/gpt2-large-japanese), [neox-**2.7b**](https://huggingface.co/abeja/gpt-neox-japanese-2.7b)) | Japanese Wikipedia, Japanese CC&#x2011;100, Japanese OSCAR | ABEJA | MIT |
| [WasedaGPT](https://huggingface.co/nlp-waseda/gpt2-xl-japanese) | GPT-NeoX <br> ([small](https://huggingface.co/nlp-waseda/gpt2-small-japanese), [**xl(1.5b)**](https://huggingface.co/nlp-waseda/gpt2-xl-japanese)) | Wikipédia en japonais, Japanese CC&#x2011;100 | Université de Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 |
| [StockmarkGPT](https://stockmark.co.jp/news/20230808) | GPT-NeoX <br>([**1.4b**](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b)) | Wikipédia en japonais (0.88B tokens), Japanese CC&#x2011;100 (10.5B tokens), ensembles de données privés (8.6B tokens) | Stockmark | MIT |
| [YellowbackGPT](https://tech.yellowback.net/posts/gpt-neo-japanese) | GPT-NeoX <br>([**1.3b**](https://huggingface.co/yellowback/gpt-neo-japanese-1.3B)) | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR | Yellowback | Apache 2.0 |
| [colorfulscoop GPT](https://huggingface.co/colorfulscoop/gpt2-small-ja) | GPT-NeoX <br>([small](https://huggingface.co/colorfulscoop/gpt2-small-ja)) | Wikipédia en japonais | Colorful Scoop | CC BY&#x2011;SA 3.0 |
| [TitechGPT](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/H9-1.pdf) | GPT-NeoX <br>([medium](https://huggingface.co/okazaki-lab/japanese-gpt2-medium-unidic), [medium-reversed](https://huggingface.co/okazaki-lab/japanese-reversed-gpt2-medium-unidic)) [^3] | Wikipédia en japonais, Japanese CC&#x2011;100 | Titech Okazaki Lab | CC BY&#x2011;SA 4.0 |
| [KyotoUniversityGPT](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) | GPT-NeoX <br>([small](https://huggingface.co/ku-nlp/gpt2-small-japanese-char), [medium](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char)) | Wikipédia en japonais (3.2GB), Japanese CC&#x2011;100 (85GB), Japanese OSCAR (54GB) | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 |
| [JapaneseBART](https://huggingface.co/ku-nlp/bart-base-japanese) | BART <br>([base](https://huggingface.co/ku-nlp/bart-base-japanese), [large](https://huggingface.co/ku-nlp/bart-large-japanese)) | Wikipédia en japonais (18M sentences) | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 |
| [Megagon Labs T5](https://github.com/megagonlabs/t5-japanese) | T5 <br>([base](https://huggingface.co/megagonlabs/t5-base-japanese-web)) | Japanese mC4 (782 GB), Wikipédia en japonais 40b (2 GB) | Megagon Labs <br> (Recruit) | Apache 2.0 |

<a id="generative-scratch-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Architecture  |  Données d'entraînement  |  Développeur  | Licence |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Japanese Dialog Transformer](https://github.com/nttcslab/japanese-dialog-transformers) | Dialogue | Transformer | Pairs de réponses venant de Twitter | NTT | [License en évaluaiton](https://github.com/nttcslab/japanese-dialog-transformers/blob/main/LICENSE.md) |
| [Japanese News BART](https://tech.stockmark.co.jp/blog/bart-japanese-base-news/) | Affaires |  BART ([base](https://huggingface.co/stockmark/bart-base-japanese-news)) | Articles de l'actualité économique en japonais (21M articles) | Stockmark | MIT |
| [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | Science | BART ([base](https://huggingface.co/EhimeNLP/AcademicBART)) | CiNii Japanese Papers | Université d'Ehime AI Lab | Apache 2.0 |

<a id="english-based-models"></a>
### Modèles développés à partir d'LLM en anglais (avec une apprentissage continue en japonais)

<a id="generative-continual-general"></a>
#### D'usage général

|    | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|
| [Japanese Stable LM Beta 70B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-70b), [instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b)) | Llama 2 (**70b**) | Stability AI | Llama 2 Community License |
| [ELYZA-japanese-Llama-2-7b](https://note.com/elyza/n/na405acaca130)<br> ([7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct), [7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast), [7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct)) | Llama 2 (**7b**) | ELYZA | Llama 2 Community License |
| [Youri 7B](https://rinna.co.jp/news/2023/10/20231031.html)<br>([7b](https://huggingface.co/rinna/youri-7b), [7b-instruction](https://huggingface.co/rinna/youri-7b-instruction), [7b-chat](https://huggingface.co/rinna/youri-7b-chat), [7b-gptq](https://huggingface.co/rinna/youri-7b-gptq), [7b-instruction-gptq](https://huggingface.co/rinna/youri-7b-instruction-gptq), [7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq)) | Llama 2 (**7b**) | rinna | Llama 2 Community License |
| [Japanese Stable LM Beta 7B](https://ja.stability.ai/blog/japanese-stable-lm-beta)<br>([base-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-beta-7b), [base-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-ja_vocab-beta-7b), [instruct-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-7b), [instruct-ja_vocab-beta-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-ja_vocab-beta-7b)) |  Llama 2 (**7b**) | Stability AI | Llama 2 Community License |
| [Japanese Stable LM Gamma 7B](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([base-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b), [instruct-gamma-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b)) | Mistral-7B-v0.1 (**7b**) |  Stability AI |  Apache 2.0  |
| [lightblue/japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) | MPT (**7b**) | Lightblue | Apache 2.0 |
| [Japanese Stable LM 3B-4E1T](https://ja.stability.ai/blog/japanese-stable-lm-3b-4e1tjapanese-stable-lm-gamma-7b)<br>([3b-4e1t-base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base), [3b-4e1t-instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-instruct)) | StableLM-3B-4E1T (**3b**) | Stability AI |  Apache 2.0  |

<a id="generative-continual-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [ELYZA-japanese-CodeLlama-7b](https://note.com/elyza/n/n5bce23d7c9c8)<br>([7b](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b), [7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-CodeLlama-7b-instruct)) | Codage | Code Llama<br>(**7b**) | ELYZA | Llama 2 Community License |
| [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) | Génération de récits | GPT-J (**6b**) | Industrial Dream[^5] | CreativeML OpenRAIL-M License |
| [NovelAI/genji-jp](https://huggingface.co/NovelAI/genji-jp) | Génération de récits | GPT-J (**6b**) | NovelAI |  ？  |

<a id="instruction-only-models"></a>
### Modèles développés à partir d'LLM en anglais (avec un affinement par instructions en japonais)

<a id="generative-instruction-only-general"></a>
#### D'usage général

|    | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|
| [AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese](https://huggingface.co/AIgroup-CVM-utokyohospital/Llama-2-70b-chat-4bit-japanese) | Llama 2 (**70b**) | Université de Tokyo - AI Group du Département hospitalier de médecine cardiovasculaire |  Llama 2 Community License |
| [doshisha-mil/llama-2-70b-chat-4bit-japanese-v1](https://huggingface.co/doshisha-mil/llama-2-70b-chat-4bit-japanese-v1) | Llama 2 (**70b**) | Université de Doshisha Media Informatics Lab | ？ |
| [Sparticle/llama-2-13b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-13b-chat-japanese-lora) | Llama 2 (**13b**) | Sparticle | ？ |
| [izumi-lab/llama-13b-japanese-lora-v0-1ep](https://huggingface.co/izumi-lab/llama-13b-japanese-lora-v0-1ep) | Llama (**13b**) | Université de Tokyo Izumi Lab |  ？ |
| [ganchengguang/Yoko-7B-Japanese-v1](https://huggingface.co/ganchengguang/Yoko-7B-Japanese-v1) | Llama 2 (**7b**) | Université nationale de Yokohama Mori Lab |  ？  |
| [Sparticle/llama-2-7b-chat-japanese-lora](https://huggingface.co/Sparticle/llama-2-7b-chat-japanese-lora) | Llama 2 (**7b**) | Sparticle |  ？  |
| [izumi-lab/llama-7b-japanese-lora-v0-5ep](https://huggingface.co/izumi-lab/llama-7b-japanese-lora-v0-5ep) | Llama (**7b**) | Université de Tokyo Izumi Lab |  ？  |
| [lightblue/jod](https://huggingface.co/lightblue/jod) | Mistral-7B-SlimOrca (**7b**) | Lightblue | Apache 2.0 |
| [NTQAI/chatntq-7b-jpntuned](https://huggingface.co/NTQAI/chatntq-7b-jpntuned) | RWKV-4 World (**7b**)| NTQ Solution |  ？  |

<a id="generative-instruction-only-domain-specific"></a>
#### Spécifique à un domaine

|    | Domaine | Base du Model  |  Développeur  |  Licence  |
|:---|:---:|:---:|:---:|:---:|
| [JMedLoRA](https://arxiv.org/pdf/2310.10083.pdf)<br>([llama2-jmedlora-6.89ep](https://huggingface.co/AIgroup-CVM-utokyohospital/llama2-jmedlora-6.89ep)) | Médecine | Llama 2 (**70b**) | Université de Tokyo - AI Group du Département hospitalier de médecine cardiovasculaire | CC BY-NC 4.0 |

<a id="autoencoding"></a>
## Modèles encodeur

<a id="autoencoding-general"></a>
### D'usage général

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? [^4] |
|:---|:---:|:---:|:---:|:---:|:---:|
|  [KyotoUniBERT](https://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)  |  BERT (base, large)  |  Wikipédia en japonais (18M articles)  |  Université de Kyoto Laboratoire de traitement des langues et des médias | Apache 2.0 | △ |
|  [TohokuUniversityBERT](https://github.com/cl-tohoku/bert-japanese)  |  BERT (base, large)  |  base (v1):<br>Wikipédia en japonais (17M articles / 2.6GB)<br>base (v2) & large:<br>Wikipédia en japonais 4.0GB<br>base (v3) & large (v2):<br>Wikipédia en japonais (4.9GB), Japanese CC&#x2011;100 (74.3GB)   |  Université de Tohoku - Groupe TAL | base (v1, v2) & large: CC BY&#x2011;SA 3.0<br>base (v3) & large (v2): Apache 2.0 |◯<br>([base (v1)](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking), [base (v1, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-whole-word-masking), [base (v2)](https://huggingface.co/cl-tohoku/bert-base-japanese-v2), [base (v2, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2), [large](https://huggingface.co/cl-tohoku/bert-large-japanese), [large (char-level)](https://huggingface.co/cl-tohoku/bert-large-japanese-char), [base (v3)](https://huggingface.co/cl-tohoku/bert-base-japanese-v3), [base (v3, char-level)](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v3), [large (v2)](https://huggingface.co/cl-tohoku/bert-large-japanese-v2), [large (v2, char-level)](https://huggingface.co/cl-tohoku/bert-large-japanese-char-v2)) |
| [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/index.html)   |  BERT (base)  |  Wikipédia en japonais  |  NICT  | CC BY 4.0 | △ |
| [colorfulscoop BERT](https://huggingface.co/colorfulscoop/bert-base-ja) | BERT (base) | Wikipédia en japonais | Colorful Scoop | CC BY&#x2011;SA 3.0 | [◯](https://huggingface.co/colorfulscoop/bert-base-ja) |
| [UniversityOfTokyoBERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small) | Wikipédia en japonais (2.9GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/izumi-lab/bert-small-japanese) |
| [chiTra (Sudachi Transformers)](https://www.worksap.co.jp/news/2022/0225/) | BERT (base) | NINJAL Web Japanese Corpus (148GB) | NINJAL & WAP Tokushima - Laboratoire IA et TAL | Apache 2.0 | △ |
| [ACCMS BERT](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) | BERT (base) | Wikipédia en japonais (3.3GB) | Université de Kyoto ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) |
| [HitachiBERT](https://aclanthology.org/2023.acl-srw.5.pdf) | BERT (base) | Wikipédia en japonais, Japanese CC&#x2011;100 | Hitachi | CC BY&#x2011;NC&#x2011;SA 4.0 | [◯](https://huggingface.co/hitachi-nlp/bert-base-japanese_jumanpp-bpe)[^6] |
| [Bandai Namco DistilBERT](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) | DistilBERT |  (Distillation de BERT (base) de l'Université du Tohoku)  | Bandai Namco Research | MIT | [◯](https://huggingface.co/bandainamco-mirai/distilbert-base-japanese) |
| [LINE DistilBERT](https://engineering.linecorp.com/ja/blog/line-distilbert-high-performance-fast-lightweight-japanese-language-model) | DistilBERT | (Distillation de LINE en interne BERT model)| LINE | Apache 2.0 | [◯](https://huggingface.co/line-corporation/line-distilbert-base-japanese) |
| [rinna RoBERTa](https://rinna.co.jp/news/2021/08/20210825.html) | RoBERTa (base) |  Wikipédia en japonais, Japanese CC&#x2011;100 | rinna | MIT | [◯](https://huggingface.co/rinna/japanese-roberta-base) |
| [WasedaRoBERTa](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) | RoBERTa (base, large) | Wikipédia en japonais, Japanese CC&#x2011;100 | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | ◯<br>([base](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp), [large](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp), [large (seq512)](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512-with-auto-jumanpp))[^7] |
| [InformatixRoBERTa](https://www.informatix.co.jp/en/pr-roberta/) | RoBERTa (base) | Wikipédia en japonais, Web Articles <br> (25GB) | Informatix | Apache 2.0 | △ |
| [KyotoUniversityRoBERTa](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) | RoBERTa (base, large) | Wikipédia en japonais, Japanese CC&#x2011;100 | Université de Kyoto Laboratoire de traitement des langues et des médias | CC BY&#x2011;SA 4.0 | ◯<br>([base (char-level)](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm), [large (char-level)](https://huggingface.co/ku-nlp/roberta-large-japanese-char-wwm)) |
| [YokohamaNationalRoBERTa](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) | RoBERTa (base) | Wikipédia en japonais (3.45GB) | Université nationale de Yokohama - Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/RoBERTa-base-janpanese) |
| [Megagon Labs RoBERTa](https://huggingface.co/megagonlabs/roberta-long-japanese) | RoBERTa (base)[^8] | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit) | MIT | [◯](https://huggingface.co/megagonlabs/roberta-long-japanese)  |
| [ACCMS RoBERTa](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) | RoBERTa (base) | Wikipédia en japonais (3.3GB) + Japanese CC&#x2011;100 (70GB) | Université de Kyoto ACCMS | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ku-accms/roberta-base-japanese-ssuw) |
| [CinnamonELECTRA](https://cinnamon.is/ideas/2020/06/22/20200619_research_001/) | ELECTRA (small) | Wikipédia en japonais | Cinnamon | Apache 2.0 | [◯](https://huggingface.co/Cinnamon/electra-small-japanese-discriminator)  |
| [Megagon Labs ELECTRA](https://www.recruit.co.jp/newsroom/pressrelease/2021/0826_9293.html) | ELECTRA (base) | Japanese mC4 (200M sentences) | Megagon Labs <br> (Recruit) | MIT | [◯](https://huggingface.co/megagonlabs/electra-base-japanese-discriminator)  |
| [UniversityOfTokyoELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small, base) | Wikipédia en japonais (2.9GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 | ◯<br>([small](https://huggingface.co/izumi-lab/electra-small-japanese-discriminator), [base](https://huggingface.co/izumi-lab/electra-base-japanese-discriminator))  |
| [JapaneseRoFormer](https://huggingface.co/ganchengguang/Roformer-base-japanese) | RoFormer (base) | Wikipédia en japonais (3.45GB) | Université nationale de Yokohama - Mori Lab | Apache 2.0 | [◯](https://huggingface.co/ganchengguang/Roformer-base-japanese) |
| [JapaneseLUKE](https://www.ousia.jp/ja/page/ja/2022/11/17/luke-japanese/) | LUKE (base, large) | Wikipédia en japonais | Studio Ousia | Apache 2.0 | ◯<br>([base](https://huggingface.co/studio-ousia/luke-japanese-base-lite), [large](https://huggingface.co/studio-ousia/luke-japanese-large-lite)) |
| [KyotoUniversityDeBERTaV2](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) | DeBERTaV2 (tiny, base, large) | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR<br> (171GB)  | Université de Kyoto - Laboratoire du traitement des langues et médias | CC BY&#x2011;SA 4.0 | ◯<br>([tiny](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese), [tiny (char-level)](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm), [base](https://huggingface.co/ku-nlp/deberta-v2-base-japanese), [large](https://huggingface.co/ku-nlp/deberta-v2-large-japanese)) | 
| [UniversityOfTokyoDeBERTaV2](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | DeBERTaV2 (small, base) | Wikipédia en japonais, Japanese Wikinews, Japanese CC-100, Japanese mC4, Japanese OSCAR<br>(En outre, pré-entraîné avec des résumés en japonais de résultats financiers, de rapports sur les valeurs mobilières et d'articles de presse pour le modèle de base) | University of Tokyo Izumi Lab | CC BY-SA 4.0 | ◯ ([small](https://huggingface.co/izumi-lab/deberta-v2-small-japanese), [base](https://huggingface.co/izumi-lab/deberta-v2-base-japanese)) | 
| [JapaneseBigBird](https://huggingface.co/nlp-waseda/bigbird-base-japanese) | BigBird (base) | Wikipédia en japonais, Japanese CC&#x2011;100, Japanese OSCAR | Waseda Kawahara Lab | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/nlp-waseda/bigbird-base-japanese) |

<a id="autoencoding-domain-specific"></a>
### Spécifique à un domaine

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
| [JapaneseNewsBERT](https://qiita.com/mkt3/items/3c1278339ff1bcc0187f) | BERT (base) | Articles sur l'économie en japonais(3M articles) | Stockmark | CC BY 4.0 | △ |
| [JapaneseNewsXLNet](https://qiita.com/mkt3/items/4d0ae36f3f212aee8002) |  XLNet (base) | Articles sur l'économie en japonais (3M articles) | Stockmark | ？ | [◯](https://huggingface.co/hajime9652/xlnet-japanese) <br> ※ Version non officielle |
| [JapaneseNewsALBERT](https://qiita.com/mkt3/items/b41dcf0185e5873f5f75) | ALBERT (base) | Articles sur l'économie en japonais (3M articles) | Stockmark | ？ | △ |
| [Laboro BERT](https://laboro.ai/activity/column/engineer/laboro-bert/) | BERT (base, large) | Corpus web en japonais <br> (Actualités, blogs, etc) (12GB) | Laboro.AI | CC BY&#x2011;NC 4.0 | ✕ |
| [Laboro DistilBERT](https://laboro.ai/activity/column/engineer/laboro-distilbert/) | DistilBERT |  (Distillation of Laboro BERT(base)) | Laboro.AI | CC BY&#x2011;NC 4.0 | [◯](https://huggingface.co/laboro-ai/distilbert-base-japanese) |
| [JapaneseBlogELECTRA](https://www.anlp.jp/proceedings/annual_meeting/2022/pdf_dir/E2-5.pdf) | ELECTRA (small) | Corpus de blogs en japonais (354M sentences)  | Université de technologie de Kitami - Laboratoire de Masui-Ptaszynski | CC BY&#x2011;SA 4.0 | [◯](https://huggingface.co/ptaszynski/yacis-electra-small-japanese)  |
| [JapaneseSpokenLanguageBERT](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) | BERT (base) | Formation supplémentaire pour TohokuUniversityBERT en utilisant le Corpus of Spontaneous Japanese (CSJ)<br> (Dans le modèle DAPT, le compte rendu de la diète est également utilisé) | Retrieva | Apache 2.0 | [◯](https://huggingface.co/retrieva-jp/japanese-spoken-language-bert) |
| [JapaneseFinancialBERT](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | BERT (small, base)[^9] | Wikipédia en japonais, Japanese Financial Corpus (27M sentences/5.2GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |◯<br>([small](https://huggingface.co/izumi-lab/bert-small-japanese-fin), [base](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional)) |
| [JapaneseFinancialELECTRA](https://sites.google.com/socsim.org/izumi-lab/tools/language-model) | ELECTRA (small) | Wikipédia en japonais (20M sentences/2.9GB), Japanese Financial Corpus (27M sentences/5.2GB) | Université de Tokyo Izumi Lab | CC BY&#x2011;SA 4.0 |  [◯](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator) |
| [UTH-BERT](https://ai-health.m.u-tokyo.ac.jp/home/research/uth-bert) | BERT (base) | Dossiers médicaux en japonais (120M lignes) | Université de Tokyo Hôpital <br>Cours de développement en IA pour la médecine | CC BY&#x2011;NC&#x2011;SA 4.0 | △ |
| [medBERTjp](https://github.com/ou-medinfo/medbertjp) | BERT (base) | Wikipédia en japonais, Corpus médical en japonais ("今日の診療プレミアム/Today's Care Premium" Web Version) | Université d'Osaka Hôpital <br> Laboratoire d'information médicale | CC BY&#x2011;NC&#x2011;SA 4.0 | △ |
| [JMedRoBERTa](https://www.anlp.jp/proceedings/annual_meeting/2023/pdf_dir/P3-1.pdf) | RoBERTa (base) | Japanese Medical Papers (11M sentences/1.8GB) | Université de Tokyo Aizawa Lab | CC BY&#x2011;NC&#x2011;SA 4.0 | ◯<br>([ManbyoWordPiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece), [SentencePiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece))[^10] |
| [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | RoBERTa (base) | CiNii Japanese Papers (6.3M sentences) | Université d'Ehime Laboratoire IA | Apache 2.0 | [◯](https://huggingface.co/EhimeNLP/AcademicRoBERTa) |

<a id="embeddings"></a>
## Plongement lexical par mots et par documents

|    | Architecture |  Développeur  |  Licence | 
|:---|:---:|:---:|:---:|
| [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) | Sentence-BERT | Colorful Scoop | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/SBERT-JSNLI-base](https://huggingface.co/MU-Kindai/SBERT-JSNLI-base)<br>[MU-Kindai/SBERT-JSNLI-large](https://huggingface.co/MU-Kindai/SBERT-JSNLI-large) | Sentence-BERT | Université de Kindai | ？ |
| [MU-Kindai/Japanese-SimCSE-BERT-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-unsup)<br>[MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-RoBERTa-base-unsup)<br>[MU-Kindai/Japanese-SimCSE-BERT-base-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-base-sup)<br>[MU-Kindai/Japanese-SimCSE-BERT-large-sup](https://huggingface.co/MU-Kindai/Japanese-SimCSE-BERT-large-sup) | SimCSE | Université de Kindai | MIT |
| [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) | SimCSE | PKSHA Technology | CC BY&#x2011;SA 4.0 |
| [cl-nagoya/unsup-simcse-ja-base](https://huggingface.co/cl-nagoya/unsup-simcse-ja-base)<br>[cl-nagoya/unsup-simcse-ja-large](https://huggingface.co/cl-nagoya/unsup-simcse-ja-large)<br>[cl-nagoya/sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base)<br>[cl-nagoya/sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large) | SimCSE | Université de Nagoya - Takeda-Sasano Group | CC BY&#x2011;SA 4.0 |
| [MU-Kindai/Japanese-MixCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-base)<br>[MU-Kindai/Japanese-MixCSE-BERT-large](https://huggingface.co/MU-Kindai/Japanese-MixCSE-BERT-large) | MixCSE | Université de Kindai | MIT |
| [MU-Kindai/Japanese-DiffCSE-BERT-base](https://huggingface.co/MU-Kindai/Japanese-DiffCSE-BERT-base) | DiffCSE | Université de Kindai | MIT | 
| [pkshatech/GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) | Modèle de plongement lexical basé sur  LUKE | PKSHA Technology | Apache 2.0 |

<a id="multimodal"></a>
## Modèles Vision-Language

<a id="multimodal-text-generation"></a>
### Multimodal vers texte

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Japanese Stable VLM](https://ja.stability.ai/blog/japanese-stable-vlm) | LLaVA-1.5 | Japanese CC12M, STAIR Captions, jeu de données Japanese Visual Genome VQA | Stability AI | STABILITY AI JAPANESE STABLE VLM COMMUNITY LICENSE | [◯](https://huggingface.co/stabilityai/japanese-stable-vlm) |
| [Heron](https://github.com/turingmotors/heron) | BLIP / GIT | LLaVA-Instruct-150K-JA, Japanese STAIR Captions, jeu de données Japanese Visual Genome VQA | Turing | CC BY&#x2011;NC 4.0 | ◯<br>([blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0), [git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0), [git-ELYZA-fast-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ELYZA-fast-7b-v0)) |
| [Japanese InstructBLIP Alpha](https://stability.ai/blog/announcing-japanese-instructblip-alpha) | InstructBLIP | Japanese CC12M, STAIR Captions, jeu de données Japanese Visual Genome VQA | Stability AI | JAPANESE STABLELM RESEARCH LICENSE |  [◯](https://huggingface.co/stabilityai/japanese-instructblip-alpha) |
| [rinna MiniGPT-4](https://rinna.co.jp/news/2023/07/20230731.html)[^11] | MiniGPT-4 | CC12M, COCO 2014, Visual Genome, STAIR Captions, Japanese Visual Genome VQA dataset | rinna | MIT | [◯](https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4) |

<a id="multimodal-others"></a>
### Autres

|    |  Architecture  |  Données d'entraînement  |  Développeur  | Licence | HuggingFace? |
|:---|:---:|:---:|:---:|:---:|:---:|
| [Japanese Stable CLIP](https://ja.stability.ai/blog/japanese-stable-clip) | SigLIP | CC12M traduit en japonais, STAIR Captions | Stability AI | STABILITY AI JAPANESE STABLE CLIP COMMUNITY LICENSE | [◯](https://huggingface.co/stabilityai/japanese-stable-clip-vit-l-16) |
| [rinna CLIP](https://rinna.co.jp/news/2022/05/20220512.html) | CLIP | CC12M traduit en japonais | rinna | Apache 2.0 | [◯](https://huggingface.co/rinna/japanese-clip-vit-b-16) |
| [rinna CLOOB](https://rinna.co.jp/news/2022/05/20220512.html) | CLOOB | CC12M traduit en japonais | rinna | Apache 2.0 | [◯](https://huggingface.co/rinna/japanese-cloob-vit-b-16) |
| [Japanese Stable Diffusion XL](https://ja.stability.ai/blog/japanese-stable-diffusion-xl) | Stable Diffusion | Inconnu | Stability AI | STABILITY AI JAPANESE STABLE DIFFUSION XL COMMUNITY LICENSE | [◯](https://huggingface.co/stabilityai/japanese-stable-diffusion-xl) | 
| [TohokuUniversity Stable Diffusion](https://huggingface.co/cl-tohoku/stable-diffusion-xl-jp-base-1.0) | Stable Diffusion | Corpus parallèle anglais-japonais de la tâche partagée WMT2023, environ 13 millions de légendes de laion2B-multi | Université de Tohoku - Groupe TAL | CreativeML OpenRAIL-M License | ◯ ([base](https://huggingface.co/cl-tohoku/stable-diffusion-xl-jp-base-1.0), [refiner](https://huggingface.co/cl-tohoku/stable-diffusion-xl-jp-refiner-1.0)) | 
| [rinna Stable Diffusion](https://rinna.co.jp/news/2022/09/20220909.html) | Stable Diffusion | LAION-5B Japanese Subset (100M images) | rinna | CreativeML OpenRAIL-M License | [◯](https://huggingface.co/rinna/japanese-stable-diffusion) |

<a id="benchmark-suites"></a>
## Standard d'évaluation pour les LLM en japonais

#### Référence traditionnelle basé sur des tâches de Compréhension du langage naturel (NLU)

- [llm-jp-eval Leaderboard](http://wandb.me/llm-jp-leaderboard) (LLM-jp)
  - Classement basé sur les résultats du script [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) qui évalue automatiquement les LLM japonais sur plusieurs ensembles de données. Dès la sortie de LLM-jp-13B, [Jamp](https://github.com/tomo-ut/temporalNLI_dataset), [JaNLI](https://github.com/verypluming/JaNLI), [JCommonsenseQA](https://github.com/yahoojapan/JGLUE), [JEMHopQA](https://github.com/aiishii/JEMHopQA), [JNLI](https://github.com/yahoojapan/JGLUE), [JSeM](https://github.com/DaisukeBekki/JSeM), [JSICK](https://github.com/verypluming/JSICK), [JSQuAD](https://github.com/yahoojapan/JGLUE), [JSTS](https://github.com/yahoojapan/JGLUE), et [NIILC](https://github.com/mynlp/niilc-qa) sont utilisés comme jeu de données d'évaluation.
- [JGLUE](https://github.com/yahoojapan/JGLUE) (Université de Waseda Laboratoire Kawahara et Yahoo)
  - Version japonais de [GLUE](https://gluebenchmark.com/) référence suite, avec les tâches MARC-ja, JCoLA, JSTS, JNLI, JSQuAD, et JCommonsenseQA. [JCoLA](https://github.com/osekilab/JCoLA) vient du laboratoire d'Oseki de l'université de Tokyo. Voir [ici](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.317.pdf) and [here (ja only)](https://techblog.yahoo.co.jp/entry/2022122030379907/) pour plus d'informations sur chaque tâches.
- [JP Language Model Evaluation Harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) (Stability AI)
  - Fork de [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) cela ajoute des tâches en japonais comme JGLUE et d'autres.
  - Un résumé d'évaluation détaillé par rinna est disponible: [[rinna] Benchmark of Stability-AI/lm-evaluation-harness](https://rinnakk.github.io/research/benchmarks/lm/)
- [Nejumi LLM Leaderboard](https://wandb.ai/wandb/LLM_evaluation_Japan/reports/LLM-JGLUE---Vmlldzo0NTUzMDE2?accessToken=u1ttt89al8oo5p5j12eq3nldxh0378os9qjjh14ha1yg88nvs5irmuao044b6eqa) (Weights & Biases)
  - Classement basé sur la performance de JGLUE en zero-shot.

#### Standard des tâches génératives ouvertes

- [Rakuda Benchmark](https://yuzuai.jp/benchmark) (YuzuAI)
  - Classement basé sur les réponses des modèles avec [40 questions ouvertes](https://huggingface.co/datasets/yuzuai/rakuda-questions) la géographie, l'histoire, la politique, et la société japonaise. Utilise GPT-4 pour évaluer les résultats du modèle par paires, puis classe les modèles en ajustant le maximum de vraisemblance sur le modèle de probabilité d'Elo/Bradley-Terry avec les préférences de GPT-4. Voir [ici](https://github.com/yuzu-ai/japanese-llm-ranking) pour les données et le code utilisé afin de générer le classement [ici](https://yuzuai.jp/blog/rakuda) pour obtenir davantage d'explications.
- [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) (ELYZA)
  - Classement basé sur les réponses des modèles avec [100 tâches complexes et diverses](https://huggingface.co/datasets/elyza/ELYZA-tasks-100), y compris les tâches testant la synthèse, la correction, l'abstraction, l'induction et d'autres compétences. Utilise des humains pour noter les réponses du modèle, puis classe les modèles en fonction de leurs scores moyens. Voir [ici](https://docs.google.com/spreadsheets/d/1mtoy4QAqDPk2f_B0vDogFoOrbA5G42DBEEHdqM4VmDI/edit#gid=1023787356) pour les données utilisées pour générer le classement et [ici](https://zenn.dev/elyza/articles/5e7d9373c32a98) pour obtenir davantage d'explications.
- [Japanese MT-bench](https://github.com/Stability-AI/FastChat/tree/jp-stable/fastchat/llm_judge) (Stability AI)
  - Version japonaise du [MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) qui interroge sur la capacité à converser en plusieurs tournures. Il inclut 80 questions, 10 de chacune des 8 catégories : écriture, jeu de rôle, raisonnement, maths, codage, extraction, STEM, sciences humaines. Certaines questions ont été modifiées pour s'adapter à la culture japonaise lors de la création de la version japonaise. Il comprend également un script qui réalise une évaluation absolue en 10 niveaux par GPT-4. Les résultats de l'évaluation sont détaillés dans l'article récapitulatif suivant de shi3z: "[無償LLM 日本語能力ベンチマークまとめ](https://note.com/shi3zblog/n/n6b2ac5874021)"
- [Japanese Vicuna QA Benchmark](https://github.com/hitoshizuku7/ja-vicuna-qa-benchmark) (Université de Kyoto Laboratoire de traitement des langues et des médias)
  - Il s'agit de la version japonaise de [vicuna-blog-eval](https://github.com/lm-sys/vicuna-blog-eval), qui est le précurseur de MT-Bench. Il comprend 80 questions sur la connaissance générale, le jeu de rôle, le bon sens, l'estimation de Fermi, la pensée contrefactuelle, le codage, les mathématiques, et l'écriture. Il comprend également un script pour une évaluation automatique par GPT-4 (calcul du taux de victoire).
- [Stockmark Business Questions](https://huggingface.co/datasets/stockmark/business-questions) (Stockmark)
  - La collection comprend 50 questions qui approfondissent les connaissances sur des sujets tels que les tendances du marché, l'actualité, les problèmes sociaux et les tendances commerciales.

<a id="reference"></a>
## Références par architecture des modèles

| Architecture | Date | Meeting/Journal | Papier |
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
| ELECTRA | 2020.03.23 | ICLR 2020 | [ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators](https://arxiv.org/abs/2003.10555) |
| GPT-3 | 2020.05.28 | NeurIPS 2020 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) |
| DeBERTa | 2020.06.05 | ICLR 2021 | [DeBERTa: Decoding-enhanced BERT with Disentangled Attention](https://arxiv.org/abs/2006.03654) |
| BigBird | 2020.07.28 | NeurIPS 2020 | [Big Bird: Transformers for Longer Sequences](https://arxiv.org/abs/2007.14062) |
| LUKE | 2020.10.02 | EMNLP 2020 | [LUKE: Deep Contextualized Entity Representations with Entity-aware Self-attention](https://aclanthology.org/2020.emnlp-main.523/) |
| CLIP | 2021.02.26 | ICML 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) |
| SimCSE | 2021.04.18 | EMNLP 2021 | [SimCSE: Simple Contrastive Learning of Sentence Embeddings](https://aclanthology.org/2021.emnlp-main.552/) |
| RoFormer | 2021.04.20 | - | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864) |
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
| InstructBLIP | 2023.05.11 | - | [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://arxiv.org/abs/2305.06500) |
| RWKV | 2023.05.22 | - | [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048) |
| Llama 2 | 2023.07.18 | - | [Llama 2: Open Foundation and Fine-Tuned Chat Models](https://arxiv.org/abs/2307.09288) |
| LLaVA-1.5 | 2023.10.05 | - | [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) |

<a id="contributors"></a>
## Nos contributeurs

Nous aimons les contributeurs ! N'hésitez pas à contribuer à ce projet.

<a href="https://github.com/llm-jp/awesome-japanese-llm/graphs/contributors">
  <img src="figures/contributors.svg" />
</a>

---

[^1]: Certaines améliorations de performances ont été apportées au modèle Llama original. Voir [ici](https://tech.preferred.jp/ja/blog/llm-plamo/) pour plus détails.

[^2]: Les détails n'ont pas été rendus publics, mais l'ensemble de données privé comprend des jeux de données de l'équipe japonaise du projet EleutherAI Polyglot et des membres de Stable Community Japan.

[^3]: Ce projet a mené des recherches d'évaluation sur l'utilisation de la génération de droite à gauche au lieu de la génération habituelle de gauche à droite, en publiant des modèles de gauche à droite et de droite à gauche.

[^4]: ○: Le modèle se trouve sur le Model Hub d'HuggingFace et peut être chargé avec la commande `AutoModel.from_pretrained()` . △: Le modèle ne se trouve pas sur le Model Hub mais peut être chargé manuellement avec la bibliothèque de transformateurs HuggingFace. ✕: Le modèle ne se charge pas avec HuggingFace.

[^5]: Développement réalisé par [Hiroyuki Osone](https://soneo1127.github.io/) avec la coopération de [AI Buncho](https://bun-cho.work/).

[^6]: Ce projet a mené des recherches d'évaluation sur l'analyse morphologique avant la tokenisation et a publié son modèle le plus performant, qui utilisait Juman++ et BPE.

[^7]: nlp-waseda/roberta-base-japanese et nlp-waseda/roberta-large-japanese entrainé avec une longueur de context 128 token, mais nlp-waseda/roberta-large-japanese-seq512 étendu la longueur du contexte à 512.

[^8]: Étendu la longueur du contexte de 128 à 512.

[^9]: Le modèle "Small" s'entraîne sur Wikipédia japonais et le Corpus financier japonais simultanément, tandis que le modèle "Base" prend le TohokuUniversityBERT et dispense un apprentissage supplémentaire sur le Corpus financier japonais.

[^10]: ManbyoWordPiece lance une étape de prétokenization en utilisant MeCab (IPA+Manbyo dictionaries), puis utilise WordPiece pour la tokenization sous-mots, pendant que le modèle SentencePiece segmente le texte directement en utilisant un modèle unigram.

[^11]: Voir "[Japanese MiniGPT-4: rinna 3.6bとBLIP-2を組み合わせてマルチモーダルチャットのモデルを作る](https://zenn.dev/rinna/articles/5fad41e3f2a401)" pour plus de détails. L'article parle de l'utilisation de rinna/japanese-gpt-neox-3.6b comme un composant du LLM plutôt que du modèle rinna/bilingual-gpt-neox-4b comme MiniGPT-4 réellement utilisé.