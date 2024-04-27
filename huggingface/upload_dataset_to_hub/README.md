# [Hugging Face] 내가 만든 Dataset을 Hugging Face에 올려보기

<br/>

## Blog Link
---
https://giliit.tistory.com/entry/Hugging-Face-%EB%82%B4%EA%B0%80-%EB%A7%8C%EB%93%A0-Dataset%EC%9D%84-Hugging-Face%EC%97%90-%EC%98%AC%EB%A0%A4%EB%B3%B4%EA%B8%B0

<br/>
 
## Prerequest
---

```
datasets==2.19.0
transformers==4.40.1
```
현재 업로드를 기준으로 제 라이브러리 버전을 가져왔습니다. 허깅페이스에 dataset upload는 버전에 크게 상관 없습니다!

##  Overview
---

1. Dataset 생성
2. DatasetDcit 생성
3. 허깅페이스 로그인
4. 허깅페이스 업로드