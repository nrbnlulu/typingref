![Logo](./assets/logo.png){ align=center width=350}
*Introspect Python type annotation, with ease.*


## Installation

<div class="termy">

```console

$ pip install typingref

---> 100%
```

</div>

### Sample Usage:

```python
from typingref import TypeHinter
from typing import Union


class MyType:
    ...


def foo(p: Union[int, str, float]) -> MyType:
    ...


p_type = TypeHinter.from_annotation(foo.__annotations__['p'])

if p_type.is_union():
    for t in p_type.of_type:
        ...

assert Union[int, str, float] == TypeHinter.as_annotation()
```
