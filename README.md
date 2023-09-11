# MulTag2Pix: Tag-adaptive Multi-character Line Art Colorization with Text Tag
![image](show.jpg)
[title] MulTag2Pix: Tag-adaptive Multi-character Line Art Colorization with Text Tag
[Abstract] Line art illustrations often depict multiple characters, yet existing automatic colorization approaches typically focus on single-character line art, leaving a gap in research for multi-character line art colorization. Moreover, automatic colorization methods without user guidance often fail to meet users' personalized needs. To address these issues, we propose MulTag2Pix, a multi-character line art colorization network based on color text tags, which caters to personalized and interactive colorization demands. In addition, existing approaches often fail to adaptively color and coordinate with user-provided color text tags, leading to color errors. Then we innovatively give a Tag-Adaptive Colorization Refinement module (TACR) to handle the challenges. Furthermore, the color bleeding issues severely affect the quality of colorization. Therefore, a dual-branch encoder embedded with skeleton maps is utilized to fuse different sources of information, providing more accurate region segmentation and avoiding inconsistent colors within a given semantic region. Experimental results on a large-scale illustration dataset show that our network achieves high-quality personalized colorization of line art across multiple characters. Furthermore, our network also outperforms state-of-the-art methods in single-character line art colorization.

## Prerequisite
- pytorch == 1.9.0
- torchvision == 0.10.0
- numpy == 1.22.0
- scipy == 1.10.1
- python-opencv == 4.8.0.76
- scikit-image ==0.21.0
- Pillow == 10.0.0
- imageio == 2.31.3
- tqdm == 4.66.1
- keras == 2.13.1
- tensorflow == 2.13.0

## Training 
```
python main.py --epoch=300 --input_size=512 --batch_size=4 --model=convnet_dev_skeleton_Adain --cit_cvt_weight 40 50 10 --two_step_epoch=10 --brightness_epoch=24 --save_all_epoch=24  --tag_txt='tags_single.txt'
```

## Test
```
python main.py --test --thread=1 --batch=8 --convnet_dev_skeleton_Adain  --data_dir=testset --input_size=512
```
Saved images will be placed in results/tag2pix_512.


