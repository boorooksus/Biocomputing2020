# Biocomputing2020

### 1_k-nearest_neighbor

#### 프로그램 설명
- 파이썬을 통해 구현한 k-nearest neighbor을 이용하여 ribosomal/non-ribosomal 단백질 data set를 classification을 한 뒤, 분류 결과의 Sensitivity, Specificity, Accuracy를 구한다.

#### 사용 방법
 프로그램을 실행시키기 전에, 프로그램에 입력할 positive training set, negative training set, test set 파일들을 준비한 뒤 같은 폴더 내에 위치시켜야 합니다. 참고로 6-fold cross validation에 사용한 입력 파일들을 그룹별로 분류하여 ‘input data’ 폴더에 넣어두었으니 활용하시길 바랍니다.
프로그램을 실행시킨 뒤 “input location of input file” 이라는 문구가 뜨면 positive training set, negative training set, test set 파일들이 저장된 주소를 입력하고 엔터키를 누릅니다. 그 다음 “input file name of positive training set” 문구가 뜨면 positive training set이 들어있는 파일 이름을 입력하고 엔터키를 누릅니다. 그 다음 “input file name of negative training set” 문구가 뜨면 negative training set이 들어있는 파일 이름을 입력하고 엔터키를 누릅니다. 그 다음 “input file name of test set” 문구가 뜨면 test set이 들어있는 파일 이름을 입력하고 엔터키를 누릅니다. 마지막으로 “Input k and p” 문구가 뜨면 k값과 p 값을 띄어쓰기로 구분하여 입력합니다. 
입력 데이터를 commend line으로 직접 입력하지 않고 파일로 전달하는 이유는 데이터가 너무 커서 컴파일 프로그램에 따라 입력이 잘리는 경우가 있기 때문입니다.
프로그램이 완료되면 입력 데이터 파일이 저장된 위치에 “knn.out”이 생성되어 결과가 저장됩니다.

#### 사용 예시
![입력 예시3](https://user-images.githubusercontent.com/55964775/93007213-31aa3700-f5a1-11ea-8e23-0153f8df19cb.JPG)

#### 결과 예시
![image](https://user-images.githubusercontent.com/55964775/93007255-e3496800-f5a1-11ea-8dac-3ac9237f9cf0.png)


***

### 2_K-Means_Clustering

#### 프로그램 설명
- 파이썬을 통해 구현한 K-means clustering을 통해 데이터를 클러스터링.

#### 사용 방법
프로그램을 실행시킨 뒤 “input k (k is number of clusters” 문구가 뜨면 입력 데이터 파일이 저장된 주소를 입력하고 엔터키를 누릅니다. 그 다음 “input location of input file” 문구가 뜨면 입력 데이터 파일이 저장된 주소를 입력하고 엔터키를 누릅니다. 그 다음 “input name of input file” 문구가 뜨면 입력 데이터 파일의 이름을 입력하고 엔터키를 누릅니다. 그 다음 “input ‘s’ or ‘r’” 문구가 뜨면 ‘s’ 또는 ‘r’을 입력 후 엔터키를 누릅니다. ‘r’은 center 위치를 랜덤하게 지정하겠다는 의미이고 ‘s’는 center 위치를 사용자가 지정하겠다는 의미입니다. 만약 ‘r’을 입력하면 클러스터링을 시작합니다. 만약 ‘s’를 입력하면 “input file name of center data” 문구가 뜨는데 center로 사용할 데이터가 들어있는 파일 이름을 입력하면 클러스터링을 시작합니다. 

#### 사용 예시

1. center 위치 랜덤으로 했을 때<br>
![kmc1](https://user-images.githubusercontent.com/55964775/89909172-bc59e800-dc29-11ea-8015-bb6acd9915d5.jpg)


2. center 위치 지정할 때<br>
![kmc2](https://user-images.githubusercontent.com/55964775/89909262-d693c600-dc29-11ea-8aac-c746ff6a1318.jpg)

#### 결과 예시
![kmc결과1](https://user-images.githubusercontent.com/55964775/90325248-2b319b00-dfb4-11ea-8f4a-ee3e1fa5cd47.JPG)<br>
      .<br>
      .<br>
      .<br>
![kmc결과2](https://user-images.githubusercontent.com/55964775/90325249-2d93f500-dfb4-11ea-9e1e-fa7a83beca67.JPG)<br>
      .<br>
      .<br>
      .<br>

  
