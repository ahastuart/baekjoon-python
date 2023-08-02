import cv2
import os

txt_folder = "runs/detect/exp12/labels"
image_folder = "new_data/"
output_folder = "crop_output/"
additional_output_folder = "crop_output/real"

# 지정한 디렉토리에서 텍스트 파일 목록 얻기
txt_files = os.listdir(txt_folder)

for txt_file in txt_files:
    # 텍스트 파일 경로를 생성.
    txt_file_path = os.path.join(txt_folder, txt_file)

    # 텍스트 파일의 이름에서 확장자 제거하고 이미지 파일 이름 생성해서
    image_file = os.path.splitext(txt_file)[0] + ".jpg"
    image_path = os.path.join(image_folder, image_file) # 이미지 파일의 경로 생성

    # 결과(잘라낸 이미지) 저장 폴더
    output_subfolder = os.path.splitext(txt_file)[0] # 텍스트 파일 이름을 폴더 이름으로 저장.
    output_path = os.path.join(output_folder, output_subfolder) # 결과를 저장할 폴더 경로 생성.
    additional_output_path = os.path.join(additional_output_folder, output_subfolder)
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(additional_output_path, exist_ok=True)

    class_results = {}

    with open(txt_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split() # txt파일의 각 줄을 공백 기준으로 분리해서 리스트로 저장
            class_label = int(parts[0])
            x, y, w, h = map(float, parts[1:5]) # 실수형

            image = cv2.imread(image_path)
            height, width, _ = image.shape

            x_pixel = int(x * width)
            y_pixel = int(y * height)
            w_pixel = int(w * width)
            h_pixel = int(h * height)
            print('qqq',x_pixel, y_pixel, w_pixel, h_pixel)
            crop1 = max(y_pixel - int((h_pixel * 0.55)), 1) # 이미지 경계가 넘어가지 않도록 최소값 1로 제한.
            crop2 = min(y_pixel + int((h_pixel * 0.55)), height - 1)
            crop3 = max(x_pixel - int((w_pixel * 0.55)), 1)
            crop4 = min(x_pixel + int((w_pixel * 0.55)), width - 1)
            print('www', crop1, crop2, crop3, crop4)

            # 계산한 좌표를 이용해서 실제로 이미지를 잘라낸다.
            crop_region = image[crop1:crop2, crop3:crop4]

            # 잘라낸 이미지 저장
            output_file = f"class_{class_label}.jpg"
            output_file_path = os.path.join(output_path, output_file)
            additional_output_file_path = os.path.join(additional_output_path, output_file)

            cv2.imwrite(output_file_path, crop_region)
            if class_label != 0: # 클래스 레이블이 0이 아니면 추가적으로 잘라낸 이미지를 저장.
                cv2.imwrite(additional_output_file_path, crop_region)

            # 클래스별 결과 저장
            if class_label not in class_results:
                class_results[class_label] = []
            class_results[class_label].append(output_file_path)

            print("Crop 저장 완료:", output_file_path)
            if class_label != 0:
                print("추가 Crop 저장 완료:", additional_output_file_path)

    # 중복
    print("중복 클래스 Crop 결과:")
    for class_label, results in class_results.items():
        if len(results) > 1:
            print("Class", class_label)
            for result in results:
                print(result)
                # Crop된 이미지를 동일한 폴더에 저장하는 부분 추가
                output_file_path = os.path.join(output_path, os.path.basename(result))
                cv2.imwrite(output_file_path, crop_region)
            print()

