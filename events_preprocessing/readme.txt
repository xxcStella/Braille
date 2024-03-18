本文件用于说明input_process.py文件中的各种参数

函数：find_clip_time
限制预处理裁剪边缘的参数-sum1_lim, sum2_lim, t-len, range
sum1_lim, sum2_lim: edges limitation of spikes occurring at the same time
        depth=0.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(100,750)
        depth=1.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,850)
        depth=1.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,850)
        depth=2.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,980)
        depth=2.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(210,1200)
        depth=3.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,1300)

    pure-depth, unseen data参数：
        depth=0.6mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,550)
        depth=0.7mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,480)
        depth=0.8mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,500)
        depth=0.9mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,530)
        depth=1.1mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,550)
        depth=1.2mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,580)
        depth=1.3mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,600)
        depth=1.4mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,620)
        depth=1.6mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(120,660)
        depth=1.7mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,680)
        depth=1.8mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,700)
        depth=1.9mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,720)
        depth=2.1mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(125,750)
        depth=2.2mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,770)
        depth=2.3mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,820)
        depth=2.4mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,830)
        depth=2.6mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,870)
        depth=2.7mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,890)
        depth=2.9mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(130,910)
    
    effect-xyposition: (depth=1.5mm)
        r_bias=2.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(145,1300)
        r_bias=1.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,1000)
        r_bias=0.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(135,1200)，第一阶段
        r_bias=0.5mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(550,1400)，第二阶段
        r_bias=0.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(140,1000)

    effect-xyposition: (depth=2.5mm)
        r_bias=1.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(150,1300)，第一阶段
        r_bias=1.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(150,1300)，第二阶段
        r_bias=2.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(170,1300)，第一阶段
        r_bias=2.0mm; sum1_lim=3, sum2_lim=3; t_len=700; range=(150,1300)，第二阶段