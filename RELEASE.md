Release type: minor

This release fixes a case where

`list['SomeType']` would raise exception due to not passing ns further on.

This release also adds support for `ForwardRef` instances.
