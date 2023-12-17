# <p align=center>`Awesome CLIP in Medical Imaging`</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

:fire::fire: This is a collection of awesome articles about CLIP in medical imaging:fire::fire:

- Our survey paper on arXiv: [CLIP in medical imaging: A comprehensive survey](https://arxiv.org/abs/2312.07353)

### Citation

```python
@article{zhao2023clip,
  title={CLIP in Medical Imaging: A Comprehensive Survey},
  author={Zihao Zhao and Yuxiao Liu and Han Wu and Yonghao Li and Sheng Wang and Lin Teng and Disheng Liu and  Zhiming Cui and Qian Wang and Dinggang Shen},
  journal={arXiv preprint arXiv:2312.07353},
  year={2023},
}
```

## Overview

- [`Awesome CLIP in Medical Imaging`](#awesome-clip-in-medical-imaging)
  - [Citation](#citation)
  - [Overview](#overview)
  - [Updates](#updates)
  - [Dataset Resource](#dataset-resource)
  - [Pre-training](#pre-training)
    - [Multi-scale](#multi-scale)
    - [Data-efficient](#data-efficient)
    - [Knowledge-enhanced](#knowledge-enhanced)
    - [Others](#others)
  - [CLIP-driven Application](#clip-driven-application)
    - [Classification](#classification)
    - [Dense Prediction](#dense-prediction)
    - [Cross-modal](#cross-modal)

## Updates

- **ArXiv preprint release:** December 13, 2023
- **Github repo release:** December 12, 2023

---

## Dataset Resource

|                                       dataset                                        |  domain   | image | text |             source              | language | pre-trained CLIP |
| :----------------------------------------------------------------------------------: | :-------: | :---: | :--: | :-----------------------------: | :------: | :--------------: |
|                   [ROCO](https://github.com/razorx89/roco-dataset)                   | multiple  |  87K  | 87K  |         research papers         |    En    |    PubMedCLIP    |
|                    [MedICaT](https://github.com/allenai/medicat)                     | multiple  | 217K  | 217K |         research papers         |    En    |        /         |
|               [PMC-OA](https://huggingface.co/datasets/axiong/pmc_oa)                | multiple  | 1.6M  | 1.6M |         research papers         |    En    |     PMCCLIP      |
|          [ChiMed-VL](https://huggingface.co/datasets/williamliu/ChiMed-VL)           | multiple  | 580K  | 580K |         research papers         |  En/zh   |        /         |
|                     [FFA-IR](https://github.com/mlii0117/FFA-IR)                     |  fundus   |  1M   | 10K  |         medical reports         |  En/zh   |        /         |
|              [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/)              |    cxr    | 160K  | 109K |         medical reports         |    Sp    |        /         |
|             [MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.0.0/)              |    cxr    | 377K  | 227K |         medical reports         |    En    | BioViL/BioViL-T  |
| [OpenPath](https://drive.google.com/drive/folders/1b5UT8BzUphkHZavRG-fmiyY9JWYIWZER) | histology | 208K  | 208K |          social media           |    En    |       PLIP       |
|                        [Quilt-1M](https://quilt1m.github.io/)                        | histology |  1M   |  1M  | research papers<br>social media |    En    |     QuiltNet     |

---

## Pre-training

### Multi-scale

[**MICCAI 2020**] Joint Modeling of Chest Radiographs and Radiology Reports for Pulmonary Edema Assessment \
_Geeticka Chauhan, Ruizhi Liao, William Wells, Jacob Andreas, Xin Wang, Seth Berkowitz, Steven Horng, Peter Szolovits, Polina Golland_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-030-59713-9_51)] [[code](https://github.com/RayRuizhiLiao/joint_chestxray)]

[**ICCV 2021**] GLoRIA: A Multimodal Global-Local Representation Learning Framework for Label-efficient Medical Image Recognition \
_Shih-Cheng Huang, Liyue Shen, Matthew P. Lungren, Serena Yeung_ \
[[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Huang_GLoRIA_A_Multimodal_Global-Local_Representation_Learning_Framework_for_Label-Efficient_Medical_ICCV_2021_paper.html)] [[code](https://github.com/marshuang80/gloria)]

[**MICCAI 2021**] Multimodal Representation Learning via Maximization of Local Mutual Information \
_Ruizhi Liao, Daniel Moyer, Miriam Cha, Keegan Quigley, Seth Berkowitz, Steven Horng, Polina Golland, and William M. Wells_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-030-87196-3_26)]

[**ECCV 2022**] Joint Learning of Localized Representations from Medical Images and Reports \
_Philip Müller, Georgios Kaissis, Congyu Zou, Daniel Rückert_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-19809-0_39)] [[code](https://github.com/philip-mueller/lovt)]

[**ECCV 2022**] Making the Most of Text Semantics to Improve Biomedical Vision–Language Processing \
_Benedikt Boecking, Naoto Usuyama, Shruthi Bannur, Daniel C. Castro, Anton Schwaighofer, Stephanie Hyland, Maria Wetscherek, Tristan Naumann, Aditya Nori, Javier Alvarez-Valle, Hoifung Poon, and Ozan Oktay_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-20059-5_1)] [[code](https://hi-ml.readthedocs.io/en/latest/multimodal.html)]

[**NeurIPS 2022 Workshop**] The Role of Local Alignment and Uniformity in Image-Text Contrastive Learning on Medical Images \
_Philip Müller, Georgios Kaissis, Daniel Rueckert_ \
[[paper](https://sslneurips22.github.io/pages/accepted-paper.html)]

[**MICCAI 2022**] Breaking with Fixed Set Pathology Recognition through Report-Guided Contrastive Training \
_Constantin Seibold, Simon Reiß, M. Saquib Sarfraz, Rainer Stiefelhagen, Jens Kleesiek_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16443-9_66)]

[**MICCAI 2022**] Vision-Language Contrastive Learning Approach to Robust Automatic Placenta Analysis Using Photographic Images \
_Yimu Pan, Alison D. Gernand, Jeﬀery A. Goldstein, Leena Mithal, Delia Mwinyelle, James Z. Wang_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16437-8_68)]

[**ICLR 2023**] Advancing Radiograph Representation Learning with Masked Record Modeling \
_Hong-Yu Zhou, Chenyu Lian, Liansheng Wang, Yizhou Yu_ \
[[paper](https://openreview.net/forum?id=w-x7U26GM7j)] [[code](https://github.com/RL4M/MRM-pytorch)]

[**ICCV 2023**] LIMITR: Leveraging Local Information for Medical Image-Text Representation \
_Gefen Dawidowicz, Elad Hirsch, Ayellet Tal_ \
[[paper](https://arxiv.org/abs/2303.11755)]

[**ICCV 2023**] PRIOR: Prototype Representation Joint Learning from Medical Images and Reports \
_Pujin Cheng, Li Lin, Junyan Lyu, Yijin Huang, Wenhan Luo, Xiaoying Tang_ \
[[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Cheng_PRIOR_Prototype_Representation_Joint_Learning_from_Medical_Images_and_Reports_ICCV_2023_paper.html)] [[code](https://github.com/QtacierP/PRIOR)]

[**MICCAI 2023**] Contrastive Masked Image-Text Modeling for Medical Visual Representation Learning \
_Cheng Chen, Aoxiao Zhong, Dufan Wu, Jie Luo, Quanzheng Li_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43904-9_48)] [[code](https://github.com/cchen-cc/CMITM)]

[**MICCAI 2023**] Enhancing Automatic Placenta Analysis through Distributional Feature Recomposition in Vision-Language Contrastive Learning \
Yimu Pan, Tongan Cai, Manas Mehta, Alison D. Gernand, Jeﬀery A. Goldstein, Leena Mithal, Delia Mwinyelle, Kelly Gallagher, James Z. Wang \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43987-2_12)]

[**MLHC 2023**] TIER: Text-Image Entropy Regularization for Medical CLIP-style models \
_Anil Palepu, Andrew Beam_ \
[[paper](https://arxiv.org/abs/2212.06710)] [[code](https://github.com/apalepu13/TIER_Regularized_CLIP)]

[**EMNLP 2023**] Fine-grained Medical Vision-Language Representation Learning for Radiology Report Generation \
_Siyuan Wang, Bo Peng, Yichao Liu, Qi Peng_ \
[[paper](https://aclanthology.org/2023.emnlp-main.989/)]

[**MedIA 2023**] Self-supervised multi-modal training from uncurated images and reports enables monitoring AI in radiology \
_Sangjoon Park, Eun Sun Lee, Kyung Sook Shin, Jeong Eun Lee, Jong Chul Ye_ \
[[paper](https://www.sciencedirect.com/science/article/abs/pii/S1361841523002815)]

[**TMM 2023**] Multi-task Paired Masking with Alignment Modeling for Medical Vision-Language Pre-training \
_Ke Zhang, Yan Yang, Jun Yu, Hanliang Jiang, Jianping Fan, Qingming Huang, Weidong Han_ \
[[paper](https://ieeexplore.ieee.org/abstract/document/10288259)]

[**ESA 2023**] MITER: Medical Image–TExt joint adaptive pretRaining with multi-level contrastive learning \
_Chang Shu, Yi Zhu, Xiaochu Tang, Jing Xiao, Youxin Chen, Xiu Li, Qian Zhang, Zheng Lu_ \
[[paper](https://www.sciencedirect.com/science/article/pii/S0957417423020286)] [[code](https://github.com/ZhuYi98/MITER)]

[**arXiv 2023**] Local Contrastive Learning for Medical Image Recognition \
_Syed A. Rizvi, Ruixiang Tang, Xiaoqian Jiang, Xiaotian Ma, Xia Hu_ \
[[paper](https://arxiv.org/abs/2303.14153)]

[**arXiv 2023**] G2D: From Global to Dense Radiography Representation Learning via
Vision-Language Pre-training \
_Che Liu, Cheng Ouyang, Sibo Cheng, Anand Shah, Wenjia Bai, Rossella Arcucci_ \
[[paper](https://arxiv.org/abs/2312.01522)]

[**arXiv 2023**] Fine-Grained Image-Text Alignment in Medical Imaging
Enables Cyclic Image-Report Generation \
_Wenting Chen, Xiang Li, Linlin Shen, Yixuan Yuan_ \
[[paper](https://arxiv.org/abs/2312.08078)]

---

### Data-efficient

[**EMNLP 2022**] MedCLIP: Contrastive Learning from Unpaired Medical Images and Text \
_Zifeng Wang, Zhenbang Wu, Dinesh Agarwal, Jimeng Sun_ \
[[paper](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiwuqrXjvWCAxWriVYBHR8TCN8QFnoECAsQAQ&url=https%3A%2F%2Faclanthology.org%2F2022.emnlp-main.256.pdf&usg=AOvVaw0Ph_QYrWg8OUoQBvfvSXoq&opi=89978449)] [[code](https://github.com/RyanWangZf/MedCLIP)]

[**NeurIPS 2022**] Multi-Granularity Cross-modal Alignment for Generalized Medical Visual Representation Learning \
_Fuying Wang, Yuyin Zhou, Shujun Wang, Varut Vardhanabhuti, Lequan Yu_ \
[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/d925bda407ada0df3190df323a212661-Abstract-Conference.html)] [[code](https://github.com/HKU-MedAI/MGCA)]

[**ISBRA 2023**] TCSA: A Text-Guided Cross-View Medical Semantic Alignment Framework for Adaptive Multi-view Visual Representation Learning \
_Hongyang Lei, Huazhen Huang, Bokai Yang, Guosheng Cui, Ruxin Wang, Dan Wu , and Ye Li_ \
[[paper](https://link.springer.com/chapter/10.1007/978-981-99-7074-2_11#auth-Hongyang-Lei)]

[**CVPR 2023**] Learning to Exploit Temporal Structure for Biomedical Vision–Language Processing \
_Shruthi Bannur,∗ Stephanie Hyland∗, Qianchu Liu, Fernando P ́ erez-Garc ́ıa, Maximilian Ilse, Daniel C. Castro, Benedikt Boecking, Harshita Sharma, Kenza Bouzid, Anja Thieme, Anton Schwaighofer, Maria Wetscherek, Matthew P. Lungren, Aditya Nori Javier Alvarez-Valle, Ozan Oktay_ \
[[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Bannur_Learning_To_Exploit_Temporal_Structure_for_Biomedical_Vision-Language_Processing_CVPR_2023_paper.html)] [[code](https://github.com/microsoft/hi-ml/tree/main/hi-ml-multimodal)]

[**MICCAI 2023**] CXR-CLIP: Toward Large Scale Chest X-ray Language-Image Pre-training \
_Kihyun You, Jawook Gu, Jiyeon Ham, Beomhee Park, Jiho Kim, Eun K. Hong, Woonhyuk Baek, Byungseok Roh_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43895-0_10)] [[code](https://github.com/kakaobrain/cxr-clip)]

[**TMI 2023**] Improving Medical Vision-Language Contrastive
Pretraining with Semantics-aware Triage \
_Bo Liu, Donghuan Lu, Dong Wei, Xian Wu, Yan Wang, Yu Zhang, Yefeng Zheng_ \
[[paper](https://ieeexplore.ieee.org/document/10182304)]

[**QIMS 2023**] SDA-CLIP: surgical visual domain adaptation using video and text labels \
_Yuchong Li, Shuangfu Jia, Guangbi Song, Ping Wang, Fucang Jia_ \
[[paper](https://qims.amegroups.org/article/view/117648/html)]

[**arXiv 2023**] UniBrain: Universal Brain MRI Diagnosis with Hierarchical Knowledge-enhanced Pre-training \
_Jiayu Lei, Lisong Dai, Haoyun Jiang, Chaoyi Wu, Xiaoman Zhang, Yao Zhang, Jiangchao Yao, Weidi Xie, Yanyong Zhang, Yuehua Li, Ya Zhang, Yanfeng Wang_ \
[[paper](https://arxiv.org/abs/2309.06828)] [[code](https://github.com/ljy19970415/UniBrain)]

[**arXiv 2023**] Unified Medical Image-Text-Label Contrastive Learning With Continuous Prompt \
_Yuhao Wang_ \
[[paper](https://arxiv.org/abs/2307.05920)]

[**arXiv 2023**] Significantly Improving Zero-Shot X-ray Pathology Classification via Fine-tuning Pre-trained Image-Text Encoders \
_Jongseong Jang∗, Daeun Kyung∗, Seung Hwan Kim, Honglak Lee, Kyunghoon Bae, Edward Choi_ \
[[paper](https://arxiv.org/abs/2212.07050)]

[**arXiv 2023**] IMITATE: Clinical Prior Guided Hierarchical Vision-Language Pre-training \
_Che Liu, Sibo Cheng, Miaojing Shi, Anand Shah, Wenjia Bai, Rossella Arcucci_ \
[[paper](https://arxiv.org/abs/2310.07355)]

---

### Knowledge-enhanced

[**ACM MM 2022**] Align, Reason and Learn: Enhancing Medical Vision-and-Language Pre-training with Knowledge \
_Zhihong Chen, Guanbin Li, Xiang Wan_ \
[[paper](https://arxiv.org/abs/2209.07118)] [[code](https://github.com/zhjohnchan/ARL)]

[**ICCV 2023**] MedKLIP: Medical Knowledge Enhanced Language-Image Pre-Training for X-ray Diagnosis \
_Chaoyi Wu, Xiaoman Zhang, Ya Zhang, Yanfeng Wang, Weidi Xie_ \
[[paper](https://arxiv.org/abs/2301.02228)] [[code](https://github.com/MediaBrain-SJTU/MedKLIP)]

[**MICCAI 2023**] Knowledge Boosting: Rethinking Medical Contrastive Vision-Language Pre-Training \
_Xiaofei Chen, Yuting He, Cheng Xue, Rongjun Ge, Shuo Li, Guanyu Yang_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_39)] [[code](https://github.com/ChenXiaoFei-CS/KoBo)]

[**Nature Communication 2023**] Knowledge-enhanced visual-language pre-training on chest radiology images \
_Xiaoman Zhang, Chaoyi Wu, Ya Zhang, WeidiXie & Yanfeng Wang_ \
[[paper](https://www.nature.com/articles/s41467-023-40260-7)] [[code](https://github.com/xiaoman-zhang/KAD)]

[**npj digital medicine 2023**] A medical multimodal large language model for future pandemics \
_Fenglin Liu, Tingting Zhu, Xian Wu, Bang Yang, Chenyu You, Chenyang Wang, Yefeng Zheng, Xu Sun, Yang Yang, Lei Clifton, David A. Clifton_ \
[[paper](https://www.nature.com/articles/s41746-023-00952-2)]

[**arXiv 2023**] Towards Medical Artificial General Intelligence via Knowledge-Enhanced Multimodal Pretraining \
_Bingqian Lin, Zicong Chen, Mingjie Li, Haokun Lin, Hang Xu, Yi Zhu, Jianzhuang Liu, Wenjia Cai, Lei Yang, Shen Zhao, Chenfei Wu, Ling Chen, Xiaojun Chang, Yi Yang, Lei Xing, Xiaodan Liang_ \
[[paper](https://arxiv.org/abs/2304.14204)] [[code](https://github.com/chenzcv7/MOTOR)]

[**arXiv 2023**] A Foundation LAnguage-Image model of the Retina (FLAIR): Encoding expert knowledge in text supervision \
_Julio Silva-Rodriguez, Hadi Chakor, Riadh Kobbi, Jose Dolz, Ismail Ben Ayed_ \
[[paper](https://arxiv.org/abs/2308.07898)] [[code](https://github.com/jusiro/FLAIR)]

---

### Others

[**MLHC 2022**] Contrastive Learning of Medical Visual Representations from Paired Images and Text \
_Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P. Langlotz_ \
[[paper](https://proceedings.mlr.press/v182/zhang22a.html)] [[code](https://github.com/edreisMD/ConVIRT-pytorch)]

[**NMI 2022**] Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports\
_Hong-Yu Zhou, Xiaoyu Chen, Yinghao Zhang, Ruibang Luo, Liansheng Wang, Yizhou Yu_ \
[[paper](https://www.nature.com/articles/s42256-021-00425-9)] [[code](https://github.com/funnyzhou/REFERS)]

[**ICCV 2023**] Towards Unifying Medical Vision-and-Language Pre-Training via Soft Prompts \
_Zhihong Chen, Benyou Wang, Shizhe Diao, Guanbin Li, Xiang Wan_ \
[[paper](https://arxiv.org/abs/2302.08958)] [[code](https://github.com/zhjohnchan/ptunifier)]

[**ICCV 2023**] Cross-Modal Translation and Alignment for Survival Analysis \
_Fengtao Zhou, Hao Chen_ \
[[paper](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi9ibPDn4SDAxUP_WEKHWVZB6kQFnoECA0QAw&url=https%3A%2F%2Fopenaccess.thecvf.com%2Fcontent%2FICCV2023%2Fpapers%2FZhou_Cross-Modal_Translation_and_Alignment_for_Survival_Analysis_ICCV_2023_paper.pdf&usg=AOvVaw0M39tXtqEkk3BQUCKASxwn&opi=89978449)] [[code](https://github.com/ft-zhou-zzz/cmta)]

[**NeurIPS 2023**] Med-UniC: Unifying Cross-Lingual Medical Vision-Language Pre-Training by Diminishing Bias \
_Zhongwei Wan, Che Liu, Mi Zhang, Jie Fu, Benyou Wang, Sibo Cheng, Lei Ma, César Quilodrán-Casas, Rossella Arcucci_ \
[[paper](https://arxiv.org/abs/2305.19894)] [[code](https://github.com/sustechbruce/med-unic)]

[**MICCAI 2023**] M-FLAG: Medical Vision-Language Pre-training with Frozen Language Models and Latent Space Geometry Optimization \
_Che Liu, Sibo Cheng, Chen Chen, Mengyun Qiao, Weitong Zhang, Anand Shah, Wenjia Bai, Rossella Arcucci_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_61)] [[code](https://github.com/cheliu-computation/M-FLAG-MICCAI2023)]

[**MICCAI 2023**] Pathology-and-genomics Multimodal Transformer for Survival Outcome Prediction \
_Kexin Ding, Mu Zhou, Dimitris N. Metaxas, Shaoting Zhang_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43987-2_60)] [[code](https://github.com/Cassie07/PathOmics)]

[**MICCAI 2023**] Surgical Video Captioning with Mutual-Modal Concept Alignment \
_Zhen Chen, Qingyu Guo, Leo K. T. Yeung, Danny T. M. Chan, Zhen Lei, Hongbin Liu & Jinqiao Wang_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43996-4_3)] [[code](https://github.com/franciszchen/SCA-Net)]

[**arXiv 2023**] Utilizing Synthetic Data for Medical Vision-Language Pre-training: Bypassing the Need for Real Images \
_Che Liu, Anand Shah, Wenjia Bai, Rossella Arcucci_ \
[[paper](https://arxiv.org/abs/2310.07027)]

---

## CLIP-driven Application

### Classification

[**MICCAI 2022**] CLIP-Lung: Textual Knowledge-Guided Lung Nodule Malignancy Prediction \
_Yiming Lei, Zilong Li, Yan Shen, Junping Zhang, Hongming Shan_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43990-2_38)] \[[code](https://github.com/ymLeiFDU/CLIP-Lung)]

[**ACL 2022**] Language over Labels: Contrastive Language Supervision Exceeds Purely Label-Supervised Classification Performance on Chest X-Rays \
_Anton Wiehe, Florian Schneider, Sebastian Blank, Xintong Wang, Hans-Peter Zorn, Christian Biemann_ \
[[paper](https://aclanthology.org/2022.aacl-srw.11.pdf)] \[[code](https://github.com/NotNANtoN/master_thesis)]

[**ICCE-Asia 2022**] Transfer Learning for Medical Image Classification on Multiple Datasets using PubMedCLIP \
_Hong N. Dao, Tuyen Nguyen Quang, Incheon Paik_ \
[[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9954669)]

[**Nature BME 2022**] Expert-level detection of pathologies from unannotated chest X-ray images via self-supervised learning \
_Ekin Tiu, Ellie Talius, Pujan Patel, Curtis P. Langlotz, Andrew Y. Ng & Pranav Rajpurkar_ \
[[paper](https://www.nature.com/articles/s41551-022-00936-9)] \[[code](https://github.com/rajpurkarlab/CheXzero)]

[**ISBI 2023**] Self-Supervised Learning with Radiology Reports, A Comparative Analysis of Strategies for Large Vessel Occlusion and Brain CTA Images \
_S Pachade, S Datta, Y Dong, S Salazar-Marioni, R Abdelkhaleq, A Niktabe, K Roberts, SA Sheth, L Giancardo_ \
[[paper](https://ieeexplore.ieee.org/abstract/document/10230623)]

[**ISBI 2023**] Joint representation learning from french radiological
reports and ultrasound images \
_Hind Dadoun, Hervé Delingette, Anne-Laure Rousseau, Eric de Kerviler, Nicholas Ayache_ \
[[paper](https://ieeexplore.ieee.org/document/10230642)]

[**ISBI 2023**] Multimodal Representation Learning for Blastocyst Assessment \
_Youcheng Wang, Zhe Zheng, Na Ni, Guoqing Tong, Nuo Cheng, Kai Li, Ping Yin, Yuanyuan Chen, Yingna Wu, Guangping Xie_ \
[[paper](https://ieeexplore.ieee.org/abstract/document/10230468)]

[**CEUR Workshop 2023**] Multi-stage Medical Image Captioning using Classification and CLIP \
_Masaki Aono, Hiroki Shinoda, Tetsuya Asakawa, Kazuki Shimizu, Takuya Togawa, Takuyuki Komoda_ \
[[paper](https://ceur-ws.org/Vol-3497/paper-113.pdf)]

[**MIDL 2023**] Improving Zero-Shot Detection of Low Prevalence Chest Pathologies using Domain Pre-trained Language Models \
_Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P. Langlotz_ \
[[paper](https://proceedings.mlr.press/v182/zhang22a.html)] \[[code](https://github.com/yuhaozhang/convirt)]

[**MIDL 2023**] MEDIMP: 3D Medical Images with clinical Prompts from limited tabular data for renal transplantation \
_Leo Milecki, Vicky Kalogeiton, Sylvain Bodard, Dany Anglicheau, Jean-Michel Correas, Marc-Olivier Timsit, Maria Vakalopoulou_ \
[[paper](https://centralesupelec.hal.science/hal-04040697v2/document)] \[[code](https://github.com/leomlck/MEDIMP)]

[**MIDL 2023**] Radiology Reports Improve Visual Representations Learned from Radiographs \
_Haoxu Huang, Samyak Rawlekar, Sumit Chopra, Cem M Deniz_ \
[[paper](https://openreview.net/pdf?id=S9EfOVFJIxQh)] \[[code](https://github.com/denizlab/MIMICCXR-MultiModal-SelfSupervision)]

[**ICCV 2023 workshop**] CLIPath: Fine-tune CLIP with Visual Feature Fusion for Pathology Image Analysis Towards Minimizing Data Collection Efforts \
_Zhengfeng Lai, Zhuoheng Li, Luca Cerny Oliveira, Joohi Chauhan, Brittany N. Dugger, Chen-Nee Chuah_ \
[[paper](https://openaccess.thecvf.com/content/ICCV2023W/CVAMD/papers/Lai_CLIPath_Fine-Tune_CLIP_with_Visual_Feature_Fusion_for_Pathology_Image_ICCVW_2023_paper.pdf)]

[**MICCAI 2023**] Xplainer: From X-Ray Observations to Explainable Zero-Shot Diagnosis \
_Chantal Pellegrini, Matthias Keicher, Ege Özsoy, Petra Jiraskova, Rickmer Braren, Nassir Navab_ \
[[paper](https://arxiv.org/pdf/2303.13391.pdf)] \[[code](https://github.com/ChantalMP/Xplainer)]

[**MICCAI 2023 workshop**] Concept Bottleneck with Visual Concept Filtering for Explainable Medical Image Classification \
_Injae Kim, Jongha Kim, Joonmyung Choi, Hyunwoo J. Kim_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-47401-9_22)]

[**arXiv 2022**] Towards Reliable Zero Shot Classification in Self-Supervised Models with Conformal Prediction \
_Bhawesh Kumar, Anil Palepu, Rudraksh Tuwani, Andrew Beam_ \
[[paper](https://arxiv.org/pdf/2210.15805.pdf)]

[**arXiv 2023**] Decoding Radiologists Intense Focus for Accurate CXR Diagnoses: A Controllable and Interpretable AI System \
_Trong Thang Pham, Jacob Brecheisen, Anh Nguyen, Hien Nguyen, Ngan Le_ \
[[paper](https://arxiv.org/pdf/2309.13550.pdf)]

[**arXiv 2023**] Domain-Controlled Prompt Learning \
_Qinglong Cao, Zhengqin Xu, Yuantian Chen, Chao Ma, Xiaokang Yang_ \
[[paper](https://arxiv.org/pdf/2310.07730.pdf)]

[**arXiv 2023**] ETP: Learning Transferable Ecg Representations Via Ecg-Text Pre-training \
_Che Liu, Zhongwei Wan, Sibo Cheng, Mi Zhang, Rossella Arcucci_ \
[[paper](https://arxiv.org/pdf/2309.07145.pdf)]

[**arXiv 2023**] A ChatGPT Aided Explainable Framework for Zero-Shot Medical Image Diagnosis \
_Jiaxiang Liu, Tianxiang Hu, Yan Zhang, Xiaotang Gai, Yang Feng, Zuozhu Liu_ \
[[paper](https://arxiv.org/pdf/2307.01981.pdf)]

[**arXiv 2023**] Are Natural Domain Foundation Models Useful for Medical Image Classification? \
_Joana Palés Huix, Adithya Raju Ganeshan, Johan Fredin Haslum, Magnus Söderberg, Christos Matsoukas, Kevin Smith_ \
[[paper](https://arxiv.org/pdf/2310.19522.pdf)] \[[code](https://github.com/joanaapa/Foundation-Medical)]

[**arXiv 2023**] Exploring Low-Resource Medical Image Classification with Weakly Supervised Prompt Learning \
_Fudan Zheng, Jindong Cao, Weijiang Yu, Zhiguang Chen, Nong Xiao, Yutong Lu_ \
[[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4578827)]

[**arXiv 2023**] Exploring the Transfer Learning Capabilities of CLIP in Domain Generalization for Diabetic Retinopathy \
_Baliah, Sanoojan ; Maani, Fadillah A. ; Sanjeev, Santosh ; Haris Khan, Muhammad_ \
[[paper](https://arxiv.org/pdf/2308.14212.pdf)] \[[code](https://github.com/Sanoojan/CLIP-DRDG)]

[**arXiv 2023**] Exploring the Versatility of Zero-Shot CLIP for Interstitial Lung Disease Classification (ICLR underview) \
_Cara Van Uden, Christian Bluethgen, Maayane Attias, Malgorzata Polacin, Haiwei Henry Guo, Neha Simha, Rishi Raj, Curtis Langlotz_ \
[[paper](https://arxiv.org/pdf/2306.01111.pdf)]

[**arXiv 2023**] Few-shot medical image classification with simple shape and texture text descriptors using vision-language models \
_Michal Byra, Muhammad Febrian Rachmadi, Henrik Skibbe_ \
[[paper](https://arxiv.org/pdf/2308.04005.pdf)] [[code](https://github.com/BrainImageAnalysis/FSC-CLIP-GPT)]

[**arXiv 2023**] Fostering transparent medical image AI via an image-text foundation model grounded in medical literature \
_Chanwoo Kim, Soham U. Gadgil, Alex J. DeGrave, Zhuo Ran Cai, Roxana Daneshjou, Su-In Lee_ \
[[paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10312868/)] \[[code](https://github.com/suinleelab/MONET)]

[**arXiv 2023**] Increasing Textual Context Size Boosts Medical Image-Text Matching \
_Idan Glassberg, Tom Hope_ \
[[paper](https://arxiv.org/pdf/2303.13340.pdf)] [[code](https://github.cs.huji.ac.il/tomhope-lab/ClipMD)]

[**arXiv 2023**] Robust and Interpretable Medical Image Classifiers via Concept Bottleneck Models \
_An Yan, Yu Wang, Petros Karypis, Zexue He, Chengyu Dong, Zihan Wang, Yiwu Zhong, Jingbo Shang, Amilcare Gentili, Chun-Nan Hsu, Julian McAuley_ \
[[paper](https://arxiv.org/pdf/2310.03182.pdf)] \[[code](https://github.com/denizlab/MIMICCXR-MultiModal-SelfSupervision)]

[**arXiv 2023**] Towards Concept-based Interpretability of Skin Lesion Diagnosis using Vision-Language Models \
_Cristiano Patr´ıcio, Luis F. Teixeira, Joao C. Neves_ \
[[paper](https://arxiv.org/abs/2311.14339)] [[code](https://github.com/cristianopatricio/concept-based-interpretability-vlm)]

---

### Dense Prediction

[**MICCAI 2022**] Radiological Reports Improve Pre-training for Localized Imaging Tasks on Chest X-Rays\
_Philip Müller, Georgios Kaissis, Congyu Zou, Daniel Rueckert_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16443-9_62)]

[**ASMUS 2023**] Synthetic Boost: Leveraging Synthetic Data for Enhanced Vision-Language Segmentation in Echocardiography\
_Rabin Adhikari, Manish Dhakal, Safal Thapaliya, Kanchan Poudel, Prasiddha Bhandari & Bishesh Khanal_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-44521-7_9)] [[code](https://github.com/naamiinepal/synthetic-boost)]

[**ICCV 2023**] CLIP-Driven Universal Model for Organ Segmentation and Tumor Detection\
_Jie Liu, Yixiao Zhang, Jie-Neng Chen, Junfei Xiao, Yongyi Lu, Bennett A Landman, Yixuan Yuan, Alan Yuille, Yucheng Tang, Zongwei Zhou_\
[[paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_CLIP-Driven_Universal_Model_for_Organ_Segmentation_and_Tumor_Detection_ICCV_2023_paper.pdf)] [[code](https://github.com/ljwztc/CLIP-Driven-Universal-Model)]

[**MICCAI 2023**] Multiple Prompt Fusion for Zero-Shot Lesion Detection Using Vision-Language Models\
_Miaotian Guo, Huahui Yi, Ziyuan Qin, Haiying Wang, Aidong Men, Qicheng Lao_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43904-9_28)]

[**MICCAI 2023**] Zero-shot Nuclei Detection via Visual-Language Pre-trained Models\
_Yongjian Wu, Yang Zhou, Jiya Saiyin, Bingzheng Wei, Maode Lai, Jianzhong Shou, Yubo Fan, Yan Xu_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43987-2_67)] [[code](https://github.com/wuyongjianCODE/VLPMNuD)]

[**MICCAI 2023**] TCEIP: Text Condition Embedded Regression Network for Dental Implant Position Prediction\
_Xinquan Yang, Jinheng Xie, Xuguang Li, Xuechen Li, Xin Li, Linlin Shen, Yongqiang Deng_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43987-2_31)]

[**MICCAI 2023**] Continual Learning for Abdominal Multi-Organ and Tumor Segmentation\
_Yixiao Zhang, Xinyi Li, Huimiao Chen, Alan L. Yuille, Yaoyao Liu, Zongwei Zhou_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43895-0_4)] [[code](https://github.com/MrGiovanni/ContinualLearning)]

[**MICCAI 2023**] TPRO: Text-prompting-based Weakly Supervised Histopathology Tissue Segmentation\
_Shaoteng Zhang, Jianpeng Zhang, Yutong Xie, Yong Xia_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43907-0_11)] [[code](https://github.com/zhangst431/TPRO)]

[**arXiv 2023**] Exploring Transfer Learning in Medical Image Segmentation using Vision-Language Models\
_Kanchan Poudel, Manish Dhakal, Prasiddha Bhandari, Rabin Adhikari, Safal Thapaliya, Bishesh Khanal_\
[[paper](https://arxiv.org/pdf/2308.07706.pdf)] [[code](https://github.com/naamiinepal/medvlsm)]

[**arXiv 2023**] One-shot Localization and Segmentation of Medical Images with Foundation Models\
_Deepa Anand, Gurunath Reddy M, Vanika Singhal, Dattesh D. Shanbhag, Shriram KS, Uday Patil, Chitresh Bhushan, Kavitha Manickam, Dawei Gui, Rakesh Mullick, Avinash Gopal, Parminder Bhatia, Taha Kass-Hout_\
[[paper](https://arxiv.org/ftp/arxiv/papers/2310/2310.18642.pdf)]

[**arXiv 2023**] AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection\
_Qihang Zhou, Guansong Pang, Yu Tian, Shibo He, Jiming Chen_\
[[paper](https://arxiv.org/pdf/2310.18961.pdf)] [[code](https://github.com/zqhang/AnomalyCLIP)]

---

### Cross-modal

[**IPMI 2023**] X-TRA: Improving Chest X-ray Tasks with Cross-Modal Retrieval Augmentation \
_Tom van Sonsbeek, Marcel Worring_ \
[[paper](https://arxiv.org/pdf/2302.11352.pdf)]

[**ACL 2023**] PubMedCLIP: How Much Does CLIP Benefit Visual Question Answering in the Medical Domain? \
_Sedigheh Eslami, Gerard de Melo, Christoph Meinel_ \
[[paper](https://arxiv.org/pdf/2305.10415.pdf)] \[[code](https://xiaoman-zhang.github.io/PMC-VQA/)]

[**MIDL 2023**] FlexR: Few-shot Classification with Language Embeddings for Structured Reporting of Chest X-rays \
_Matthias Keicher, Kamilia Zaripova, Tobias Czempiel, Kristina Mach, Ashkan Khakzar, Nassir Navab_ \
[[paper](https://arxiv.org/pdf/2203.15723.pdf)]

[**MICCAI 2023**] Open-Ended Medical Visual Question Answering Through Prefix Tuning of Language Models \
_Tom van Sonsbeek, Mohammad Mahdi Derakhshani, Ivona Najdenkoska, Cees G. M. Snoek, and Marcel Worring_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43904-9_70)] \[[code](github.com/tjvsonsbeek/open-ended-medical-vqa)]

[**MICCAI 2023**] A Medical Semantic-Assisted Transformer for Radiographic Report Generation \
_Zhanyu Wang, Mingkang Tang, Lei Wang, Xiu Li, Luping Zhou_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16437-8_63)]

[**TETCI 2023**] Parameter-Efficient Transfer Learning for Medical Visual Question Answering \
_Jiaxiang Liu , Tianxiang Hu, Yan Zhang, Yang Feng, Jin Hao , Junhui Lv, and Zuozhu Liu_ \
[[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10256025)]

[**arXiv 2023**] PMC-VQA: Visual Instruction Tuning for Medical Visual Question Answering \
_Xiaoman Zhang, Chaoyi Wu, Ziheng Zhao, Weixiong Lin, Ya Zhang, Yanfeng Wang, Weidi Xie_ \
[[paper](https://arxiv.org/pdf/2305.10415.pdf)] \[[code](https://xiaoman-zhang.github.io/PMC-VQA/)]
