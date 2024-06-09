# Blog_Post
[[Python] 타입 힌트를 위한 typing 모듈에 대해 알아보자](https://giliit.tistory.com/entry/Python-%ED%83%80%EC%9E%85-%ED%9E%8C%ED%8A%B8%EB%A5%BC-%EC%9C%84%ED%95%9C-typing-%EB%AA%A8%EB%93%88%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)

## 코드 개요

- 기본 데이터 타입 : int, float, str, bool
- 컨테이너 타입 : List, Dict, Set, Tuple, Mapping, Iterable, NamedTuple
- 복합 타입 : Union, Optional, Any
- 특수 타입 : Callable NewType

## 라이브러리 
```python
# 기본 데이터 타입
# 라이브러리 사용 필요 X

# 컨테이너 타입
from typing import (
    List,
    Dict,
    Set,
    Tuple,
    Mapping,
    Iterable,
    NamedTuple
)

# 복합 타입
from typing import Union, Optional, Any

# 특수 타입
from typing import Callable, NewType

```