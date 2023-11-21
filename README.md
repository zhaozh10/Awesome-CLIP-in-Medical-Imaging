# <p align=center>`Awesome CLIP in Medical Imaging`</p>

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/amirhossein-kz/Awesome-Diffusion-Models-in-Medical-Imaging)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

:fire::fire: This is a collection of awesome articles about CLIP in medical imaging:fire::fire:

- Our survey paper on MedIA: [Diffusion Models in Medical Imaging: A Comprehensive Survey](https://www.sciencedirect.com/science/article/pii/S1361841523001068) :heart:
- Our survey paper on arXiv: [Diffusion Models for Medical Image Analysis: A Comprehensive Survey](https://arxiv.org/abs/2211.07804) :heart:

#### Citation

```python
@article{kazerouni2023diffusion,
  title={Diffusion models in medical imaging: A comprehensive survey},
  author={Kazerouni, Amirhossein and Aghdam, Ehsan Khodapanah and Heidari, Moein and Azad, Reza and Fayyaz, Mohsen and Hacihaliloglu, Ilker and Merhof, Dorit},
  journal={Medical Image Analysis},
  pages={102846},
  year={2023},
  publisher={Elsevier}
}
```

## Updates

- Check out our new paper accepted in MICCAI 2023 PRIME Workshop: [DermoSegDiff: A Boundary-aware Segmentation Diffusion Model for Skin Lesion Delineation](https://arxiv.org/abs/2308.02959) 🥳
- **Third release:** June 3, 2023
- :sunglasses: April 8, 2023: Our paper is accepted for publication in the **Medical Image Analysis Journal (IF: 13.83)** :sunglasses:
- **Second release:** March 29, 2023
- **First release:** November 14, 2022

## Contents

- [`Awesome CLIP in Medical Imaging`](#awesome-clip-in-medical-imaging) - [Citation](#citation)
  - [Updates](#updates)
  - [Contents](#contents)
  - [Survey Papers](#survey-papers)
  - [Papers](#papers)
    - [Anomaly Detection](#anomaly-detection)
    - [Denoising](#denoising)
    - [Segmentation](#segmentation)
    - [Image-to-Image Translation](#image-to-image-translation)
    - [Reconstruction](#reconstruction)
    - [Image Generation](#image-generation)
    - [Text-to-Image](#text-to-image)
    - [Registration](#registration)
    - [Classification](#classification)
    - [Object Detection](#object-detection)
    - [Image Restoration](#image-restoration)
      - [Inpainting](#inpainting)
      - [Super Resolution](#super-resolution)
      - [Enhancement](#enhancement)
    - [Adversarial Attacks](#adversarial-attacks)
    - [Time Series](#time-series)
    - [Multi-task](#multi-task)
    - [Other Applications](#other-applications)

## Survey Papers

**A Comprehensive Review of Generative AI in Healthcare** \
_Yasin Shokrollahi, Sahar Yarmohammadtoosky, Matthew M. Nikahd, Pengfei Dong, Xianqi Li, Linxia Gu_ \
[24th Jul., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2310.00795)]

**Generative AI for Medical Imaging: extending the MONAI Framework** :fire: \
_Walter H. L. Pinaya, Mark S. Graham, Eric Kerfoot, Petru-Daniel Tudosiu, Jessica Dafflon, Virginia Fernandez, Pedro Sanchez, Julia Wolleb, Pedro F. da Costa, Ashay Patel, Hyungjin Chung, Can Zhao, Wei Peng, Zelong Liu, Xueyan Mei, Oeslle Lucena, Jong Chul Ye, Sotirios A. Tsaftaris, Prerna Dogra, Andrew Feng, Marc Modat, Parashkev Nachev, Sebastien Ourselin, M. Jorge Cardoso_ \
[27th Jul., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2307.15208)] [[Github](https://github.com/Project-MONAI/GenerativeModels)]

**Deep Learning Approaches for Data Augmentation in Medical Imaging: A Review** \
_Aghiles Kebaili, Jérôme Lapuyade-Lahorgue, Su Ruan_ \
[24th Jul., 2023] [Journal of Imaging, 2023] \
[[Paper](https://arxiv.org/abs/2307.13125)]

**A Comprehensive Survey on Generative Diffusion Models for Structured Data** \
_Heejoon Koo, To Eun Kim_ \
[7th Jun., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2306.04139)]

**Diffusion Models for Time Series Applications: A Survey** \
_Lequan Lin, Zhengkun Li, Ruikun Li, Xuliang Li, Junbin Gao_ \
[1st May, 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2305.00624)]

**A Comprehensive Survey on Knowledge Distillation of Diffusion Models** \
_Weijian Luo_ \
[9th Apr., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2304.04262)]

## Papers

### Anomaly Detection

**Modality Cycles with Masked Conditional Diffusion for Unsupervised Anomaly Segmentation in MRI** \
_Ziyun Liang, Harry Anthony, Felix Wagner, Konstantinos Kamnitsas_ \
[30th Aug, 2023] [arXiv, 2023]<br>
[[Paper](https://arxiv.org/abs/2308.16150)] [[Github](https://github.com/ZiyunLiang/MMCCD)]

**AnoDDPM: Anomaly Detection with Denoising Diffusion Probabilistic Models using Simplex Noise** \
_Julian Wyatt, Adam Leach, Sebastian M. Schmon, Chris G. Willcocks_ \
[1st Jun., 2022] [CVPR Workshop, 2022] \
[[Paper](https://openaccess.thecvf.com/content/CVPR2022W/NTIRE/papers/Wyatt_AnoDDPM_Anomaly_Detection_With_Denoising_Diffusion_Probabilistic_Models_Using_Simplex_CVPRW_2022_paper.pdf)] [[Github](https://github.com/Julian-Wyatt/AnoDDPM)]

**The Swiss Army Knife for Image-to-Image Translation: Multi-Task Diffusion Models** \
_Julia Wolleb, Robin Sandkühler, Florentin Bieder, Philippe C. Cattin_ \
[6th Apr., 2022] [arXiv, 2022]<br>
[[Paper](https://arxiv.org/abs/2204.02641)]

**Diffusion Models for Medical Anomaly Detection** <br>
_Julia Wolleb, Florentin Bieder, Robin Sandkühler, Philippe C. Cattin_<br>
[8th Mar., 2022] [MICCAI, 2022]<br>
[[Paper](https://arxiv.org/abs/2203.04306)] [[Github](https://github.com/JuliaWolleb/diffusion-anomaly)]

---

### Denoising

**Deep Ultrasound Denoising Using Diffusion Probabilistic Models** \
_Hojat Asgariandehkordi, Sobhan Goudarzi, Adrian Basarab, Hassan Rivaz_ \
[12th June, 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2306.07440)]

**A Diffusion Probabilistic Prior for Low-Dose CT Image Denoising** \
_Xuan Liu, Yaoqin Xie, Songhui Diao, Shan Tan, Xiaokun Liang_ \
[25th May, 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2305.15887)]

---

### Segmentation

**Introducing Shape Prior Module in Diffusion Model for Medical Image Segmentation** \
_Zhiqing Zhang, Guojia Fan, Tianyong Liu, Nan Li, Yuyang Liu, Ziyu Liu, Canwei Dong, Shoujun Zhou_ \
[12th Aug., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2309.05929)]

---

### Image-to-Image Translation

**A Novel Unified Conditional Score-based Generative Framework for Multi-modal Medical Image Completion** \
_Xiangxi Meng, Yuning Gu, Yongsheng Pan, Nizhuan Wang, Peng Xue, Mengkang Lu, Xuming He, Yiqiang Zhan, Dinggang Shen_ \
[7th Jul., 2022] [arXiv, 2022] \
[[Paper](https://arxiv.org/abs/2207.03430)]

---

### Reconstruction

**Learning Fourier-Constrained Diffusion Bridges for MRI Reconstruction** \
_Muhammad U. Mirza, Onat Dalmaz, Hasan A. Bedel, Gokberk Elmas, Yilmaz Korkmaz, Alper Gungor, Salman UH Dar, Tolga Çukur_ \
[4th Aug., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2308.01096)] [[Github](https://github.com/icon-lab/FDB)]

**Robust Compressed Sensing MRI with Deep Generative Priors** <br>
_Ajil Jalal, Marius Arvinte, Giannis Daras, Eric Price, Alexandros G. Dimakis, Jonathan I. Tamir_<br>
[3rd Aug., 2021] [NeurIPS, 2021]<br>
[[Paper](https://arxiv.org/abs/2108.01368)] [[Github](https://github.com/utcsilab/csgm-mri-langevin)]

---

### Image Generation

**MedDiffusion: Boosting Health Risk Prediction via Diffusion-based Data Augmentation** \
_Yuan Zhong, Suhan Cui, Jiaqi Wang, Xiaochen Wang, Ziyi Yin, Yaqing Wang, Houping Xiao, Mengdi Huai, Ting Wang, Fenglong Ma_ \
[4th Oct., 2023] [MICCAI, 2023] \
[[Paper](https://arxiv.org/abs/2310.02520)]

**Diffusion Models for Realistic CT Image Generation** \
_Maialen Stephens Txurio, Karen López-Linares Román, Andrés Marcos-Carrión, Pilar Castellote-Huguet, José M. Santabárbara-Gómez, Iván Macía Oliver, Miguel A. González Ballester_ \
[31th May, 2023] [KES, 2023] \
[[Paper](https://link.springer.com/chapter/10.1007/978-981-99-3311-2_30)]

**High-Fidelity Image Synthesis from Pulmonary Nodule Lesion Maps using Semantic Diffusion Model** \
_Xuan Zhao, Benjamin Hou_ \
[2nd May, 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2305.01138)]

**MedGen3D: A Deep Generative Framework for Paired 3D Image and Mask Generation** \
_Kun Han, Yifeng Xiong, Chenyu You, Pooya Khosravi, Shanlin Sun, Xiangyi Yan, James Duncan, Xiaohui Xie_ \
[8th Apr., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2304.04106)]

**Towards Realistic Ultrasound Fetal Brain Imaging Synthesis** \
_Michelle Iskandar, Harvey Mannering, Zhanxiang Sun, Jacqueline Matthew, Hamideh Kerdegari, Laura Peralta, Miguel Xochicale_ \
[8th Apr., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2304.03941)] [[Github](https://github.com/budai4medtech/midl2023)]

**2D Medical Image Synthesis Using Transformer-based Denoising Diffusion Probabilistic Model** \
_Shaoyan Pan, Tonghe Wang, Richard L J Qiu, Marian Axente, Chih-Wei Chang, Junbo Peng, Ashish B Patel, Joseph Shelton, Sagar A Patel, Justin Roper_ \
[4th Apr., 2023] [Physics in Medicine & Biology, 2023] \
[[Paper](https://iopscience.iop.org/article/10.1088/1361-6560/acca5c/meta)]

**ViT-DAE: Transformer-driven Diffusion Autoencoder for Histopathology Image Analysis** \
_Xuan Xu, Saarthak Kapse, Rajarsi Gupta, Prateek Prasanna_ \
[3rd Apr., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2304.01053)]

**A Diffusion Model Predicts 3D Shapes from 2D Microscopy Images** \
_Dominik J. E. Waibel, Ernst Röell, Bastian Rieck, Raja Giryes, Carsten Marr_ \
[30th Aug., 2022] [arXiv, 2022] \
[[Paper](https://arxiv.org/abs/2208.14125)] [[Github](https://github.com/marrlab/dispr)]

**Diffusion Deformable Model for 4D Temporal Medical Image Generation** \
_Boah Kim, Jong Chul Ye_ \
[27th Jan., 2022] [MICCAI, 2022] \
[[Paper](https://arxiv.org/abs/2206.13295)] [[Github](https://github.com/torchddm/ddm)]

**Three-Dimensional Medical Image Synthesis with Denoising Diffusion Probabilistic Models** \
_Zolnamar Dorjsembe, Sodtavilan Odonchimed, Furen Xiao_ \
[22nd Apr., 2022] [MIDL, 2022] \
[[Paper](https://openreview.net/pdf?id=Oz7lKWVh45H)] [[Github](https://github.com/DL-Circle/3D-DDPM)]

---

### Text-to-Image

**PIE: Simulating Disease Progression via Progressive Image Editing** \
_Kaizhao Liang, Xu Cao, Kuei-Da Liao, Tianren Gao, Wenqian Ye, Zhengyu Chen, Jianguo Cao, Tejas Nama, Jimeng Sun_ \
[21st Sep., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2309.11745)]

**Adapting Pretrained Vision-Language Foundational Models to Medical Imaging Domains** \
_Pierre Chambon, Christian Bluethgen, Curtis P. Langlotz, Akshay Chaudhari_ \
[9th Oct., 2022] [arXiv, 2022] \
[[Paper](https://arxiv.org/abs/2210.04133)]

---

### Registration

**FSDiffReg: Feature-wise and Score-wise Diffusion-guided Unsupervised Deformable Image Registration for Cardiac Images** \
_Yi Qin, Xiaomeng Li_ \
[22nd Jul., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2307.12035)] [[Github](https://github.com/xmed-lab/FSDiffReg.git)]

**DiffuseMorph: Unsupervised Deformable Image Registration Along Continuous Trajectory Using Diffusion Models** \
_Boah Kim, Inhwa Han, Jong Chul Ye_ \
[9th Dec., 2021] [ECCV, 2022] \
[[Paper](https://arxiv.org/abs/2112.05149)]

---

### Classification

**Improving Nonalcoholic Fatty Liver Disease Classification Performance With Latent Diffusion Models** \
_Romain Hardy, Cornelia Ilin, Joe Klepich, Ryan Mitchell, Steve Hall, Jericho Villareal_ \
[13th Jul., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2307.06507)]

**Interpretable Alzheimer's Disease Classification Via a Contrastive Diffusion Autoencoder** \
_Ayodeji Ijishakin, Ahmed Abdulaal, Adamos Hadjivasiliou, Sophie Martin, James Cole_ \
[5th Jun., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2306.03022)]

**DiffMIC: Dual-Guidance Diffusion Network for Medical Image Classification** \
_Yijun Yang, Huazhu Fu, Angelica I. Aviles-Rivero, Carola-Bibiane Schönlieb, Lei Zhu_ \
[19th Mar., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2303.10610)] [[Github](https://github.com/scott-yjyang/DiffMIC)]

---

### Object Detection

**Diffusion-Based Hierarchical Multi-Label Object Detection to Analyze Panoramic Dental X-rays** \
_Ibrahim Ethem Hamamci, Sezgin Er, Enis Simsar, Anjany Sekuboyina, Mustafa Gundogar, Bernd Stadlinger, Albert Mehl, Bjoern Menze_ \
[11th Mar., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2303.06500)] [[Github](https://github.com/ibrahimethemhamamci/HierarchicalDet)]

---

### Image Restoration

#### Inpainting

**Multitask Brain Tumor Inpainting with Diffusion Models: A Methodological Report** \
_Pouria Rouzrokh, Bardia Khosravi, Shahriar Faghani, Mana Moassefi, Sanaz Vahdati, Bradley J. Erickson_ \
[21st Oct., 2022] [arXiv, 2022] \
[[Paper](https://arxiv.org/abs/2210.12113)] [[GitHub](https://github.com/Mayo-Radiology-Informatics-Lab/MBTI)] [[Online Tool](https://1f1f559d51c361e2.gradio.app/)]

---

#### Super Resolution

**InverseSR: 3D Brain MRI Super-Resolution Using a Latent Diffusion Model** \
_Jueqi Wang, Jacob Levman, Walter Hugo Lopez Pinaya, Petru-Daniel Tudosiu, M. Jorge Cardoso, Razvan Marinescu_ \
[23rd Aug, 2023] [MICCAI, 2023] \
[[Paper](https://arxiv.org/abs/2308.12465)] [[GitHub](https://github.com/BioMedAI-UCSC/InverseSR)]

---

#### Enhancement

**LLCaps: Learning to Illuminate Low-Light Capsule Endoscopy with Curved Wavelet Attention and Reverse Diffusion** \
_Long Bai, Tong Chen, Yanan Wu, An Wang, Mobarakol Islam, Hongliang Ren_ \
[5th July, 2023] [arXiv, 20223 \
[[Paper](https://arxiv.org/abs/2307.02452)] [[GitHub](https://github.com/longbai1006/LLCaps)]

---

### Adversarial Attacks

**On enhancing the robustness of Vision Transformers: Defensive Diffusion** \
_Raza Imam, Muhammad Huzaifa, Mohammed El-Amine Azz_ \
[14th May, 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2305.08031)] [[GitHub](https://github.com/Muhammad-Huzaifaa/Defensive_Diffusion)]

**Fight Fire With Fire: Reversing Skin Adversarial Examples by Multiscale Diffusive and Denoising Aggregation Mechanism** \
_Yongwei Wang, Yuan Li, Zhiqi Shen_ \
[22nd Aug., 2022] [arXiv, 2022] \
[[Paper](https://arxiv.org/abs/2208.10373)]

---

### Time Series

**A Comprehensive Survey on Generative Diffusion Models for Structured Data** \
_Heejoon Koo, To Eun Kim_ \
[7th Jun., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2306.04139)]

**Restoration of Time-Series Medical Data with Diffusion Model** \
_Jiwoon Lee, Cheolsoo Park_ \
[6th Oct., 2022] [ICCE-Asia, 2022] \
[[Paper](https://www.researchgate.net/profile/Jiwoon-Lee-3/publication/363520751_Restoration_of_Time-Series_Medical_Data_with_Diffusion_Model/links/63210895071ea12e362ee672/Restoration-of-Time-Series-Medical-Data-with-Diffusion-Model.pdf)]

---

### Multi-task

**Application-driven Validation of Posteriors in Inverse Problems** \
_Tim J. Adler, Jan-Hinrich Nölke, Annika Reinke, Minu Dietlinde Tizabi, Sebastian Gruber, Dasha Trofimova, Lynton Ardizzone, Paul F. Jaeger, Florian Buettner, Ullrich Köthe, Lena Maier-Hein_ \
[18th Sep., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2309.09764)]

---

### Other Applications

**Reconstruction of Patient-Specific Confounders in AI-based Radiologic Image Interpretation using Generative Pretraining** \
_Tianyu Han, Laura Žigutytė, Luisa Huck, Marc Huppertz, Robert Siepmann, Yossi Gandelsman, Christian Blüthgen, Firas Khader, Christiane Kuhl, Sven Nebelung, Jakob Kather, Daniel Truhn_ \
[29th Sep., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2309.17123)] [[GitHub](https://github.com/peterhan91/diffchest)] [[Demo](https://colab.research.google.com/drive/1gHWCQxreE1Olo2uQiXfSFSVInmiX85Nn?usp=sharing)]

**AugDiff: Diffusion based Feature Augmentation for Multiple Instance Learning in Whole Slide Image** \
_Zhuchen Shao, Liuxi Dai, Yifeng Wang, Haoqian Wang, Yongbing Zhang_ \
[11th Mar., 2023] [arXiv, 2023] \
[[Paper](https://arxiv.org/abs/2303.06371)]
