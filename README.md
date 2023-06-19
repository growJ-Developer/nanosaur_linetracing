# nanosaur_linetracing
Nanosaur와 ROS를 사용한 라인 트레이싱 로봇

### 🗂️ 프로젝트 소개
Nanosaur 로봇을 검은 라인에 따라 목적지까지 이동합니다. 카메라 센서를 사용하며, 제어 컴퓨터로는 Jetson Nano, 제어 소프트웨어로는 ROS를 사용했습니다.
<br>

### 📆 개발 기간
* 2023년 6월 1일 ~ 2023년 6월 19일

#### 🙋🏻‍♂️ 멤버 구성
 - 장성용: Nanosaur 로버 환경 설정, 개발용 Docker image 구축, 모듈 이식 진행
 - [박동주](https://github.com/PDJ107): Line Following 모듈 제작 및 Gazebo 시뮬레이션 개발
 - [한준혁](https://github.com/Dreams5712): Line Following 모듈 제작 및 Gazebo 시뮬레이션 개발

#### 🔖 주요 기능
 - Pi Camera를 이용한 Line Detection, Extracting
 - Line 데이터와 nanosaur 로버를 이용한 Line Following

#### 🚗 로버 환경
 - Robot Platform: `Ubuntu 18.04(JetPack 4.6.1)`, `ROS Humble(Docker based / aarch64)`
 - Rover H/W: `Jetson Nano 2GB Development Kit`, `Pi Camera v2.1`

#### 🖥️ Gazebo 시뮬레이션 및 개발 환경
 - Develop Platform: `Mac OS 13 Ventura`, `ROS Humble(Docker based / aarch64)`
 - Gazebo Simulation Platform: `Ubuntu 22.04`, `ROS Humble(Docker based / amd64)`

##### - Gazebo 시뮬레이션 결과
[![Video Label](http://img.youtube.com/vi/mh1ZJo_Cqmo/0.jpg)](https://youtu.be/mh1ZJo_Cqmo)

#### 🧩 로버 구조

#### 🧰 도커 레이어 구조
<img width="813" alt="Docker Layer" src="https://github.com/growJ-Developer/nanosaur_linetracing/assets/74158951/e20336f6-8ab6-457a-b849-664b7f28bfa3">

##### 1) Jetson Nano용 Docker Image
 - Jetson의 카메라 기능은 Jetson-utils에서 제공하고 있으며, Jetson-inference 내부에 포함
 - `dustynv/ros:humble-pytorch-l4t-r34.3.1` 이미지를 기반으로 Jetson용 Docker Image 구축
```bash
docker pull addps5012/ros:humble_nano
```

##### 2) Gazebo Simulation용 Docker Image
```bash
 docker pull addps5012/ros:humble_x86
```




