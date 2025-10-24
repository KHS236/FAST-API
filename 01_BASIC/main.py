from fastapi import FastAPI, HTTPException, status, Query, Path, Header, Cookie, UploadFile, File, Form, Response, Depends, BackgroundTasks
from pydantic import BaseModel, Field
from enum import Enum
from typing import List, Optional, Dict

app = FastAPI(title="FastAPI Minimal Step-by-Step")
# ───────────────────────────────────────────────
# 0) HealthCheck
# GET /health
# Postman: GET http://localhost:8000/health
# ───────────────────────────────────────────────
@app.get("/health") # FastAPI의 데코레이터 - 웹요청(GET,POST..) 처리 핸들러 등록
def health():
    return{"status": "HelloWorld"}
# health라는 엔드포인트를 반환하면 health 실행


@app.get("/")
def root():
    return {"message": "Fast API Main EndPoint"}

# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────

@app.get("/echo")
def echo(name: str = Query(..., min_length=1, description="이름")):
    return {"hello": name}
# echo의 파라미터 name의 밸류 자료형 str, ...은 필수 파라미터 유무
# POSTMAN GET요청 http://localhost:8000/echo?name=hong
    # { name : "hong" }


# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────
@app.get("./items/{item_id}")
def read_item(
    item_id: int = Path(..., ge=1),
    q: Optional[str] = Query(None, max_length=50),
):
    return {"item_id": item_id, "q": q}

class ItemIn(BaseModel):        # 사용자로부터 전달받는 내용 저장하는 DTO
                                    # BasaModel : Json->Python 변환/유효성 검증
    name : str=Field(..., min_length=1)     # 상품명
    price : float = Field(..., gt=0)        # 상품가격
    tags : List[str] = []                   # 태그
    in_stock : bool = True                  # 재고여부

class ItemOut(BaseModel):
    id : int
    name : str=Field(..., min_length=1)
    price : float = Field(..., gt=0)
    tags : List[str] = []
    in_stock : bool = True

# _next_id 기본값
_next_id = 1

#ID 생성하는 코드
# 리턴값을 정수형으로 처리하겠다는 명시
def _gen_id() -> int:
    global _next_id
    val = _next_id
    _next_id += 1
    return val
# ':' = type hint 문법 (Dict[int,ItemOut] : 초기값 자료형을 제한)
DB : Dict[int,ItemOut] = {}

@app.post("/items", response_model=ItemOut, status_code = status.HTTP_201_CREATED)
def create_item(payload: ItemIn):
    new_id = _gen_id()
    ItemOut(id=1, name="Hong", price=1, tags=[],in_stock=True)
    item = ItemOut(id=new_id, name=payload.name, price=payload.price, tash=payload.tags, in_stock=payload.in_stock)
    DB[new_id] = item
    # print("ItemIn",payload)
# POSTMAN POST요청 localhost:8000/items
# body에 json 데이터 넣어주기 headers contents-type 어플리케이션.json
# 요청 후 콘솔 확인
    return item
    

# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────







# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────








# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────






# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────





# ───────────────────────────────────────────────
# 
# ───────────────────────────────────────────────











