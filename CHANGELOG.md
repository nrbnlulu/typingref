CHANGELOG
=========

0.103.0 - 2023-03-29
--------------------

This release fixes a case where

`list['SomeType']` would raise exception due to not passing ns further on.

This release also adds support for `ForwardRef` instances.

Contributed by [ניר](https://github.com/nrbnlulu) via [PR #7](https://github.com/nrbnlulu/typingref/pull/7/)


0.102.0 - 2023-03-29
--------------------

- rename `TypeHinter.from_annotaitons` -> `TypeHinter.from_annotaiton`
- support namespace for `TypeHinter.from_annotaiton`

Contributed by [ניר](https://github.com/nrbnlulu) via [PR #5](https://github.com/nrbnlulu/typingref/pull/5/)


0.101.0 - 2023-03-29
--------------------

First release...

