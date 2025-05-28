from lib.yolo import perform_object_detection

if __name__ == '__main__':
    print('python lib study...')

    # 预训练的 YOLO 模型，对本地图片、网络图片以及视频进行目标检测
    perform_object_detection()