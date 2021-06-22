# django Form

- form - 입력공간.

  - 사용자가 데이터베이스 형식에 맞게끔 입력하여 서버로 전달할 수 있게 도와주는 기능

- forms.py 주요한 기능

  1. 데이터베이스에 컬럼을 추가하기 위해 많은 파일들의 수정을 진행해야했는데, forms.py를 통해 이러한 단순작업을 줄여줌
  2. 유효성 검사 - html 내에서 데이터베이스로 보내려는 데이터가 적합한지 검사하려면 템플릿 문법의 if를 이용해야했지만, (multivaluedictkeyerror 발생) forms.py를 통해서 이에 대한 검사도 메소드를 통해 진행하게 됨

- forms.py 다루기
  1. app 디렉토리에 forms.py 생성 및 코드작성
     - blogForm class정의 후 내부에 meta클래스를 추가로 젇의한다. (지정한 모델에 fields를 연결하겠다는 뜻) -> 이를 바탕으로 BlogForm이라는 입력공간을 만들겠다.
     - Blog를 모델로하고, 입력할 forms공간을 fields 리스트에 받는다.
     - pub_date를 받지 않은 이유 - 사용자로부터 입력받는 데이터가 아님!! (자동저장)
  2. new.html로 넘어가서 이전에 정의했던 form공간 모두 삭제!!
     - 이후 `{{form}}` 입력하면 대체됨
     - `{{form.as_p}}` 를 통해 p태그에 감싸서 입력공간 만들기 가능
     - `<table> {{form.as_table}} </table>` 로 테이블에 감싸서 입력공간 만들기 가능 (tbody, th, tr...등)
  3. views.py 수정

```python
# forms.py
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'writer','body', 'image']
```

```python
from .forms import BlogForm # new code
def new(request):
    form = BlogForm() # new code
    return render(request,'new.html', {'form': form}) # new code, 객체 넘겨주기
```

- new.html의 `{{form}}`에서 views.py의 create함수로 요청을 보내는데, new.html에서 입력된 데이터들이 모델에 맞는 데이터인지 검사하는 일도 forms.py가 대신해준다. -> create함수 수정

```python
# 수정 전 코드
def create(request):
    new_blog = Blog()
    new_blog.title =request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)
```

- BlogForm객체를 생성한 뒤 is_valid메소드를 통해 데이터 유효성 검사를 진행한다.
- form.save를 진행하기에 앞서 publish date 데이터는 이후에 저장해야하므로 `form.save(commit=False)` 파라미터 전달을 통해 임시 저장을 진행한다.
- 이후 pub date 저장하고, 최종적으로 객체 데이터를 저장한 뒤 페이지에 리다이렉트 진행
- 이 모든 절차는 데이터의 유효성이 valid했을때임. 유효하지 않으면 home으로 이동하도록 설계!

```python
def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False) # 임시 저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')
```
