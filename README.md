Opencv_KNN_Captcha Hacking
============
Opencv_test 폴더
------------
### Opencv_test - Captcha Hacking에 제가만든 파일들이 있습니다.

* captcha hack 프로젝트 폴더는 https://github.com/ndb796/Python-Data-Analysis-and-Image-Processing-Tutorial에서 받은
폴더입니다. SCTF2017예선에서 출제된 captcha해킹 문제에 관한 파일로 해당 폴더의 run.py를 실행하면 문제를 내는 사이트가 열립니다.

* captcha hacking프로젝트는 나동빈님(https://www.youtube.com/channel/UChflhu32f5EUHlY7_SetNWw) 의 강의 영상을 바탕으로 만들어졌습니다.

### utils.py 
<img src="https://github.com/Pulyong/first_KNN_opencv/blob/master/Opencv_test/1.png?raw=true" width="250px" height="150px" title="px(픽셀) 크기 설정" alt="number"></img>
* get_chars는 위의 사진에서 실제로 필요한 부분을 색깔 별로 나누는 함수입니다. 색깔별로 원하는 색을 제외한 부분은 검은색으로 변환시킵니다.

* extract_chars는 threshold를 통해 전처리하는 과정입니다. 임계점에 해당하는 값을 기준으로 흑,백을 분리합니다. 이후 contours라는 함수로 외곽선을 처리해줍니다. 또한 크기에 제한을 두어 일정한
크기 이상인 데이터에만 데이터로 판단할 수 있게 만듭니다.
 
* resize20함수를 통해 크기를 20x20으로 만들고 모양을 1x400으로 일자로 길게 만듭니다.

* remove_first_0함수는 마지막에 eval함수를 통해 문자열로된 데이터를 숫자 처리를 할 때 앞에 0이 존재해 오류가 나는 상황을 없애기 위하여 필요합니다.

### make_train_data

* 여러개의 사진들을 받아와서 컴퓨터가 학습하기 전에 숫자를 나누는 과정입니다. 키보드를 직접 입력하여 나누어진 사진들이 training_data폴더에 들어가게됩니다.

### knn_trainer.py

* 파일을 정제하는 과정입니다. make_train_data에서 분류된 파일들을 컴퓨터가 학습을 할 수 있도록 파일의 구조를 바꿔줍니다.

### run.py

* knn알고리즘을 통한 머신러닝을 합니다.

* 이후 프로그램이 웹페이지에 접속하여 파일을 target_images에 넣고 숫자를 판단하고 답을 페이지에 넣습니다.

후기
----

* 처음으로 인공지능과 머신러닝을 맛볼 수 있는 프로젝트 였습니다.

* KNN알고리즘. 쉽게말해 가까이 있는 이웃을 통해 판단하는 알고리즘을 체험해봤습니다.

* 가장 간단하다고도 하는 KNN도 이렇게 어렵기 때문에 열심히 공부해야 할 것 같습니다.

* 저의 공부 방향성을 잡아준 정말 재밌었던 프로젝트였습니다.
