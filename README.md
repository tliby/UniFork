# UniFork: Exploring Modality Alignment for Unified Multimodal Understanding and Generation

<p align="left">
  <a href="https://arxiv.org/abs/2506.17202">
    <img
      src="https://img.shields.io/badge/UniFork-Paper-red?logo=arxiv&logoColor=red"
      alt="BAGEL Paper on arXiv"
    />
  </a>
</p>


Official implementation of UniFork: Exploring Modality Alignment for Unified Multimodal Understanding and Generation

[Teng Li](https://scholar.google.com/citations?user=U38Pk_kAAAAJ&hl=en), [Quanfeng Lu](https://lqf-hfnju.github.io/), Lirui Zhao, [Hao Li](https://cpsxhao.github.io/), [Xizhou Zhu](https://scholar.google.com/citations?user=02RXI00AAAAJ&hl=en), [Yu Qiao](https://mmlab.siat.ac.cn/yuqiao), [Jun Zhang](https://eejzhang.people.ust.hk/), [Wenqi Shao](https://wqshao126.github.io/)



## Updates

- [2025/06/20] We release the training, inference and evaluation codes of UniFork.

## Introduction

This paper presents UniFork, a Y-shaped architecture for unified image generation and understanding:

- We analyze task-specific modality alignment patterns in expert models, highlighting the differing needs of image understanding and generation, and providing insights for unified model design.

  ![analysis](assets/analysis.png)

- We propose UniFork, a Y-shaped architecture that decouples task-specific learning in the later layers while retaining shared semantic representation learning in the early layers. This design enables cross-task learning and alleviates performance conflicts between tasks.

  <img src="assets/method.png" alt="method" style="zoom: 20%;" />

## Installation

### Environment setup

```bash
git clone https://github.com/tliby/UniFork.git
cd UniFork
conda create -n unifork python=3.10
conda activate unifork
pip install -r requirements.txt
```

### Install pretrained models for training

Our code is based on Qwen2.5-0.5B LLM and VILA-U-256 tokenizer. Please download the pretrained weights:

- [Qwen2.5-0.5B LLM](https://huggingface.co/Qwen/Qwen2.5-0.5B)
- [VILA-U-256 tokenizer](https://huggingface.co/mit-han-lab/vila-u-7b-256/tree/main/vision_tower)

We have modified the tokenizer configuration with [`configs/config.json`](configs/config.json) to adjust the size of the image head. You can replace the default tokenizer config with this file before launching training.

### Prepare training datasets

The training Stage1 of UniFork is conducted on the following datasets:

- [ImageNet-1K](https://www.image-net.org/)
- [Laion-En](https://laion.ai/blog/laion-5b/)
- [COYO](https://huggingface.co/datasets/kakaobrain/coyo-700m)

By default, our pipeline expects the annotation for each dataset to be organized as a folder containing `.jsonl` or `.txt` files. To use your own dataset, you should modify the dataset loading logic in [`unifork/train/data_utils.py`](unifork/train/data_utils.py).

## Training

We provide all the scripts in [`scripts/train`](scripts/train). Suppose you have access to a SLURM clsuter, you can run the following command to start training:

```
sbatch scripts/train/s1_imagenet.sh
```

## Inference

Once the training is complete, you can run inference using the following command:

### Image generation

```
python infer_t2i.py \
    --model-path /path/to/model \
    --prompt "your prompt"
```

### Image understanding

```
python infer_mmu.py \
    --model_path /path/to/model \
    --image-path /path/to/your/image \
    --query "your query"
```

## Evaluation

### Image generation

We provide sampling scripts for the MJHQ-30K and Geneval benchmarks. Your need to download the annotation file: \[[Geneval prompt](https://github.com/djghosh13/geneval/blob/main/prompts/evaluation_metadata.jsonl)] [[MJHQ-30K prompt](https://huggingface.co/datasets/playgroundai/MJHQ-30K/blob/main/meta_data.json)]. Then run following command:

```
python scripts/eval_gen/sample_geneval_batch.py \
    --model-path /path/to/model \
    --metadata-file geneval/<PROMPT_FOLDER>/evaluation_metadata.jsonl \
    --outdir geneval/<IMAGE_FOLDER>
```

After generation, clone the [[Geneval](https://github.com/djghosh13/geneval/)] repo and follow their instructions to compute accuracy-based metrics.

```
python scripts/eval_gen/sample_mjhq_batch.py \
    --model-path /path/to/model \
    --metadata-file mjhq-30k/meta_data.json \
    --outdir output/generated_samples_mjhq
```

After generation, download the [[MJHQ-30K images](https://huggingface.co/datasets/playgroundai/MJHQ-30K/blob/main/mjhq30k_imgs.zip)], clone the [[pytorch-fid](https://github.com/mseitzer/pytorch-fid)] repo and follow their instructions to compute fid score.

### Image Understanding

Our evaluation framework is based on the [[LLaVA](https://github.com/haotian-liu/LLaVA/blob/main/docs/Evaluation.md)] codebase. We provide scripts on common benchmarks:

```bash
bash scripts/eval_und/mme.sh
bash scripts/eval_und/pope.sh
bash scripts/eval_und/seed.sh
bash scripts/eval_und/vqav2.sh
```

For evaluation on more benchmarks, we recommend integrating your model into [[VLMEvalKit](https://github.com/open-compass/VLMEvalKit)], a comprehensive evaluation toolkit for vision-language models.

## Acknowledgement

Our code is built on [LLaVA](https://github.com/haotian-liu/LLaVA),  [LlamaGen](https://github.com/FoundationVision/LlamaGen) and [Qwen2.5](https://github.com/QwenLM/Qwen3). Thanks for their efforts!

## BibTeX

```
@article{li2025unifork,
  title={UniFork: Exploring Modality Alignment for Unified Multimodal Understanding and Generation},
  author={Li, Teng and Lu, Quanfeng and Zhao, Lirui and Li, Hao and Zhu, Xizhou and Qiao, Yu and Zhang, Jun and Shao, Wenqi},
  journal={arXiv preprint arXiv:2506.17202},
  year={2025}
}
```

