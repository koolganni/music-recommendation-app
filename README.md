# music-recommendation-app

- <b>Flask</b> 기반 웹 어플리케이션 
- <b>PostgreSQL</b> 데이터베이스 사용
- <b>음악 데이터 수집 :</b> Spotipy API (Spotify Web API 를 Python 기반으로 쉽게 가져오는 오픈 소스 라이브러리)
- <b>추천 시스템 방식 :</b> 단순 장르 정보 기반 + 유사한 음악 검색 (Contents Based System, 유사도 Metric : Cosine Similarity)

> 취향을 기반으로 노래를 추천 받고 친구들과 공유할 수 있는 서비스, Ganni Music 입니다.

![image](https://user-images.githubusercontent.com/76609403/115146972-e060a980-a093-11eb-97cd-68af0f390544.png)

## 서비스 화면 구성

### 홈 화면

유저가 서비스에서 가장 먼저 접하는 홈 화면입니다.

![image](https://user-images.githubusercontent.com/76609403/115147131-78f72980-a094-11eb-981b-101b786c2dea.png)

### 유저네임 등록 화면

유저가 유저네임을 등록하는 화면입니다.

![image](https://user-images.githubusercontent.com/76609403/115147144-94623480-a094-11eb-985c-0538c2ca732b.png)

### 선호 장르 선택 화면

먼저 유저가 가장 좋아하는 장르가 무엇인지 물어봅니다.

![image](https://user-images.githubusercontent.com/76609403/115147171-b0fe6c80-a094-11eb-8755-fb795c71d6b7.png)

Pop, K-pop, 힙합, R&B 등의 장르를 포함한 총 12개의 장르가 주어집니다. 

![image](https://user-images.githubusercontent.com/76609403/115147189-c6739680-a094-11eb-8132-1b92c863b6c1.png)

장르를 선택하면 다음 화면으로 넘어갑니다.

![image](https://user-images.githubusercontent.com/76609403/115147203-d25f5880-a094-11eb-8dc9-55ce1d47f888.png)

### 장르 기반 음악 추천 화면

유저가 선택한 장르를 기반으로 추천된 음악 목록입니다.

![image](https://user-images.githubusercontent.com/76609403/115147227-fc187f80-a094-11eb-9531-09e5eb92e5c6.png)

미리듣기가 가능한 노래의 경우 30초 미리듣기가 가능하며 마음에 들었다면 + 버튼을 눌러 마이 뮤직에 저장할 수 있습니다.

![image](https://user-images.githubusercontent.com/76609403/115147241-118da980-a095-11eb-849c-4cb71c2eaaec.png)

더 다양한 노래를 추천받고 싶다면, 추천받기 버튼을 눌러 유저가 저장한 노래들을 기반으로 유사한 노래를 추천받을 수 있습니다.

![image](https://user-images.githubusercontent.com/76609403/115147252-210cf280-a095-11eb-92e3-ef3229784916.png)

### 취향 기반 음악 추천 화면

유저가 좋아하는 노래들을 기반으로 새로운 노래들이 추천된 화면입니다.  

![image](https://user-images.githubusercontent.com/76609403/115147274-341fc280-a095-11eb-9f65-ba150b6784a1.png)

### 마이 뮤직 피드 화면

본인을 포함해 다른 유저들이 저장해놓은 노래를 확인할 수 있습니다.

![image](https://user-images.githubusercontent.com/76609403/115147328-64fff780-a095-11eb-93f0-60032ff9d39a.png)

### 마이 뮤직 리스트 화면

Kim 이라는 유저가 좋아하는 노래 목록 (마이 뮤직) 입니다.

![image](https://user-images.githubusercontent.com/76609403/115147337-7517d700-a095-11eb-8cf5-c493c6051c2a.png)

## 데이터베이스 스키마

- user 테이블, tracks 테이블 N:N 관계
- user 가 저장한 track 은 mymusic 테이블에 매핑 정보 저장

<img src="https://user-images.githubusercontent.com/76609403/112965120-edb90100-9183-11eb-88d4-90af5edbab3a.png" width="500">

## References
  - [Spotipy - a lightweight Python library for the Spotify Web API](https://spotipy.readthedocs.io/en/2.17.1/)
  - [Spotify for Developers](https://developer.spotify.com/documentation/)
