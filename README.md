# Starburst Detection

# 故事介紹

在2015年，一部名為「刀劍神域」的動畫在全球掀起了一股熱潮，吸引了大量的粉絲。然而，有些網友在論壇上對其優劣進行激烈的爭論。這場爭論引來了大量看熱鬧的網友，他們將刀劍神域中的角色做成梗圖，以此諷刺那些不接受批評的粉絲。這些梗圖被統稱為「星爆圖」，取名自主角的著名招式。由於這些圖片具有一定的幽默感，因此已成為8年級生間的網路文化。

然而，並非所有人都喜歡這些「星爆圖」。有些人可能會希望過濾掉這些內容。在這種情況下，這個模型就可以派上用場了。它可以識別出這些「星爆圖」，並將其過濾掉，以確保使用者只看到他們希望看到的內容。

此外，這個模型還可以用來找出隱藏的「星爆圖」。有時候，這些圖片可能會被巧妙地隱藏在其他內容中(如下圖)，但是這個模型可以識別出它們，並將其框選出來。

![Starburst_20.jpg](Image/Starburst_20.jpg)

# 資料集介紹

- 本專題所使用到的圖片皆為從網路上人工搜集而來，圖源：
    - Dcard-梗圖版
    - 巴哈姆特-場外休憩區
    - Google搜尋
    
    ![Untitled](Image/Untitled.png)
    

### 資料增強：

- RandomBrightness
- RandomContrast
- GaussNoise

### 偵測類別：

- 人物特徵
    - kirito_eye_1
        
        <img src="Image/4d3da01ff2914ce4e338053ed9ff5a17.png" width="200">
        
    - kirito_mouth_1
        
        <img src="Image/21ec095bc5ec42d8be6f4be25e8206c1.png" width="200">
        
    - kirito_eye_2
        
        <img src="Image/f32c8b3bb33aaf63854ae4bc9636c171.png" width="200">
        
    - kirito_mouth_2
        
        <img src="Image/12a001e88363344027241eefd506dea0.png" width="200">
        
    - kirito_eye_3
        
        <img src="Image/fc7181d51e9a29763ed73bbce0d1751a.png" width="200">
        
    - kirito_mouth_3
        
        <img src="Image/7c28003ee3607599c314d9a01a71a40b.png" width="200">
        
    - kirito_hair
        
        <img src="Image/FIZVaM8.png" width="200">
        

- 生物
    - The_Gleameyes
        - 閃耀魔眼
            
            <img src="Image/953992af0c836791cc4ec36349d9b639.png" width="200">
            
    - Ragout_Rabbit
        - 雜燴兔
            
            <img src="Image/%25E9%259B%259C%25E7%2587%25B4%25E5%2585%2594-%25E5%2589%258D.png" width="200">
            

- 道具類
    - Elucidator
        - 闡釋者
            
            <img src="Image/1-3.png" width="200">
            
    - Dark_Repulsor
        - 逐暗者
            
            <img src="Image/1-2.png" width="200">
            
    - Liberator
        - 解放者
            
            <img src="Image/5-4.png" width="200">
            
    - Zanbato_Sword
        - 斬馬刀
            
            <img src="Image/%25E9%2596%2583%25E8%2580%2580%25E9%25AD%2594%25E7%259C%25BC%25E5%258A%258D.png" width="200">
            
    - Nervgear
        
        <img src="Image/NVG-%25E5%2589%258D.png" width="200">
        

- 其他
    - torch
        - 火炬
            
            <img src="Image/74%25E5%25B1%25A4%25E7%2581%25AB%25E7%2582%25AC.png" width="200">
            
    - Aincrad
        - 艾恩葛朗特
            
            <img src="Image/kHIh2te.png" width="200" >
            
    - Starburst_Stream_pose
        - 星爆氣流斬pose
            
            <img src="Image/KEaF4bm.png" width="200" >

            

# Result

<img src="Image/labels.jpg" width="800">

![results.png](Image/results.png)

<img src="Image/confusion_matrix.png" width="800">

<img src="Image/%25E6%259C%25AA%25E5%2591%25BD%25E5%2590%258D-1.png" width="800">

