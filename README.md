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
[[paper](https://www.nature.com/articles/s42256-021-00425-9)] [[code](https://github.com/funnyzhou/REFERS)]

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
