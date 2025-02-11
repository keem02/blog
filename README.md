블로그 만들기
---

주요 기능<br>
게시글 CRUD (Create, Read, Update, Delete)
### 🔹 1. 게시글 목록 조회 (`post_list`)
  1. `GET` 요청을 받으면 `Post` 모델에서 모든 게시글을 조회
  2. 검색어(`q`)가 있을 경우 `title` 또는 `content`에 해당 검색어가 포함된 게시글만 필터링
  3. 결과를 `post_list.html` 템플릿에 전달

### 🔹 2. 게시글 생성 (`create_post`)
  1. `POST` 요청 시 `PostForm`을 이용하여 데이터 유효성 검사
  2. 검증이 완료되면 새 게시글을 저장 후 `post_list`로 리디렉션
  3. `GET` 요청 시 빈 작성 폼을 제공

### 🔹 3. 게시글 상세 조회 (`post_detail`)
  1. URL의 `pk` 값을 이용해 `Post` 객체를 조회 (`get_object_or_404`)
  2. 조회된 게시글을 `post_detail.html`에 전달

### 🔹 4. 게시글 수정 (`edit_post`)
  1. `pk` 값으로 해당 게시글을 조회
  2. `POST` 요청 시 수정된 데이터를 `PostForm`을 이용해 검증 후 저장
  3. 저장 후 해당 게시글의 상세 페이지로 리디렉션
  4. `GET` 요청 시 기존 데이터가 채워진 폼을 제공

### 🔹 5. 게시글 삭제 (`delete_post`)
  1. `pk` 값으로 해당 게시글을 조회
  2. `POST` 요청이 오면 게시글 삭제 후 `post_list`로 리디렉션
  3. `GET` 요청 시 삭제 확인 페이지(`delete_post.html`) 제공
