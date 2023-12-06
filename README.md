# <p align=center>`Awesome CLIP in Medical Imaging`</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

:fire::fire: This is a collection of awesome articles about CLIP in medical imaging:fire::fire:

- Our survey paper on arXiv: [CLIP in medical imaging: A comprehensive survey](https://arxiv.org/abs/2211.07804) :heart:

<!-- #### Citation -->

<!-- ```python
@article{kazerouni2023diffusion,
  title={Diffusion models in medical imaging: A comprehensive survey},
  author={Kazerouni, Amirhossein and Aghdam, Ehsan Khodapanah and Heidari, Moein and Azad, Reza and Fayyaz, Mohsen and Hacihaliloglu, Ilker and Merhof, Dorit},
  journal={Medical Image Analysis},
  pages={102846},
  year={2023},
  publisher={Elsevier}
}
``` -->

## Updates

- **First release:** December 21, 2023

## Papers

---

### Pre-training

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

[**NeurIPS 2022**] Multi-Granularity Cross-modal Alignment for Generalized Medical Visual Representation Learning \
_Fuying Wang, Yuyin Zhou, Shujun Wang, Varut Vardhanabhuti, Lequan Yu_ \
[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/d925bda407ada0df3190df323a212661-Abstract-Conference.html)] [[code](https://github.com/HKU-MedAI/MGCA)]

[**NeurIPS 2022 Workshop**] The Role of Local Alignment and Uniformity in Image-Text Contrastive Learning on Medical Images \
_Philip Müller, Georgios Kaissis, Daniel Rueckert_ \
[[paper](https://sslneurips22.github.io/pages/accepted-paper.html)]

[**EMNLP 2022**] MedCLIP: Contrastive Learning from Unpaired Medical Images and Text \
_Zifeng Wang, Zhenbang Wu, Dinesh Agarwal, Jimeng Sun_ \
[[paper](https://www.google.com.hk/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiwuqrXjvWCAxWriVYBHR8TCN8QFnoECAsQAQ&url=https%3A%2F%2Faclanthology.org%2F2022.emnlp-main.256.pdf&usg=AOvVaw0Ph_QYrWg8OUoQBvfvSXoq&opi=89978449)] [[code](https://github.com/RyanWangZf/MedCLIP)]

[**MICCAI 2022**] Breaking with Fixed Set Pathology Recognition through Report-Guided Contrastive Training \
_Constantin Seibold, Simon Reiß, M. Saquib Sarfraz, Rainer Stiefelhagen, Jens Kleesiek_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16443-9_66)]

[**MICCAI 2022**] Vision-Language Contrastive Learning Approach to Robust Automatic Placenta Analysis Using Photographic Images \
_Yimu Pan, Alison D. Gernand, Jeﬀery A. Goldstein, Leena Mithal, Delia Mwinyelle, James Z. Wang_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16437-8_68)]

[**ACM MM 2022**] Align, Reason and Learn: Enhancing Medical Vision-and-Language Pre-training with Knowledge \
_Zhihong Chen, Guanbin Li, Xiang Wan_ \
[[paper](https://arxiv.org/abs/2209.07118)] [[code](https://github.com/zhjohnchan/ARL)]

[**MLHC 2022**] Contrastive Learning of Medical Visual Representations from Paired Images and Text \
_Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P. Langlotz_ \
[[paper](https://proceedings.mlr.press/v182/zhang22a.html)] [[code](https://github.com/edreisMD/ConVIRT-pytorch)]

[**NMI 2022**] Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports\
_Hong-Yu Zhou, Xiaoyu Chen, Yinghao Zhang, Ruibang Luo, Liansheng Wang, Yizhou Yu_\

[**ICLR 2023**] Advancing Radiograph Representation Learning with Masked Record Modeling \
_Hong-Yu Zhou, Chenyu Lian, Liansheng Wang, Yizhou Yu_ \
[[paper](https://openreview.net/forum?id=w-x7U26GM7j)] [[code](https://github.com/RL4M/MRM-pytorch)]

[**arXiv 2023**] Local Contrastive Learning for Medical Image Recognition \
_Syed A. Rizvi, Ruixiang Tang, Xiaoqian Jiang, Xiaotian Ma, Xia Hu_ \
[[paper](https://arxiv.org/abs/2303.14153)]

[**ISBRA 2023**] TCSA: A Text-Guided Cross-View Medical Semantic Alignment Framework for Adaptive Multi-view Visual Representation Learning \
_Hongyang Lei, Huazhen Huang, Bokai Yang, Guosheng Cui, Ruxin Wang, Dan Wu , and Ye Li_ \
[[paper](https://link.springer.com/chapter/10.1007/978-981-99-7074-2_11#auth-Hongyang-Lei)]

[**arXiv 2023**] Towards Medical Artificial General Intelligence via Knowledge-Enhanced Multimodal Pretraining \
_Bingqian Lin, Zicong Chen, Mingjie Li, Haokun Lin, Hang Xu, Yi Zhu, Jianzhuang Liu, Wenjia Cai, Lei Yang, Shen Zhao, Chenfei Wu, Ling Chen, Xiaojun Chang, Yi Yang, Lei Xing, Xiaodan Liang_ \
[[paper](https://arxiv.org/abs/2304.14204)] [[code](https://github.com/chenzcv7/MOTOR)]

[**CVPR 2023**] Learning to Exploit Temporal Structure for Biomedical Vision–Language Processing \
_Shruthi Bannur,∗ Stephanie Hyland∗, Qianchu Liu, Fernando P ́ erez-Garc ́ıa, Maximilian Ilse, Daniel C. Castro, Benedikt Boecking, Harshita Sharma, Kenza Bouzid, Anja Thieme, Anton Schwaighofer, Maria Wetscherek, Matthew P. Lungren, Aditya Nori Javier Alvarez-Valle, Ozan Oktay_ \
[[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Bannur_Learning_To_Exploit_Temporal_Structure_for_Biomedical_Vision-Language_Processing_CVPR_2023_paper.html)] [[code](https://github.com/microsoft/hi-ml/tree/main/hi-ml-multimodal)]

[**arXiv 2023**]A Foundation LAnguage-Image model of the Retina (FLAIR): Encoding expert knowledge in text supervision \
_Julio Silva-Rodriguez, Hadi Chakor, Riadh Kobbi, Jose Dolz, Ismail Ben Ayed_ \
[[paper](https://arxiv.org/abs/2308.07898)] [[code](https://github.com/jusiro/FLAIR)]

---
### CLIP-Driven Application

#### Classification Task

[**arXiv 2023**] A ChatGPT Aided Explainable Framework for Zero-Shot Medical Image Diagnosis  \
_Jiaxiang Liu, Tianxiang Hu, Yan Zhang, Xiaotang Gai, Yang Feng, Zuozhu Liu_ \
[[paper](https://arxiv.org/pdf/2307.01981.pdf)] 

[**arXiv 2023**]  Are Natural Domain Foundation Models Useful for Medical Image Classification?  \
_Joana Palés Huix, Adithya Raju Ganeshan, Johan Fredin Haslum, Magnus Söderberg, Christos Matsoukas, Kevin Smith_ \
[[paper](https://arxiv.org/pdf/2310.19522.pdf)]   \[[code](https://github.com/joanaapa/Foundation-Medical)] 


[**MICCAI 2022**] CLIP-Lung: Textual Knowledge-Guided Lung Nodule Malignancy Prediction  \
_Yiming Lei, Zilong Li, Yan Shen, Junping Zhang, Hongming Shan_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43990-2_38)]  \[[code](https://github.com/ymLeiFDU/CLIP-Lung )] 

[**ICCV 2023 workshop**] CLIPath: Fine-tune CLIP with Visual Feature Fusion for Pathology Image Analysis Towards Minimizing Data Collection Efforts \
_Zhengfeng Lai, Zhuoheng Li, Luca Cerny Oliveira, Joohi Chauhan, Brittany N. Dugger, Chen-Nee Chuah_ \
[[paper](https://openaccess.thecvf.com/content/ICCV2023W/CVAMD/papers/Lai_CLIPath_Fine-Tune_CLIP_with_Visual_Feature_Fusion_for_Pathology_Image_ICCVW_2023_paper.pdf)] 

[**MICCAI 2023 workshop**] Concept Bottleneck with Visual Concept Filtering for Explainable Medical Image Classification \
_Injae Kim, Jongha Kim, Joonmyung Choi, Hyunwoo J. Kim_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-47401-9_22)] 

[**arXiv 2023**] Decoding Radiologists Intense Focus for Accurate CXR Diagnoses: A Controllable and Interpretable AI System \
_Trong Thang Pham, Jacob Brecheisen, Anh Nguyen, Hien Nguyen, Ngan Le_ \
[[paper](https://arxiv.org/pdf/2309.13550.pdf)] 

[**arXiv 2023**] Domain-Controlled Prompt Learning \
_Qinglong Cao, Zhengqin Xu, Yuantian Chen, Chao Ma, Xiaokang Yang_ \
[[paper](https://arxiv.org/pdf/2310.07730.pdf)] 

[**arXiv 2023**] ETP: Learning Transferable Ecg Representations Via Ecg-Text Pre-training \
_Che Liu, Zhongwei Wan, Sibo Cheng, Mi Zhang, Rossella Arcucci_ \
[[paper](https://arxiv.org/pdf/2309.07145.pdf)] 

[**Nature BME 2022**] Expert-level detection of pathologies from unannotated chest X-ray images via self-supervised learning \
_Ekin Tiu, Ellie Talius, Pujan Patel, Curtis P. Langlotz, Andrew Y. Ng & Pranav Rajpurkar_ \
[[paper](https://www.nature.com/articles/s41551-022-00936-9)] \[[code](https://github.com/rajpurkarlab/CheXzero)] 

[**arXiv 2023**] Exploring Low-Resource Medical Image Classification with Weakly Supervised Prompt Learning \
_Fudan Zheng, Jindong Cao, Weijiang Yu, Zhiguang Chen, Nong Xiao, Yutong Lu_ \
[[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4578827)] 

[**arXiv 2023**] Exploring the Transfer Learning Capabilities of CLIP in Domain Generalization for Diabetic Retinopathy \
_Baliah, Sanoojan ; Maani, Fadillah A. ; Sanjeev, Santosh ; Haris Khan, Muhammad_ \
[[paper](https://arxiv.org/pdf/2308.14212.pdf)]  \[[code](https://github.com/Sanoojan/CLIP-DRDG )] 

[**arXiv 2023**] Exploring the Versatility of Zero-Shot CLIP for Interstitial Lung Disease Classification (ICLR underview) \
_Cara Van Uden, Christian Bluethgen, Maayane Attias, Malgorzata Polacin, Haiwei Henry Guo, Neha Simha, Rishi Raj, Curtis Langlotz_ \
[[paper](https://arxiv.org/pdf/2306.01111.pdf)] 

[**arXiv 2023**] Few-shot medical image classification with simple shape and texture text descriptors using vision-language models \
_Michal Byra, Muhammad Febrian Rachmadi, Henrik Skibbe_ \
[[paper](https://arxiv.org/pdf/2308.04005.pdf)] [[code](https://github.com/BrainImageAnalysis/FSC-CLIP-GPT )] 

[**arXiv 2023**] Fostering transparent medical image AI via an image-text foundation model grounded in medical literature \
_Chanwoo Kim, Soham U. Gadgil, Alex J. DeGrave, Zhuo Ran Cai, Roxana Daneshjou, Su-In Lee_ \
[[paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10312868/)]  \[[code]( https://github.com/suinleelab/MONET)] 

[**MIDL 2023**] Improving Zero-Shot Detection of Low Prevalence Chest Pathologies using Domain Pre-trained Language Models \
_Yuhao Zhang, Hang Jiang, Yasuhide Miura, Christopher D. Manning, Curtis P. Langlotz_ \
[[paper](https://proceedings.mlr.press/v182/zhang22a.html)]  \[[code](https://github.com/yuhaozhang/convirt)] 

[**ACL 2022**] Language over Labels: Contrastive Language Supervision Exceeds Purely Label-Supervised Classification Performance on Chest X-Rays \
_Anton Wiehe, Florian Schneider, Sebastian Blank, Xintong Wang, Hans-Peter Zorn, Christian Biemann_ \
[[paper](https://aclanthology.org/2022.aacl-srw.11.pdf)] \[[code](https://github.com/NotNANtoN/master_thesis)]

[**MIDL 2023**] MEDIMP: 3D Medical Images with clinical Prompts from limited tabular data for renal transplantation \
_Leo Milecki, Vicky Kalogeiton, Sylvain Bodard, Dany Anglicheau, Jean-Michel Correas, Marc-Olivier Timsit, Maria Vakalopoulou_ \
[[paper](https://centralesupelec.hal.science/hal-04040697v2/document)] \[[code](https://github.com/leomlck/MEDIMP
)]

[**MIDL 2023**] Radiology Reports Improve Visual Representations Learned from Radiographs \
_Haoxu Huang, Samyak Rawlekar, Sumit Chopra, Cem M Deniz_ \
[[paper](https://openreview.net/pdf?id=S9EfOVFJIxQh)] \[[code](https://github.com/denizlab/MIMICCXR-MultiModal-SelfSupervision
)]

[**arXiv 2023**] Robust and Interpretable Medical Image Classifiers via Concept Bottleneck Models \
_An Yan, Yu Wang, Petros Karypis, Zexue He, Chengyu Dong, Zihan Wang, Yiwu Zhong, Jingbo Shang, Amilcare Gentili, Chun-Nan Hsu, Julian McAuley_ \
[[paper](https://arxiv.org/pdf/2310.03182.pdf)] \[[code](https://github.com/denizlab/MIMICCXR-MultiModal-SelfSupervision
)]

[**arXiv 2022**] Towards Reliable Zero Shot Classification in Self-Supervised Models with Conformal Prediction \
_Bhawesh Kumar, Anil Palepu, Rudraksh Tuwani, Andrew Beam_ \
[[paper](https://arxiv.org/pdf/2210.15805.pdf)] 

[**IEEE-Asia 2022**] Transfer Learning for Medical Image Classification on Multiple Datasets using PubMedCLIP \
_Hong N. Dao, Tuyen Nguyen Quang, Incheon Paik_ \
[[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9954669)] 

[**MICCAI 2023**] Xplainer: From X-Ray Observations to Explainable Zero-Shot Diagnosis \
_Chantal Pellegrini, Matthias Keicher, Ege Özsoy, Petra Jiraskova, Rickmer Braren, Nassir Navab_ \
[[paper](https://arxiv.org/pdf/2303.13391.pdf)] \[[code](https://github.com/ChantalMP/Xplainer
)]


#### Dense Prediction Task

[**MICCAI 2022**] Radiological Reports Improve Pre-training for Localized Imaging Tasks on Chest X-Rays\
_Philip Müller, Georgios Kaissis, Congyu Zou, Daniel Rueckert_\
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16443-9_62)]

[**arXiv 2023**] Exploring Transfer Learning in Medical Image Segmentation using Vision-Language Models\
_Kanchan Poudel, Manish Dhakal, Prasiddha Bhandari, Rabin Adhikari, Safal Thapaliya, Bishesh Khanal_\
[[paper](https://arxiv.org/pdf/2308.07706.pdf)] [[code](https://github.com/naamiinepal/medvlsm)]

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

[**arXiv 2023**] One-shot Localization and Segmentation of Medical Images with Foundation Models\
_Deepa Anand, Gurunath Reddy M, Vanika Singhal, Dattesh D. Shanbhag, Shriram KS, Uday Patil, Chitresh Bhushan, Kavitha Manickam, Dawei Gui, Rakesh Mullick, Avinash Gopal, Parminder Bhatia, Taha Kass-Hout_\
[[paper](https://arxiv.org/ftp/arxiv/papers/2310/2310.18642.pdf)]

[**arXiv 2023**] AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection\
_Qihang Zhou, Guansong Pang, Yu Tian, Shibo He, Jiming Chen_\
[[paper](https://arxiv.org/pdf/2310.18961.pdf)] [[code](https://github.com/zqhang/AnomalyCLIP)]


#### Cross-Modal Task

[**IPMI 2023**] X-TRA: Improving Chest X-ray Tasks with Cross-Modal Retrieval Augmentation \
_Tom van Sonsbeek, Marcel Worring_ \
[[paper](https://arxiv.org/pdf/2302.11352.pdf)] 

[**MICCAI 2023**] Open-Ended Medical Visual Question Answering Through Prefix Tuning of Language Models \
_Tom van Sonsbeek, Mohammad Mahdi Derakhshani, Ivona Najdenkoska, Cees G. M. Snoek, and Marcel Worring_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-43904-9_70)] \[[code](github.com/tjvsonsbeek/open-ended-medical-vqa)]


[**IEEE Transactions on Emerging Topics in Computational Intelligence**] Parameter-Efficient Transfer Learning for Medical Visual Question Answering \
_Jiaxiang Liu , Tianxiang Hu, Yan Zhang, Yang Feng, Jin Hao , Junhui Lv, and Zuozhu Liu_ \
[[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10256025)] 


[**arXiv 2023**] PMC-VQA: Visual Instruction Tuning for Medical Visual Question Answering \
_Xiaoman Zhang, Chaoyi Wu, Ziheng Zhao, Weixiong Lin, Ya Zhang, Yanfeng Wang, Weidi Xie_ \
[[paper](https://arxiv.org/pdf/2305.10415.pdf)]  \[[code](https://xiaoman-zhang.github.io/PMC-VQA/)]


[**ACL 2023**] PubMedCLIP: How Much Does CLIP Benefit Visual Question Answering in the Medical Domain? \
_Sedigheh Eslami, Gerard de Melo, Christoph Meinel_ \
[[paper](https://arxiv.org/pdf/2305.10415.pdf)]  \[[code](https://xiaoman-zhang.github.io/PMC-VQA/)]

[**MICCAI 2023**] A Medical Semantic-Assisted Transformer for Radiographic Report Generation \
_Zhanyu Wang, Mingkang Tang, Lei Wang, Xiu Li, Luping Zhou_ \
[[paper](https://link.springer.com/chapter/10.1007/978-3-031-16437-8_63)]

[**MIDL 2023**] FlexR: Few-shot Classification with Language Embeddings for Structured Reporting of Chest X-rays \
_Matthias Keicher, Kamilia Zaripova, Tobias Czempiel, Kristina Mach, Ashkan Khakzar, Nassir Navab_ \
[[paper](https://arxiv.org/pdf/2203.15723.pdf)]
